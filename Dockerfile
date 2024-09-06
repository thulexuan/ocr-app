FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY ./app /app

CMD exec gunicorn --bind :$PORT --workers 4 --worker-class uvicorn.workers.UvicornWorker --timeout 300 main:app