# Layer 1: Base image — slim Python to keep image small
FROM python:3.11-slim

# Layer 2: Set working directory inside the container
WORKDIR /app

# Layer 3: Copy dependency list first (better caching)
COPY requirements.txt .

# Layer 4: Install dependencies
# (this layer is cached until requirements.txt changes)
RUN pip install --no-cache-dir -r requirements.txt

# Layer 5: Copy app code (changes most often — put last)
COPY . .

# Document which port the app listens on
EXPOSE 5000

# Set an environment variable
ENV APP_ENV=production

# Command to run when container starts
CMD ["python", "app.py"]
