FROM python:slim

WORKDIR /app

EXPOSE 2024

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["langgraph" , "dev", "--host", "0.0.0.0", "--port", "2024"]