from flask import Flask, render_template, request ,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/add/<int:a>/<int:b>')
# def sum(a,b):
#     return "True"

@app.route('/armstrong/<int:num>')
def armstrong(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print("The number is an Armstrong number.")
        result = {
            'is_armstrong': True,
            
        }
    else:
        print("The number is not an Armstrong number.")
        result = {
            'is_armstrong': False,
            'armstrong_sum': sum,
            'server': 'Server response False'
        }
    return jsonify(result)
    

if __name__ == '__main__':
    app.run(debug=True)