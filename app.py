from flask import Flask, send_file
from flask import request,render_template
import qrcode.image.svg as qr
import qrcode
from barcode import EAN13
from barcode.writer import ImageWriter

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index', methods=['GET','POST'])
def qr():
    if request.method == 'POST':
        s = request.form['url']
        q=qrcode.QRCode(version=1,box_size=10,border=5)
        q.add_data(s)
        q.make(fit=True)
        img=q.make_image(fill='black',back_color='white')
        img.save('static\qrcode.jpg')
    return render_template("result.html",img_data=img)

@app.route('/bar', methods=['GET','POST'])
def bar():
    if request.method == 'POST':
        number=request.form['num']
        my_code = EAN13(number, writer=ImageWriter())
        my_code.save("static/new_code")
    return render_template("bar.html",img_data=my_code)

@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "./static/qrcode.jpg"
    return send_file(path, as_attachment=True)

@app.route('/downloadBar')
def downloadBar ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "./static/new_code.png"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)