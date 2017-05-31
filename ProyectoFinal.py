from tkinter import*
import random

v=Tk()
v.title("DEATH RACE")
can=Canvas(v,width=680,height=480)
can.config(bg="black")
can.pack()
can.focus_set()
#IMPORTAR IMAGENES=========================
fondomenu=PhotoImage(file="Menu5.png")
jugador1=PhotoImage(file="Player12.png")
jugador2=PhotoImage(file="Player22.png")
Mini=PhotoImage(file="Mini.png")
Runner=PhotoImage(file="Runner.png")
Runner2=PhotoImage(file="Runner2.png")
Mancha=PhotoImage(file="ManchaAceite.png")
Gasolina=PhotoImage(file="gasolina.png")
Titulo=PhotoImage(file="titulo.png")
GameOver=PhotoImage(file="gameover.png")
ChoqueI=PhotoImage(file="choque.png")
#MENU=====================================
def Menu():
    """
    Descripcion: Este es el primer menu, que cuenta con los botones de
    Nuevo Juego, Cargar Partida y Salir.
    """
    Menu1=Label(can,image=fondomenu)
    Menu1.place(x=0,y=0)
    botonsalir=Button(can,command=v.destroy,text="Salir",font=("Fixedsys",20))
    botonsalir.place(x=310,y=400)
    botonnew=Button(can,command=Menu2,text="Nuevo Juego",font=("Fixedsys",20))
    botonnew.place(x=270,y=200)
    botoncargar=Button(can,command=Cargar,text="Cargar Partida",font=("Fixedsys",20))
    botoncargar.place(x=240,y=300)
    Titulo1=Label(can,image=Titulo)
    Titulo1.place(x=170,y=20)
#SELECCIONAR NIVEL==============================
def Menu2():
    """
    Descripcion: En este menu se abre al darle Nuevo Juego, y en este se
    escriben los nombres de los dos jugadores, y se selecciona el nivel.
    """
    global TextUsuario1,TextUsuario2,entrada,entrada2
    Menu2=Label(can,image=fondomenu)
    Menu2.place(x=0,y=0)
    #USUARIOS
    Usuario1=Label(can,text="Usuario1:", font=("Fixedsys",15))
    Usuario1.place(x=30,y=100)
    entrada=StringVar()
    TextUsuario1=Entry(can,textvariable=entrada)
    TextUsuario1.place(x=120,y=100)
    Usuario2=Label(can,text="Usuario2:", font=("Fixedsys",15))
    Usuario2.place(x=30,y=200)
    entrada2=StringVar()
    TextUsuario1=Entry(can,textvariable=entrada2)
    TextUsuario1.place(x=120,y=200)
    #BOTONES NIVELES
    botonNivel1=Button(can,command=Level,text="Nivel1",font=("Fixedsys",15))
    botonNivel1.place(x=550,y=100)
    botonNivel2=Button(can,command=Level2,text="Nivel2",font=("Fixedsys",15))
    botonNivel2.place(x=550,y=150)
    botonNivel3=Button(can,command=Level3,text="Nivel3",font=("Fixedsys",15))
    botonNivel3.place(x=550,y=200)
    botonNivel4=Button(can,command=Level4,text="Nivel4",font=("Fixedsys",15))
    botonNivel4.place(x=550,y=250)
    botonNivel5=Button(can,command=Level5,text="Nivel5",font=("Fixedsys",15))
    botonNivel5.place(x=550,y=300)
    #REGRESAR
    botonNivel1=Button(can,command=Menu,text="Regresar",font=("Fixedsys",15))
    botonNivel1.place(x=30,y=300)

