FROM python:3.11-slim

WORKDIR /app

# Copia lo script e il log da analizzare
COPY main.py .
COPY access.log .

# Esegui lo script all'avvio
CMD ["python", "main.py"]
