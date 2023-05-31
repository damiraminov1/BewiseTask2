FROM python:3.11-slim-buster

WORKDIR /etc/opt/site/

COPY . .

RUN pip install poetry==1.5.0
RUN poetry install --with production

EXPOSE 5000
ENTRYPOINT ["bash", "entrypoint.sh"]