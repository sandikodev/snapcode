# 🚀 PM2 Deployment (JavaScript Runtime Alternative)

## 📦 What is PM2?

PM2 adalah process manager untuk Node.js/JavaScript runtime, tapi bisa juga manage Python apps!

**Alternative to:** Supervisor  
**Best for:** JavaScript developers, Node.js ecosystem

---

## 🎯 Why PM2?

### vs Supervisor
| Feature | PM2 | Supervisor |
|---------|-----|------------|
| **Ecosystem** | JavaScript/Node.js | Python |
| **Config** | JavaScript | INI file |
| **Monitoring** | Built-in dashboard | Log files |
| **Cluster Mode** | ✅ Yes | ❌ No |
| **Zero-downtime** | ✅ Yes | ❌ No |
| **Load Balancing** | ✅ Built-in | ❌ Need external |

---

## 📦 Installation

```bash
# Install PM2 globally
npm install -g pm2

# Or with yarn
yarn global add pm2

# Verify
pm2 --version
```

---

## 🚀 Quick Start

### 1. Basic Start
```bash
# Start app
pm2 start server.py --name snapcode --interpreter python3

# View status
pm2 status

# View logs
pm2 logs snapcode
```

### 2. With Config File
```bash
# Copy config
cp deployment/bare-metal/pm2/ecosystem.config.js .

# Start with config
pm2 start ecosystem.config.js

# Save process list
pm2 save

# Setup startup script
pm2 startup
```

---

## 🔧 Configuration

### ecosystem.config.js
```javascript
module.exports = {
  apps: [{
    name: 'snapcode',
    script: 'server.py',
    interpreter: 'python3',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '500M',
    env: {
      PORT: 8000
    }
  }]
};
```

---

## 📊 Management Commands

```bash
# Start
pm2 start snapcode

# Stop
pm2 stop snapcode

# Restart
pm2 restart snapcode

# Reload (zero-downtime)
pm2 reload snapcode

# Delete
pm2 delete snapcode

# Status
pm2 status

# Logs
pm2 logs snapcode

# Monitor
pm2 monit
```

---

## 🎨 Advanced Features

### 1. Cluster Mode (Multiple Instances)
```javascript
{
  instances: 4,  // or 'max' for CPU cores
  exec_mode: 'cluster'
}
```

### 2. Auto-restart on File Change
```javascript
{
  watch: true,
  ignore_watch: ['node_modules', 'logs']
}
```

### 3. Memory Limit
```javascript
{
  max_memory_restart: '500M'
}
```

### 4. Cron Restart
```javascript
{
  cron_restart: '0 0 * * *'  // Restart daily at midnight
}
```

---

## 📈 Monitoring

### Built-in Monitor
```bash
pm2 monit
```

### Web Dashboard (PM2 Plus)
```bash
pm2 link <secret> <public>
```

### Logs
```bash
# Real-time logs
pm2 logs

# Last 100 lines
pm2 logs --lines 100

# JSON format
pm2 logs --json
```

---

## 🔄 Zero-Downtime Deployment

```bash
# Update code
git pull

# Reload without downtime
pm2 reload snapcode
```

---

## 🎯 Production Setup

```bash
# 1. Start app
pm2 start ecosystem.config.js

# 2. Save process list
pm2 save

# 3. Setup startup script
pm2 startup systemd
# Follow the command output

# 4. Verify
sudo systemctl status pm2-<user>
```

---

## 📊 Comparison with Supervisor

### Supervisor (Python Ecosystem)
```bash
sudo supervisorctl start snapcode
```
- ✅ Native Python tool
- ✅ Simple INI config
- ❌ No cluster mode
- ❌ No zero-downtime reload

### PM2 (JavaScript Ecosystem)
```bash
pm2 start snapcode
```
- ✅ Rich features
- ✅ Built-in monitoring
- ✅ Cluster mode
- ✅ Zero-downtime reload
- ⚠️ Requires Node.js

---

## 🎓 Use Cases

**Choose PM2 if:**
- ✅ You're familiar with Node.js ecosystem
- ✅ You need cluster mode
- ✅ You want zero-downtime deployment
- ✅ You need built-in monitoring

**Choose Supervisor if:**
- ✅ You prefer Python ecosystem
- ✅ You want simple setup
- ✅ You don't need advanced features
- ✅ You're on Linux server

---

## 📝 Example Workflow

```bash
# Development
pm2 start server.py --name snapcode-dev --watch

# Staging
pm2 start ecosystem.config.js --env staging

# Production
pm2 start ecosystem.config.js --env production
pm2 save
pm2 startup
```

---

**Status:** ✅ PM2 Alternative Ready!