#JUGAR===================================================
def jugar():
    """
    Descripcion: Esta funcion basicamente es para ahorra llamar funciones, se
    llaman aqui, y luego esta funcion es llamada en los niveles.
    """
    global Tiempo, player2,player1,BarraG1,BarraG2,BarraGrafica1,BarraGrafica2,Tiempo1,Tiempo2,Temporizador1,Temporizador2,juego,NombreUsuario1,entrada,entrada2,Contador1,Contador2
    juego=True
    Contador1=0
    Contador2=0
    NombreUsuario1=Label(can,text=entrada.get())
    NombreUsuario1.place(x=1250,y=10)
    NombreUsuario2=Label(can,text=entrada2.get())
    NombreUsuario2.place(x=1250,y=400)
    Temporizador1=Label(can,text="Temporizador1: 0")
    Temporizador1.place(x=1200,y=110)
    Temporizador2=Label(can,text="Temporizador2: 0")
    Temporizador2.place(x=1200,y=500)
    Tiempo1=0
    Tiempo2=0
    BarraGrafica1=can.create_rectangle(1300,110,1330,310,fill="Blue")
    BarraGrafica2=can.create_rectangle(1300,500,1330,700,fill="Red")
    BarraG1=200
    BarraG2=200
    player1=can.create_image(200,500,image=jugador1,anchor=NW)
    player2=can.create_image(800,500,image=jugador2,anchor=NW)
    Tiempo=0
    entrada=entrada.get()
    entrada2=entrada2.get()
    MovMapa()
    Movimiento()
    Enemigos()
    AparecerEne()
    PerdidaG()
    
#PERDIDA GASOLINA============================================
def PerdidaG():
    """
    Descripcion: En esta funcion se crean los rectangulos los cuales son
    las barras de gasolina de ambos jugadores. Se especifica que si la gasolina
    de ambos es igual a cero pierden respectivamente.
    """
    global BarraG1,BarraG2,BarraGrafica1,BarraGrafica2,Temporizador1,Temporizador2
    if(juego):
        Temporizador1.destroy()
        Temporizador2.destroy()
        Temporizador1=Label(can,text="Temporizador1: "+str(Tiempo1))
        Temporizador1.place(x=1250,y=60)
        Temporizador2=Label(can,text="Temporizador2: "+str(Tiempo2))
        Temporizador2.place(x=1250,y=450)
        if(BarraG1>=0):
            can.delete(BarraGrafica1)
            BarraGrafica1=can.create_rectangle(1300,110,1330,110+BarraG1,fill="Blue")
            if(BarraG1==0):
                BarraG1-=1
                can.delete(player1)
        if(BarraG2>=0):
            can.delete(BarraGrafica2)
            BarraGrafica2=can.create_rectangle(1300,500,1330,500+BarraG2,fill="Red")
            if(BarraG2==0):
                BarraG2-=1
                can.delete(player2)
        if(BarraG2<=0 and BarraG1<=0):
            Perder()
        v.after(300,PerdidaG)

#NIVEL1=================================================
def Level():
    """
    Descripcion: Esta funcion es la del nivel 1, en esta se cargan la imagen,
    y se anima este nivel.
    """
    global can, player1,Level1, Level12, x,fondonivel1,fondonivel12,tiempoaparecer,vel,Nivel
    x=30
    tiempoaparecer=2200
    vel=2
    Nivel=1
    fondonivel1=PhotoImage(file="Nivel1.png")
    fondonivel12=PhotoImage(file="Nivel12.png")
    can.destroy()
    can=Canvas(v,width=1400,height=1012)
    can.config(bg="black")
    can.pack()
    Level1=can.create_image(0,0,image=fondonivel1,anchor=NW)
    Level12=can.create_image(0,-1012,image=fondonivel12,anchor=NW)
    can.bind("<Key>",key1)
    can.bind("<KeyRelease>",key2)
    can.focus_set()
    jugar()
    
#NIVEL2============================================
def Level2():
    """
    Descripcion: Esta funcion es la del nivel 2, en esta se cargan la imagen,
    y se anima este nivel.
    """
    global can, player1,Level1, Level12, x,fondonivel1,fondonivel12,tiempoaparecer,vel,Nivel
    x=40
    tiempoaparecer=2000
    vel=4
    Nivel=2
    fondonivel1=PhotoImage(file="Nivel2.png")
    fondonivel12=PhotoImage(file="Nivel22.png")
    can.destroy()
    can=Canvas(v,width=1400,height=1012)
    can.config(bg="black")
    can.pack()
    Level1=can.create_image(0,0,image=fondonivel1,anchor=NW)
    Level12=can.create_image(0,-1012,image=fondonivel12,anchor=NW)
    can.bind("<Key>",key1)
    can.bind("<KeyRelease>",key2)
    can.focus_set()
    jugar()
