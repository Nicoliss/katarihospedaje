from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/reserva')
def reserva():
    return render_template('reserva.html')

if __name__=='__main__':
    app.run(debug=True)

    