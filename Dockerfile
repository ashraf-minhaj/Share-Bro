FROM python:3.7-alpine3.16

WORKDIR /API

COPY API/requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
# CMD [ "echo hellow-bro'" ]
RUN python3 -m flask run --host=0.0.0.0
