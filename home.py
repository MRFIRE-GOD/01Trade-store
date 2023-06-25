from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process', methods=['POST'])
def process_form():
    name = request.form.get('name')
    message = f"Hello, {name}!"
    return render_template('home.html', message=message)

if __name__ == '__main__':
    app.run()
