"""Daily AI news digest. Fetches Reddit + HN + arXiv, filters/groups via Claude, emails via Gmail SMTP."""

import json
import os
import smtplib
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import quote

import requests

SENDER = os.environ["GMAIL_SENDER"]
APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"].replace(" ", "")
RECIPIENTS = [e.strip() for e in os.environ["GMAIL_RECIPIENTS"].split(",")]
ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY", "").strip()

DHAKA = timezone(timedelta(hours=6))
TODAY = datetime.now(DHAKA)
TODAY_STR = TODAY.strftime("%Y-%m-%d")

UA = "ai-daily-digest/1.0 (github actions)"

SUBS = [
    "LocalLLaMA",
    "MachineLearning",
    "singularity",
    "ChatGPT",
    "artificial",
    "ArtificialInteligence",
]


def fetch_reddit(sub):
    url = f"https://www.reddit.com/r/{sub}/top.json?t=day&limit=30"
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=15)
        if r.status_code != 200:
            print(f"[reddit {sub}] HTTP {r.status_code}", file=sys.stderr)
            return []
        data = r.json()
        posts = []
        for child in data.get("data", {}).get("children", []):
            p = child.get("data", {})
            posts.append({
                "source": f"r/{sub}",
                "title": p.get("title", ""),
                "url": p.get("url_overridden_by_dest") or f"https://reddit.com{p.get('permalink', '')}",
                "permalink": f"https://reddit.com{p.get('permalink', '')}",
                "selftext": (p.get("selftext") or "")[:600],
                "score": p.get("score", 0),
                "num_comments": p.get("num_comments", 0),
                "created_utc": p.get("created_utc", 0),
            })
        return posts
    except Exception as e:
        print(f"[reddit {sub}] error: {e}", file=sys.stderr)
        return []


def fetch_hn():
    try:
        top = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", timeout=15).json()[:80]
        items = []
        for hid in top:
            try:
                it = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{hid}.json", timeout=10).json()
                if not it:
                    continue
                title = (it.get("title") or "")
                t_low = title.lower()
                if not any(k in t_low for k in ("ai", "llm", "gpt", "claude", "gemini", "anthropic", "openai", "deepmind", "model", "agent", "ml ", "neural", "rag", "transformer", "diffusion", "mistral", "llama", "qwen")):
                    continue
                items.append({
                    "source": "HackerNews",
                    "title": title,
                    "url": it.get("url") or f"https://news.ycombinator.com/item?id={hid}",
                    "permalink": f"https://news.ycombinator.com/item?id={hid}",
                    "selftext": "",
                    "score": it.get("score", 0),
                    "num_comments": it.get("descendants", 0),
                    "created_utc": it.get("time", 0),
                })
            except Exception:
                continue
            time.sleep(0.05)
        return items
    except Exception as e:
        print(f"[hn] error: {e}", file=sys.stderr)
        return []


def fetch_arxiv():
    cats = ["cs.AI", "cs.LG", "cs.CL"]
    items = []
    for cat in cats:
        try:
            url = f"http://export.arxiv.org/api/query?search_query=cat:{cat}&sortBy=submittedDate&sortOrder=descending&max_results=20"
            r = requests.get(url, headers={"User-Agent": UA}, timeout=15)
            if r.status_code != 200:
                continue
            root = ET.fromstring(r.content)
            ns = {"a": "http://www.w3.org/2005/Atom"}
            for entry in root.findall("a:entry", ns):
                title = (entry.find("a:title", ns).text or "").strip().replace("\n", " ")
                link = entry.find("a:id", ns).text.strip()
                summary = (entry.find("a:summary", ns).text or "").strip().replace("\n", " ")[:600]
                published = entry.find("a:published", ns).text
                items.append({
                    "source": f"arXiv/{cat}",
                    "title": title,
                    "url": link,
                    "permalink": link,
                    "selftext": summary,
                    "score": 0,
                    "num_comments": 0,
                    "created_utc": int(datetime.fromisoformat(published.replace("Z", "+00:00")).timestamp()),
                })
        except Exception as e:
            print(f"[arxiv {cat}] error: {e}", file=sys.stderr)
    return items


