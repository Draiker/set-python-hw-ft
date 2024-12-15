from flask import Flask
from flask import render_template
from schedule import Schedule

app = Flask(__name__)

api_url = "https://be-svitlo.oe.if.ua"
api_endpoint = "/GavByQueue"
queueList = ["1.1", "1.2", "2.1", "2.2", "3.1", "3.2", "4.1", "4.2", "5.1", "5.2", "6.1", "6.2"]

@app.route('/')
def start():
    
    fullSchedule = Schedule(api_url, api_endpoint, queueList)
    
    # print(fullSchedule.getScheduleByQueue())
    return render_template('index.html', message=fullSchedule.getScheduleFull())

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000,
            use_reloader=True, threaded=True)