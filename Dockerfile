FROM python:2

WORKDIR /app

COPY . /app

ENTRYPOINT ["/bin/bash"]
