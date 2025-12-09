# 🐳 Docker Deployment

## 📦 Prerequisites

```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo apt install docker-compose
```

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)
```bash
# Build and start
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

### Option 2: Docker Only
```bash
# Build image
docker build -t snapcode .

# Run container
docker run -d -p 8000:8000 --name snapcode snapcode

# View logs
docker logs -f snapcode

# Stop
docker stop snapcode
docker rm snapcode
```

### Option 3: With Nginx
```bash
# Start with nginx profile
docker-compose --profile with-nginx up -d

# Access via nginx
http://localhost
```

## 🔧 Management

```bash
# View running containers
docker ps

# View logs
docker-compose logs -f snapcode

# Restart
docker-compose restart snapcode

# Update
git pull
docker-compose up -d --build

# Shell access
docker exec -it snapcode sh
```

## 📊 Monitoring

```bash
# Container stats
docker stats snapcode

# Health check
docker inspect --format='{{.State.Health.Status}}' snapcode

# Logs
docker logs --tail 100 snapcode
```

## 🌐 Production Setup

### 1. Environment Variables
```bash
# Create .env file
cat > .env << EOF
PORT=8000
ENVIRONMENT=production
EOF
```

### 2. Docker Compose Override
```yaml
# docker-compose.override.yml
version: '3.8'
services:
  snapcode:
    environment:
      - ENVIRONMENT=production
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
```

### 3. SSL with Let's Encrypt
```bash
# Use certbot
docker run -it --rm \
  -v /etc/letsencrypt:/etc/letsencrypt \
  certbot/certbot certonly --standalone \
  -d snapcode.yourdomain.com
```

## 🎯 Features
- ✅ Isolated environment
- ✅ Easy deployment
- ✅ Auto-restart
- ✅ Health checks
- ✅ Resource limits
- ✅ Scalable

## 📦 Docker Hub (Optional)

```bash
# Build
docker build -t sandikodev/snapcode:latest .

# Push
docker push sandikodev/snapcode:latest

# Pull & Run
docker run -d -p 8000:8000 sandikodev/snapcode:latest
```

## 🔍 Troubleshooting

```bash
# Check logs
docker-compose logs snapcode

# Rebuild
docker-compose up -d --build --force-recreate

# Clean up
docker system prune -a
```
