.PHONY: help build dev deploy-github deploy-docker deploy-supervisor clean

help: ## Show this help
	@echo "SnapCode - Deployment Commands"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

build: ## Generate file lists
	@echo "🔨 Building..."
	python3 build.py
	@echo "✅ Build complete!"

dev: ## Run local development server
	@echo "🚀 Starting dev server..."
	python3 server.py

deploy-github: build ## Deploy to GitHub Pages
	@echo "📦 Deploying to GitHub Pages..."
	git add .
	git commit -m "Deploy: $$(date '+%Y-%m-%d %H:%M:%S')" || true
	git push origin main
	@echo "✅ Deployed to GitHub Pages!"

deploy-docker: build ## Deploy with Docker Compose
	@echo "🐳 Deploying with Docker..."
	docker-compose up -d --build
	@echo "✅ Docker deployment complete!"
	@echo "🌐 Access: http://localhost:8000"

deploy-docker-nginx: build ## Deploy with Docker + Nginx
	@echo "🐳 Deploying with Docker + Nginx..."
	docker-compose --profile with-nginx up -d --build
	@echo "✅ Docker + Nginx deployment complete!"
	@echo "🌐 Access: http://localhost"

deploy-supervisor: build ## Deploy with Supervisor
	@echo "🖥️  Deploying with Supervisor..."
	sudo cp deployment/supervisor/snapcode.conf /etc/supervisor/conf.d/
	sudo supervisorctl reread
	sudo supervisorctl update
	sudo supervisorctl restart snapcode
	@echo "✅ Supervisor deployment complete!"

logs-docker: ## View Docker logs
	docker-compose logs -f

logs-supervisor: ## View Supervisor logs
	sudo tail -f /var/log/snapcode/access.log

stop-docker: ## Stop Docker containers
	docker-compose down

stop-supervisor: ## Stop Supervisor service
	sudo supervisorctl stop snapcode

restart-docker: ## Restart Docker containers
	docker-compose restart

restart-supervisor: ## Restart Supervisor service
	sudo supervisorctl restart snapcode

status-docker: ## Check Docker status
	docker-compose ps

status-supervisor: ## Check Supervisor status
	sudo supervisorctl status snapcode

clean: ## Clean build artifacts
	@echo "🧹 Cleaning..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	@echo "✅ Clean complete!"

test: ## Test the application
	@echo "🧪 Testing..."
	@echo "Testing file generation..."
	python3 build.py
	@echo "Testing server..."
	timeout 2 python3 server.py || true
	@echo "✅ Tests complete!"
