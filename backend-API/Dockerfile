FROM python:latest

WORKDIR /API

# COPY requirements.txt requirements.txt
# COPY app.py .
COPY . . 

RUN pip3 install -r requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt -t .

CMD [ "flask", "run", "--host=0.0.0.0" ]