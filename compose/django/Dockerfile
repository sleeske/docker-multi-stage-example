ARG PYTHON_VERSION=3.7.0-alpine3.8

FROM python:${PYTHON_VERSION}
ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache \
            --upgrade \
            --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
        alpine-sdk \
        postgresql-dev \
        postgresql-client \
        libpq \
        gettext \
    && apk add --no-cache \
               --upgrade \
               --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
        geos \
        proj4 \
        gdal \
    && ln -s /usr/lib/libproj.so.13 /usr/lib/libproj.so \
    && ln -s /usr/lib/libgdal.so.20 /usr/lib/libgdal.so \
    && ln -s /usr/lib/libgeos_c.so.1 /usr/lib/libgeos_c.so

COPY ./requirements /tmp/requirements
RUN pip install -U pip \
    && pip install -r /tmp/requirements/dev.txt

COPY ./entrypoint.sh /

WORKDIR /code
COPY ./src /code

ENTRYPOINT [ "/entrypoint.sh" ]
