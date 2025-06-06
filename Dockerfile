FROM python:3.11-slim

# Imposta working dir
WORKDIR /app

# Copia file
COPY main.py .
COPY requirements.txt .

# Installa dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Espone la porta usata da Flask
EXPOSE 8080

# Avvia il server
CMD ["python", "main.py"]
