import traceback

def passWord(pwd):
    if not pwd.isalnum() or not pwd.islower():
        raise Exception('字元格式不符')
    if len(pwd) < 6:
        raise Exception('輸入密碼太短')
    if len(pwd) > 8:
        raise Exception('輸入密碼太長')
    print('密碼格式符合')

pwd = input('請輸入密碼：')
try:
    passWord(pwd)
except Exception as err:
    errlog = open('errch13-3.txt', 'a')
    errlog.write(traceback.format_exc())
    errlog.close()
    print('將Traceback寫入錯誤檔案errch13-3.txt完成')
    print('密碼長度檢查異常發生：', str(err))
