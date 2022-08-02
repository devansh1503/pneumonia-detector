from flask import  Flask,render_template,request
from Pred import predict
from werkzeug.utils import secure_filename
import os
dir = './inputimg/img'
#dst = open('./inputimg/img/imgn.jpeg','wb')
def delete():
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
app = Flask(__name__)
@app.route("/")
def hello():
    try:
        os.remove(os.path.join(dir,'imgn.jpeg'))
    except:
        return render_template('index.html',result="")
    else:
        return render_template('index.html',result="")

app.config['IMAGES_UPLOAD'] = '/inputimg/img/'
@app.route("/upload", methods=['GET','POST'])
def pre():
    res = ""
    if request.method == 'POST':
        img = request.files['image']
        #delete()
        dst = open('./inputimg/img/imgn.jpeg','wb')
        img.save(dst)
        res = predict()
    return render_template('index.html',result=res)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')