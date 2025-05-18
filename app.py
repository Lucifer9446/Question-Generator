from flask import Flask, render_template, request
from generate_mcq_questions import generate_mcq_questions
from generate_true_false import generate_true_false
from generate_short_answer_questions import generate_short_answer_questions

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/get-started')
def get_started():
    return render_template('get_started.html')


@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    question_type = request.form['question-type']
    num_questions = int(request.form['num-questions'])

    if question_type == 'mcq':
        questions = generate_mcq_questions(text, num_questions)
    elif question_type == 'true-false':
        questions = generate_true_false(text, num_questions)
    elif question_type == 'short-answer':
        questions, _ = generate_short_answer_questions(text, num_questions)

    return render_template('questions.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
