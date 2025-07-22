FROM ghcr.io/marimo-team/marimo:latest

WORKDIR /app

COPY --link requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["marimo", "edit", "--no-token", "-p", "8000", "--host", "0.0.0.0"]