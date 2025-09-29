from flask import Flask, request, jsonify

app = Flask(__name__)

# ------------------------------
# Problem 1: Register Voter
# ------------------------------
voters = {}

@app.route("/api/voters", methods=["POST"])
def create_voter():
    """
    Create a new voter.
    Example:
    POST {"voter_id": 1, "name": "Alice", "age": 22}
    -> {"message": "Voter created", "data": {...}}
    """
    data = request.get_json()
    voter_id = data.get("voter_id")
    if voter_id in voters:
        return jsonify({"error": "Voter already exists"}), 400
    voters[voter_id] = data
    return jsonify({"message": "Voter created", "data": data}), 201


# ------------------------------
# Problem 2: List Voters
# ------------------------------
@app.route("/api/voters", methods=["GET"])
def list_voters():
    """
    List all voters.
    Example: GET /api/voters -> {"voters": [...]}
    """
    return jsonify({"voters": list(voters.values())})


# ------------------------------
# Problem 3: Update Voter
# ------------------------------
@app.route("/api/voters/<int:voter_id>", methods=["PUT"])
def update_voter(voter_id):
    """
    Update an existing voter.
    Example: PUT /api/voters/1 {"name": "Updated"}
    """
    if voter_id not in voters:
        return jsonify({"error": "Voter not found"}), 404
    data = request.get_json()
    voters[voter_id].update(data)
    return jsonify({"message": f"Voter {voter_id} updated", "data": voters[voter_id]})


# ------------------------------
# Problem 4: Delete Voter
# ------------------------------
@app.route("/api/voters/<int:voter_id>", methods=["DELETE"])
def delete_voter(voter_id):
    """
    Delete a voter.
    Example: DELETE /api/voters/1
    """
    if voter_id not in voters:
        return jsonify({"error": "Voter not found"}), 404
    deleted = voters.pop(voter_id)
    return jsonify({"message": f"Voter {voter_id} deleted", "data": deleted})


# ------------------------------
# Problem 5: Register Candidate
# ------------------------------
candidates = {}

@app.route("/api/candidates", methods=["POST"])
def register_candidate():
    """
    Register a new candidate.
    Example: POST {"candidate_id": 1, "name": "Bob", "party": "X"}
    """
    data = request.get_json()
    candidate_id = data.get("candidate_id")
    if candidate_id in candidates:
        return jsonify({"error": "Candidate already exists"}), 400
    candidates[candidate_id] = {**data, "votes": 0}
    return jsonify({"message": "Candidate registered", "data": data}), 201


# ------------------------------
# Problem 6: List Candidates (optional filter)
# ------------------------------
@app.route("/api/candidates", methods=["GET"])
def list_candidates():
    """
    List all candidates, filter by party.
    Example: GET /api/candidates?party=X
    """
    party = request.args.get("party")
    if party:
        filtered = [c for c in candidates.values() if c.get("party") == party]
        return jsonify({"candidates": filtered, "filtered_by": party})
    return jsonify({"candidates": list(candidates.values())})


# ------------------------------
# Problem 7: Candidate Vote Count
# ------------------------------
@app.route("/api/candidates/<int:candidate_id>/votes", methods=["GET"])
def candidate_votes(candidate_id):
    """
    Get total votes for a candidate.
    """
    if candidate_id not in candidates:
        return jsonify({"error": "Candidate not found"}), 404
    return jsonify({"candidate_id": candidate_id, "votes": candidates[candidate_id]["votes"]})


# ------------------------------
# Problem 8: Cast Vote
# ------------------------------
@app.route("/api/votes", methods=["POST"])
def cast_vote():
    """
    Cast a vote.
    Example: POST {"voter_id": 1, "candidate_id": 1}
    """
    data = request.get_json()
    voter_id = data.get("voter_id")
    candidate_id = data.get("candidate_id")

    if voter_id not in voters:
        return jsonify({"error": "Invalid voter"}), 400
    if candidate_id not in candidates:
        return jsonify({"error": "Invalid candidate"}), 400

    candidates[candidate_id]["votes"] += 1
    return jsonify({"message": "Vote casted", "data": data})