#NIVEL3============================================
def Level3():
    """
    Descripcion: Esta funcion es la del nivel 3, en esta se cargan la imagen,
    y se anima este nivel.
    """
    global can, player1,Level1, Level12, x,fondonivel1,fondonivel12,tiempoaparecer,vel,Nivel
    x=60
    tiempoaparecer=1500
    vel=6
    Nivel=3
    fondonivel1=PhotoImage(file="Nivel3.png")
    fondonivel12=PhotoImage(file="Nivel32.png")
    can.destroy()
    can=Canvas(v,width=1400,height=1012)
    can.config(bg="black")
    can.pack()
    Level1=can.create_image(0,0,image=fondonivel1,anchor=NW)
    Level12=can.create_image(0,-1012,image=fondonivel12,anchor=NW)
    can.bind("<Key>",key1)
    can.bind("<KeyRelease>",key2)
    can.focus_set()
    jugar()

#NIVEL4============================================
def Level4():
    """
    Descripcion: Esta funcion es la del nivel 4, en esta se cargan la imagen,
    y se anima este nivel.
    """
    global can, player1,Level1, Level12, x,fondonivel1,fondonivel12,tiempoaparecer,vel,Nivel
    x=70
    tiempoaparecer=1000
    vel=8
    Nivel=4
    fondonivel1=PhotoImage(file="Nivel4.png")
    fondonivel12=PhotoImage(file="Nivel42.png")
    can.destroy()
    can=Canvas(v,width=1400,height=1012)
    can.config(bg="black")
    can.pack()
    Level1=can.create_image(0,0,image=fondonivel1,anchor=NW)
    Level12=can.create_image(0,-1012,image=fondonivel12,anchor=NW)
    can.bind("<Key>",key1)
    can.bind("<KeyRelease>",key2)
    can.focus_set()
    jugar()

#NIVEL5============================================
def Level5():
    """
    Descripcion: Esta funcion es la del nivel 5, en esta se cargan la imagen,
    y se anima este nivel.
    """
    global can, player1,Level1, Level12, x,fondonivel1,fondonivel12,tiempoaparecer,vel,Nivel
    x=90
    tiempoaparecer=600
    vel=20
    Nivel=5
    fondonivel1=PhotoImage(file="Nivel5.png")
    fondonivel12=PhotoImage(file="Nivel52.png")
    can.destroy()
    can=Canvas(v,width=1400,height=1012)
    can.config(bg="black")
    can.pack()
    Level1=can.create_image(0,0,image=fondonivel1,anchor=NW)
    Level12=can.create_image(0,-1012,image=fondonivel12,anchor=NW)
    can.bind("<Key>",key1)
    can.bind("<KeyRelease>",key2)
    can.focus_set()
    jugar()

#TECLADO======================
def key1(event):
    """
    Descripcion: En esta funcion se agrega una letra a una lista, para
    posteriormente darle movimiento, para que el programa reconozca las teclas.
    """
    global Teclas
    tecla=repr(event.char)
    if tecla=="'g'":
        Guardar()
        juego=False
        v.destroy()
    elif(not(tecla in Teclas)):
        Teclas.append(tecla)
    

def key2(event):
    """
    Descripcion: Aqui se elimina la letra anteriormente agregada, para que se
    mueve a un lado cada que se presiona, y si no, no se mueva.
    """
    global Teclas
    tecla=repr(event.char)
    if(tecla in Teclas):
        Teclas.remove(tecla)
    
#MOVIMIENTO JUGADOR1======================
def Movimiento():
    """
    Descripcion: En esta funcion se hace el movimiento hacia derecha e izquierda
    con ayuda de condicionales, y se limita para que no pasen fuera de la pista.
    """
    global player1, player2
    if(juego):
        #TECLAS JUGADOR1
        if(BarraG1>0 and Contador1 <=0):
            if("'a'" in Teclas and can.coords(player1)[0]>=150):
                can.move(player1,-13,0)
            if("'d'" in Teclas and can.coords(player1)[0]<=980):
                can.move(player1,13,0)
            if("'w'" in Teclas and can.coords(player1)[1]>=0):
                can.move(player1,0,-5)
            if("'s'" in Teclas and can.coords(player1)[1]<=500):
                can.move(player1,0,5)
        #TECLAS JUGADOR2
        if(BarraG2>0 and Contador2 <=0):
            if("'j'" in Teclas and can.coords(player2)[0]>=150):
                can.move(player2,-13,0)
            if("'l'" in Teclas and can.coords(player2)[0]<=980):
                can.move(player2,13,0)
            if("'i'" in Teclas and can.coords(player2)[1]>=0):
                can.move(player2,0,-5)
            if("'k'" in Teclas and can.coords(player2)[1]<=500):
                can.move(player2,0,5)
        v.after(60,Movimiento)

