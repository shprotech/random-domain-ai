FROM python:3.9.2-alpine3.13

RUN apk --update add bash nano

ENV STATIC_URL /static
ENV STATIC_PATH static

COPY requirements.txt /var/www/requirements.txt
WORKDIR /var/www/domain_app
RUN pip install -r ../requirements.txt

CMD ["python3", "app.py"]
