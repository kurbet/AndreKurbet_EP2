#AndréKurbet
from turtle import * 
import time
import string
t = Turtle()
window = Screen() 
window.bgcolor("red")
window.title("Jogo da Forca")

palavras_jogo = [] #lista para palavras do jogo
tentativas = [] #lista para onde serão enviadas as letras usadas
erros_total = 0 #para criar a media geral

def forca():  #função de desenho da forca
    t.ht()
    t.left(90)  
    t.forward(400) 
    t.right(90)  
    t.forward(150)
    t.right(90)  
    t.forward(50) 
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(250)
    t.left(90)
    t.fd(450)
    t.left(90)
    t.forward(50)
    t.penup()
    t.fd(50)
    t.color("white")

continuar = 'sim'

while continuar  =='sim': #enquanto o jogador digitar sim, recomeça
    t.setheading(0)
    t.speed(10)  
    t.penup()      
    t.setpos(-250,-200)
    t.hideturtle()
    
    t.pendown()
    t.color("white")
    forca()
    chutadas=[] 
    palavras=open("entrada.txt", encoding="utf-8") #abre o aquivo entrada.txt
    leitura=palavras.readlines() #lê o arquivo entrada
    lista_palavras=[] #para onde vão as palavras do arquivo entrda após serem limpas 
    for i in leitura:
        linha=i.strip() #limpa as palavras 
        if linha!="":
            lista_palavras.append(linha) #caso a linha não esteja em branco, 
            #é adicionada a lista lista_palavras 
    from random import choice
    sorteio = choice(lista_palavras)#soreteio das palavras da lista_palavras 
    while sorteio in palavras_jogo: #para não repetir palvras,
    #se a palvra sorteada ja tiver sido usada, o soreteio ocorre de novo
        sorteio = choice(lista_palavras)#sorteia novamente
        
    print(sorteio)
    palavras_jogo.append(sorteio) #acrescenta o sorteio a lista de palavras usadas 
    sorteio=sorteio.upper()#todas as letras viram maiúsculas
    def desenhar_tracos():#desenha os traçinhos
        for i in sorteio:
            if i == " ": #se for espaço não desenhe o traço
                t.penup()
                t.fd(40)
                    
            else: #se não for espaço desenhe o traço
                t.pendown()
                t.fd(30)
                t.penup()
                t.fd(10)
                t.penup
                ht()
    desenhar_tracos() #chama a função que desenha a forca
    
    def cabeca(): #funçaõ que desenha a cabeça
        t.penup()
        t.setpos(-75,150)
        t.pendown()
        t.left(180)
        t.circle(40)
        t.penup()
    
    def corpo(): #função que desenha o corpo
        t.penup()
        t.setpos(-75,70)
        t.pendown()
        t.setpos(-75,-100)
        t.penup()
        
    def perna1(): #função que desenha a perna1
        t.penup()
        t.setpos(-75,-100)
        t.pendown()
        t.left(45)
        t.fd(100)
        t.penup()
        
    def perna2(): #função que desenha a perna2
        t.penup()
        t.setpos(-75,-100)
        t.pendown()
        t.left(90)
        t.fd(100)
        t.penup()
        
    def braco1(): #função que desenha o braco1
        t.penup()
        t.setpos(-75,25)
        t.pendown()
        t.fd(100)
        t.penup()
        
    def braco2(): #função que desenha o braco2
        t.penup()
        t.setpos(-75,25)
        t.pendown()
        t.right(90)
        t.fd(100)
        t.penup()
        
    acertos = 0 
    erros = 0 
    while erros<6 and acertos<len(sorteio)-sorteio.count(' '): 
    #quando a palavra ainda não acabou
           
        variavel = window.textinput(" ", "Arrisque uma letra:")  
        variavel = variavel.upper() #transforma todas as letras em maiúsculas
        
        if variavel not in tentativas: #
            tentativas.append(variavel)
            found=0
            for i in range(len(sorteio)):
                
                if variavel == sorteio[i]: #se a letra digitada(variavel) for 
                #igual a alguma letra da palavra escreva a letra
                    t.setpos(-200+i*40,-200)
                    pendown()
                    t.write (sorteio[i], font='arial, 16')
                    acertos=acertos+1 #adiciona 1 a variavel acertos
                    penup()
                    found=1
                elif variavel == 'A' and sorteio[i] == 'Ã': #iguala acentos e não acentos
                    #Ao digitar A, o Ã é escrito também
                    t.setpos(-200+i*40,-200)
                    pendown()
                    t.write (sorteio[i], font='arial, 16')
                    acertos=acertos+1
                    penup()
                    found=1
                elif variavel == 'E' and sorteio[i] == 'Ê': #elimina acentos
                #Ao digitar E, o Ê também é escrito
                    t.setpos(-200+i*40,-200)
                    pendown()
                    t.write (sorteio[i], font='arial, 16') 
                    acertos=acertos+1
                    penup()
                    found=1
                elif variavel == 'I' and sorteio[i] == 'Í': #retira acentos
                #Ao digitar I, o Í também é escrito
                    t.setpos(-200+i*40,-200)
                    pendown()
                    t.write (sorteio[i], font='arial, 16')
                    acertos=acertos+1
                    penup()
                    found=1
                elif variavel == 'O' and sorteio[i] == 'Ó': 
                #elimina acentos. Ao digitar O, o Ó também é escrito
                    t.setpos(-200+i*40,-200)
                    pendown()
                    t.write (sorteio[i], font='arial, 16')
                    acertos=acertos+1
                    penup()
                    found=1
                elif variavel == 'O' and sorteio[i] == 'Ô':
                #acentos. Ao digitar O, o Ô também é escrito
                    t.setpos(-200+i*40,-200)
                    pendown()
                    t.write (sorteio[i], font='arial, 16')
                    acertos=acertos+1
                    penup()
                    found=1
                
                    
            if found==0 and len(variavel)==1 and variavel!=" " and variavel not in string.digits : 
            #se a letra digitada for tiver 1 caractér e ser diferente de espaço, 
            #é valida, mas a letra não esta na palavra
                    erros=erros+1 #adiciona 1 a variavel erro
                    erros_total=erros_total+1 #adiciona 1 a variavel erro_total
                    #para o calculo da média
                    print(erros_total)
                            
                    if erros == 1:
                        cabeca() #chama a função que desenha a cabeça
                    if erros == 2:
                        corpo() #chama a função que desenha o corpo
                    if erros == 3:
                        perna1() #chama a função que desenha a perna1
                    if erros == 4:
                        perna2() #chama a função que desenha a perna2
                    if erros == 5:
                        braco1() #chama a função que desenha a braco1
                    if erros == 6:
                        braco2() #chama a função que desenha a braco2
                        
            if len(variavel)!=1 or variavel==" " or variavel in string.digits : #se a letra digitada(variavel)
            #tiver um número de caracteres diferentes de 1 ou igual a espaço, 
            #escreva que a palavra é inválida
                t1 = Turtle()
                t1.hideturtle()
                t1.write ('letra inválida', font=('arial', 18))
                time.sleep(1.5)
                t1.clear()
                
                    
        else: #se a letra estiver na lista de letras_usadas
            t2 = Turtle()
            t2.hideturtle()
            t2.write ('letra já inserida', font=('arial', 18))
            time.sleep(1.5)
            t2.clear()
            
    if erros>=6: #quando a variavel erros for igual a 6 (boneco for completo)
        t.penup()
        t.setpos(0,0)
        t.pendown()
        t.write ('ENFORCADO- FIM DE JOGO', font=('arial', 16))#escreve que foi enforcado, fim do jogo
        t.penup()
        t.setpos(50,200)
        t.pendown()
        t.write ('PLACAR:' + str(erros) + ' erros', font=('arial', 16))
        #escreve o numero de erros naquela rodada
        t.penup()
        t.setpos(50,150)
        t.pendown()
        t.write ('MÉDIA DE ERROS:' + str((erros_total)/len(palavras_usadas)) + ' erros', font=('arial', 16))
        #digita a media de erros por rodada
        t.penup()
        

    if acertos == len(sorteio)-sorteio.count(' '):#quando o número de acertos
    #for igual ao número de letras, a palavra estará completa
        t.penup()
        t.setpos(0,0)
        t.pendown()
        t.write ('VOCÊ GANHOU', font=('arial', 16)) #escreve que você ganhou
        t.penup()
        t.setpos(50,200)
        t.pendown()
        t.write ('PLACAR:' + str(erros) + ' erros', font=('arial', 16))#escreve
        #o número de erros naquela rodada
        t.penup()
        t.setpos(50,150)
        t.pendown()
        t.write ('MÉDIA DE ERROS:' + str((erros_total)/len(palavras_usadas)) + ' erros', font=('arial', 16))
        #escreve a média de erros em todas as rodadas
        t.penup()
        

    if len(palavras_usadas)!=len(lista_palavras): #quando o numero de palavras_usadas
    #for diferente do número de palavras da lista_palavras, pergunta se deseja jogar de novo
        continuar = window.textinput("", "VOCÊ QUER JOGAR NOVAMENTE?")
        t.clear()

    else: #caso o número de palavras da lista palavras_usadas for igual ao número de
    #palavras da lista lista_palavras, o jogo se encerra, pois não sobraram palavras novas.
        continuar = 'nao'
        t.clear()
        t.penup()
        t.setpos(-300,0)    
        t.write ('VOCÊ TERMINOU O JOGO', font=('arial', 22))#avisa que o jogo terminou
        t.penup()
        t.setpos(-300,50)
        t.pendown()
        t.write ('MÉDIA DE ERROS:' + str((erros_total)/len(palavras_usadas)) + ' erros', font=('arial', 16))
        #escreve a media de erros de todas as rodadas
        t.penup()
        
        
exitonclick()    #fecha a janela com um click