FROM ubuntu

ADD . /task
WORKDIR /task

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    unzip
RUN pip3 install -r requirements.txt

RUN mkdir ~/.kaggle
RUN echo '{"username":"septt48","key":"474ecb35a12086a911a215983704b886"}' >> ~/.kaggle/kaggle.json


RUN kaggle datasets download -d san-francisco/sf-police-calls-for-service-and-incidents
RUN mkdir data
RUN unzip sf-police-calls-for-service-and-incidents.zip -d data
