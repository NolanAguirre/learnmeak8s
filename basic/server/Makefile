.PHONY: help start test docker-build docker-run docker-test docker-stop docker-clean

help:
	@echo "Available targets:"
	@echo "  start         Start the express server using environment variables in env-dev/"
	@echo "  test          Run tests (currently placeholder)"
	@echo "  docker-build  Build the Docker image"
	@echo "  docker-run    Run the Docker container using base image (no build required)"
	@echo "  docker-test   Test the running Docker container with curl"
	@echo "  docker-stop   Stop the Docker container"
	@echo "  docker-clean  Remove the Docker container and image"
	@echo "  help          Show this help message"

start:
	@echo "Starting server with env-dev variables..."
	envdir ./env-dev node index.js

test:
	@echo "No tests defined yet."

docker-build:
	@echo "Building Docker image..."
	docker build -t express-server .

docker-run:
	@echo "Starting Docker container using base Node.js image..."
	docker run -d -p 5007:5007 --name express-server-container \
		-v $(PWD):/app \
		-w /app \
		-e HOST=0.0.0.0 \
		-e PORT=5007 \
		node:18-alpine \
		sh -c "npm install && node index.js"
	@echo "Container started. Waiting for server to be ready..."
	@sleep 5
	@echo "Server should be ready at http://localhost:5007"

docker-test:
	@echo "Testing Docker container with curl..."
	@echo "Testing root endpoint..."
	@curl -s http://localhost:5007/ | jq . || curl -s http://localhost:5007/
	@echo ""
	@echo "Testing health endpoint..."
	@curl -s http://localhost:5007/health | jq . || curl -s http://localhost:5007/health
	@echo ""
	@echo "Testing with verbose output:"
	@curl -v http://localhost:5007/health

docker-stop:
	@echo "Stopping Docker container..."
	docker stop express-server-container || echo "Container not running or already stopped"

docker-clean:
	@echo "Cleaning up Docker container and image..."
	docker stop express-server-container 2>/dev/null || true
	docker rm express-server-container 2>/dev/null || true
	docker rmi express-server 2>/dev/null || true
	@echo "Cleanup complete"
