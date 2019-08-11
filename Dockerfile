FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3 python3-numpy
RUN apt-get -y install python3-pip

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY colourtest.py .

CMD ["python3", "colourtest.py"]

