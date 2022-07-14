# Proyecto número 2
# Dos juegos: Cálculo matemático y conversión binaria
# Este es el programa principal.

from gameclasses import BinaryGame, MathGame, Game
from usrclases import UsrClase


def print_instructions(instruction):
    print(instruction)


math_instrucciones = """
    En este juego, se le hará una pregunta matemática,
    \ncada respuesta correcta le dará un punto.
    \nNo se reducen puntos por respuesta equivocadas
    """
binary_instrucciones = """
    En este juego se le presentara un número en base 10.
        \nSu tarea es convertir este número a base 2.
        \ncada respuesta correcta le dará un punto.
        \nNo se reducen puntos por respuesta equivocadas
        """

juego = Game()
bg = BinaryGame()
mg = MathGame()
usr = UsrClase()
try:
    user_name = input("Ingrese su nombre ")
    user_score = int(usr.getuser_score(user_name))
    if user_score == -1:
        user_score = 0
        new_user = True
    else:
        new_user = False

    print(f"\n¡Hola {user_name}!,¡Bienvenido al juego!")
    print(f"Tu puntaje actual es {user_score}")

    user_choice = "0"
    while user_choice != "-1":
        user_game = input("\n¿Juego matemático(1) o juego Binario(2)? ")
        while user_game != "1" and user_game != "2":
            print("\nSu respuesta debe ser 1 o 2")
            user_game = input("\n¿Juego matemático(1) o juego Binario(2)? ")

        num_prompt = input("\n¿Cuántas preguntas quieres por juego (1 a 10)? ")
        while True:
            try:
                num = int(num_prompt)
                break
            except ValueError:
                print(
                    "No ha ingresado un número válido,\
                      por favor inténtelo nuevamente"
                )
                num_prompt = input(
                    "\n¿Cuántas preguntas quieres por juego\
                                  (1 a 10) ?"
                )

        if user_game == "1":
            mg.no_of_questions = num
            print_instructions(math_instrucciones)
            user_score = user_score + mg.generate_questions()
        else:
            bg.no_of_questions = num
            print_instructions(binary_instrucciones)
            user_score = user_score + bg.generate_questions()

        print(f"\nSu puntaje actual es {user_score}")
        user_choice = input("¿Desea continuar el juego?. Digite -1 para salir ")
    usr.upadateuser_score(new_user, user_name, user_score)
except ValueError:
    print("No se ha ingresado un número")
