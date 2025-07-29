### flask app for hello world
from flask import Flask
import os 

app = Flask(__name__)
@app.route('/',methods=['GET'])
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True , host = "0.0.0.0", port = 5000) 



# build an app
# docker build -t welcome-app .


# see images
# docker images

# run the docker image
#docker run -d -p 5000:5000 welcome-app


# check the running container
#docker ps


# remove images 
#docker image rm -f welcome-app

# change the name of the container
#docker tag welcome-app megathree/welcome-app

# stop docker image
#docker stop <container_id>


# push the docker image to docker hub
#docker build -t megathree/welcome-app .
#docker push megathree/welcome-app:latest 