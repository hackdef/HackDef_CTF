FROM python:3

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY . .

ENV FLAG="hackdef{c00k1es_&_A3s-ECB_b4D_1d34}" 

#
RUN pip install -r requirements.txt
#
CMD ["python","app.py"]


EXPOSE 5000


#docker build . -t node-crypto-200
