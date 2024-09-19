from flask import Flask, render_template, request, jsonify
import random
import pyttsx3

app = Flask(__name__)

# Initialize the text-to-speech engine
tts_engine = pyttsx3.init()

# Define role-playing scenarios
scenarios = [
    {
        "role": "doctor",
        "description": "You are not feeling well. Who should you approach?",
        "dialogue": "Hello! How can I help you today?",
        "image": "https://cdn.vectorstock.com/i/1000v/86/90/cute-little-female-doctor-cartoon-waving-hand-vector-1468690.jpg"  # Add the image path
    },
    {
        "role": "teacher",
        "description": "You have a question about your homework. Who should you approach?",
        "dialogue": "Hello! How can I help you today?",
        "image": "https://thumbs.dreamstime.com/z/cartoon-teacher-vector-illustration-86426749.jpg"
    },
    {
        "role": "shopkeeper",
        "description": "You want to buy some groceries. Who should you approach?",
        "dialogue": "Hello! How can I help you today?",
        "image": "https://cdn.vectorstock.com/i/1000v/94/61/shopkeeper-and-customer-at-vegetables-vendor-vector-31059461.jpg"
    },
    {
        "role": "mechanic",
        "description": "Your car broke down. Who should you approach?",
        "dialogue": "Hello! How can I help you today?",
        "image": "https://img.favpng.com/24/10/6/cartoon-automobile-repair-shop-maintenance-png-favpng-pxq4dWJixk90AmCbiA95yL9s9.jpg"
    },
    {
        "role": "nurse",
        "description": "You need to get a vaccination. Who should you approach?",
        "dialogue": "Hello! How can I assist you today",
        "image": "https://cliparts.co/cliparts/riL/9K5/riL9K5oi8.jpg"
    }
]

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/get_scenario', methods=['GET'])
def get_scenario():
    scenario = random.choice(scenarios)
    return jsonify(scenario)

@app.route('/evaluate_response', methods=['POST'])
def evaluate_response():
    data = request.json
    user_response = data['response']
    correct_answer = data['correct_answer']
    if user_response.lower() == correct_answer.lower():
        return jsonify(result="Correct!", dialogue=scenarios[0]['dialogue'])
    else:
        return jsonify(result="Incorrect. Try again.")

if __name__ == '__main__':
    app.run(debug=True)