# app.py
from flask import Flask, render_template, request
from num2words import num2words # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        number = int(request.form['number'])
        result = num2words(number, lang='id')  # Mengubah angka menjadi teks dalam bahasa Indonesia
        return render_template('index.html', result=result, number=number)
    except ValueError:
        return render_template('index.html', error="Masukkan angka yang valid.")

if __name__ == '__main__':
    app.run(debug=True)
