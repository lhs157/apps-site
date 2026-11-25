#!/usr/bin/env python3
"""Shared cross-promo copy (promo/copy/): every app name, tagline and campaign text in every locale.

  python3 tool/promo_copy.py check                  # every text in promo/copy has every locale (exit 1 if not)
  python3 tool/promo_copy.py learn <patch.json>     # patch = {"<en text>": {"<locale>": "<text>"}}; fills empty cells only
  python3 tool/promo_copy.py fill <file.json>...    # adds missing locales to any {"en": ...} map whose English is in the library;
                                                    # never overwrites; exit 1 if a text is not in the library or still lacks a locale
"""
import json, sys, glob, os
COPY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "promo", "copy")
LOCALES = json.load(open(os.path.join(COPY, "_common.json")))["locales"]

def maps(o):
    """Every localized text map ({"en": str, "<locale>": str, ...}) inside a JSON value."""
    if isinstance(o, dict):
        if isinstance(o.get("en"), str) and all(isinstance(v, str) and len(k) <= 7 for k, v in o.items()):
            yield o; return
        for v in o.values(): yield from maps(v)
    elif isinstance(o, list):
        for v in o: yield from maps(v)

def library():
    files = {f: json.load(open(f)) for f in sorted(glob.glob(os.path.join(COPY, "*.json")))}
    memory = {}
    for data in files.values():
        for m in maps(data): memory.setdefault(m["en"], m)
    return files, memory

def save(path, data):
    with open(path, "w") as f: json.dump(data, f, ensure_ascii=False, indent=2); f.write("\n")

def main(cmd, *args):
    files, memory = library()
    if cmd == "check":
        gaps = [(os.path.basename(f), m["en"], l) for f, d in files.items() for m in maps(d) for l in LOCALES if not m.get(l, "").strip()]
        for g in gaps: print("missing", *g, sep=" | ")
        print(f"{len(memory)} texts x {len(LOCALES)} locales, {len(gaps)} missing"); return 1 if gaps else 0
    if cmd == "learn":
        patch = json.load(open(args[0]))
        for f, d in files.items():
            for m in maps(d):
                for l, t in patch.get(m["en"], {}).items():
                    if not m.get(l, "").strip(): m[l] = t
            save(f, d)
        return main("check")
    if cmd == "fill":
        bad = 0
        for path in args:
            data = json.load(open(path)); added = 0
            for m in maps(data):
                src = memory.get(m["en"])
                if src is None: print(f"{path}: not in library: {m['en']!r}"); bad += 1; continue
                for l in LOCALES:
                    if not m.get(l, "").strip() and src.get(l, "").strip(): m[l] = src[l]; added += 1
                if any(not m.get(l, "").strip() for l in LOCALES): print(f"{path}: still missing locales: {m['en']!r}"); bad += 1
            save(path, data); print(f"{path}: +{added} cells")
        return 1 if bad else 0
    print(__doc__); return 2

if __name__ == "__main__": sys.exit(main(*sys.argv[1:]) if len(sys.argv) > 1 else main(""))
