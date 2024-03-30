FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip \
    pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src .

CMD ["streamlit", "run", "src/main.py"]