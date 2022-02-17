FROM python:3.10

WORKDIR /test_url

COPY . /test_url


RUN pip3 install -r requirements.txt


COPY . /test_url

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
