import smtplib
from email.message import EmailMessage

def send_delete_email ( nome, cognome, codice_fiscale, ora, giorno):

    mail_server= "smtp.gmail.com"
    port_mail_server= 587

    sender_email = "send.abdulmanager@gmail.com"
    password = "!Einaudi"
    destination_email = "info.abdulmanager@gmail.com"

    email_message = "<h3 class=\"LC20lb DKV0Md\">⚠️ AVVISO IMPORTANTE: Dipendente eliminato alle ore <span style=\"color: #ff0000;\">" + ora + "</span> il <span style=\"color: #ff0000;\">" + giorno + "</span>:</h3><p>Ecco l'anagrafica del dipendente eliminato:</p><p><strong>Nome:</strong> " + nome + "</p><p><strong>Cognome:</strong> " + cognome + "</p><p><strong>Codice fiscale:</strong> " + codice_fiscale + "</p>"

    email = EmailMessage()
    email['Subject'] = "Eliminazione dipendente"
    email['From'] = sender_email
    email['To'] = destination_email
    email.set_content(email_message, subtype='html')



    with smtplib.SMTP(mail_server, port_mail_server) as mail_client:

        mail_client.ehlo()
        mail_client.starttls()

        mail_client.login(sender_email, password=password)
        mail_client.send_message(email)
        mail_client.quit()