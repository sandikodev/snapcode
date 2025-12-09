# ⚡ Quick Reference Card

## 🚀 One-Line Deployments

```bash
# GitHub Pages
python3 build.py && git add . && git commit -m "Deploy" && git push

# Docker
docker-compose up -d --build

# Supervisor
sudo supervisorctl restart snapcode
```

---

## 📦 Setup Commands

### GitHub Pages
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/sandikodev/snapcode.git
git push -u origin main
# Enable Pages in GitHub Settings
```

### Supervisor
```bash
sudo apt install supervisor
sudo cp deployment/supervisor/snapcode.conf /etc/supervisor/conf.d/
sudo supervisorctl reread && sudo supervisorctl update
sudo supervisorctl start snapcode
```

### Docker
```bash
docker-compose up -d
```

---

## 🔧 Management Commands

| Action | GitHub Pages | Supervisor | Docker |
|--------|-------------|------------|--------|
| **Deploy** | `git push` | `supervisorctl restart` | `docker-compose up -d` |
| **Logs** | GitHub Actions | `tail -f /var/log/snapcode/access.log` | `docker-compose logs -f` |
| **Status** | GitHub Pages tab | `supervisorctl status` | `docker ps` |
| **Stop** | - | `supervisorctl stop snapcode` | `docker-compose down` |
| **Restart** | Push again | `supervisorctl restart` | `docker-compose restart` |

---

## 🎯 Quick Decisions

**Need free hosting?** → GitHub Pages  
**Have VPS?** → Supervisor  
**Learning DevOps?** → Docker  
**Need scaling?** → Docker  
**Want simplicity?** → GitHub Pages  

---

## 📁 File Structure

```
snapcode.me/
├── index.html              # Main app
├── server.py               # Python server
├── build.py                # Build script
├── Dockerfile              # Docker config
├── docker-compose.yml      # Docker Compose
├── Makefile                # Commands
├── DEPLOYMENT.md           # Full guide
│
├── content/
│   └── files.json          # Generated
│
├── docs/
│   └── files.json          # Generated
│
└── deployment/
    ├── github-pages/
    ├── supervisor/
    └── docker/
```

---

## 🐛 Quick Fixes

### Port already in use
```bash
# Find process
sudo lsof -i :8000
# Kill it
sudo kill -9 <PID>
```

### Docker not starting
```bash
docker-compose down
docker-compose up -d --build --force-recreate
```

### Supervisor not working
```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart snapcode
```

---

## 🔗 URLs

- **Local:** http://localhost:8000
- **GitHub Pages:** https://snapcode.sandikodev.github.io
- **VPS:** http://your-server-ip:8000

---

## 📊 Health Checks

```bash
# Local
curl http://localhost:8000

# Docker
docker inspect --format='{{.State.Health.Status}}' snapcode

# Supervisor
sudo supervisorctl status snapcode
```

---

**Keep this card handy!** 📌
