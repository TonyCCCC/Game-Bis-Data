import requests
from lxml import etree
import os

class MifeiLogin:
    def __init__(self ,start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def get_auth(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0",
            "Referer": "https://www.globalpay365.com/site/login"
        }
        response = requests.get('https://www.globalpay365.com/site/login', headers=headers)
        page = response.text
        c = response.cookies
        cookies = requests.utils.dict_from_cookiejar(c)
        html = etree.HTML(page)
        token = html.xpath('//head/meta[@name="csrf-token"]/@content')
        return cookies, token

    def login(self):
        start_date = self.start_date
        end_date = self.end_date
        cookies, token = self.get_auth()
        print('Cookies: %s\nToken: %s' %(cookies, token))
        c = requests.utils.cookiejar_from_dict(cookies)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0",
        }
        acts = {
            "UC_2015": "Ucgame2015",
            "uczhuanyong": "Aa000000"
        }
        for a in acts:
            pd = {
                "_csrf": token,
                "LoginForm[username]": str(a),
                "LoginForm[password]": str(acts[a]),
                "LoginForm[rememberMe]": "0",
                "LoginForm[rememberMe]": "1",
                "login-button": ""
            }
            session = requests.session()
            response = session.post('https://www.globalpay365.com/site/login', headers=headers, data=pd, cookies=c)
            file = session.get('https://www.globalpay365.com/days/download-data?start=%s&end=%s&page=1'
                            % (start_date, end_date))
            with open('%s.csv' % a, 'w', encoding='gbk') as f:
                f.write(file.text)
            os.startfile('%s\%s.csv' %(os.getcwd(), a))