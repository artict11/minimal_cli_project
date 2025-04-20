FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir typer
CMD ["python", "main.py", "generate", "hello.md"]