#MOVIMIENTO MAPAS===============================
def MovMapa():
    """
    Descripcion: En esta funcion se animan los mapas, agregando una imagen igual
    a la otra cada vez que una termina, al igual que se eliminan los usuarios
    y se crean otra vez.
    """
    global Level1, Level12,player1,Ene,player2,Tiempo1,Tiempo2
    if(juego):
        can.move(Level1,0,x)
        can.move(Level12,0,x)
        if(BarraG1>0):
            Tiempo1+=1
        if(BarraG2>0):
            Tiempo2+=1
        if(can.coords(Level12)[1]>=0):
            can.delete(Level1)
            can.delete(Level12)
            Level1=can.create_image(0,0,image=fondonivel1,anchor=NW)
            Level12=can.create_image(0,-1012,image=fondonivel12,anchor=NW)
            if(BarraG1>0):
                tmp=can.coords(player1)
                can.delete(player1)
                player1=can.create_image(tmp[0],tmp[1],image=jugador1,anchor=NW)
            if(BarraG2>0):
                tmp=can.coords(player2)
                can.delete(player2)
                player2=can.create_image(tmp[0],tmp[1],image=jugador2,anchor=NW)

            for i in range(len(Ene)):
                tmp=can.coords(Ene[i][0])
                can.delete(Ene[i][0])
                if(Ene[i][1]==1):
                    Ene[i][0]=can.create_image(tmp[0],tmp[1],image=Mini,anchor=NW)
                if(Ene[i][1]==2):
                    Ene[i][0]=can.create_image(tmp[0],tmp[1],image=Runner,anchor=NW)
                if(Ene[i][1]==3):
                    Ene[i][0]=can.create_image(tmp[0],tmp[1],image=Runner2,anchor=NW)
                if(Ene[i][1]==4):
                    Ene[i][0]=can.create_image(tmp[0],tmp[1],image=Mancha,anchor=NW)
                if(Ene[i][1]==5):
                    Ene[i][0]=can.create_image(tmp[0],tmp[1],image=Gasolina,anchor=NW)
        v.after(80,MovMapa)
    
#DESESTABILIZAR=============================================================
def Desestabilizar():
    """
    Descripcion: En esta funcion se desestabiliza el jugador cuando toca la
    mancha de aceite.
    """
    global player1,Ene, Tiempo,player2
    if(juego):
        if(BarraG1>0):
            if Tiempo>0:
                if (can.coords(player1)[0]>=150):
                    can.move(player1,-10,0)
                if (can.coords(player1)[1]>=0):
                    can.move(player1,0,-5)
                Tiempo-=1
        if(BarraG2>0):
            if Tiempo<0:
                if (can.coords(player2)[0]>=150):
                    can.move(player2,-10,0)
                if (can.coords(player2)[1]>=0):
                    can.move(player2,0,-5)
                Tiempo+=1
        if Tiempo!=0:
            v.after(80,Desestabilizar)
 
