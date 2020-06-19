FROM python:latest
ADD . /lora_receiver
WORKDIR /lora_receiver
RUN pip install -r library.txt
