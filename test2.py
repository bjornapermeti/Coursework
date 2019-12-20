import smtplib
content = 'prova 2'
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('bjornabooks@gmail.com','bjorna123')
mail.sendmail('bjornabooks@gmail.com','bjornabooks@gmail.com', content)
mail.close()