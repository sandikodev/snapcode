# 🖥️ Supervisor Deployment (Self-Hosted)

## 📦 Prerequisites

```bash
# Install supervisor
sudo apt update
sudo apt install supervisor python3

# Create log directory
sudo mkdir -p /var/log/snapcode
sudo chown www-data:www-data /var/log/snapcode
```

## 🚀 Setup

### 1. Clone Repository
```bash
cd /var/www
sudo git clone https://github.com/sandikodev/snapcode.git
cd snapcode
```

### 2. Configure Supervisor
```bash
# Copy config
sudo cp deployment/supervisor/snapcode.conf /etc/supervisor/conf.d/

# Edit paths
sudo nano /etc/supervisor/conf.d/snapcode.conf
# Change: /path/to/snapcode.me → /var/www/snapcode
```

### 3. Start Service
```bash
# Reload supervisor
sudo supervisorctl reread
sudo supervisorctl update

# Start snapcode
sudo supervisorctl start snapcode

# Check status
sudo supervisorctl status snapcode
```

## 🔧 Management

```bash
# Start
sudo supervisorctl start snapcode

# Stop
sudo supervisorctl stop snapcode

# Restart
sudo supervisorctl restart snapcode

# View logs
sudo tail -f /var/log/snapcode/access.log
```

## 🌐 Nginx Reverse Proxy (Optional)

```nginx
server {
    listen 80;
    server_name snapcode.yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 🎯 Features
- ✅ Auto-restart on crash
- ✅ Log management
- ✅ Process monitoring
- ✅ Production-ready

## 📊 Monitoring
```bash
# CPU/Memory usage
ps aux | grep server.py

# Logs
sudo supervisorctl tail snapcode
```
