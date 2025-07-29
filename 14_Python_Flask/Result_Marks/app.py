from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/submit', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        sub1 = int(request.form['sub1'])
        sub2 = int(request.form['sub2'])
        sub3 = int(request.form['sub3'])
        sub4 = int(request.form['sub4'])
        name = request.form['name']
        data = [
            {'subject': 'Maths','marks': sub1},
            {'subject': 'Science','marks': sub2},
            {'subject': 'English','marks': sub3},
            {'subject': 'Social Studies','marks': sub4}
        ]
        return f'''name is {name}
            sub1 marks is {sub1}
            sub2 marks is {sub2}
            sub3 marks is {sub3}
            sub4 marks is {sub4}
            '''
    return render_template('form.html',data = data)

if __name__ == '__main__':
    app.run(debug=True)
