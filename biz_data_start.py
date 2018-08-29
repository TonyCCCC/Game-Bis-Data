from huiyiyou import hyyCPI
from mifei import MifeiLogin
from flexion import FlexionLogin

start_date = '2018-08-20'
end_date = '2018-08-26'

hyy = hyyCPI(start_date, end_date)
mf = MifeiLogin(start_date, end_date)
mf.login()
flx = FlexionLogin(start_date, end_date)
flx.login()