FROM python:3.10-slim-buster

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=nobody:nogroup . /usr/src/app
USER nobody
WORKDIR /usr/src/app
VOLUME /usr/src/app/db
EXPOSE 8000
RUN python manage.py collectstatic --no-input
CMD sh -c "python manage.py migrate && python manage.py runserver 0:8000"
