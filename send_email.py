import yagmail
def send_email():
    try:
        yag = yagmail.SMTP(user='placement.training.mpstme@gmail.com',password='chiragsir')
        yag.send(
            to='krisha9jan@gmail.com',
            subject='Test Email',
            contents="Attendance",
            attachments=['11-12-2020_09_47_01.csv']
        )
        print("Email Sent Successfully")

    except:
        print("Error...")