#ENEMIGOS CHOQUE==============================================
Ene=[]
def Enemigos():
    """
    Descripcion: En esta funcion se crean todos los enemigos, tanto las manchas
    de aceite como todos los vehiculos enemigos, cambiando las coordenadas en
    X y en Y. Aqui tambien se incluye la gasolina, pero esta no quitan gasolina
    sino que por el contrario aumenta.
    """
    global Ene, Tiempo, BarraG1,BarraG2,Contador1,Contador2
    if(juego):
        for i in range(len(Ene)):
            #MACHAS DE ACEITE
            if Ene[i][1]==4:
                can.move(Ene[i][0],0,x)
                if(BarraG1>0):
                    if (max(can.coords(Ene[i][0])[0],(can.coords(player1)[0]))-min((can.coords(Ene[i][0])[0],(can.coords(player1)[0])))<=80):
                        if((max(can.coords(Ene[i][0])[1],(can.coords(player1)[1]))-min((can.coords(Ene[i][0])[1],(can.coords(player1)[1]))))<=150):
                            Tiempo=40
                            Desestabilizar()
                            can.delete(Ene[i][0])
                            Ene.pop(i)
                            break
                if(BarraG2>0):
                    if (max(can.coords(Ene[i][0])[0],(can.coords(player2)[0]))-min((can.coords(Ene[i][0])[0],(can.coords(player2)[0])))<=80):
                        if((max(can.coords(Ene[i][0])[1],(can.coords(player2)[1]))-min((can.coords(Ene[i][0])[1],(can.coords(player2)[1]))))<=150):
                            Tiempo=-40
                            Desestabilizar()
                            can.delete(Ene[i][0])
                            Ene.pop(i)
                            break
            #GASOLINA
            if Ene[i][1]==5:
                can.move(Ene[i][0],0,x)
                if(BarraG1>0):
                    if (max(can.coords(Ene[i][0])[0],(can.coords(player1)[0]))-min((can.coords(Ene[i][0])[0],(can.coords(player1)[0])))<=80):
                        if((max(can.coords(Ene[i][0])[1],(can.coords(player1)[1]))-min((can.coords(Ene[i][0])[1],(can.coords(player1)[1]))))<=150):
                            Tiempo=40
                            can.delete(Ene[i][0])
                            Ene.pop(i)
                            if BarraG1<200:
                                BarraG1=BarraG1+50
                            if BarraG1>=200:
                                pass
                            
                            break
                if(BarraG2>0):
                    if (max(can.coords(Ene[i][0])[0],(can.coords(player2)[0]))-min((can.coords(Ene[i][0])[0],(can.coords(player2)[0])))<=80):
                        if((max(can.coords(Ene[i][0])[1],(can.coords(player2)[1]))-min((can.coords(Ene[i][0])[1],(can.coords(player2)[1]))))<=150):
                            Tiempo=-40
                            can.delete(Ene[i][0])
                            Ene.pop(i)
                            if BarraG2<200:
                                BarraG2=BarraG2+50
                            if BarraG2>=200:
                                pass
                            
                            break
            #ENEMIGO MINIVAN
            if Ene[i][1]==1:
                can.move(Ene[i][0],0, 6+vel)
                if(BarraG1>0):
                    if (max(can.coords(Ene[i][0])[0],(can.coords(player1)[0]))-min((can.coords(Ene[i][0])[0],(can.coords(player1)[0])))<=80):
                        if((max(can.coords(Ene[i][0])[1],(can.coords(player1)[1]))-min((can.coords(Ene[i][0])[1],(can.coords(player1)[1]))))<=150):
                            Contador1=10
                            Choque()
                            can.delete(Ene[i][0])
                            Ene.pop(i)
                            BarraG1=BarraG1-50
                            break
                if(BarraG2>0):
                    if (max(can.coords(Ene[i][0])[0],(can.coords(player2)[0]))-min((can.coords(Ene[i][0])[0],(can.coords(player2)[0])))<=80):
                        if((max(can.coords(Ene[i][0])[1],(can.coords(player2)[1]))-min((can.coords(Ene[i][0])[1],(can.coords(player2)[1]))))<=150):
                            Contador2=10
                            Choque()
                            can.delete(Ene[i][0])
                            Ene.pop(i)
                            BarraG2=BarraG2-50
                            break
            #ENEMIGO RUNNER
            if Ene[i][1]==2:
                can.move(Ene[i][0],5*Ene[i][2], 6+vel)
                if(can.coords(Ene[i][0])[0] >= 980 or can.coords(Ene[i][0])[0] <= 150):
                    Ene[i][2]*=-1
                if(BarraG1>0):
                    if (max(can.coords(Ene[i][0])[0],(can.coords(player1)[0]))-min((can.coords(Ene[i][0])[0],(can.coords(player1)[0])))<=80):
                        if((max(can.coords(Ene[i][0])[1],(can.coords(player1)[1]))-min((can.coords(Ene[i][0])[1],(can.coords(player1)[1]))))<=150):
                            Contador1=10
                            Choque()
                            can.delete(Ene[i][0])
                            Ene.pop(i)
                            BarraG1=BarraG1-50
                            break
                if(BarraG2>0):
                    if (max(can.coords(Ene[i][0])[0],(can.coords(player2)[0]))-min((can.coords(Ene[i][0])[0],(can.coords(player2)[0])))<=80):
                        if((max(can.coords(Ene[i][0])[1],(can.coords(player2)[1]))-min((can.coords(Ene[i][0])[1],(can.coords(player2)[1]))))<=150):
                            Contador2=10
                            Choque()
                            can.delete(Ene[i][0])
                            Ene.pop(i)
                            BarraG2=BarraG2-50
                            break
            #ENEMIGO FIGHTER       
            if Ene[i][1]==3:
                if(Ene[i][2]==1):
                    if(BarraG1>0):
                        if(can.coords(Ene[i][0])[0]>can.coords(player1)[0]):
                            can.move(Ene[i][0],-6,(4+vel))
                        else:
                            can.move(Ene[i][0],6,(4+vel))
                    else:
                        can.move(Ene[i][0],0,(4+vel))
                elif(Ene[i][2]==2):
                    if(BarraG2>0):
                        if(can.coords(Ene[i][0])[0]>can.coords(player2)[0]):
                            can.move(Ene[i][0],-6,(4+vel))
                        else:
                            can.move(Ene[i][0],6,(4+vel))
                    else:
                        can.move(Ene[i][0],0,(4+vel))
                if(BarraG1>0):
                    if (max(can.coords(Ene[i][0])[0],(can.coords(player1)[0]))-min((can.coords(Ene[i][0])[0],(can.coords(player1)[0])))<=80):
                        if((max(can.coords(Ene[i][0])[1],(can.coords(player1)[1]))-min((can.coords(Ene[i][0])[1],(can.coords(player1)[1]))))<=150):
                            Contador1=10
                            Choque()
                            can.delete(Ene[i][0])
                            Ene.pop(i)
                            BarraG1=BarraG1-50
                            break
                if(BarraG2>0):
                    if (max(can.coords(Ene[i][0])[0],(can.coords(player2)[0]))-min((can.coords(Ene[i][0])[0],(can.coords(player2)[0])))<=80):
                        if((max(can.coords(Ene[i][0])[1],(can.coords(player2)[1]))-min((can.coords(Ene[i][0])[1],(can.coords(player2)[1]))))<=150):
                            Contador2=10
                            Choque()
                            can.delete(Ene[i][0])
                            Ene.pop(i)
                            BarraG2=BarraG2-50
                            break
                        
        v.after(80,Enemigos)
