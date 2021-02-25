FROM python:3.9
WORKDIR /
RUN pip install flask

COPY . .
CMD [ "python3", "app.py" ]
