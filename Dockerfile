FROM ubuntu:14.04
ADD . /task
WORKDIR /task

RUN apt-get update && apt-get install -y \
    python-pip
RUN pip install -r requirements.txt
RUN mkdir ~/.kaggle
RUN echo '{"username":"septt48","key":"c0e2e64e4b92dc52fdaf68973403176b"}' > ~/.kaggle/kaggle.json

RUN kaggle datasets download -d san-francisco/sf-police-calls-for-service-and-incidents
RUN mkdir data
RUN unzip san-francisco/sf-police-calls-for-service-and-incidents.zip data
