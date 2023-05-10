FROM python:3.9
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /code/app
COPY ./templates /code/templates
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app.main:app
