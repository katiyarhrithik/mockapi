FROM python:3.13-alpine
ENV PYTHONUNBUFFERED 1
# Creating working directory
RUN mkdir /code
WORKDIR /code
COPY ./ .

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]
