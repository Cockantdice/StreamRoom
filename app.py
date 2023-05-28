from flask import Flask, render_template
app = Flask(__name__)

#JOBS=[{'MOROSI SAKHE', 21, 'MALE'}, {'NANDIPHA', 20, 'FEMALE'}, {'OLWETHU MOROSI', 26, 'MALE'}
  #  ]
@app.route('/')
def hello_world():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)