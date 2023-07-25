FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /eduplatform/eduplatform
COPY poetry.lock pyproject.toml /eduplatform/eduplatform/
RUN pip install -U pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install
COPY . .
COPY ../.env ./.env
EXPOSE 8000
