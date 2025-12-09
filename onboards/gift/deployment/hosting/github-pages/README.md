# 🌐 GitHub Pages Deployment

## 📦 Setup

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/sandikodev/snapcode.git
git push -u origin main
```

### 2. Enable GitHub Pages
```
Settings → Pages
Source: Deploy from branch
Branch: main / (root)
Save
```

### 3. Custom Domain (Optional)
```
Custom domain: snapcode.sandikodev.github.io
```

### 4. CNAME Record
```
Type: CNAME
Name: snapcode
Value: sandikodev.github.io
```

## 🤖 Auto-Build

GitHub Actions (`.github/workflows/build.yml`) will:
- Run `build.py` on every push
- Generate `files.json`
- Auto-deploy

## 🎯 Features
- ✅ Free hosting
- ✅ Auto SSL
- ✅ CDN
- ✅ Auto-build
- ✅ Zero config

## 🔗 URL
https://snapcode.sandikodev.github.io
