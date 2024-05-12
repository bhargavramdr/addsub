


from flask import Flask, render_template, request
import random

app = Flask(__name__)
app.config['CORRECT_COUNT'] = 0
app.config['INCORRECT_COUNT'] = 0
app.config['TOTAL_COUNT'] = 0

def generate_question():
    num1 = random.randint(0, 99)
    num2 = random.randint(0, 99)
    operator = random.choice(['+', '-'])
    return f"{num1} {operator} {num2}"

@app.route('/')
def index():
    question = generate_question()
    return render_template('index.html', question=question)

@app.route('/', methods=['POST'])
@app.route('/', methods=['POST'])
def check_answer():
    question = request.form['question']
    user_answer = request.form['answer']
    num1, operator, num2 = question.split()
    num1, num2 = int(num1), int(num2)
    correct_answer = abs(num1 - num2) if operator == '-' else num1 + num2
    if int(user_answer) == correct_answer:
        result = 'Correct!'
        app.config['CORRECT_COUNT'] += 1
    else:
        result = f'Incorrect. The correct answer is {correct_answer}.'
        app.config['INCORRECT_COUNT'] += 1
    app.config['TOTAL_COUNT'] += 1
    return render_template('index.html', question=generate_question(), result=result, correct_count=app.config['CORRECT_COUNT'], incorrect_count=app.config['INCORRECT_COUNT'], total_count=app.config['TOTAL_COUNT'])


