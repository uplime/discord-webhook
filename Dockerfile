FROM python:3.9
COPY discord-webhook.py /app/discord-webhook.py
COPY discohook/* /app/discohook/
RUN ["pip3.9", "install", "requests"]
ENTRYPOINT ["python3.9", "/app/discord-webhook.py"]