#APARECER ENEMIGOS===========================================================
def AparecerEne():
    """
    Descripcion: En esta funcion se crea una lista para guardar a todos los enemigos
    y para hacer que aparezcan de forma aleatoria.
    """
    global Ene
    if(juego):
        posicion=random.randint(150,980)
        tipoene=random.randint(1,6)
        enemigos=[0,0,0]
        desplazamiento=[-1,1]
        if tipoene==1:
            enemigos[0]=can.create_image(posicion,-200,image=Mini,anchor=NW)
            enemigos[1]=tipoene
        if tipoene==2:
            enemigos[0]=can.create_image(posicion,-200,image=Runner,anchor=NW)
            enemigos[1]=tipoene
            t=random.randint(0,1)
            enemigos[2]=desplazamiento[t]
        if tipoene==3:
            enemigos[0]=can.create_image(posicion,-200,image=Runner2,anchor=NW)
            enemigos[1]=tipoene
            if(BarraG1>0 and BarraG2 >0):
                enemigos[2]=random.randint(1,2)
            elif(BarraG1>0):
                enemigos[2]=1
            elif(BarraG2>0):
                enemigos[2]=2
        if tipoene==4:
            enemigos[0]=can.create_image(posicion,-200,image=Mancha,anchor=NW)
            enemigos[1]=tipoene
        if tipoene==5:
            enemigos[0]=can.create_image(posicion,-200,image=Gasolina,anchor=NW)
            enemigos[1]=tipoene
        Ene.append(enemigos)

        v.after(tiempoaparecer,AparecerEne)
    
