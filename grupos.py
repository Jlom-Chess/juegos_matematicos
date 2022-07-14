# grupos
#Variables
jugador=["pc", "participante", "empate"]
funciones=["piedra","papel","tijera"]
piedra=funciones[0];
papel=funciones[1];
tijera=funciones[2];
tiros=0;
jugadas=[0,0,0];
historiadeljuego=[];
ganador="";
mostrarfunciones=[0,1,2]
opcionparticipante="";
import random;

jugador[1]=input("Ingresar nombre del jugador: ");
print("bienvenido al juego:"+'participante');
print("elije una funcion: ","","1) piedra", "2) papel", "3)tijera", "",sep="\n");

while True:
    if (tiros < 3 and jugadas[0] !=2 and jugadas[1]!=2):
        opcionparticipante = (int(input("Selecciona una opcion: ")));
        opcionpc=(random.randrange(0,3));

        #gana pc
        if ((opcionparticipante == piedra and opcionpc == papel) or
            (opcionparticipante == papel and opcionpc == tijera) or
            (opcionparticipante == tijera and opcionpc == piedra)):
            jugada[0]=jugada[0]+1;
            ganador=jugador[0];

            #gana participante
        elif ((opcionparticipante == papel and opcionpc == piedra) or
            (opcionparticipante == tijera and opcionpc == papel) or
            (opcionparticipante == piedra and opcionpc == tijera)):
            jugada[1]=jugada[1]+1;
            ganador=jugador[1];

         #empate
        elif ((opcionparticipante == piedra and opcionpc == piedra) or
            (opcionparticipante == papel and opcionpc == papel) or
            (opcionparticipante == tijera and opcionpc == tijera)):
            jugada[2]=jugada[2]+1;
            ganador=jugador[2];
        tiros=tiros+1;

        print("----------------------")
        print("pc-"+ jugador[1]);
        print(opcionpc, opcionparticipante);
        print("ganador:"+ganador);
        print("jugadas:",juego);
        print("---------------------\n")
    else:
        if(juegadas[0]>jugadas[1]):
            ganador=participante[0];
        else:
            ganador=participante[1];
            historiadeljuego.append([jugadas[0], jugadas[1], jugadas[2],ganador]);

        sino=input("Desea continuar? Si/No")
        if sino.upper()!="Si":
            break
        else:
            tiros=0
            jugadas=[0,0,0];

print("El resultado del juego es: ");
print(historiadeljuego);