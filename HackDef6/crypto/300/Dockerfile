
FROM python:3

# Create app directory
WORKDIR /usr/src/app

COPY . .

ENV FLAG="hackdef{Rs4_&_H0mOMorF1Smo_1ns3Gur0}" 

#
RUN pip install -r requirements.txt
#
CMD ["python","app.py"]


EXPOSE 5000

#docker build . -t node-crypto-300

#sudo docker run -p 4004:5000 -d node-crypto-300
