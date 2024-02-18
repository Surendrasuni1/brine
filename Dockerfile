FROM python:3.9-slim
WORKDIR /app
COPY task.py /app
COPY orders.csv /app
CMD ["python", "main.py"]