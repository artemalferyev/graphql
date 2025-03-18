FROM python:3.10 AS app

WORKDIR /

COPY . .

RUN pip install pytest --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "GrahQL:app", "--host", "0.0.0.0", "--port", "8000"]