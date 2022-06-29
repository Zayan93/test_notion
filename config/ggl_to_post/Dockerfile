FROM python:3.9.6-alpine
WORKDIR /opt/ggl
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN apk --no-cache add \
#    icu-dev \
#    gettext \
#    gettext-dev

RUN pip install --upgrade pip
COPY ./ggl_to_psql/requirements.txt .
RUN pip install -r requirements.txt