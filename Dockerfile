FROM python:3.12-slim
WORKDIR /app
COPY app/ /app/
EXPOSE 8081
CMD ["python", "server.py"]
