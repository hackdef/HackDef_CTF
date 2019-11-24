FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN echo "HackDef{SSTI_th3_n3w_SQLi}" >> /tmp/flag
ENTRYPOINT ["python"]
CMD ["app.py"]
