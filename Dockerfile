# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Set PYTHONPATH so Python can find the src folder
ENV PYTHONPATH=/app/src

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and models
COPY ./src ./src
COPY ./models ./models

# Make sure model files have correct permissions
RUN chmod -R 755 /app/models

# Expose port
EXPOSE 9696

# Run Uvicorn
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "9696", "--reload"]
