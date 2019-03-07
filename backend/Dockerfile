FROM python:3-alpine

EXPOSE 8000

RUN pip install molten requests gunicorn

WORKDIR /src

ADD . /src

CMD ["gunicorn", "--reload", "-b", "0.0.0.0:8000", "--access-logfile", "-", "app:app"]