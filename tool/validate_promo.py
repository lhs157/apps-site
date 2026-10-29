#!/usr/bin/env python3
"""Validate the cross-promo config in promo/ before it goes live.

Spec: hao-app docs/superpowers/specs/2026-10-30-cross-promo-design.md (§4, §5.3, §6).
Usage: python3 tool/validate_promo.py [--online]
  --online  also checks that every app marked "listed" is really public on its store.
Exit 1 on any error; warnings never fail the run.
"""
import json
import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMO = ROOT / "promo"
PLACEMENTS = {"popup", "native", "settings"}
PLATFORMS = {"ios", "android"}
TEXT_KEYS = ("label", "headline", "body", "cta", "ctaInstalled", "dismiss")
POPUP_SIZE = (1200, 800)  # 3:2, em chọn tạm 30/10/2026

errors, warnings = [], []


def err(where, msg):
    errors.append(f"{where}: {msg}")


def warn(where, msg):
    warnings.append(f"{where}: {msg}")


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001 — report any parse failure as a config error
        err(path.name, f"không đọc được JSON ({e})")
        return None


def check_asset(where, rel, size=None):
    p = ROOT / rel
    if not p.is_file():
        err(where, f"thiếu file {rel}")
        return
    if size:
        try:
            from PIL import Image
            got = Image.open(p).size
            if got != size:
                err(where, f"{rel} cỡ {got[0]}x{got[1]}, cần {size[0]}x{size[1]}")
        except ImportError:
            warn(where, "không có Pillow, bỏ qua kiểm cỡ ảnh")


def parse_time(where, s):
    try:
        t = datetime.fromisoformat(s)
    except ValueError:
        err(where, f"thời gian không đúng ISO 8601: {s}")
        return None
    if t.tzinfo is None:
        err(where, f"thời gian thiếu múi giờ: {s}")
        return None
    return t


def check_text(where, obj, locales):
    for key in TEXT_KEYS:
        val = obj.get(key)
        if not isinstance(val, dict):
            err(where, f"thiếu '{key}'")
            continue
        for loc in locales:
            s = val.get(loc, "")
            if not s.strip():
                err(where, f"'{key}' thiếu ngôn ngữ {loc}")
            # Luật 19/10/2026: chữ quảng bá không ghi cứng con số nội dung.
            elif re.search(r"\d", s.replace("{app}", "")):
                err(where, f"'{key}.{loc}' có chữ số: {s!r}")


def check_catalog(cat):
    apps = cat.get("apps", {})
    if cat.get("schemaVersion") != 1:
        err("catalog.json", "schemaVersion phải là 1")
    for aid, a in apps.items():
        w = f"catalog.{aid}"
        for k in ("name", "tagline"):
            for loc in ("vi", "en"):
                if not a.get(k, {}).get(loc):
                    err(w, f"thiếu {k}.{loc}")
        check_asset(w, a.get("icon", ""), (256, 256))
        ios, android = a.get("ios"), a.get("android")
        if ios:
            if not re.fullmatch(r"\d{9,12}", str(ios.get("appStoreId", ""))):
                err(w, "ios.appStoreId không hợp lệ")
            if not ios.get("scheme"):
                err(w, "ios.scheme trống")
            if not isinstance(ios.get("listed"), bool):
                err(w, "ios.listed phải là true/false")
        if android:
            if not re.fullmatch(r"[a-z][\w.]+", android.get("package", "")):
                err(w, "android.package không hợp lệ")
            if not isinstance(android.get("listed"), bool):
                err(w, "android.listed phải là true/false")
    return apps


