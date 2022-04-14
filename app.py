from flask import Flask
from flask import request,render_template
import pyqrcode


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['GET','POST'])
def qr():
    if request.method == 'POST':
        s = request.form['url']
        url = pyqrcode.create(s)
        url.png('myqr.png', scale = 6)

if __name__ == '__main__':
    app.run(debug=True)