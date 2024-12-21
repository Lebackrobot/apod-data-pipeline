FROM python:3.12

ENV TZ=America/Sao_Paulo

COPY . .

RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
