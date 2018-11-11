import requests
from choco.settings import SMS_LOGIN, SMS_PASSWORD

login=SMS_LOGIN
psw=SMS_PASSWORD

def sendSms(phone, message):    
    r = requests.get('http://smsc.kz/sys/send.php?login=%s&psw=%s&phones=%s&mes=%s'%(login,psw,phone,message))
    return r