def check_rules(path, apps):
    cfg = load(path)
    if cfg is None:
        return
    host = path.name.split(".")[0]
    w = path.name
    if host not in apps:
        err(w, f"app chủ '{host}' không có trong catalog")
    if cfg.get("schemaVersion") != 1:
        err(w, "schemaVersion phải là 1")
    if not isinstance(cfg.get("enabled"), bool):
        err(w, "enabled phải là true/false")
    if not 1 <= cfg.get("refreshHours", 0) <= 48:
        err(w, "refreshHours phải trong 1–48")
    pl = cfg.get("placements", {})
    if set(pl) - PLACEMENTS:
        err(w, f"chỗ hiển thị lạ: {sorted(set(pl) - PLACEMENTS)}")
    popup = pl.get("popup")
    if popup:
        if popup.get("cooldownHours", 0) < 24:
            err(w, "popup.cooldownHours dưới 24 (chặn cứng của app)")
        if not 0 <= popup.get("chance", 1) <= 1:
            err(w, "popup.chance phải trong 0–1")
    settings = pl.get("settings")
    if settings:
        for loc in ("vi", "en"):
            if not settings.get("title", {}).get(loc):
                err(w, f"settings.title thiếu {loc}")
        for a in settings.get("apps", []):
            if a not in apps:
                err(w, f"settings.apps có '{a}' không có trong catalog")
            if a == host:
                err(w, "settings.apps không được chứa chính app chủ")
    seen = set()
    for c in cfg.get("campaigns", []):
        cw = f"{w}#{c.get('id', '?')}"
        if c.get("id") in seen:
            err(cw, "trùng id chiến dịch")
        seen.add(c.get("id"))
        target = c.get("app")
        if target not in apps:
            err(cw, f"app '{target}' không có trong catalog")
            continue
        if target == host:
            err(cw, "không quảng bá chính app chủ")
        if set(c.get("placements", [])) - PLACEMENTS:
            err(cw, "placements lạ")
        plats = set(c.get("platforms", []))
        if not plats or plats - PLATFORMS:
            err(cw, "platforms phải là tập con khác rỗng của ios/android")
        for p in plats:
            if not apps[target].get(p):
                err(cw, f"{target} không có trên {p}")
            elif not apps[target][p].get("listed"):
                warn(cw, f"{target} chưa lên store {p} (listed=false) — app sẽ bỏ qua tới khi listed=true")
        if not 0 <= c.get("rolloutPercent", 100) <= 100:
            err(cw, "rolloutPercent phải trong 0–100")
        if not 1 <= c.get("maxImpressions", 1) <= 10:
            err(cw, "maxImpressions phải trong 1–10")
        start = parse_time(cw, c["startAt"]) if "startAt" in c else None
        end = parse_time(cw, c["endAt"]) if "endAt" in c else None
        if start and end and start >= end:
            err(cw, "startAt phải trước endAt")
        check_text(cw, c, c.get("locales", ["vi", "en"]))
        for placement, rel in c.get("banner", {}).items():
            check_asset(cw, rel, POPUP_SIZE if placement == "popup" else None)
        if "popup" in c.get("placements", []) and "popup" not in c.get("banner", {}):
            err(cw, "chiến dịch popup thiếu banner.popup")


def is_live(platform, ref):
    url = (f"https://itunes.apple.com/lookup?id={ref}" if platform == "ios"
           else f"https://play.google.com/store/apps/details?id={ref}&hl=en")
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            return json.load(r)["resultCount"] > 0 if platform == "ios" else r.status == 200
    except urllib.error.HTTPError as e:
        return False if e.code == 404 else None
    except Exception:  # noqa: BLE001 — network trouble is a warning, not a verdict
        return None


def check_online(apps):
    for aid, a in apps.items():
        for platform, ref in (("ios", a.get("ios", {}).get("appStoreId")),
                              ("android", a.get("android", {}).get("package"))):
            if not ref:
                continue
            live = is_live(platform, ref)
            listed = a[platform].get("listed")
            w = f"catalog.{aid}.{platform}"
            if live is None:
                warn(w, "không kiểm được store (mạng)")
            elif listed and not live:
                err(w, "listed=true nhưng app chưa công khai trên store")
            elif live and not listed:
                warn(w, "app đã công khai trên store — đổi listed=true để bắt đầu quảng bá")


def main():
    cat = load(PROMO / "catalog.json")
    apps = check_catalog(cat) if cat else {}
    for path in sorted(PROMO.glob("*.json")):
        if path.name != "catalog.json":
            check_rules(path, apps)
    if "--online" in sys.argv and apps:
        check_online(apps)
    for m in warnings:
        print("CẢNH BÁO", m)
    for m in errors:
        print("LỖI", m)
    print(f"{len(errors)} lỗi, {len(warnings)} cảnh báo")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
