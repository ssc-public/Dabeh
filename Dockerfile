FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Run Gunicorn with 3 workers when the container starts
CMD ["gunicorn", "--bind", "0.0.0.0:8001", "--workers", "2", "dabeh.wsgi"]
