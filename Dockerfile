# Container image that runs your code
FROM python:alpine

RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev 

RUN pip install --no-cache-dir pygithub
COPY entrypoint.py /entrypoint.py

RUN chmod +x /entrypoint.py
ENTRYPOINT ["/entrypoint.py"]