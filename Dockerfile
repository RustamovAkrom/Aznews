FROM python:3.10.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /Aznews

COPY . .

RUN pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate

EXPOSE 8000

CMD [ "python", "manage.py", "runserver" ]