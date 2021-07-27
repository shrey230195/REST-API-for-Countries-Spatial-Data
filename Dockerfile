FROM python:3.8.3-slim-buster

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

# Set the default workdir
WORKDIR /usr/src/app

RUN apt update && apt install -y --no-install-recommends \
        libgdal-dev \
        g++ \
        gcc && \
pip install numpy==1.18.1 && \
pip install gdal==2.4.0 && \
        apt remove -y gcc g++ && \
        rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ./wait-for-postgres.sh /usr/src/app/wait-for-postgres.sh

RUN chmod +x ./wait-for-postgres.sh

COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/wait-for-postgres.sh"]