FROM python:latest

WORKDIR /API

COPY requirements.txt /API

RUN pip3 install -r requirements.txt

# COPY app.py .
COPY . . 

# RUN pip install --no-cache-dir -r requirements.txt -t .
# EXPOSE 8080

# CMD [ "flask", "run", "--host=0.0.0.0" ]
CMD [ "python3", "main.py" ]