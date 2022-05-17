FROM python:3.9-alpine

WORKDIR /code

COPY . /code

RUN apk add --update tesseract-ocr build-base

RUN pip install setuptools && pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
