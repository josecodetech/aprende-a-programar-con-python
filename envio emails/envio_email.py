from config import *
import smtplib
from email.message import EmailMessage

def menu():
    print("1. Enviar email")
    print("2. Enviar email con archivo adjunto")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def enviar_email(destinatario, asunto, cuerpo, archivo_adjunto = None):
    remitente = CORREO
    clave = CLAVE
    servidor_smtp = SERVIDOR_SMTP
    puerto_smtp = PUERTO_SMTP
    try:
        mensaje = EmailMessage()
        mensaje['From'] = remitente
        mensaje['To'] = destinatario
        mensaje['Subject'] = asunto
        mensaje.set_content(cuerpo)
        if archivo_adjunto!=None:
            with open(archivo_adjunto, 'rb') as archivo:
                contenido_adjunto = archivo.read()
            mensaje.add_attachment(contenido_adjunto, maintype='application', subtype='octet-stream', filename=archivo_adjunto)
        servidor = smtplib.SMTP_SSL(servidor_smtp, puerto_smtp)
        servidor.login(remitente, clave)
        servidor.send_message(mensaje)
        servidor.quit()
        print("El email se envio correctamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
def main():
    while True:
        opcion = menu()
        if opcion == 1:
            destinatario = input("Ingrese el destinatario: ")
            asunto = input("Ingrese el asunto: ")
            cuerpo = input("Ingrese el cuerpo del email: ")
            enviar_email(destinatario, asunto, cuerpo)
        elif opcion == 2:
            destinatario = input("Ingrese el destinatario: ")
            asunto = input("Ingrese el asunto: ")
            cuerpo = input("Ingrese el cuerpo del email: ")
            archivo_adjunto = input("Ingrese el nombre del archivo adjunto: ")
            enviar_email(destinatario, asunto, cuerpo, archivo_adjunto)
        elif opcion == 3:
            print("Saliendo del programa... ")
            break
        else:
            print("Opcion invalida.")
if __name__ == "__main__":
    main()