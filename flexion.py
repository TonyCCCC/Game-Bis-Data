import requests


class FlexionLogin:

    def get_auth(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0",
            "Referer": "https://reports.flexionmobile.com/msp.report.frontend/login.jsp",
        }
        response = requests.get('https://reports.flexionmobile.com/msp.report.frontend/login.jsp', headers=headers)
        c = response.cookies
        cookies = requests.utils.dict_from_cookiejar(c)
        return cookies

    def login(self, start_date, end_date, filename):
        cookies = self.get_auth()
        print('Cookies: %s' % cookies)
        c = requests.utils.cookiejar_from_dict(cookies)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0",
        }
        pd = {
            "login": "9game",
            "passwd": "xdDEhhLn",
            "doLogin": "Login"
        }
        session = requests.session()
        response = session.post('https://reports.flexionmobile.com/msp.report.frontend/login.jsp', headers=headers, data=pd, cookies=c)
        date = {
            "format": "csv",
            "filtering": "product",
            "toCurrency": "USD",
            "from":"2018-08-13",
            "to": "2018-08-19",
            "group_report_day": "true",
            "group_affiliate": "true",
            "group_publisher": "true",
            "group_application": "true",
            "group_inapp_item": "true"
        }
        file = session.post('https://reports.flexionmobile.com/msp.report.frontend/flexionsdkreport/download', data=date, cookies=c)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(file.text)


if __name__ == '__main__':
    L = FlexionLogin()
    L.login('2018-08-13', '2018-08-19', 'flexion.csv')