from flask import Flask
from flask import request,render_template
import pyqrcode
import qrcode.image.svg as qr
import qrcode
import base64
import io
from PIL import Image

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


if __name__ == '__main__':
    app.run(debug=True)

"""url = pyqrcode.create(s)
        #url.png('myqr.png', scale = 6)
        
        q=qrcode.QRCode(version=1,box_size=10,border=5)
        q.add_data(s)
        q.make(fit=True)
        img=q.make_image(fill='black',back_color='white')
        ip=img.save('imagesqrcode.jpg')
        data = io.BytesIO()
        ip.save(data, "JPEG")
        encoded_img_data = base64.b64encode(data.getvalue())
        return render_template("index.html", img_data=encoded_img_data.decode('utf-8'))"""