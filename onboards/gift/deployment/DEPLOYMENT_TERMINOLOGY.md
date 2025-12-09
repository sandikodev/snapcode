# 📚 Deployment Terminology

## 🎯 Istilah yang Tepat

### 1. **Bare Metal / Native Deployment**
**Istilah:** Bare Metal, Native, Self-Hosted

Deploy langsung di server tanpa kontainer/virtualisasi.

**Contoh:**
- VPS dengan Supervisor
- Dedicated server
- Physical server

**Karakteristik:**
- ✅ Akses langsung ke OS
- ✅ Full control
- ✅ No overhead
- ⚠️ Manual dependency management

**SnapCode:** `python3 server.py` + Supervisor

---

### 2. **Containerized Deployment**
**Istilah:** Containerized, Docker-based

Deploy dalam container (Docker, Podman, etc).

**Contoh:**
- Docker
- Docker Compose
- Kubernetes
- Podman

**Karakteristik:**
- ✅ Isolated environment
- ✅ Portable
- ✅ Easy scaling
- ⚠️ Container overhead

**SnapCode:** `docker-compose up -d`

---

### 3. **Static Hosting / JAMstack**
**Istilah:** Static Hosting, JAMstack, CDN Hosting

Deploy sebagai static files tanpa server-side processing.

**Contoh:**
- GitHub Pages
- Vercel
- Netlify
- Cloudflare Pages
- AWS S3 + CloudFront

**Karakteristik:**
- ✅ No server needed
- ✅ CDN distribution
- ✅ Auto-scaling
- ✅ Free tier available
- ⚠️ Static only (no backend)

**SnapCode:** `git push` → Auto-deploy

---

## 📊 Comparison Table

| Type | Terminology | SnapCode Example | Best For |
|------|-------------|------------------|----------|
| **Bare Metal** | Native, Self-Hosted | Supervisor on VPS | Full control |
| **Container** | Containerized | Docker Compose | DevOps, Scaling |
| **Static** | JAMstack, CDN | GitHub Pages | Frontend apps |

---

## 🏗️ SnapCode Deployment Types

### Type 1: **Bare Metal Deployment**
```bash
# Native/Self-Hosted
sudo supervisorctl start snapcode
```

**Terms:**
- ✅ Bare Metal
- ✅ Native Deployment
- ✅ Self-Hosted
- ✅ On-Premise (if own hardware)

---

### Type 2: **Containerized Deployment**
```bash
# Docker-based
docker-compose up -d
```

**Terms:**
- ✅ Containerized
- ✅ Docker Deployment
- ✅ Container Orchestration (if K8s)

---

### Type 3: **Static Hosting**
```bash
# JAMstack
git push origin main
```

**Terms:**
- ✅ Static Hosting
- ✅ JAMstack Deployment
- ✅ CDN Hosting
- ✅ Serverless (technically)
- ✅ Edge Deployment

---

## 🎓 Industry Terms

### Bare Metal
```
Physical Server → OS → Application
```
- **Also called:** Native, Self-Hosted, On-Premise
- **Example:** VPS, Dedicated Server

### Virtualized
```
Physical Server → Hypervisor → VM → OS → Application
```
- **Also called:** VM-based, Virtual Machine
- **Example:** AWS EC2, DigitalOcean Droplet

### Containerized
```
Physical Server → OS → Container Runtime → Container → Application
```
- **Also called:** Docker-based, Container Orchestration
- **Example:** Docker, Kubernetes, ECS

### Serverless
```
Cloud Provider → Function Runtime → Your Code
```
- **Also called:** FaaS (Function as a Service)
- **Example:** AWS Lambda, Vercel Functions

### Static/JAMstack
```
CDN → Static Files → Browser
```
- **Also called:** Static Hosting, Edge Hosting
- **Example:** GitHub Pages, Vercel, Netlify

---

## 📝 Correct Usage

### ❌ Incorrect:
- "Deploy di host langsung" (ambiguous)
- "Deploy tanpa Docker" (negative definition)
- "Deploy biasa" (unclear)

### ✅ Correct:
- "Bare metal deployment"
- "Native deployment"
- "Self-hosted deployment"
- "Deploy directly on VPS"

---

## 🎯 SnapCode Terminology

### Update Documentation:

**Before:**
```
1. Self-Hosted (Supervisor)
2. Docker
3. GitHub Pages
```

**After:**
```
1. Bare Metal / Native (Supervisor on VPS)
2. Containerized (Docker / Docker Compose)
3. Static Hosting / JAMstack (GitHub Pages, Vercel)
```

---

## 📚 Platform-Specific Terms

### GitHub Pages
- **Type:** Static Hosting
- **Category:** JAMstack
- **Also:** CDN Hosting, Git-based Deployment

### Vercel
- **Type:** Static Hosting + Serverless Functions
- **Category:** JAMstack Platform
- **Also:** Edge Deployment

### Netlify
- **Type:** Static Hosting + Serverless Functions
- **Category:** JAMstack Platform
- **Also:** Continuous Deployment

### AWS S3 + CloudFront
- **Type:** Static Hosting
- **Category:** Object Storage + CDN
- **Also:** Cloud Storage Hosting

### Heroku
- **Type:** PaaS (Platform as a Service)
- **Category:** Managed Hosting
- **Also:** Container-based (uses Docker internally)

### DigitalOcean App Platform
- **Type:** PaaS
- **Category:** Managed Container Platform
- **Also:** Containerized Deployment

---

## 🎨 Visual Hierarchy

```
Deployment Types
│
├── Bare Metal / Native
│   ├── Physical Server
│   ├── VPS (Virtual Private Server)
│   └── Dedicated Server
│
├── Virtualized
│   ├── Virtual Machines (VM)
│   └── Hypervisor-based
│
├── Containerized
│   ├── Docker
│   ├── Kubernetes
│   └── Container Orchestration
│
├── Serverless / FaaS
│   ├── AWS Lambda
│   ├── Vercel Functions
│   └── Cloudflare Workers
│
└── Static Hosting / JAMstack
    ├── GitHub Pages
    ├── Vercel
    ├── Netlify
    └── CDN-based
```

---

## 💡 Summary

**SnapCode supports:**

1. **Bare Metal** (Native/Self-Hosted)
   - Supervisor on VPS
   - Direct OS deployment

2. **Containerized** (Docker-based)
   - Docker Compose
   - Container orchestration

3. **Static Hosting** (JAMstack)
   - GitHub Pages
   - Vercel, Netlify
   - Any CDN hosting

---

**Use these terms in documentation!** ✅
