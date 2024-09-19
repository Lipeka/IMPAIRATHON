from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

def generate_schedule(activities, durations, wake_time, bed_time):
    schedule = []
    current_time = datetime.datetime.strptime(wake_time, '%H:%M')
    bed_time = datetime.datetime.strptime(bed_time, '%H:%M')
    
    for activity, duration in zip(activities, durations):
        end_time = current_time + datetime.timedelta(minutes=duration)
        if end_time > bed_time:
            break
        schedule.append(f"{current_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}: {activity}")
        current_time = end_time

    return schedule

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule', methods=['POST'])
def schedule():
    data = request.json
    activities = data['activities']
    durations = list(map(int, data['durations']))
    wake_time = data['wake_time']
    bed_time = data['bed_time']
    
    schedule = generate_schedule(activities, durations, wake_time, bed_time)
    
    return jsonify(schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True)
