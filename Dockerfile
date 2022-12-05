FROM python:3.9
COPY call-webhook.py ./call-webhook.py
RUN ["pip3.9", "install", "requests"]
ENTRYPOINT ["python3.9", "./call-webhook.py"]
