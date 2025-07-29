from flask import Flask

# It Create a INstance of the Flask class
# which will be your WSGI application
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello hey I am omkar'

@app.route('/about')
def about():
    return 'About page'

if __name__ == '__main__':
    # Run the application on the local development server
    app.run(debug= True) 
