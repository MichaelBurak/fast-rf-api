# sketch, not production-worthy
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
LABEL maintainer="Emily T. Burak -- https://www.emilytburak.com/"
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt
COPY rf.pkl /app 
COPY ./app /app
