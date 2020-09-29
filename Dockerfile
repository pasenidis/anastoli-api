FROM python:3.8

WORKDIR /app

COPY src/requirements.txt ./

RUN pip install -r requirements.txt

COPY src /app

EXPOSE 8000
CMD [ "cd", "/app" ]
CMD [ "hypercorn", "run:app" ]
