FROM python:3.11.3-slim
LABEL mantainer="walefy@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY biblioteca /biblioteca

WORKDIR /biblioteca


EXPOSE 8080


RUN pip install --upgrade pip && \
    pip install -r /biblioteca/requirements.txt




CMD ["sh", "-c", "python manage.py collectstatic --noinput && python manage.py makemigrations --noinput && python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8080"]