import flask
import qrcode
# #from flask import render_template
app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template('main.html')

@app.route("/qr",methods=["POST"])
def qr():
    #第一步：获取要生成的二维码数据
    data = flask.request.form.get("data")
    print(flask.request.data)

    #第二步：生成二维码图像
    img = qrcode.make(data)

    #第三步：页面上显示二维码图片
    img.save(r"F:\Python\DAY6\代码\qrcode_tool_online\static\qr.png")
    return '<img src="/static/qr.png">'

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")