# ------------------------------
# Problem 9: Weighted Vote
# ------------------------------
@app.route("/api/votes/weighted", methods=["POST"])
def weighted_vote():
    """
    Cast a weighted vote.
    Example: POST {"voter_id":1,"candidate_id":1,"weight":3}
    """
    data = request.get_json()
    voter_id = data.get("voter_id")
    candidate_id = data.get("candidate_id")
    weight = data.get("weight", 1)

    if voter_id not in voters or candidate_id not in candidates:
        return jsonify({"error": "Invalid voter or candidate"}), 400

    candidates[candidate_id]["votes"] += weight
    return jsonify({"message": "Weighted vote cast", "data": data})


# ------------------------------
# Problem 10: Vote Timeline
# ------------------------------
@app.route("/api/votes/timeline", methods=["GET"])
def vote_timeline():
    """
    Dummy timeline for a candidate's votes.
    Example: GET /api/votes/timeline?candidate_id=1
    """
    candidate_id = request.args.get("candidate_id")
    return jsonify({"candidate_id": candidate_id, "timeline": ["t1: +1", "t2: +2"]})


# ------------------------------
# Problem 11: Leaderboard
# ------------------------------
@app.route("/api/results", methods=["GET"])
def results():
    """
    Return all candidates sorted by votes.
    """
    leaderboard = sorted(candidates.values(), key=lambda c: c["votes"], reverse=True)
    return jsonify({"results": leaderboard})


# ------------------------------
# Problem 12: Winner
# ------------------------------
@app.route("/api/results/winner", methods=["GET"])
def winner():
    """
    Return the top candidate(s).
    """
    if not candidates:
        return jsonify({"winners": []})
    max_votes = max(c["votes"] for c in candidates.values())
    winners = [c for c in candidates.values() if c["votes"] == max_votes]
    return jsonify({"winners": winners})


# ------------------------------
# Problem 13: Encrypted Ballot
# ------------------------------
@app.route("/api/ballots/encrypted", methods=["POST"])
def encrypted_ballot():
    """
    Accept an encrypted ballot (dummy).
    Example: POST {"ballot":"ENCRYPTED123"}
    """
    data = request.get_json()
    return jsonify({"message": "Encrypted ballot received", "data": data})


# ------------------------------
# Problem 14: Ranked Choice
# ------------------------------
@app.route("/api/ballots/ranked", methods=["POST"])
def ranked_ballot():
    """
    Accept ranked-choice ballot (dummy).
    Example: POST {"voter_id":1,"ranking":[2,1,3]}
    """
    data = request.get_json()
    return jsonify({"message": "Ranked ballot received", "data": data})


# ------------------------------
# Problem 15: DP Analytics
# ------------------------------
@app.route("/api/analytics/dp", methods=["POST"])
def dp_analytics():
    """
    Dummy differential privacy analytics.
    Example: POST {"query":"total votes"}
    """
    data = request.get_json()
    return jsonify({"answer": {"noise": 42}, "query": data})


# ------------------------------
# Problem 16: Risk-Limiting Audit
# ------------------------------
@app.route("/api/audits/plan", methods=["POST"])
def audit_plan():
    """
    Dummy audit plan.
    Example: POST {"sample_size":100}
    """
    data = request.get_json()
    return jsonify({"audit_plan": {"status": "planned"}, "data": data})


# ------------------------------
# Problem 17: Health Check
# ------------------------------
@app.route("/", methods=["GET"])
def home():
    """
    Root endpoint for health check.
    """
    return jsonify({"message": "HackTheAI API is running 🚀"})


# ------------------------------
# Extra dummy problems to cover 20
# ------------------------------
@app.route("/api/stats/voters", methods=["GET"])
def voter_stats():
    """
    Return simple stats about voters.
    """
    return jsonify({"total_voters": len(voters)})


@app.route("/api/stats/candidates", methods=["GET"])
def candidate_stats():
    """
    Return simple stats about candidates.
    """
    return jsonify({"total_candidates": len(candidates)})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
