# 🖥️ Bare Metal / Native Deployment Guide

## 📚 Table of Contents

1. [Process Managers](#process-managers)
   - Supervisor (Python)
   - PM2 (JavaScript)
2. [Reverse Proxies](#reverse-proxies)
   - Nginx
   - Traefik
   - HAProxy
3. [Comparison](#comparison)

---

## 🔧 Process Managers

### 1. Supervisor (Python Ecosystem)

**Best for:** Python developers, simple setup

```bash
sudo apt install supervisor
sudo cp ../supervisor/snapcode.conf /etc/supervisor/conf.d/
sudo supervisorctl start snapcode
```

**Features:**
- ✅ Native Python tool
- ✅ Simple INI config
- ✅ Auto-restart on crash
- ✅ Log management

📖 [Supervisor Guide](../supervisor/README.md)

---

### 2. PM2 (JavaScript Ecosystem)

**Best for:** Node.js developers, advanced features

```bash
npm install -g pm2
pm2 start server.py --name snapcode --interpreter python3
pm2 save
pm2 startup
```

**Features:**
- ✅ Cluster mode
- ✅ Zero-downtime reload
- ✅ Built-in monitoring
- ✅ Load balancing

📖 [PM2 Guide](pm2/README.md)

---

## 🌐 Reverse Proxies

### Why Reverse Proxy?

```
Client → Reverse Proxy → Backend Server(s)
```

**Benefits:**
- ✅ SSL/TLS termination
- ✅ Load balancing
- ✅ Caching
- ✅ Security (hide backend)
- ✅ Compression

---

### 1. Nginx (Most Popular)

**Best for:** General purpose, high performance

```bash
sudo apt install nginx
sudo cp nginx/snapcode.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/snapcode.conf /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

**Features:**
- ✅ High performance
- ✅ Simple config
- ✅ Static file serving
- ✅ Load balancing
- ✅ Caching

**Use Cases:**
- Static file serving
- Simple reverse proxy
- Load balancing
- SSL termination

📖 [Nginx Configs](nginx/)

---

### 2. Traefik (Modern, Cloud-Native)

**Best for:** Microservices, Docker, auto-discovery

```bash
# Install
wget https://github.com/traefik/traefik/releases/download/v2.10.0/traefik_v2.10.0_linux_amd64.tar.gz
tar -xzf traefik_v2.10.0_linux_amd64.tar.gz
sudo mv traefik /usr/local/bin/

# Configure
sudo cp traefik/traefik.yml /etc/traefik/
sudo cp traefik/dynamic.yml /etc/traefik/

# Start
traefik --configFile=/etc/traefik/traefik.yml
```

**Features:**
- ✅ Auto SSL (Let's Encrypt)
- ✅ Dynamic configuration
- ✅ Built-in dashboard
- ✅ Service discovery
- ✅ Middleware support

**Use Cases:**
- Microservices
- Docker/Kubernetes
- Auto SSL management
- Dynamic routing

📖 [Traefik Configs](traefik/)

---

### 3. HAProxy (High Performance)

**Best for:** High traffic, advanced load balancing

```bash
sudo apt install haproxy
sudo cp haproxy/haproxy.cfg /etc/haproxy/
sudo systemctl restart haproxy
```

**Features:**
- ✅ Highest performance
- ✅ Advanced load balancing
- ✅ Health checks
- ✅ Stats dashboard
- ✅ Connection pooling

**Use Cases:**
- High traffic sites
- Advanced load balancing
- TCP/HTTP load balancing
- Performance critical apps

📖 [HAProxy Configs](haproxy/)

---

## 📊 Comparison

### Process Managers

| Feature | Supervisor | PM2 |
|---------|-----------|-----|
| **Ecosystem** | Python | JavaScript |
| **Config** | INI | JavaScript |
| **Cluster Mode** | ❌ | ✅ |
| **Zero-downtime** | ❌ | ✅ |
| **Monitoring** | Logs | Dashboard |
| **Setup** | Easy | Easy |
| **Best for** | Python devs | Node.js devs |

---

### Reverse Proxies

| Feature | Nginx | Traefik | HAProxy |
|---------|-------|---------|---------|
| **Performance** | High | Medium | Highest |
| **Config** | Simple | YAML | Complex |
| **Auto SSL** | Manual | ✅ Built-in | Manual |
| **Dashboard** | ❌ | ✅ | ✅ |
| **Docker** | Manual | ✅ Auto | Manual |
| **Learning Curve** | Easy | Medium | Hard |
| **Best for** | General | Microservices | High traffic |

---

## 🎯 Recommended Stacks

### Stack 1: Simple & Popular
```
Supervisor + Nginx
```
- ✅ Easy to learn
- ✅ Well documented
- ✅ Production ready
- ✅ Python ecosystem

### Stack 2: Modern & Dynamic
```
PM2 + Traefik
```
- ✅ Auto SSL
- ✅ Zero-downtime
- ✅ Modern features
- ✅ JavaScript ecosystem

### Stack 3: High Performance
```
Supervisor + HAProxy
```
- ✅ Maximum performance
- ✅ Advanced load balancing
- ✅ High traffic ready
- ✅ Enterprise grade

---

## 🚀 Quick Start Examples

### Example 1: Nginx + Supervisor
```bash
# 1. Start app with Supervisor
sudo supervisorctl start snapcode

# 2. Setup Nginx
sudo cp nginx/snapcode.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/snapcode.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx

# 3. Setup SSL
sudo certbot --nginx -d snapcode.yourdomain.com
```

### Example 2: Traefik + PM2
```bash
# 1. Start app with PM2
pm2 start ecosystem.config.js
pm2 save

# 2. Setup Traefik
sudo cp traefik/*.yml /etc/traefik/
traefik --configFile=/etc/traefik/traefik.yml
```

### Example 3: HAProxy + Supervisor
```bash
# 1. Start multiple instances
sudo supervisorctl start snapcode:*

# 2. Setup HAProxy
sudo cp haproxy/haproxy.cfg /etc/haproxy/
sudo systemctl restart haproxy

# 3. View stats
# Visit: http://your-server:8404/stats
```

---

## 🎓 Learning Path

### Beginner
1. Start with **Supervisor + Nginx**
2. Learn basic reverse proxy
3. Setup SSL with Let's Encrypt

### Intermediate
1. Try **PM2** for zero-downtime
2. Explore **Traefik** for auto SSL
3. Setup load balancing

### Advanced
1. Master **HAProxy** for performance
2. Implement connection pooling
3. Advanced load balancing strategies

---

## 📝 Load Balancing Strategies

### 1. Round Robin (Default)
```
Request 1 → Server 1
Request 2 → Server 2
Request 3 → Server 3
Request 4 → Server 1 (repeat)
```

### 2. Least Connections
```
Request → Server with fewest active connections
```

### 3. IP Hash
```
Same client IP → Always same server
(Sticky sessions)
```

### 4. Weighted
```
Server 1 (weight 3) → 50% traffic
Server 2 (weight 2) → 33% traffic
Server 3 (weight 1) → 17% traffic
```

---

## 🔍 Connection Pooling

**What:** Reuse connections instead of creating new ones

**Benefits:**
- ✅ Reduced latency
- ✅ Lower resource usage
- ✅ Better performance

**Implementation:**
- Nginx: `keepalive` directive
- HAProxy: `http-reuse` directive
- Traefik: Built-in

---

## 📊 Monitoring

### Nginx
```bash
# Access logs
tail -f /var/log/nginx/access.log

# Error logs
tail -f /var/log/nginx/error.log

# Status module
curl http://localhost/nginx_status
```

### Traefik
```bash
# Dashboard
http://localhost:8080/dashboard/

# API
curl http://localhost:8080/api/http/routers
```

### HAProxy
```bash
# Stats page
http://localhost:8404/stats

# Socket commands
echo "show stat" | socat stdio /run/haproxy/admin.sock
```

---

## 🎯 Summary

**Choose your stack based on:**

1. **Ecosystem familiarity**
   - Python → Supervisor
   - JavaScript → PM2

2. **Requirements**
   - Simple → Nginx
   - Modern → Traefik
   - Performance → HAProxy

3. **Scale**
   - Small → Supervisor + Nginx
   - Medium → PM2 + Traefik
   - Large → Supervisor + HAProxy

---

**All configs included!** Pick your stack and deploy! 🚀