def dedupe(items):
    seen = set()
    out = []
    for it in items:
        url_key = (it["url"] or "").split("?")[0].rstrip("/").lower()
        title_key = "".join(c for c in it["title"].lower() if c.isalnum())[:80]
        key = (url_key, title_key)
        if key in seen:
            continue
        seen.add(key)
        out.append(it)
    return out


FALLBACK_DROP = [
    "meme", "lol", "funny", "joke", "shitpost",
    "what do you think", "what do yall think", "what do you guys think",
    "how do i", "how to get started", "beginner", "newbie",
    "help me", "can someone", "is it just me",
    "hot take", "unpopular opinion",
]

FALLBACK_KEEP = [
    "release", "releases", "launched", "announces", "announcing", "announce",
    "model", "benchmark", "paper", "research", "study",
    "api", "funding", "raised", "acquires", "acquisition", "ipo",
    "open source", "open-source", "open weights", "weights",
    "state of the art", "sota", "results", "outperforms",
    "gpu", "training", "dataset", "fine-tune", "fine tune",
    "agent", "agentic", "tool use", "function calling",
    "rag", "retrieval", "context window",
]


def heuristic_filter(items):
    out = []
    for it in items:
        t = it["title"].lower()
        if any(bad in t for bad in FALLBACK_DROP):
            continue
        if "arxiv" in it["source"].lower():
            out.append(it)
            continue
        if it.get("score", 0) < 20 and "arxiv" not in it["source"].lower() and "HackerNews" not in it["source"]:
            continue
        if any(good in t for good in FALLBACK_KEEP) or it.get("score", 0) > 200:
            out.append(it)
    return out


def heuristic_rank(items):
    now = time.time()
    for it in items:
        age_h = max(1, (now - it.get("created_utc", now)) / 3600)
        recency_bonus = 1.2 if age_h < 6 else (1.0 if age_h < 24 else 0.7)
        it["_rank"] = (it.get("score", 0) + it.get("num_comments", 0) * 2 + 50) * recency_bonus
    return sorted(items, key=lambda x: x["_rank"], reverse=True)


def heuristic_group(items):
    groups = {
        "Models & Releases": [],
        "Research": [],
        "Tools & Products": [],
        "Industry News": [],
        "Community Insights": [],
    }
    for it in items[:25]:
        t = it["title"].lower()
        if "arxiv" in it["source"].lower() or "paper" in t or "study" in t:
            groups["Research"].append(it)
        elif any(k in t for k in ["release", "launched", "announces", "model", "weights", "api"]):
            groups["Models & Releases"].append(it)
        elif any(k in t for k in ["funding", "raised", "acquires", "acquisition", "ipo", "layoff"]):
            groups["Industry News"].append(it)
        elif any(k in t for k in ["tool", "product", "app", "plugin", "extension"]):
            groups["Tools & Products"].append(it)
        else:
            groups["Community Insights"].append(it)
    return groups


