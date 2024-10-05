FROM python:3.12

WORKDIR /server

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./server /server 

#--- TODO: Remove this env copy step in prod
COPY ./.env /server/.env 

RUN pip install  -r /server/requirements.txt

RUN python3 /server/manage.py collectstatic


CMD ["gunicorn", "--bind", "0.0.0.0:8080", "core.wsgi:application","--workers", "4", "--reload"]
