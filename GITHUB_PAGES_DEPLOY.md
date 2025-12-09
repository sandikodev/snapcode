# 🚀 GitHub Pages Deployment Guide

## ✅ Jawaban: Tidak Bisa Baca Directory dari GitHub Pages

GitHub Pages adalah **static hosting**, tidak bisa baca directory listing.

**Solusi:** Generate `files.json` saat build!

---

## 🎯 How It Works

### 3-Tier Fallback System:

```
1. Try files.json (GitHub Pages) ✅
   ↓ fail
2. Try /api/files/ (Local server) ✅
   ↓ fail
3. Use hardcoded list (Fallback) ✅
```

---

## 📦 Deployment Steps

### 1. Generate File Lists
```bash
python3 build.py
```

Output:
```
✅ Generated content/files.json (3 files)
✅ Generated docs/files.json (11 files)
```

### 2. Commit & Push
```bash
git add .
git commit -m "Deploy to GitHub Pages"
git push origin main
```

### 3. Enable GitHub Pages
```
GitHub Repo → Settings → Pages
Source: Deploy from branch
Branch: main / (root)
```

### 4. Configure Custom Domain (Optional)
```
Custom domain: snapcode.sandikodev.github.io
CNAME file: snapcode
```

---

## 🤖 Auto-Build with GitHub Actions

File `.github/workflows/build.yml` sudah dibuat!

### What It Does:
1. **Trigger:** Setiap push ke main branch
2. **Run:** `python3 build.py`
3. **Generate:** `files.json` untuk setiap folder
4. **Commit:** Auto-commit file lists
5. **Deploy:** GitHub Pages auto-deploy

### Enable:
```
GitHub Repo → Actions → Enable workflows
```

---

## 📁 File Structure for GitHub Pages

```
snapcode.me/
├── index.html              # Main app
├── build.py                # Build script
│
├── content/
│   ├── files.json          # Generated file list ✨
│   ├── default.md
│   └── sample.md
│
└── docs/
    ├── files.json          # Generated file list ✨
    ├── INDEX.md
    └── ...
```

---

## 🔄 Workflow

### Local Development:
```bash
# Run with server (dynamic)
python3 server.py
# → Uses /api/files/ endpoint
```

### Before Deploy:
```bash
# Generate file lists
python3 build.py
# → Creates files.json
```

### GitHub Pages:
```
User visits snapcode.sandikodev.github.io
→ Loads index.html
→ Fetches content/files.json
→ Loads all files dynamically ✅
```

---

## 🎨 files.json Format

```json
[
  {
    "name": "INDEX.md",
    "size": 1100
  },
  {
    "name": "QUICKSTART.md",
    "size": 4500
  }
]
```

---

## ✨ Benefits

### For GitHub Pages:
- ✅ **No hardcoding** needed
- ✅ **Auto-generated** file lists
- ✅ **Dynamic loading** from JSON
- ✅ **Easy maintenance** - just run build.py

### For Local Dev:
- ✅ **Full dynamic** with server.py
- ✅ **No build step** needed
- ✅ **Real-time** file detection

---

## 🧪 Testing

### Test Local:
```bash
# With server (dynamic API)
python3 server.py
# Open http://localhost:8000

# Without server (files.json)
python3 build.py
open index.html
```

### Test GitHub Pages:
```bash
# After deploy
# Visit: https://snapcode.sandikodev.github.io
# Click "Docs" → Loads from files.json ✅
```

---

## 📝 Adding New Files

### Method 1: Auto (GitHub Actions)
```bash
# 1. Add file
echo "# New" > docs/NEW.md

# 2. Push
git add docs/NEW.md
git commit -m "Add new doc"
git push

# 3. GitHub Actions runs build.py automatically
# 4. files.json updated
# 5. Deployed!
```

### Method 2: Manual
```bash
# 1. Add file
echo "# New" > docs/NEW.md

# 2. Generate lists
python3 build.py

# 3. Commit all
git add .
git commit -m "Add new doc"
git push
```

---

## 🔧 Custom Domain Setup

### 1. Add CNAME Record
```
Type: CNAME
Name: snapcode
Value: sandikodev.github.io
```

### 2. Configure GitHub
```
Settings → Pages → Custom domain
Enter: snapcode.sandikodev.github.io
Save
```

### 3. Enable HTTPS
```
☑ Enforce HTTPS
```

---

## 🎯 Summary

**Q:** Bisa baca directory dari GitHub Pages?  
**A:** ❌ Tidak bisa (static hosting)

**Q:** Solusinya?  
**A:** ✅ Generate `files.json` dengan `build.py`

**Q:** Otomatis?  
**A:** ✅ Ya, dengan GitHub Actions

**Q:** Perlu update manual?  
**A:** ❌ Tidak, GitHub Actions auto-generate

---

## 📊 Comparison

| Environment | Method | Auto-update |
|-------------|--------|-------------|
| **Local Dev** | server.py API | ✅ Real-time |
| **GitHub Pages** | files.json | ✅ On push |
| **Static** | Hardcoded | ❌ Manual |

---

## 🚀 Quick Deploy

```bash
# 1. Generate file lists
python3 build.py

# 2. Commit & push
git add .
git commit -m "Deploy to GitHub Pages"
git push origin main

# 3. Done! Visit:
# https://snapcode.sandikodev.github.io
```

---

**Status:** ✅ Ready for GitHub Pages!  
**URL:** https://snapcode.sandikodev.github.io 🎉