#PERDER==================================================
def Perder():
    """
    Descripcion: En esta funcion se abre una ventana con la imagen GAMEOVER cuando
    ambos jugadores han perdido, y posteriormente un mensaje indicando que
    jugador ha ganado mostrando su puntaje.
    """
    global can,juego
    juego=False
    can.destroy()
    can=Canvas(v,width=450,height=450)
    can.config(bg="black")
    can.pack()
    Over=Label(can,image=GameOver)
    Over.place(x=0,y=0)
    Over.pack()
    if(Tiempo1>Tiempo2):
        Ganador1=Label(text="El Usuario1 es el ganador con un puntaje de : "+str(Tiempo1))
        Ganador1.place(x=500,y=500)
        Ganador2=Label(text="El Usuario2 es el perdedor con un puntaje de : "+str(Tiempo2))
        Ganador2.place(x=500,y=550)
    elif(Tiempo2>Tiempo1):
        Ganador2=Label(text="El Usuario2 es el ganador con un puntaje de : "+str(Tiempo2))
        Ganador2.place(x=500,y=500)
        Ganador1=Label(text="El Usuario1 es el perdedor con un puntaje de : "+str(Tiempo1))
        Ganador1.place(x=500,y=550)
        
#CHOCAR UN ENEMIGO======================================================
def Choque():
    """
    Descripcion: En esta funcion se crea el efecto de explosion cuando un jugador
    choca contra un carro enemigo. Se cambia la imagen del jugador por la de
    una explosion por unos segundos.
    """
    global player1,player2,Contador1,Contador2
    if(juego):
        if(BarraG1>0):
            if Contador1>0:
                if(Contador1==10):
                    tmp=can.coords(player1)
                    can.delete(player1)
                    player1=can.create_image(tmp[0],tmp[1],image=ChoqueI,anchor=NW)
                Contador1-=1
                if Contador1==1:
                    tmp=can.coords(player1)
                    can.delete(player1)
                    player1=can.create_image(tmp[0],tmp[1],image=jugador1,anchor=NW)
                    Contador1=0
        if(BarraG2>0):
            if Contador2>0:
                if(Contador2==10):
                    tmp=can.coords(player2)
                    can.delete(player2)
                    player2=can.create_image(tmp[0],tmp[1],image=ChoqueI,anchor=NW)
                Contador2-=1
                if Contador2==1:
                    tmp=can.coords(player2)
                    can.delete(player2)
                    player2=can.create_image(tmp[0],tmp[1],image=jugador2,anchor=NW)
                    Contador2=0
        if (Contador1!=0 or Contador2!=0):
            v.after(50,Choque)
    
#GUARDAR===========================================================
def Guardar():
    """
    Descripcion: En esta funcion se guardan en un archivo llamado partida los
    datos mas importantes del juego. Como lo son la posicion de ambos jugadores,
    sus nombres, el tiempo y la barra de gasolina,la velocidad del nivel,
    vel de los enemigos,tiempo que tienen en aparecer y el nivel para saber en
    que nivel se encuentran. Se guardan las coordenadas
    siempre y cuando no esten muertos, sino guarda cualquier variable.
    Para habilitar esta opcion se presiona la letra "g".
    """
    archivo=open("Partida.txt","w")
    archivo.write(entrada+"\n")
    archivo.write(entrada2+"\n")
    if(BarraG1>0):
        archivo.write(str(can.coords(player1)[0])+"\n")
        archivo.write(str(can.coords(player1)[1])+"\n")
    else:
        archivo.write(str(10)+"\n")
        archivo.write(str(19)+"\n")
    if(BarraG2>0):
        archivo.write(str(can.coords(player2)[0])+"\n")
        archivo.write(str(can.coords(player2)[1])+"\n")
    else:
        archivo.write(str(10)+"\n")
        archivo.write(str(10)+"\n")
    archivo.write(str(Tiempo1)+"\n")
    archivo.write(str(Tiempo2)+"\n")
    archivo.write(str(BarraG1)+"\n")
    archivo.write(str(BarraG2)+"\n")
    archivo.write(str(x)+"\n")
    archivo.write(str(tiempoaparecer)+"\n")
    archivo.write(str(vel)+"\n")
    archivo.write(str(Nivel)+"\n")
    archivo.close()

