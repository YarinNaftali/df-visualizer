FROM python:3.10-slim

WORKDIR /fastapi-backend

COPY requirements.txt .

RUN pip install --upgrade pip \
    pip install --no-cache-dir --upgrade -r requirements.txt \
    python -m pytest

COPY ./src .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--forwarded-allow-ips", "*"]