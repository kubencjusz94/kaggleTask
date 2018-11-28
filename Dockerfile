FROM ubuntu
ADD . /task
WORKDIR /task

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    unzip
RUN pip3 install -r requirements.txt
RUN mkdir ~/.kaggle
RUN echo '{"username":"septt48","key":"c0e2e64e4b92dc52fdaf68973403176b"}' > ~/.kaggle/kaggle.json

RUN kaggle datasets download -d san-francisco/sf-police-calls-for-service-and-incidents
RUN mkdir data
RUN unzip sf-police-calls-for-service-and-incidents.zip -d data
