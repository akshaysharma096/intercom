FROM python:alpine3.8

WORKDIR /code
COPY src /code/src
COPY requirements.txt /code
RUN pip install -r requirements.txt
CMD ["python", "-m", "src"]