FROM python:3.12-alpine

WORKDIR /usr/src/app

COPY main.py .

ENV APP_ENV="Staging"
ENV DATA_LIMIT="100"

CMD ["python", "main.py"]