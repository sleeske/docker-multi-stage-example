ARG PYTHON_VERSION=3.7.0-alpine3.8

FROM python:${PYTHON_VERSION} as builder
ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache \
            --upgrade \
            --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
        alpine-sdk \
        postgresql-dev

WORKDIR /wheels
COPY ./requirements/ /wheels/requirements/
RUN pip install -U pip \
        && pip wheel -r ./requirements/dev.txt


FROM python:${PYTHON_VERSION}
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache \
            --upgrade \
            --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
        gettext \
        libpq \
        postgresql-client \
    && apk add --no-cache \
               --upgrade \
               --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
            geos=3.6.2-r0 \
            proj4=5.0.1-r0 \
            gdal=2.3.1-r0 \
    && ln -s /usr/lib/libproj.so.13 /usr/lib/libproj.so \
    && ln -s /usr/lib/libgdal.so.20 /usr/lib/libgdal.so \
    && ln -s /usr/lib/libgeos_c.so.1 /usr/lib/libgeos_c.so \
    && rm -rf /var/cache/apk/*

COPY --from=builder /wheels /wheels
RUN pip install -U pip \
        && pip install --no-cache-dir \
                       -r /wheels/requirements/dev.txt \
                       -f /wheels \
        && rm -rf /wheels

WORKDIR /code
COPY ./src /code

COPY ./entrypoint.sh /
ENTRYPOINT [ "/entrypoint.sh" ]
