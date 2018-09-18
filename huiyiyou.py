import requests
import time
import os


class hyyCPI:
    def __init__(self, start_date, end_date):
        self.ss = requests.session()
        self.start_date = start_date
        self.end_date = end_date

    def captcha(self):
        captcha = self.ss.get('http://www.51app.co:8090/Login/CheckCode?ID=1')
        t = time.strftime('%y%m%d-%H%M', time.localtime(time.time()))
        cap_file = r"C:\Users\Administrator\PycharmProjects\Game Biz Data\captcha" + "\\" + t + r'.png'
        with open(cap_file, 'wb') as f:
            f.write(captcha.content)
        os.startfile(cap_file)
        #captcha = input("Input CAPTCHA:")

    def get_data(self, captcha):
        pd = {
            "UName": "cust_aliuc718",
            "Pwd": "123456",
            "Code": captcha
        }
        response = self.ss.post('http://www.51app.co:8090/Login/CheckUserLogin', data=pd)
        file_url = 'http://www.51app.co:8090/Channel/ExportAnalysts?ProductName=&ChannelCode=&InputDateTime=' \
                   + self.start_date + '&EndInputDateTime=' + self.end_date \
                   + '&SettlementCurrency=-1&CooperationMode=0&HasCheck=true'
        f = self.ss.get(file_url)
        with open('huiyiyou.xls', 'wb') as file:
            file.write(f.content)
        os.startfile('%s\huiyiyou.xls' % os.getcwd())


if __name__ == '__main__':
    hyy = hyyCPI('2018-08-20', '2018-08-26')
