# Proyecto número 2
# Dos juegos: Cálculo matemático y conversión binaria
# Aquí se definirán las clases
# Habrá tres clases: Game, MathGame y BinaryGame

# Primera clase: Game
# La primera clase Game, será la clase padre o super clase de la cual
# se derivarán las otras

from random import randint


class Game:
    def __init__(self, no_of_questions=0):
        self.no_of_questions = no_of_questions
        if self.no_of_questions < 1:
            print(
                "\nMínimo número de preguntas es 1. \nEl numero de\
                  preguntas será establecido en 1"
            )
            self.no_of_questions = 1
        elif self.no_of_questions > 10:
            print(
                "\nMáximo número de preguntas es 10. \nEl numero de\
                  preguntas será establecido en 10"
            )
            self.no_of_questions = 10


class BinaryGame(Game):
    def generate_questions(self):
        score = 0
        for i in range(self.no_of_questions):
            base10 = randint(1, 100)
            print("\nConvierta el siguiente número a binario", base10)
            user_result = input("\nIngrese su respuesta ")
            while True:
                try:
                    answer = int(user_result, base=2)
                    if answer == base10:
                        score += 1
                        print("\n¡Respuesta correcta!")
                        break
                    else:
                        print(
                            f"\nRespuesta incorrecta. La respuesta correcta es {base10}"
                        )
                        break
                except ValueError:
                    print(
                        "Usted no ha ingresado un número binario,\nPor\
                          favor vuelva a ingresar su respuesta"
                    )
                    user_result = input("\nIngrese su nueva respuesta ")
        return score


class MathGame(Game):
    def __init__(self, no_of_questions):
        super().__init__(no_of_questions)

        self.question_string = ""
        self.score = 0
        self.operand_list = [0, 0, 0, 0, 0]
        self.operator_list = ["", "", "", ""]
        self.operator_dict = {1: "+", 2: "-", 3: "*", 4: "/", 5: "**"}

    def generate_questions(self):
        for i in range(self.no_of_questions):
            while True:
                for j, valor in enumerate(self.operand_list):
                    valor = randint(1, 9)
                    self.operand_list[j] = valor

                operator_anterior = ""
                for j, valor in enumerate(self.operator_list):
                    valor = self.operator_dict[randint(1, 5)]
                    self.operator_list[j] = valor
                    if self.operator_list[j] == "**" and operator_anterior == "**":
                        self.operator_list[j] = self.operator_dict[randint(1, 4)]
                        operator_anterior = self.operator_list[j]

                # Genera la expresión matemática
                open_bracket = randint(0, 3)
                close_bracket = randint(open_bracket + 1, 4)
                for j in range(0, 5):
                    if j == 0:
                        if open_bracket == 0:
                            self.question_string = "(" + str(self.operand_list[j])
                        else:
                            self.question_string = str(self.operand_list[j])
                    else:
                        if j == open_bracket:
                            self.question_string = (
                                self.question_string
                                + self.operator_list[j - 1]
                                + "("
                                + str(self.operand_list[j])
                            )
                        elif j == close_bracket:
                            self.question_string = (
                                self.question_string
                                + self.operator_list[j - 1]
                                + str(self.operand_list[j])
                                + ")"
                            )
                        else:
                            self.question_string = (
                                self.question_string
                                + self.operator_list[j - 1]
                                + str(self.operand_list[j])
                            )

                new_result = round(float(self.question_string), 2)
                if -50000 <= new_result <= 50000:
                    break
            self.question_string = self.question_string.replace("**", "^")

            print(f"\n{self.question_string}")
            respuesta = input(
                "Por favor ingrese su respuesta redondeado a 2 decimales) "
            )
            while True:
                try:
                    if float(respuesta) == new_result:
                        print(
                            "\n"
                            + "¡Respuesta correcta!,\
                              ha ganado un punto"
                        )
                        self.score += 1
                        break
                    else:
                        print(
                            "\n"
                            + "Respuesta incorrecta,\
                              la respuesta correcta es ",
                            new_result,
                        )
                        break
                except ValueError:
                    print(
                        "Usted no ingresó un número, por favor\
                          intente otra vez"
                    )
                    respuesta = input("Por favor ingrese su respuesta ")
        return self.score
