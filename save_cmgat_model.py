
import argparse
import torch

def save_state_dict(model, path: str):
    """Save only the weights (recommended)."""
    torch.save(model.state_dict(), path)
    return path

def save_full_model(model, path: str):
    """Save the entire model object (architecture + weights). Use only if you must."""
    torch.save(model, path)
    return path

def convert_full_to_state(full_model_path: str, out_state_path: str):
    """Load a full-model .pth and export just the state_dict to out_state_path."""
    mdl = torch.load(full_model_path, map_location="cpu")
    # If this is already a state_dict, just re-save
    if isinstance(mdl, dict) and all(isinstance(k, str) for k in mdl.keys()):
        torch.save(mdl, out_state_path)
    else:
        torch.save(mdl.state_dict(), out_state_path)
    return out_state_path

def main():
    ap = argparse.ArgumentParser(description="Save/convert CMGAT model checkpoints.")
    ap.add_argument("--from-full", help="Path to a full-model checkpoint (.pth) to convert to state_dict.")
    ap.add_argument("--to-state", help="Output path for state_dict (.pth). Required if --from-full is used.")
    args = ap.parse_args()

    if args.from_full:
        if not args.to_state:
            raise SystemExit("--to-state is required when using --from-full")
        out = convert_full_to_state(args.from_full, args.to_state)
        print(f"✓ Exported state_dict to: {out}")
    else:
        print("This module is intended to be imported in your training notebook:")
        print("  from save_cmgat_model import save_state_dict, save_full_model")
        print("Then call: save_state_dict(model, 'cmgat_without_text.pth')")

if __name__ == "__main__":
    main()
