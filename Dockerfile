FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./deployment /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py"]