def llm_curate(items):
    """Use Claude to filter, dedupe, summarize, and group. Returns HTML body string."""
    if not ANTHROPIC_KEY:
        return None
    try:
        import anthropic
    except ImportError:
        return None

    client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)

    trimmed = [
        {
            "source": it["source"],
            "title": it["title"][:200],
            "url": it["url"],
            "snippet": (it.get("selftext") or "")[:400],
            "score": it.get("score", 0),
            "comments": it.get("num_comments", 0),
        }
        for it in items[:200]
    ]

    prompt = f"""You are a senior AI news curator. Below is raw data from Reddit, Hacker News, and arXiv from the last 24 hours. Produce a high-signal daily digest.

RULES:
- KEEP only: new model releases (weights/API/benchmarks), research papers with concrete results, product launches/major updates, benchmark/eval results, industry news (funding/acquisitions/policy), notable technical insights backed by data.
- DROP: memes, jokes, shitposts, opinions without data, beginner questions, how-to-do-X, drama, hot takes, hype without substance, "what do you think" posts, self-promotion without novelty.
- Dedupe items covering the same story.
- Pick top 15-25 total.
- Group into 5 sections: Models & Releases / Research / Tools & Products / Industry News / Community Insights. Omit empty sections.
- For each item, write: bold headline (rewrite for clarity if needed), 1-2 sentence summary (what happened + why it matters), source link.

OUTPUT FORMAT — return only valid HTML, no markdown, no code fences:

<p style="color:#555;font-size:14px;">AI Daily Digest — <strong>{TODAY_STR}</strong> (Asia/Dhaka) — <strong>N items</strong>.</p>
<h2 style="border-bottom:2px solid #e74c3c;color:#c0392b;">Models &amp; Releases</h2>
<p><b>Headline</b><br>
Summary sentence.<br>
<a href="URL">Source — r/sub or HackerNews or arXiv</a></p>
... (more items)
<h2 style="border-bottom:2px solid #3498db;color:#2980b9;">Research</h2>
... etc
<hr style="border:none;border-top:1px solid #ddd;margin:20px 0;">
<p style="color:#888;font-size:12px;">Sources: Reddit (r/LocalLLaMA, r/MachineLearning, r/singularity, r/ChatGPT, r/artificial, r/ArtificialInteligence), Hacker News, arXiv (cs.AI, cs.LG, cs.CL).</p>

RAW DATA (JSON):
{json.dumps(trimmed, ensure_ascii=False)}
"""

    try:
        resp = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=8000,
            messages=[{"role": "user", "content": prompt}],
        )
        html = resp.content[0].text.strip()
        if html.startswith("```"):
            html = html.split("```", 2)[1]
            if html.startswith("html"):
                html = html[4:]
            html = html.rsplit("```", 1)[0].strip()
        return html
    except Exception as e:
        print(f"[llm] error: {e}", file=sys.stderr)
        return None


def heuristic_html(groups):
    colors = {
        "Models & Releases": ("#e74c3c", "#c0392b"),
        "Research": ("#3498db", "#2980b9"),
        "Tools & Products": ("#2ecc71", "#27ae60"),
        "Industry News": ("#9b59b6", "#8e44ad"),
        "Community Insights": ("#f39c12", "#e67e22"),
    }
    count = sum(len(v) for v in groups.values())
    parts = [f'<p style="color:#555;font-size:14px;">AI Daily Digest — <strong>{TODAY_STR}</strong> (Asia/Dhaka) — <strong>{count} items</strong>.</p>']
    for name, items in groups.items():
        if not items:
            continue
        border, text = colors[name]
        parts.append(f'<h2 style="border-bottom:2px solid {border};color:{text};">{name}</h2>')
        for it in items:
            snippet = (it.get("selftext") or "")[:200]
            parts.append(
                f'<p><b>{it["title"]}</b><br>'
                f'{snippet}<br>'
                f'<a href="{it["url"]}">Source — {it["source"]}</a></p>'
            )
    parts.append('<hr style="border:none;border-top:1px solid #ddd;margin:20px 0;">')
    parts.append('<p style="color:#888;font-size:12px;">Fallback heuristic mode (no LLM). Sources: Reddit, Hacker News, arXiv.</p>')
    return "\n".join(parts)


def send_email(html_body):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"AI Daily \u2014 {TODAY_STR}"
    msg["From"] = f"AI Daily Digest <{SENDER}>"
    msg["To"] = ", ".join(RECIPIENTS)
    msg.attach(MIMEText(html_body, "html", "utf-8"))
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(SENDER, APP_PASSWORD)
        server.sendmail(SENDER, RECIPIENTS, msg.as_string())
    print(f"Sent to {RECIPIENTS}")


def main():
    print(f"Starting digest for {TODAY_STR}")
    items = []
    for sub in SUBS:
        items.extend(fetch_reddit(sub))
        time.sleep(1)
    print(f"Reddit: {len(items)} items")

    hn = fetch_hn()
    print(f"HN: {len(hn)} items")
    items.extend(hn)

    arx = fetch_arxiv()
    print(f"arXiv: {len(arx)} items")
    items.extend(arx)

    items = dedupe(items)
    print(f"After dedupe: {len(items)} items")

    html = llm_curate(items)
    if html:
        print("Using LLM-curated digest")
    else:
        print("Using heuristic digest (no LLM)")
        filtered = heuristic_filter(items)
        ranked = heuristic_rank(filtered)
        groups = heuristic_group(ranked)
        html = heuristic_html(groups)

    send_email(html)


if __name__ == "__main__":
    main()
