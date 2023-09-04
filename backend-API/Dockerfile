FROM python:3.10

WORKDIR /API

COPY requirements.txt /API

RUN pip3 install -r requirements.txt

COPY . . 

# CMD [ "flask", "run", "--host=0.0.0.0" ]
CMD [ "python3", "main.py" ]