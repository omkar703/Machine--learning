from flask import Flask,render_template,request,redirect, url_for
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

@app.route('/submit', methods=['GET', 'POST']) # redurect to submit page 
def submit():
    if request.method == 'POST':
        name = request.form['name'] # get form html page input here we add id of html page 
        return f'Hello, {name}!'
    return render_template('form.html')

# here we passing <score> as a variable in url
# here w need to give int value here in url

## Jinja2 template engine
# {{}} for taking inputs
# {{% ... % }} --> Conditional statements
# {{ #...# }} --> Comments

@app.route('/success_result/<int:score>')
def success_result(score):
    result = ""
    if score >= 80:
        result = "Excellent"
    elif score >= 60:
        result = "Good"
    else:
        result = "Failed"
     
    
    return render_template('result.html', score=score, result=result)


@app.route('/success/<int:score>')
def success(score):
    result = ""
    if score >= 80:
        result = "Excellent"
    elif score >= 60:
        result = "Good"
    else:
        result = "Failed"
     
    expresstion = {'score': score,'result': result}
    return render_template('result1.html', results =expresstion)
# Variable rule 
# here we only accept integer values in url
@app.route('/number/<int:num>')
def number(num):
    return f'The number is {num}.'

@app.route('/passcheck/<int:num>')
def passcheck(num):
    return render_template('pass.html', results = num)

@app.route('/getmarks',methods=['GET','POST'])
def getmarks():
    total_score = 0
    if request.method == 'POST':
        sub1 = int(request.form['sub1'])
        sub2 = int(request.form['sub2'])
        sub3 = int(request.form['sub3'])
        sub4 = int(request.form['sub4'])
        sub5 = int(request.form['sub5'])
        total_score = sub1 + sub2 + sub3 + sub4 + sub5 / 5
    return redirect(url_for('success', score=total_score))

        


if __name__ == '__main__':
    app.run(debug=True)
