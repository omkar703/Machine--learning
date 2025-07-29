from flask import Flask, render_template, request

app = Flask(__name__)

# Route for Main Page
@app.route('/')
def main():
    return render_template('index.html')

# Route for Form Page
@app.route('/form')
def form():
    return render_template('form.html')

# Route for Processing Form and Displaying Results
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        sub1 = int(request.form['sub1'])
        sub2 = int(request.form['sub2'])
        sub3 = int(request.form['sub3'])
        sub4 = int(request.form['sub4'])

        total = sub1 + sub2 + sub3 + sub4
        percentage = round((total / 400) * 100, 2)

        data = [
            {'subject': 'Maths', 'marks': sub1},
            {'subject': 'Science', 'marks': sub2},
            {'subject': 'English', 'marks': sub3},
            {'subject': 'Social Studies', 'marks': sub4},
        ]

    return render_template('submit.html', name=name, data=data, total=total, percentage=percentage)

if __name__ == '__main__':
    app.run(debug=True)
