# from flask import Flask, render_template, request, jsonify
# from quiz.GenerateQuestion import generate_questions
# from quiz.Evaluation import evaluate_score
# import random
# import time

# app = Flask(__name__)

# # Store quiz state in memory (for simplicity)
# quiz_data = {
#     'questions': [],
#     'current_question': 0,
#     'answers': {},
#     'start_time': 0,
#     'end_time': 0,
#     'timer': None
# }

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/start_quiz', methods=['POST'])
# def start_quiz():
#     hours = int(request.form.get('hours', 0))
#     minutes = int(request.form.get('minutes', 0))
#     seconds = int(request.form.get('seconds', 0))
    
#     total_seconds = hours * 3600 + minutes * 60 + seconds
#     quiz_data['timer'] = total_seconds if total_seconds > 0 else None
#     quiz_data['questions'] = generate_questions()
#     quiz_data['current_question'] = 0
#     quiz_data['answers'] = {}
#     quiz_data['start_time'] = time.time()
    
#     return jsonify({
#         'success': True,
#         'question': quiz_data['questions'][0],
#         'question_count': len(quiz_data['questions']),
#         'current_question': 1,
#         'timer': quiz_data['timer']
#     })

# @app.route('/next_question', methods=['POST'])
# def next_question():
#     question_index = int(request.form.get('current_question', 0))
#     answer = request.form.get('answer', None)
    
#     if answer:
#         quiz_data['answers'][question_index - 1] = answer
    
#     if question_index < len(quiz_data['questions']):
#         quiz_data['current_question'] = question_index
#         return jsonify({
#             'question': quiz_data['questions'][question_index],
#             'question_count': len(quiz_data['questions']),
#             'current_question': question_index + 1,
#             'is_last': question_index + 1 == len(quiz_data['questions'])
#         })
#     else:
#         return jsonify({'error': 'No more questions'})

# @app.route('/submit_quiz', methods=['POST'])
# def submit_quiz():
#     question_index = int(request.form.get('current_question', 0))
#     answer = request.form.get('answer', None)
    
#     if answer:
#         quiz_data['answers'][question_index - 1] = answer
    
#     quiz_data['end_time'] = time.time()
    
#     # Calculate score
#     score = 0
#     for i, question in enumerate(quiz_data['questions']):
#         if quiz_data['answers'].get(i) == question['answer']:
#             score += 1
    
#     time_taken = quiz_data['end_time'] - quiz_data['start_time']
#     hours, remainder = divmod(time_taken, 3600)
#     minutes, seconds = divmod(remainder, 60)
#     time_str = f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
    
#     evaluation = evaluate_score(score)
    
#     return jsonify({
#         'score': score,
#         'total_questions': len(quiz_data['questions']),
#         'time_taken': time_str,
#         'evaluation': evaluation
#     })

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from quiz.GenerateQuestion import generate_questions
from quiz.Evaluation import evaluate_score
from quiz.ChatBot import get_chat_response
import random
import time

app = Flask(__name__)

# Store quiz state in memory (for simplicity)
quiz_data = {
    'questions': [],
    'current_question': 0,
    'answers': {},
    'start_time': 0,
    'end_time': 0,
    'timer': None
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    hours = int(request.form.get('hours', 0))
    minutes = int(request.form.get('minutes', 0))
    seconds = int(request.form.get('seconds', 0))
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    quiz_data['timer'] = total_seconds if total_seconds > 0 else None
    quiz_data['questions'] = generate_questions()
    quiz_data['current_question'] = 0
    quiz_data['answers'] = {}
    quiz_data['start_time'] = time.time()
    
    return jsonify({
        'success': True,
        'question': quiz_data['questions'][0],
        'question_count': len(quiz_data['questions']),
        'current_question': 1,
        'timer': quiz_data['timer']
    })

@app.route('/next_question', methods=['POST'])
def next_question():
    question_index = int(request.form.get('current_question', 0))
    answer = request.form.get('answer', None)
    
    if answer:
        quiz_data['answers'][question_index - 1] = answer
    
    if question_index < len(quiz_data['questions']):
        quiz_data['current_question'] = question_index
        return jsonify({
            'question': quiz_data['questions'][question_index],
            'question_count': len(quiz_data['questions']),
            'current_question': question_index + 1,
            'is_last': question_index + 1 == len(quiz_data['questions'])
        })
    else:
        return jsonify({'error': 'No more questions'})

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    question_index = int(request.form.get('current_question', 0))
    answer = request.form.get('answer', None)
    
    if answer:
        quiz_data['answers'][question_index - 1] = answer
    
    quiz_data['end_time'] = time.time()
    
    # Calculate score
    score = 0
    for i, question in enumerate(quiz_data['questions']):
        if quiz_data['answers'].get(i) == question['answer']:
            score += 1
    
    time_taken = quiz_data['end_time'] - quiz_data['start_time']
    hours, remainder = divmod(time_taken, 3600)
    minutes, seconds = divmod(remainder, 60)
    time_str = f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
    
    evaluation = evaluate_score(score)
    
    return jsonify({
        'score': score,
        'total_questions': len(quiz_data['questions']),
        'time_taken': time_str,
        'evaluation': evaluation
    })

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form.get('message', '')
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    try:
        response = get_chat_response(message)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)