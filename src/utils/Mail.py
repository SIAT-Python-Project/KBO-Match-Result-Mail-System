import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

class Mail:
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 465

    def __init__(self, email, passwd) -> None:
        self.__email = email
        self.__passwd = passwd

    def send_test(self):
        msg = MIMEMultipart('mixed') 
        msg['From'] = self.__email
        msg['To'] = self.__email
        msg['Subject'] = '메일 전송 테스트'

        msg_text = "test"

        text = MIMEText(msg_text, 'html',_charset='UTF-8')
        msg.attach(text)

        try:
            smtp = smtplib.SMTP_SSL(self.SMTP_SERVER, self.SMTP_PORT)
            smtp.login(self.__email, self.__passwd)
            smtp.close()
        except Exception:
            raise Exception('메일 정보가 올바르지 않습니다.')
        
    def send(self, html):
        msg = MIMEMultipart('mixed') 
        msg['From'] = self.__email
        msg['To'] = self.__email
        msg['Subject'] = '야구!'

        file_name = './IO/baseball_info.html'
        with open(file_name, 'w', encoding='UTF-8') as f:
            f.write(html)
        
        with open(file_name, 'rb') as f:
            tranfer_file = MIMEApplication(f.read())
            tranfer_file.add_header('Content-Disposition', 'attachment', fileName='baseball_info.html')
            msg.attach(tranfer_file)

        smtp = smtplib.SMTP_SSL(self.SMTP_SERVER, self.SMTP_PORT)
        smtp.login(self.__email, self.__passwd)
        smtp.sendmail(self.__email, self.__email, msg.as_string())
        smtp.close()



