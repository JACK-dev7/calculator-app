
FROM python:3.14

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY calculator/ calculator/
COPY tests/ tests/

CMD ["python", "-m", "pytest", "-v"]
