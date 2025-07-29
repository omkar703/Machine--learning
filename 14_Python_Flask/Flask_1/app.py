from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "<html><h1>Welcome to the Flask App!</h1></html>"

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)