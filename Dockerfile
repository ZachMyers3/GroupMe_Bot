FROM python:3.9-slim-buster
RUN apt-get update \
    && apt-get install --yes --no-install-recommends \
    curl gfortran build-essential
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry
RUN mkdir /app/
RUN mkdir /app/src/
RUN mkdir /app/logs/
RUN mkdir /app/tags/
COPY src/* app/src/
COPY ./pyproject.toml ./poetry.lock* /app/
WORKDIR /app
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev
CMD ["python","src/start.py", "-c", "config.ini", "-g", "groups.json"]
