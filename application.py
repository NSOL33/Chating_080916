from flask import Flask,request,render_template
application = Flask(__name__)

@application.route('/')
def on_load():
    file=open("msg.txt","r")
    msg=file.readline()
    return render_template("index.html",msg=msg)
@application.route('/send',methods=['POST'])
def send():
    file=open("msg.txt","w")
    if request.method == 'POST':
        msg=request.form.get("message")
        file.write(msg)
        return render_template("index.html",msg=msg)
if __name__ == '__main__':
    application.run(debug=False,host="0.0.0.0")