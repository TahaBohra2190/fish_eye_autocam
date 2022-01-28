FROM python:3.9.9-slim-buster

EXPOSE 5000

WORKDIR /home/

COPY src ./src/

RUN apt-get update \
    && apt-get -y install --reinstall build-essential \
    && apt-get install -y gcc python-opencv 

COPY LICENSE requirements.txt ./

RUN pip install --no-cache-dir wheel \
    && pip install --no-cache-dir -r requirements.txt

COPY src ./src/

WORKDIR /home/src/

CMD ["python", "main.py"]