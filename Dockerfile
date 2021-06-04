FROM python:3.9

WORKDIR /app

RUN pip install bs4 requests

COPY index.py .

ENTRYPOINT ["python", "index.py"]
