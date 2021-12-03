import smtplib
import email.message
from sqlite3 import Error
from random import choice


# Lista de Participantes
list_part = [] 

# Verificação dos participante (idêntica a lista de participantes) - Uma Lista para evitar que o programa demore usando o método Choice do Random
list_verif = []

# E-mail dos participantes (importante está na ordem da lista)
email_part = []

# Aqui pode ser adicionado detalhes sobre o presente ( No exemplo abaixo temos: Tamanho do calçado e preferência de estampa)
tamanho = [38, 38, 36, 38, 37, 37, 38, 38, 42, 39, 37, 43, 39, 42, 40, 44, 40, 36, 33, 34, 44, 42, 36, 42, 42, 42]
estampas = ['Me surpreenda', 'Glitter/ Rosa', 'Vermelha ou da Disney', 'Verde/Preta/Harry Potter/ Bandeira Lgbt', 'Preta/ Colorida', 
'colorida, Desenho Animado ou Cultura POP', 'Marvel/Harry Potter', 'Me surpreenda', 'Me surpreenda', 'Me surpreenda', 
'Preta/Branca/Desenho', 'Preta/Roxa/Fé', 'Me surpreeda', 'Marvel', 'Anime', 'Marvel', 'Marvel', 'Anime', 'Anime', 'Anime', 'Anime/Harry Potter', 'Me surpreenda',
'Me surpreenda', 'Bob Esponja','Me surpreenda', 'Anime ou Preta']

escolhidos = []

def enviar_email():
    for c, i in enumerate(list_part):
    #for c in range(0, 1):
        teste = 1
        while teste != 0:
            escolhido = choice(list_verif)
            if escolhido not in escolhidos and escolhido != list_part[c]:
                escolhidos.append(escolhido)
                pos_e = list_part.index(escolhido)
                corpo_email = f'''
                <p>Olá {list_part[c]},</p>
                <p>O seu amigo oculto é: {escolhido}</p>
                <p>O tamanho do calçado dele(a) é: {tamanho[pos_e]}</p>
                <p>E a sugetão de estampa é: {estampas[pos_e]}</p>
                '''
                msg = email.message.Message()
                msg['Subject'] = 'Amigo Oculto'
                msg['From'] = 'email@gmail.com'
                msg['To'] = email_part[c]
                senha = 'senha'
                msg.add_header('Content-Type', 'text/html')
                msg.set_payload(corpo_email)                            
                try:
                    s = smtplib.SMTP('smtp.gmail.com: 587')
                    s.starttls()
                    # Login Credentials for sending the mail
                    s.login(msg['From'], senha)
                    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
                    print('Email enviado')
                except Error as ex:
                    print(ex)
                    print('Falha ao enviar email')
                teste = 0
                list_verif.remove(escolhido)
            else:
                teste = 1  

enviar_email()
