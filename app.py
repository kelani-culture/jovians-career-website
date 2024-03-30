from flask import Flask,  render_template, jsonify


app = Flask(__name__)


JOBS = [
    {
        'id' : 1,
        'title': "Data analyst",
        'location': 'Benglaru India',
        'salary': 'Rs. 10, 00, 000'
    },
    {
        'id' : 2,
        'title': "Data scientist",
        'location': 'Delhi India',
        'salary': 'Rs. 15, 00, 000'
    },
    {
        'id' : 3,
        'title': "Frontend engineering",
        'location': 'Remote',
        'salary': 'Rs. 12, 00, 000'
    },
    {
        'id' : 4,
        'title': "Backend engineering",
        'location': 'Sanfrasisco USA',
        'salary': '$ 12,000.00'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS)

    

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)