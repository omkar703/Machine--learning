FROM python:3.8-alpine
# Set the working directory
COPY . /app 
# from local repo copy all to app repo
WORKDIR /app
# set working dir to /app
RUN pip install -r requirements.txt
CMD python app.py