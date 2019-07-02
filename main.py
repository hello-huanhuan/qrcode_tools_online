import flask
import qrcode
import io
from datetime import timedelta
# #from flask import render_template
app = flask.Flask(__name__)
#app.config['SEND_FILE_MAX_AGE_DEFAULT']=timedelta(seconds=1)

@app.route("/")
def home():
    return flask.render_template('main.html')

@app.route("/qr",methods=["GET"])
def qr():
    #第一步：获取要生成的二维码数据
    data = flask.request.args.get("data")
    print(flask.request.data)

    #第二步：生成二维码图像
    img = qrcode.make(data)
    bi = io.BytesIO()  # 创建一个BytesIO对象，用于在内存中储存二维码图像数据
    #img.save(r"F:\Python\DAY6\代码\qrcode_tool_online\static\qr.png")
    img.save(bi,"png")  # 调用img对象的save方法将二维码图像数据以png编码格式写入bi对象管理的内存空间
    bi.seek(0)  # 将bi对象内部的位置指针移动到图像数据的起始位置

    #第三步：返回二维码图像数据
    return  flask.send_file(bi,"image/png")

if __name__ == "__main__":
   # app.run(debug=True,host="0.0.0.0")
    app.run(debug=True)
