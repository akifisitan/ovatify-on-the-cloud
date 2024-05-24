ARG PYTHON_VERSION=3.11-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
  pip install --upgrade pip && \
  pip install -r /tmp/requirements.txt && \
  rm -rf /root/.cache/
COPY . /code

EXPOSE 8089

# Parameterize the Locust file name
# ARG LOCUST_FILE
# ENV LOCUST_FILE ${LOCUST_FILE}

# CMD ["locust", "-f", "${LOCUST_FILE}", "--host", "http://0.0.0.0:8089"]
CMD ["locust"]
