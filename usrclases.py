# Proyecto número 2
# Aquí se definen las clases de los juegos: Cálculo matemático y
# conversión binaria.
# Se requieren las funciones rmove y rename del módulo os


from os import remove, rename


class UsrClase:
    def getuser_score(self, user_name):
        try:
            scores = open("user_scores.txt", "r", encoding="utf-8")
            for line in scores:
                lista_user = line.split(",")
                if lista_user[0] == user_name:
                    scores.close()
                    return lista_user[1]
                scores.close()
                return "-1"
        except IOError:
            print(
                "\nArchivo user_scores.txt no se encontró. "
                "Un nuevo archivo será creado"
            )
            scores = open("user_scores.txt", "w", encoding="utf-8")
            scores.close()
            return "-1"

    def upadateuser_score(self, new_user, user_name, score):
        if new_user:
            scores = open("user_scores.txt", "a", encoding="utf-8")
            scores.write("\n" + user_name + "," + str(score))
            scores.close()
        else:
            scores = open("user_scores.txt", "r", encoding="utf-8")
            scorestmp = open("user_scores.tmp", "w", encoding="utf-8")
            for line in scores:
                lista_user = line.split(",")
                if lista_user[0] == user_name:
                    # Al crearse una línea debe incluirse una "nueva línea"
                    line = user_name + "," + str(score) + "\n"
                # si viene directo del otro archivo ya tiene su "neva línea"
                scorestmp.write(line)
            scores.close()
            scorestmp.close()
            remove("user_scores.txt")
            rename("user_scores.tmp", "user_scores.txt")
