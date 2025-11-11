FROM python:3.12

WORKDIR /app

# copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy application files
COPY main.py .
COPY public/ ./public/

# Run the application
CMD ["python3", "main.py"]
