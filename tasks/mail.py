from notifications.mail import send_mail


def notify(report_heading, email, message):
    message_strng = ""
    for i in message:
        message_strng +=str(i)
    if len(message) > 0:
        send_mail(report_heading, 'notifications@ludaya.com', [email], message_strng)


def format_email(message, report_message):
    message.append('\n')
    message.append('Thank you')
    message.append('\n')
    message.append('\n')
    message.append('Ludaya Team')
    message.insert(0, '\n')
    message.insert(0, '\n')
    message.insert(0, report_message)
    message.insert(0, '\n')
    message.insert(0, '\n')
    message.insert(0, 'Greeting')
    return message
