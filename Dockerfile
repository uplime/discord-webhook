FROM python:3.9
COPY app /app
RUN ["pip3.9", "install", "requests"]
ENTRYPOINT ["python3.9", "/app/driver.py"]
