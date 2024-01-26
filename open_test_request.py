import requests
from open_test_sign import  Encrypted_string
from flask import Flask, request

app = Flask(__name__)

@app.route("/<api_method>",methods=["post","get"])
def open_api_test(api_method):  #接口方法

    # 设置请求头
    headers = {'Content-Type': 'application/json'}

    # 调用第三方API
    api_url = "https://slt-daily.shuliantong.cn/open/api.do"

    # 获取业务参数
    biz_params = request.form.to_dict()

    a = Encrypted_string(biz_param=biz_params,api_method=api_method)
    a.params.setdefault('sign', a.md5())  # 将 sign加入params

    url = 'https://slt-daily.shuliantong.cn/open/api.do'
    headers1 = {'Content-Type': 'application/json'}

    response = requests.post(url=url, json=a.params, headers=headers1)
    return response.text


if __name__ == '__main__':
    app.run(debug=True)