#CARGAR PARTIDA================================================
def Cargar():
    """
    Descripcion: En esta funcion se cargan todos los datos guardados en la
    funcion Guardar(), se cargan en el mismo orden, y posteriormente se
    llama a la funcion JugarCargar(). Esta funcion es llamada al presionar
    el boton en el menu de CARGAR PARTIDA.
    """
    global entrada,entrada2,player1,player2,Tiempo1,Tiempo2,BarraG1,BarraG2,x,tiempoaparecer,vel,Nivel
    archivo=open("Partida.txt","r")
    entrada=archivo.readline().strip("\n")
    entrada2=archivo.readline().strip("\n")
    player1x=float(archivo.readline())
    player1y=float(archivo.readline())
    player2x=float(archivo.readline())
    player2y=float(archivo.readline())
    Tiempo1=int(archivo.readline())
    Tiempo2=int(archivo.readline())
    BarraG1=int(archivo.readline())
    BarraG2=int(archivo.readline())
    x=int(archivo.readline())
    tiempoaparecer=int(archivo.readline())
    vel=int(archivo.readline())
    Nivel=int(archivo.readline())
    archivo.close()
    JugarCargar(player1x,player1y,player2x,player2y)

#JUGAR LA PARTIDA CARGADA==============================
def JugarCargar(player1x,player1y,player2x,player2y):
    """
    Descripcion: En esta funcion es practicamente igual a la de los
    niveles, solo que que cargan todos los datos de guardados, ya sea el nivel
    y la posicion.
    """
    global can,Level1, Level12, x,fondonivel1,fondonivel12,tiempoaparecer,vel
    global Tiempo, player2,player1,BarraG1,BarraG2,BarraGrafica1,BarraGrafica2,Tiempo1,Tiempo2,Temporizador1,Temporizador2,Nivel,juego,entrada,entrada2,Contador1,Contador2
    Contador1=0
    Contador2=0
    juego=True
    if(Nivel==1):
        fondonivel1=PhotoImage(file="Nivel1.png")
        fondonivel12=PhotoImage(file="Nivel12.png")
    elif(Nivel==2):
        fondonivel1=PhotoImage(file="Nivel2.png")
        fondonivel12=PhotoImage(file="Nivel22.png")
    elif(Nivel==3):
        fondonivel1=PhotoImage(file="Nivel3.png")
        fondonivel12=PhotoImage(file="Nivel32.png")
    elif(Nivel==4):
        fondonivel1=PhotoImage(file="Nivel4.png")
        fondonivel12=PhotoImage(file="Nivel42.png")
    elif(Nivel==5):
        fondonivel1=PhotoImage(file="Nivel5.png")
        fondonivel12=PhotoImage(file="Nivel52.png")
    can.destroy()
    can=Canvas(v,width=1400,height=1012)
    can.config(bg="black")
    can.pack()
    Level1=can.create_image(0,0,image=fondonivel1,anchor=NW)
    Level12=can.create_image(0,-1012,image=fondonivel12,anchor=NW)
    can.bind("<Key>",key1)
    can.bind("<KeyRelease>",key2)
    can.focus_set()
    Temporizador1=Label(can,text="Temporizador1: "+str(Tiempo1))
    Temporizador1.place(x=1200,y=110)
    Temporizador2=Label(can,text="Temporizador2: 0"+str(Tiempo2))
    Temporizador2.place(x=1200,y=500)
    BarraGrafica1=can.create_rectangle(1300,110,1330,110+BarraG1,fill="Blue")
    BarraGrafica2=can.create_rectangle(1300,500,1330,500+BarraG2,fill="Red")
    if(BarraG1>0):
        player1=can.create_image(player1x,player1y,image=jugador1,anchor=NW)
    if(BarraG2>0):
        player2=can.create_image(player2x,player2y,image=jugador2,anchor=NW)

    NombreUsuario1=Label(can,text=entrada)
    NombreUsuario1.place(x=1250,y=10)
    NombreUsuario2=Label(can,text=entrada2)
    NombreUsuario2.place(x=1250,y=400)
    MovMapa()
    Movimiento()
    Enemigos()
    AparecerEne()
    PerdidaG()
    
Teclas=[]       
Menu()
can.mainloop()


