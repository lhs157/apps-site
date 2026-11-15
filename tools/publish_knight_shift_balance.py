#!/usr/bin/env python3
"""Prepare immutable Knight Shift data and its version manifest; does not commit/push."""
import argparse
import hashlib
import json
from pathlib import Path

BASE = "https://lhs157.github.io/apps-site/knight-shift/"

def prepare(source, output, version, min_app=None, environment="test"):
    if environment not in ("test", "production"):
        raise ValueError("Unknown environment")
    base = BASE + ("test/" if environment == "test" else "")
    output = Path(output)
    manifest_path = output / "balance-version.json"
    old = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    if version <= old.get("dataVersion", 0):
        raise ValueError("dataVersion must increase; rollback also needs a new version")
    target = output / f"balance-v{version}.json"
    if target.exists():
        raise ValueError("Versioned data files are immutable; choose a new version")
    data = json.loads(Path(source).read_text(), parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
    for key in ("Gate", "Tuning", "Weapons", "Enemies", "Fury"):
        if key not in data:
            raise ValueError(f"Missing {key}")
    for key in ("Weapons", "Enemies"):
        ids = [row["Kind"] for row in data[key]]
        if not ids or len(set(ids)) != len(ids):
            raise ValueError(f"Empty or duplicate {key} IDs")
    if any(len(w["Levels"]) != 4 or w["AmmoPackPrice"] < 0 for w in data["Weapons"]):
        raise ValueError("Invalid weapon levels/ammo prices")
    if not 0 <= data["Fury"]["RefundCap"] <= .5:
        raise ValueError("Fury refund may not exceed half a bar")
    raw = (json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")
    if len(raw) > 2 * 1024 * 1024:
        raise ValueError("Data exceeds client size limit")
    manifest = dict(schemaVersion=1, dataVersion=version,
                    minAppVersion=min_app or old.get("minAppVersion", "2.0.0"),
                    dataUrl=base + target.name, sha256=hashlib.sha256(raw).hexdigest())
    output.mkdir(parents=True, exist_ok=True)
    target.write_bytes(raw)
    assert hashlib.sha256(target.read_bytes()).hexdigest() == manifest["sha256"]
    temp = manifest_path.with_suffix(".json.tmp")
    temp.write_text(json.dumps(manifest, indent=2) + "\n")
    temp.replace(manifest_path)
    return manifest

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True)
    parser.add_argument("--version", type=int, required=True)
    parser.add_argument("--environment", required=True, choices=("test", "production"))
    parser.add_argument("--output")
    parser.add_argument("--min-app-version")
    args = parser.parse_args()
    output = args.output or (Path(__file__).resolve().parents[1] / "knight-shift" / ("test" if args.environment == "test" else ""))
    result = prepare(args.source, output, args.version, args.min_app_version, args.environment)
    print(json.dumps(result, indent=2))
