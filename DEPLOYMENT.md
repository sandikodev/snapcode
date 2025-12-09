# 🚀 SnapCode Deployment Guide

> Belajar berbagai deployment methods: Static Hosting, Bare Metal, Containerized!

---

## 📚 Table of Contents

1. [Static Hosting (JAMstack)](#1-static-hosting-jamstack) - GitHub Pages, Vercel
2. [Bare Metal (Native)](#2-bare-metal-native) - VPS, Self-Hosted
3. [Containerized (Docker)](#3-containerized-docker) - Docker, Kubernetes
4. [Comparison](#comparison)

---

## 🎯 Deployment Types

### Type 1: **Static Hosting / JAMstack**
Deploy as static files on CDN (no server needed)

### Type 2: **Bare Metal / Native**
Deploy directly on server OS (full control)

### Type 3: **Containerized**
Deploy in containers (isolated, scalable)

---

## 1. 🌐 GitHub Pages

**Best for:** Free hosting, personal projects, demos

### Quick Start
```bash
make deploy-github
```

### Manual
```bash
python3 build.py
git add .
git commit -m "Deploy"
git push origin main
```

### Features
- ✅ Free hosting
- ✅ Auto SSL (HTTPS)
- ✅ CDN (fast worldwide)
- ✅ Auto-build with GitHub Actions
- ✅ Custom domain support

### URL
https://snapcode.sandikodev.github.io

📖 [Full Guide](deployment/github-pages/README.md)

---

## 2. 🖥️ Supervisor (Self-Hosted)

**Best for:** VPS, production, full control

### Quick Start
```bash
make deploy-supervisor
```

### Manual
```bash
# Install
sudo apt install supervisor

# Configure
sudo cp deployment/supervisor/snapcode.conf /etc/supervisor/conf.d/
sudo nano /etc/supervisor/conf.d/snapcode.conf  # Edit paths

# Start
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start snapcode
```

### Features
- ✅ Auto-restart on crash
- ✅ Log management
- ✅ Process monitoring
- ✅ Production-ready
- ✅ Full control

### Management
```bash
make logs-supervisor      # View logs
make restart-supervisor   # Restart
make status-supervisor    # Check status
```

📖 [Full Guide](deployment/supervisor/README.md)

---

## 3. 🐳 Docker

**Best for:** Containerized, scalable, modern DevOps

### Quick Start
```bash
# Basic
make deploy-docker

# With Nginx
make deploy-docker-nginx
```

### Manual
```bash
# Build & Run
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

### Features
- ✅ Isolated environment
- ✅ Easy deployment
- ✅ Auto-restart
- ✅ Health checks
- ✅ Resource limits
- ✅ Scalable

### Management
```bash
make logs-docker      # View logs
make restart-docker   # Restart
make status-docker    # Check status
make stop-docker      # Stop
```

📖 [Full Guide](deployment/docker/README.md)

---

## 📊 Comparison

| Feature | GitHub Pages | Supervisor | Docker |
|---------|-------------|------------|--------|
| **Cost** | Free | VPS cost | VPS cost |
| **Setup** | Easy | Medium | Medium |
| **Control** | Limited | Full | Full |
| **Scalability** | Auto | Manual | Easy |
| **SSL** | Auto | Manual | Manual |
| **Monitoring** | GitHub | Logs | Logs + Health |
| **Best for** | Demos | Production | DevOps |

---

## 🎯 Which One to Choose?

### Choose GitHub Pages if:
- ✅ You want free hosting
- ✅ You don't need backend
- ✅ You want auto-deploy
- ✅ You're building a demo/portfolio

### Choose Supervisor if:
- ✅ You have a VPS
- ✅ You want full control
- ✅ You need production stability
- ✅ You're comfortable with Linux

### Choose Docker if:
- ✅ You want containerization
- ✅ You need easy scaling
- ✅ You're learning DevOps
- ✅ You want modern deployment

---

## 🛠️ Makefile Commands

```bash
make help                 # Show all commands
make build               # Generate file lists
make dev                 # Run local server

# Deployment
make deploy-github       # Deploy to GitHub Pages
make deploy-supervisor   # Deploy with Supervisor
make deploy-docker       # Deploy with Docker
make deploy-docker-nginx # Deploy with Docker + Nginx

# Management
make logs-docker         # Docker logs
make logs-supervisor     # Supervisor logs
make restart-docker      # Restart Docker
make restart-supervisor  # Restart Supervisor
make status-docker       # Docker status
make status-supervisor   # Supervisor status

# Cleanup
make clean              # Clean build artifacts
```

---

## 🎓 Learning Path

### Beginner
1. Start with **GitHub Pages** (easiest)
2. Learn Git, GitHub Actions
3. Understand static hosting

### Intermediate
1. Try **Supervisor** on VPS
2. Learn Linux, process management
3. Configure Nginx reverse proxy

### Advanced
1. Master **Docker** & Docker Compose
2. Learn containerization
3. Implement CI/CD pipelines
4. Add monitoring (Prometheus, Grafana)

---

## 🔧 Tech Stack Learned

### Frontend
- HTML5, CSS3, JavaScript
- Alpine.js (reactive framework)
- Tailwind CSS (utility-first)

### Backend
- Python HTTP server
- File API endpoints
- JSON data handling

### DevOps
- Git & GitHub
- GitHub Actions (CI/CD)
- Supervisor (process manager)
- Docker & Docker Compose
- Nginx (reverse proxy)
- Linux server management

### Deployment
- Static hosting (GitHub Pages)
- VPS deployment (Supervisor)
- Container orchestration (Docker)

---

## 📝 Environment Variables

```bash
# .env file
PORT=8000
ENVIRONMENT=production
LOG_LEVEL=info
```

---

## 🔒 Security Checklist

- [ ] Use HTTPS (SSL certificate)
- [ ] Configure firewall (ufw)
- [ ] Set proper file permissions
- [ ] Use non-root user
- [ ] Enable rate limiting
- [ ] Regular updates
- [ ] Monitor logs

---

## 📊 Monitoring

### GitHub Pages
- GitHub Actions logs
- GitHub Pages status

### Supervisor
```bash
sudo supervisorctl status
sudo tail -f /var/log/snapcode/access.log
```

### Docker
```bash
docker stats snapcode
docker logs -f snapcode
docker inspect --format='{{.State.Health.Status}}' snapcode
```

---

## 🚨 Troubleshooting

### GitHub Pages not updating?
```bash
# Check Actions
GitHub → Actions → View workflow runs

# Force rebuild
git commit --allow-empty -m "Trigger rebuild"
git push
```

### Supervisor not starting?
```bash
# Check logs
sudo supervisorctl tail snapcode stderr

# Check config
sudo supervisorctl reread
```

### Docker container crashing?
```bash
# Check logs
docker logs snapcode

# Check health
docker inspect snapcode
```

---

## 🎯 Production Checklist

- [ ] Generate file lists (`make build`)
- [ ] Test locally (`make dev`)
- [ ] Configure environment variables
- [ ] Set up SSL certificate
- [ ] Configure firewall
- [ ] Set up monitoring
- [ ] Configure backups
- [ ] Test deployment
- [ ] Monitor logs

---

## 📚 Resources

- [GitHub Pages Docs](https://docs.github.com/pages)
- [Supervisor Docs](http://supervisord.org/)
- [Docker Docs](https://docs.docker.com/)
- [Nginx Docs](https://nginx.org/en/docs/)

---

## 🎉 Summary

**3 Deployment Methods:**
1. **GitHub Pages** - Free, easy, auto-deploy
2. **Supervisor** - VPS, production, full control
3. **Docker** - Containerized, scalable, modern

**All configs included!** Pick one and deploy! 🚀

---

**Made with ❤️ by @sandikodev**  
*Learn by doing!* 💪
