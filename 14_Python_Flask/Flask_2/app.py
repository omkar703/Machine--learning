from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    return "<html><h1>Welcome to the Flask App!</h1></html>"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/index',methods=['GET', 'POST'])
def google():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name'] # get form html page input here we add id of html page 
        return f'Hello, {name}!'
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
