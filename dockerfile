
# Step 1: Python base image
FROM python:3.12-slim

# Step 2: Application directory
WORKDIR /app

# Step 3: Copy requirements
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy project files
COPY . .

# Step 6: Application port
EXPOSE 5000

# Step 7: Start Python application
CMD ["python", "app.py"]
