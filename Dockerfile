FROM python:2

WORKDIR /app

COPY . /app

RUN pip install semver

ENTRYPOINT ["entrypoint.sh"]
