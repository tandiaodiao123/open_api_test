import json
import hashlib
import requests
from datetime import datetime
now = datetime.now()
formatted_now = now.strftime('%Y-%m-%d %H:%M:%S') #获取格式化时间
appsecret = "123727fa-3637-4d67-8a4a-22bbc04e65ed"

#封装加密字符串

class Encrypted_string():
    def __init__(self,biz_param,api_method):
        # self.biz_param = biz_param

        # 获取当前时间戳
        # self.formatted_now = formatted_now
        formatted_now = now.strftime('%Y-%m-%d %H:%M:%S')

        # 参数字典
        self.params = {
            "api_method": api_method,
            "api_version": "1.0",
            "app_key": "c76245e9600d4bd9",
            "biz_param":biz_param,

            "timestamp": formatted_now,
            "v": "1",
            "sign_type": "md5"
        }
    def Serialization_biz_param(self):

        #序列化 biz_param
        biz_parm = self.params["biz_param"]
        biz_parm_sorted_keys = sorted(biz_parm.keys())
        sorted_biz_param = {key:biz_parm[key] for key in biz_parm_sorted_keys }
        # print(params)

        biz_param_json = json.dumps(sorted_biz_param, separators=(',', ':'), ensure_ascii=False)

        sorted_keys = sorted(self.params.keys())
        target_list = []
        for key in sorted_keys:
            value = self.params[key]
            if key == 'biz_param':
                value = biz_param_json
            target_list.append(f"{key}={value}")



        target_list.append(f"app_secret={appsecret}")
        # print(target_list)

        target_list = sorted(target_list)
        target_str_1 = "&".join(target_list)  #拼接字符串
        # print(target_str_1)
        return target_str_1

    def md5(self):
        sign = self.Serialization_biz_param()
        hl = hashlib.md5()
        hl.update(sign.encode(encoding='utf-8'))
        return str.upper(hl.hexdigest())




if __name__ == "__main__":

    a = Encrypted_string(biz_param={'current_page': 1, 'page_size': 100 })
    a.params.setdefault('sign',a.md5()) #将 sign加入params

    url = 'https://slt-daily.shuliantong.cn/open/api.do'
    headers1 = {'Content-Type': 'application/json'}

    response = requests.post(url=url, json=a.params,headers=headers1)
    print(response.text)





