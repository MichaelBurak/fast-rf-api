# in development -- not currently working
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
LABEL maintainer="Emily T. Burak -- https://www.emilytburak.com/"
COPY ./app /app
RUN pip3 install -r requirements.txt