FROM python:3.11-alpine

WORKDIR /apps

COPY . /apps

RUN pip install -r req.txt

ENTRYPOINT ["python", "bot.py"]