# Use a lightweight Python base
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy app files into container
COPY app/ /app/
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the agent when container starts
CMD ["python", "agent.py"]