FROM python:3.10-slim-buster

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=nobody:nogroup . /usr/src/app
WORKDIR /usr/src/app
VOLUME /usr/src/app/db
USER nobody
EXPOSE 8000
CMD sh -c "python manage.py migrate && python manage.py runserver 0:8000"
