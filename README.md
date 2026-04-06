# Food Tracker PWA

A simple offline-capable food and calorie tracker built as a Progressive Web App.

## Features

- Track daily calories, protein and fat
- Pre-loaded foods: chicken breast, tuna, white rice, eggs, olive oil
- Custom food entry for anything else
- Daily progress bars vs targets
- 7-day week view with averages
- Fully offline — works without internet once installed
- Installable to home screen on iOS and Android

## Deploy to GitHub Pages

1. Fork or upload this repo to GitHub
2. Go to **Settings → Pages**
3. Set source to **main branch, root folder**
4. Your app will be live at `https://yourusername.github.io/reponame`

## Install on phone

**Android:** Open in Chrome → tap the three-dot menu → "Add to Home Screen"

**iOS:** Open in Safari → tap the Share button → "Add to Home Screen"

## Files

```
index.html      — main app
manifest.json   — PWA manifest (name, icons, display mode)
sw.js           — service worker (offline caching)
icons/
  icon-192.png  — app icon (Android)
  icon-512.png  — app icon (splash screen)
```

## Updating targets

Tap the Settings tab inside the app. Update your weekly calorie and protein targets as you progress through your reverse diet:

| Week | Calories | Protein | Fat |
|------|----------|---------|-----|
| 1    | 1,450    | 130g    | 35g |
| 2    | 1,650    | 140g    | 42g |
| 3    | 1,750    | 150g    | 48g |
| 4    | 1,900    | 155g    | 52g |

## Data storage

All data is saved locally in your browser's localStorage. It stays on your device and is not sent anywhere.
