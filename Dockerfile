FROM python:3.10-alpine

WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml ./

RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev cargo && pip install --no-cache-dir poetry && poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi -vvv && apk del gcc musl-dev python3-dev libffi-dev openssl-dev cargo
COPY . .

WORKDIR /usr/src/app

CMD [ "python", "-m", "robocop_ng", "/state" ]
