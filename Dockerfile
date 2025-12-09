FROM python:3.11-slim

LABEL maintainer="@sandikodev"
LABEL description="SnapCode - Markdown & Code Beautifier"

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Generate file lists
RUN python3 build.py

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:8000')" || exit 1

# Run server
CMD ["python3", "server.py"]
