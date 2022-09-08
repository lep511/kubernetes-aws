FROM python:3.9-slim-buster

# needed to capture stderr output
# https://github.com/bottlepy/bottle/issues/1130#issuecomment-478096704
# https://stackoverflow.com/a/59812588/109102
ENV PYTHONUNBUFFERED=1 
ENV BUCKET_NAME="my-data-bucket4-3030"
COPY app /app

WORKDIR /app

RUN pip3 install -r requirements.txt && \
    apt update  && \
    apt install -y procps curl dnsutils

CMD [ "python", "./message.py" ]
EXPOSE 8080
