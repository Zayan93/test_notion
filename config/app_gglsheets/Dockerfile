FROM python:3.9.6-alpine
WORKDIR /var/www/gglsheets_admin
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./gglsheets/requirements.txt .
RUN pip install -r requirements.txt
COPY ./config/app_gglsheets/entrypoint.sh /usr/local/bin
EXPOSE 8000