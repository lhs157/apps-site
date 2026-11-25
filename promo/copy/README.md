# Shared cross-promo copy

One place for every cross-promo text of every app (name, tagline, campaign headline/body, buttons, section titles), in every locale in `_common.json` → `locales`.

- `<app>.json`: name, tagline, campaign copy for that app (first `copy` entry is the default for new campaigns).
- `_common.json`: buttons, labels and section titles shared by all apps.
- `python3 tool/promo_copy.py check` — every text has every locale.
- `python3 tool/promo_copy.py fill <config.json>...` — fills missing locales in any app's promo config (apps-site host files, App Hub `cross-promo` / `promo-catalog`). Never overwrites.
- New text: add it here with all locales first (`learn <patch.json>`), then use it in a config.
- Campaigns do not restrict `locales`: every interface language sees cross-promo (owner, 25/11/2026).
