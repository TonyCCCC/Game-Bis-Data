import requests
from requests import exceptions
from lxml import etree
from pandas import DataFrame

class MifeiLogin:
    def __init__(self, avatar):
        self.avatar = avatar
        while 1:
            if avatar not in ['channel', 'cp']:
                avatar = input("Avatar must be 'channel' or 'cp'. Try again.")
            else:
                break

    def get_auth(self):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0",
            }
            url = lambda avatar: 'https://www.globalpay365.com/site/login' if avatar == 'channel' \
                else 'http://frontcp.globalpay365.com/site/login'
            response = requests.get(url(avatar=self.avatar), headers=headers, verify=False)
            page = response.text
            c = response.cookies
            cookies = requests.utils.dict_from_cookiejar(c)
            html = etree.HTML(page)
            token = html.xpath('//head/meta[@name="csrf-token"]/@content')
            return cookies, token
        except exceptions.RequestException as e:
            print(e)

    def login(self, username, password):
        avatar = self.avatar
        cookies, token = self.get_auth()
        print('Cookies: %s\nToken: %s' %(cookies, token))
        c = requests.utils.cookiejar_from_dict(cookies)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0",
            "X-Requested-With": "XMLHttpRequest"
        }
        pd = {
            "_csrf": token,
            "LoginForm[username]": str(username),
            "LoginForm[password]": str(password),
            "LoginForm[rememberMe]": "0",
            "LoginForm[rememberMe]": "1",
            "login-button": ""
        }
        session = requests.session()
        data = DataFrame()
        try:
            if avatar == 'channel':
                response = session.post('https://www.globalpay365.com/site/login', data=pd, cookies=c, verify=False)
                html = session.post('https://www.globalpay365.com/months/index', headers=headers, verify=False)
                dict = html.json()
                df = DataFrame(data=dict)
                data = df.loc[:, ['sample_time', 'revenue_optimized', 'payout_optimized']]
                data.columns = ['Time', 'Revenue', 'Payout']
            else:
                response = session.post('http://frontcp.globalpay365.com/site/login', data=pd, cookies=c, verify=False)
                html = session.get('http://frontcp.globalpay365.com/dashboard-rest/report-data-view?start_date=&end_date='
                                   '&dateType=month-1', headers=headers, verify=False)
                dict = html.json()['listData']
                df = DataFrame(data=dict)
                data = df.loc[:, ['sample_time', 'revenue_optimized', 'payout_optimized']]
                data.columns = ['Time', 'Revenue', 'Payout']
            return data
        except exceptions.RequestException as e:
            print(e)



if __name__ == '__main__':
    cp_list = {
        "Ruigame": "Rygm2015",
        "Coconut": "Indiapk2015",
        "jingyin": "3Car123456",
        "CDyouxifang": "Aa000000",
        "shenyou2": "Aa000000",
        "Szshenyou": "Aa000000",
        "UC_CP2017": "Aa000000",
    }
    channel_list = {
        "UC_2015": "Ucgame2015",
        "uczhuanyong": "Aa000000"
    }
    CP = MifeiLogin('cp')
    for i in cp_list:
        with open('mifei.csv', 'a') as f:
            f.write(i)
        data = CP.login(i, cp_list[i])
        data.to_csv('mifei.csv', mode='a')

    CHL = MifeiLogin('channel')
    for i in channel_list:
        with open('mifei.csv', 'a') as f:
            f.write(i)
        data = CHL.login(i, channel_list[i])
        data.to_csv('mifei.csv', mode='a', chunksize=5)
