FROM python:3.7-slim
WORKDIR /opt/ggl

#RUN apk --no-cache add \
#    icu-dev \
#    gettext \
#    gettext-dev

RUN pip install --upgrade pip
COPY ./ggl_to_psql/requirements.txt .
RUN pip install -r requirements.txt