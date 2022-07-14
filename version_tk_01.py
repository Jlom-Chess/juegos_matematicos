# juegos matemáticos
import tkinter as tk
from math import sqrt
from random import choice, randint, uniform
from tkinter import ttk

import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class Juegos:
    def __init__(self, master):
        self.master = master
        self.guardar_indice = 0
        self.vacio = 0
        self.estado = 0
        self.a = 0.0
        self.b = 0.0
        self.reg_press = 0
        self.x = 0
        self.dif = 0
        self.c = 0.0
        self.determinante = 0.0
        self.x_1 = 0.0
        self.x_2 = 0.0
        self.g = 0
        self.nombre_reg = None
        self.dni_reg = None
        self.validat = None
        self.ent_nom = None
        self.frmk = None
        self.lbl_titulo = None
        self.boton1 = None
        self.boton2 = None
        self.boton_regresar = None
        self.boton_graficos = None
        self.mostrar_ge = None
        self.mostrar_pb = None
        self.mostrar_gb = None
        self.mostrar_gp = None
        self.mostrar_pe = None
        self.mostrar_pp = None
        self.frmx = None
        self.frm5 = None
        self.ent_resolv = None
        self.boton_ecuacion = None
        self.acertaste = None
        self.boton_intentar = None
        self.imprimir = None
        self.lblcorrecto_binario = None
        self.lblcorrecto_pemdas = None
        self.verdad_o_si = None
        self.verdad_o_no = None
        self.aux = None
        self.lbl_raices_correct = None
        self.ent_resolv2 = None
        self.lbl_mostrar = None
        self.lbl_mostrar2 = None
        self.lbl_raices_correct_d1 = None
        self.lbl_raices_correct_d2 = None
        self.mostrar_ec = None
        self.variable = None
        self.variable2 = None
        self.lbl_correcto = None
        self.frm4 = None
        self.columnas = np.array(
            [
                "DNI",
                "Nombre",
                "Partidas Pemdas Ganadas",
                "Partidas Pemdas Perdidas",
                "Partidas Binario Ganadas",
                "Partidas Binario Perdidas",
                "Partidas Ecuacion Ganadas",
                "Partidas Ecuacion Perdidas",
            ]
        )
        self.df = pd.read_excel("base_datos.xlsx")
        self.cont_gp = 0
        self.cont_pp = 0
        self.cont_gb = 0
        self.cont_pb = 0
        self.cont_ge = 0
        self.cont_pe = 0

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Coordenada central de la ventana
        w = 400
        h = 500
        x = int((screen_width / 2) - (w / 2))
        y = int((screen_height / 2) - (h / 2))

        master.geometry(f"{w}x{h}+{x}+{y}")
        master.title("Juegos Matemáticos")
        master.config(bg="#8990a2")
        master.resizable(0, 0)
        self.pos = 0
        self.el1 = 0
        self.val = 0
        self.frm = tk.Frame(self.master)
        frm1 = tk.Frame(self.frm)
        frm2 = tk.Frame(self.frm)
        self.frm3 = tk.Frame(self.frm)
        frm4 = tk.Frame(self.frm)

        self.frm.pack(padx=10, pady=20)
        frm1.pack(padx=10, pady=10)
        frm2.pack(padx=10, pady=10)
        self.frm3.pack(padx=10, pady=10)
        frm4.pack(padx=10, pady=10)
        self.ak = 0

        # --------frm 1--------
        lbl_juegos = tk.Label(frm1, font=("Arial 20"), text="Juegos Matemáticos")
        lbl_juegos.grid(row=1, column=0, padx=5, pady=5)

        # --------frm 2--------
        lbl_dni = tk.Label(frm2, font=("Arial 12"), text="DNI: ")
        self.ent_dni = tk.Entry(frm2)

        lbl_dni.grid(row=0, column=0, padx=5, pady=25)
        self.ent_dni.grid(row=0, column=1, padx=5, pady=25)

        # -------frm 3--------
        lbladvertencia = tk.Label(self.frm3, font=("Arial 12"), text="Bienvenido")
        lbladvertencia.grid(row=0, column=0, padx=5, pady=25)

        self.boton_pandas_1 = ttk.Button(
            frm4, text="Ingresar", cursor="hand2", command=self.validar
        )
        self.boton_pandas_1.grid(row=0, column=0, padx=5, pady=5)

        # ------frm principal------
        ttk.Style().configure("TButton", padding=5, relief="raised", background="gray")

        self.boton_salir = ttk.Button(
            self.master,
            text="Salir",
            width=20,
            command=self.master.destroy,
            cursor="hand2",
        )

        self.boton_salir.place(x=130, y=450)

    def validar(self):
        validacion = str(self.ent_dni.get())
        validacion2 = ""
        if self.val == 1:
            validacion2 = str(self.ent_nom.get()).replace(" ", "")
            if len(validacion2) == 0:
                validacion2 = "1"

        if (
            len(validacion) == 8 and validacion.isdigit()
        ) and not validacion2.isdigit():
            validacion = int(validacion)
            if self.pos == 0:
                self.hacer_excel()
            else:
                self.nombre_reg = self.ent_nom.get()
                self.dni_reg = self.ent_dni.get()
                self.abrir()

        else:
            self.el1 = 1
            self.validat = ttk.Label(
                self.frm3, font=("Arial 11"), text="Ingrese un DNI válido"
            )
            self.validat.grid(row=1, column=0, padx=5, pady=25)

    def hacer_excel(self):
        if self.el1 == 1:
            self.validat.destroy()
        self.vacio = 0
        self.el1 = 0
        variable_df = int(self.ent_dni.get())
        self.df = pd.read_excel("base_datos.xlsx")

        self.pos = 1

        if len(self.df["DNI"]) == 0:
            self.vacio = 1
            self.ing_dni()
        else:
            for i in range(len(self.df["DNI"])):
                if variable_df == self.df["DNI"][i]:
                    self.guardar_indice = i
                    self.nombre_reg = self.df["Nombre"][i]
                    self.dni_reg = self.df["DNI"][i]
                    self.abrir()
                else:
                    if self.ak == (len(self.df["DNI"]) - 1):
                        self.guardar_indice = i
                        self.vacio = 1
                        self.ing_dni()
                    else:
                        self.ak += 1

    def ing_dni(self):
        self.frm.destroy()
        self.boton_salir.destroy()
        self.val = 1
        self.frm = tk.Frame(self.master)
        frm1 = tk.Frame(self.frm)
        frm2 = tk.Frame(self.frm)
        self.frm3 = tk.Frame(self.frm)

        self.frm.pack(padx=10, pady=20)
        frm1.pack(padx=10, pady=10)
        frm2.pack(padx=10, pady=10)
        self.frm3.pack(padx=10, pady=10)

        # --------frm 1--------
        lbl_juegos = tk.Label(frm1, font=("Arial 20"), text="Juegos Matemáticos")
        lbl_juegos.grid(row=0, column=0, padx=5, pady=5)

        # --------frm 2--------
        lbl_nombre = tk.Label(frm2, font=("Arial 12"), text="Nombre: ")
        lbl_dni = tk.Label(frm2, font=("Arial 12"), text="DNI: ")
        self.ent_nom = tk.Entry(frm2)
        self.ent_dni = tk.Entry(frm2)

        lbl_nombre.grid(row=0, column=0, padx=5, pady=25)
        lbl_dni.grid(row=1, column=0, padx=5, pady=25)
        self.ent_nom.grid(row=0, column=1, padx=5, pady=25)
        self.ent_dni.grid(row=1, column=1, padx=5, pady=25)

        adv_1 = "No se encontró DNI en la base de datos"
        lbladvertencia = tk.Label(self.frm3, font=("Arial 12"), text=adv_1)
        lbladvertencia.grid(row=0, column=0, padx=5, pady=10)

        boton_ing = ttk.Button(
            self.frm3, text="Ingresar", command=self.validar, cursor="hand2"
        )
        boton_ing.grid(row=2, column=0, padx=5, pady=5)

        # ------frm principal------
        ttk.Style().configure("TButton", padding=5, relief="raised", background="gray")

        self.boton_salir = ttk.Button(
            self.master,
            text="Salir",
            width=20,
            command=self.master.destroy,
            cursor="hand2",
        )
        self.boton_salir.place(x=130, y=460)

    def abrir(self):
        self.frm.destroy()
        self.boton_salir.destroy()
        self.estado = 1
        self.frmk = tk.Frame(self.master)
        frm1 = tk.Frame(self.frmk)
        frm2 = tk.Frame(self.frmk)
        frm3 = tk.Frame(self.frmk)
        frm4 = tk.Frame(self.frmk)

        self.frmk.pack(padx=30, pady=20)
        frm1.pack(padx=30, pady=15)
        frm2.pack(padx=30, pady=15)
        frm3.pack(padx=10, pady=15)
        frm4.pack(padx=15, pady=15)
        # --------frm 1--------
        lbl_pemdas = tk.Label(frm1, font=("Arial 12"), text="Juego PEMDAS")
        boton_pemdas = ttk.Button(
            frm1, text="¡Jugar!", command=self.abrir2, cursor="hand2"
        )

        lbl_pemdas.grid(row=0, column=0, padx=5, pady=5)
        boton_pemdas.grid(row=0, column=1, padx=5, pady=5)

        # --------frm 2--------
        lbl_binario = tk.Label(frm2, font=("Arial 12"), text="Juego Binario    ")
        boton_binario = ttk.Button(
            frm2, text="¡Jugar!", command=self.abrir3, cursor="hand2"
        )

        lbl_binario.grid(row=0, column=0, padx=5, pady=5)
        boton_binario.grid(row=0, column=1, padx=5, pady=5)

        # --------frm 3--------
        lbl_ecuacion = tk.Label(frm3, font=("Arial 12"), text="Juego Ecuacion")
        boton_ecuacion = ttk.Button(
            frm3, text="¡Jugar!", command=self.abrir4, cursor="hand2"
        )
        lbl_nombre_reg = tk.Label(
            frm4, font=("Arial 12"), text=f"¡ Bienvenido {self.nombre_reg} !"
        )

        lbl_ecuacion.grid(row=0, column=0, padx=5, pady=5)
        boton_ecuacion.grid(row=0, column=1, padx=5, pady=5)
        lbl_nombre_reg.grid(row=0, column=0, padx=5, pady=5)

        # ------frm principal------
        ttk.Style().configure("TButton", padding=5, relief="raised", background="gray")

        self.boton1 = ttk.Button(
            self.master,
            text="Estadisticas",
            width=20,
            command=self.estadistica,
            cursor="hand2",
        )

        self.boton2 = ttk.Button(
            self.master, text="Salir", width=20, command=self.salir, cursor="hand2"
        )

        self.boton1.place(x=130, y=380)
        self.boton2.place(x=130, y=450)

    # ---------------------INTERFAZ ESTADISTICA-------------------------
    def estadistica(self):
        self.hacer_dataframe()
        if self.estado == 1:
            self.frmk.destroy()
            self.boton1.destroy()
            self.boton2.destroy()
        self.estado = 0
        # SE GUARDA EL VALOR DE LAS PARTIDAS GANADAS O PERDIDAS
        # EN CASO EL USUARIO SEA ANTIGUO SE MOSTRARA SUS RESULTADOS EN GENERAL
        self.mostrar_gp = self.df.loc[self.guardar_indice, "Partidas Pemdas Ganadas"]
        self.mostrar_pp = self.df.loc[self.guardar_indice, "Partidas Pemdas Perdidas"]
        self.mostrar_gb = self.df.loc[self.guardar_indice, "Partidas Binario Ganadas"]
        self.mostrar_pb = self.df.loc[self.guardar_indice, "Partidas Binario Perdidas"]
        self.mostrar_ge = self.df.loc[self.guardar_indice, "Partidas Ecuacion Ganadas"]
        self.mostrar_pe = self.df.loc[self.guardar_indice, "Partidas Ecuacion Perdidas"]

        self.frm = tk.Frame(self.master)
        frm1 = tk.Frame(self.frm)
        frm2 = tk.LabelFrame(self.frm, text="PEMDAS")
        frm3 = tk.LabelFrame(self.frm, text="Binario")
        frm4 = tk.LabelFrame(self.frm, text="Ecuacion")

        self.frm.pack(padx=30, pady=10)
        frm1.pack(padx=30, pady=10)
        frm2.pack(padx=30, pady=10)
        frm3.pack(padx=10, pady=10)
        frm4.pack(padx=10, pady=10)

        # --------frm 1--------
        self.lbl_titulo = tk.Label(frm1, font=("Arial 25"), text="Estadisticas:")
        self.lbl_titulo.grid(row=0, column=0, padx=5, pady=5)

        # --------frm 2--------
        lbl_esta_pem_gan = tk.Label(frm2, font=("Arial 12"), text="Ganados: ")
        lbl_esta_pem_gan.grid(row=0, column=0, padx=5, pady=5)

        lbl_esta_pem_gan_val = tk.Label(frm2, font=("Arial 13"), text=self.mostrar_gp)
        lbl_esta_pem_gan_val.grid(row=0, column=1, padx=5, pady=5)

        lbl_esta_pem_per = tk.Label(frm2, font=("Arial 12"), text="Perdidos: ")
        lbl_esta_pem_per.grid(row=1, column=0, padx=5, pady=5)

        lbl_esta_pem_per = tk.Label(frm2, font=("Arial 13"), text=self.mostrar_pp)
        lbl_esta_pem_per.grid(row=1, column=1, padx=5, pady=5)

        # --------frm 3--------
        lbl_esta_bin_gan = tk.Label(frm3, font=("Arial 12"), text="Ganados: ")
        lbl_esta_bin_gan.grid(row=0, column=0, padx=5, pady=5)

        lbl_esta_bin_gan_val = tk.Label(frm3, font=("Arial 13"), text=self.mostrar_gb)
        lbl_esta_bin_gan_val.grid(row=0, column=1, padx=5, pady=5)

        lbl_esta_bin_per = tk.Label(frm3, font=("Arial 12"), text="Perdidos: ")
        lbl_esta_bin_per.grid(row=1, column=0, padx=5, pady=5)

        lbl_esta_bin_per = tk.Label(frm3, font=("Arial 13"), text=self.mostrar_pb)
        lbl_esta_bin_per.grid(row=1, column=1, padx=5, pady=5)

        # --------frm 4--------
        lbl_esta_ecu_gan = tk.Label(frm4, font=("Arial 12"), text="Ganados: ")
        lbl_esta_ecu_gan.grid(row=0, column=0, padx=5, pady=5)

        lbl_esta_ecu_gan_val = tk.Label(frm4, font=("Arial 13"), text=self.mostrar_ge)
        lbl_esta_ecu_gan_val.grid(row=0, column=1, padx=5, pady=5)

        lbl_esta_ecu_per = tk.Label(frm4, font=("Arial 12"), text="Perdidos: ")
        lbl_esta_ecu_per.grid(row=1, column=0, padx=5, pady=5)

        lbl_esta_ecu_per = tk.Label(frm4, font=("Arial 13"), text=self.mostrar_pe)
        lbl_esta_ecu_per.grid(row=1, column=1, padx=5, pady=5)

        # ------frm principal------
        ttk.Style().configure("TButton", padding=5, relief="raised", background="gray")

        self.boton_regresar = ttk.Button(
            self.master, text="Juegos", width=10, command=self.reg_e, cursor="hand2"
        )

        self.boton_graficos = ttk.Button(
            root, text="Gráficos", width=20, command=self.graficar, cursor="hand2"
        )

        self.boton_salir = ttk.Button(
            root, text="Salir", width=10, command=self.salir, cursor="hand2"
        )

        self.boton_regresar.place(x=20, y=450)
        self.boton_graficos.place(x=130, y=450)
        self.boton_salir.place(x=300, y=450)

    def graficar(self):
        self.boton_graficos.destroy()
        self.frm.destroy()
        self.boton_regresar.destroy()
        self.boton_salir.destroy()
        self.frm = tk.Frame(self.master)
        frm1 = tk.Frame(self.frm)
        frm2 = tk.LabelFrame(self.frm, text="Gráfico")

        self.frm.pack(padx=30, pady=10)
        frm1.pack(padx=30, pady=10)
        frm2.pack(padx=30, pady=10)

        # --------frm 1--------
        self.lbl_titulo = tk.Label(frm1, font=("Arial 15"), text="Grafico:")
        self.lbl_titulo.grid(row=0, column=0, padx=5, pady=5)

        # --------frm 2--------
        f = Figure(figsize=(3.5, 4.5), dpi=70)
        ax = f.add_subplot(111)

        # data = [
        # [self.mostrar_gp, self.mostrar_gb, self.mostrar_ge],
        # [self.mostrar_pp, self.mostrar_pb, self.mostrar_pe],
        # ]

        # ind = ["Pemdas", "Binario", "Ecuacion"]
        # x_axis = np.arange(len(ind))
        # width = 0.2

        # rects1 = ax.bar(ind, data[0], width)
        # rects2 = ax.bar(x_axis + 0.2, data[1], width)
        ax.legend(labels=["Ganadas", "Perdidas"])

        canvas = FigureCanvasTkAgg(f, master=frm2)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # ------frm principal------
        ttk.Style().configure("TButton", padding=5, relief="raised", background="gray")

        self.boton_regresar = ttk.Button(
            self.master, text="Volver", width=10, command=self.reg_e, cursor="hand2"
        )

        self.boton_salir = ttk.Button(
            self.master, text="Salir", width=10, command=self.salir, cursor="hand2"
        )

        self.boton_regresar.place(x=20, y=450)
        self.boton_salir.place(x=300, y=450)

    def reg_e(self):
        if self.lbl_titulo["text"] == "Estadisticas:":
            self.boton_graficos.destroy()
            self.frm.destroy()
            self.boton_regresar.destroy()
            self.boton_salir.destroy()
            self.abrir()
        else:
            self.boton_regresar.destroy()
            self.boton_salir.destroy()
            self.frm.destroy()
            self.estadistica()

    # ---------------------INSTRUCCIONES PEMDAS-------------------------
    def abrir2(self):

        self.frmk.destroy()
        self.boton1.destroy()
        self.boton2.destroy()

        self.frmx = tk.Frame(self.master)
        frm1 = tk.Frame(self.frmx)
        frm2 = tk.LabelFrame(self.frmx, text="Dificultad")
        frm3 = tk.Frame(self.frmx)

        self.frmx.pack(padx=30, pady=10)
        frm1.pack(padx=30, pady=10)
        frm2.pack(padx=30, pady=15)
        frm3.pack(padx=10, pady=10)

        self.a = tk.IntVar()

        # --------frm 1--------
        mensaje_1 = """
        Se le presentará una operación con
        suma, resta, multiplicación, división y
        exponencial. Responda correctamente
        la operacion mostrada.(aprox entero)
        """
        # --------frm 1--------
        self.lbl_titulo = tk.Label(frm1, font=("Arial 25"), text="Instrucciones")
        lbl_instrucciones_p = tk.Label(frm1, font=("Arial 12"), text=mensaje_1)

        lbl_instrucciones_p.grid(row=1, column=0, sticky=tk.W)
        self.lbl_titulo.grid(row=0, column=0, padx=5, pady=5)

        # --------frm 2--------
        radio_buton_pem = tk.Radiobutton(frm2, text="Facil", variable=self.a, value=0)
        radio_buton_pem.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        radio_buton__pem_2 = tk.Radiobutton(
            frm2, text="Intermedio", variable=self.a, value=1
        )
        radio_buton__pem_2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        radio_buton__pem_3 = tk.Radiobutton(
            frm2, text="Dificil", variable=self.a, value=2
        )
        radio_buton__pem_3.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        lbl_ecuacion = tk.Label(frm3, font=("Arial 12"), text="Juego Pemdas:")
        boton_ecuacion = ttk.Button(
            frm3, text="¡Jugar!", command=self.abrir5, cursor="hand2"
        )

        lbl_ecuacion.grid(row=0, column=0, padx=5, pady=5)
        boton_ecuacion.grid(row=0, column=1, padx=5, pady=5)

        # ------Botones--------
        ttk.Style().configure("TButton", padding=5, relief="raised", background="gray")

        self.boton_salir = ttk.Button(
            self.master, text="Salir", width=20, command=self.salir, cursor="hand2"
        )

        self.boton_regresar = ttk.Button(
            self.master,
            text="Regresar",
            width=20,
            command=self.regresar,
            cursor="hand2",
        )

        self.boton_regresar.place(x=10, y=450)
        self.boton_salir.place(x=250, y=450)

    # ---------------------INSTRUCCIONES BINARIO-------------------------

    def abrir3(self):
        self.frmk.destroy()
        self.boton1.destroy()
        self.boton2.destroy()

        self.frmx = tk.Frame(self.master)
        frm1 = tk.Frame(self.frmx)
        frm2 = tk.LabelFrame(self.frmx, text="Dificultad")
        frm3 = tk.Frame(self.frmx)

        self.frmx.pack(padx=30, pady=10)
        frm1.pack(padx=30, pady=10)
        frm2.pack(padx=30, pady=15)
        frm3.pack(padx=10, pady=15)

        self.b = tk.IntVar()
        # --------frm 1--------
        mensaje_1 = """
            Se le presentará un numero en
            base 10 para su conversión a
            un numero binario o en base 2
        """
        # --------frm 1--------
        self.lbl_titulo = tk.Label(frm1, font=("Arial 25"), text="Instrucciones")
        lbl_instrucciones_p = tk.Label(frm1, font=("Arial 12"), text=mensaje_1)

        lbl_instrucciones_p.grid(row=1, column=0, sticky=tk.W)
        self.lbl_titulo.grid(row=0, column=0, padx=5, pady=5)

        # --------frm 2--------
        radio_buton_bin = tk.Radiobutton(frm2, text="Facil", variable=self.b, value=0)
        radio_buton_bin.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        radio_buton_bin_2 = tk.Radiobutton(
            frm2, text="Intermedio", variable=self.b, value=1
        )
        radio_buton_bin_2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        radio_buton_bin_3 = tk.Radiobutton(
            frm2, text="Dificil", variable=self.b, value=2
        )
        radio_buton_bin_3.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        # --------------------
        lbl_ecuacion = tk.Label(frm3, font=("Arial 12"), text="Juego Binario:")
        boton_ecuacion = ttk.Button(
            frm3, text="¡Jugar!", command=self.abrir6, cursor="hand2"
        )
        lbl_ecuacion.grid(row=0, column=0, padx=5, pady=5)
        boton_ecuacion.grid(row=0, column=1, padx=5, pady=5)

        # ------Botones--------
        ttk.Style().configure("TButton", padding=5, relief="raised", background="gray")

        self.boton_salir = ttk.Button(
            self.master, text="Salir", width=20, command=self.salir, cursor="hand2"
        )

        self.boton_regresar = ttk.Button(
            self.master,
            text="Regresar",
            width=20,
            command=self.regresar,
            cursor="hand2",
        )

        self.boton_regresar.place(x=10, y=450)
        self.boton_salir.place(x=250, y=450)

    # ---------------------INSTRUCCIONES ECUACIÓN-------------------------
    def abrir4(self):
        # se destruye los frames anteriores
        self.frmk.destroy()
        self.boton1.destroy()
        self.boton2.destroy()
        # se creean nuevos frames
        self.g = tk.IntVar()
        self.frmx = tk.Frame(self.master)
        frm1 = tk.Frame(self.frmx)
        frm2 = tk.LabelFrame(self.frmx, text="Dificultad")
        frm3 = tk.Frame(self.frmx)

        self.frmx.pack(padx=30, pady=10)
        frm1.pack(padx=10, pady=10)
        frm2.pack(padx=30, pady=15)
        frm3.pack(padx=10, pady=15)

        # --------frm 1--------se muestra el mesaje de la instruccion
        mensaje_1 = """
            Se le mostrará una ecuación cuadrática,
            debe determinar si tiene raíces reales.
            En caso acierte, se le pedirá ingresar
            las raíces, en caso no acierte, se le
            mostrará porqué se equivocó.
        """

        self.lbl_titulo = tk.Label(frm1, font=("Arial 25"), text="Instrucciones")
        lbl_instrucciones_p = tk.Label(frm1, font=("Arial 12"), text=mensaje_1)

        lbl_instrucciones_p.grid(row=1, column=0, sticky=tk.W)
        self.lbl_titulo.grid(row=0, column=0, padx=5, pady=5)

        # --------frm 2--------
        # configuracion de los radiobuttons para la dificultad
        radio_buton_ecu = tk.Radiobutton(frm2, text="Facil", variable=self.g, value=0)
        radio_buton_ecu.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        radio_buton_ecu_2 = tk.Radiobutton(
            frm2, text="Intermedio", variable=self.g, value=1
        )
        radio_buton_ecu_2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        radio_buton_ecu_3 = tk.Radiobutton(
            frm2, text="Dificil", variable=self.g, value=2
        )
        radio_buton_ecu_3.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        # ----------frm 3---------
        lbl_ecuacion = tk.Label(frm3, font=("Arial 12"), text="Juego Ecuación:")
        boton_ecuacion = ttk.Button(
            frm3, text="¡Jugar!", command=self.abrir7, cursor="hand2"
        )

        lbl_ecuacion.grid(row=0, column=0, padx=5, pady=5)
        boton_ecuacion.grid(row=0, column=1, padx=5, pady=5)

        # ------frm principal------
        ttk.Style().configure("TButton", padding=5, relief="raised", background="gray")

        self.boton_salir = ttk.Button(
            self.master, text="Salir", width=20, command=self.salir, cursor="hand2"
        )

        self.boton_regresar = ttk.Button(
            self.master,
            text="Regresar",
            width=20,
            command=self.regresar,
            cursor="hand2",
        )

        self.boton_regresar.place(x=10, y=450)
        self.boton_salir.place(x=250, y=450)

    # ---------------------INTERFAZ JUEGO PEMDAS-------------------------
    def abrir5(self):
        # se eliminan los frames de la pestaña anterior
        self.frmx.destroy()
        self.boton_salir.destroy()
        self.boton_regresar.destroy()
        self.reg_press = 0
        # se crean nuevos frames para la pestaña
        self.frmx = tk.Frame(self.master)
        frm1 = tk.Frame(self.frmx)
        frm2 = tk.Frame(self.frmx)
        frm3 = tk.Frame(self.frmx)
        frm4 = tk.Frame(self.frmx)
        self.frm5 = tk.Frame(self.frmx)

        self.frmx.pack(padx=30, pady=10)
        frm1.pack(padx=30, pady=10)
        frm2.pack(padx=30, pady=15)
        frm3.pack(padx=10, pady=15)
        frm4.pack(padx=10, pady=10)
        self.frm5.pack(padx=10, pady=10)

        # --------frm 1--------
        self.lbl_titulo = tk.Label(frm1, font=("Arial 25"), text="Juego Pemdas")
        self.lbl_titulo.grid(row=0, column=0, padx=5, pady=5)
        # --------frm 2--------
        lbl_ecuacion = tk.Label(frm2, font=("Arial 12"), text="Resuelva:")
        lbl_ecuacion.grid(row=0, column=0, padx=5, pady=5)
        self.juego_pemdas()
        lbl_ecua_a_resolv = tk.Label(frm2, font=("Arial 14"), text=self.mostrar_ec)
        lbl_ecua_a_resolv.grid(row=0, column=1, padx=5, pady=5)
        # -------frm 3--------
        self.ent_resolv = tk.Entry(frm3, textvariable=tk.IntVar())
        lbl_ingresar_pemdas = tk.Label(
            frm3, font=("Arial 12"), text="Escriba la respuesta:"
        )
        lbl_ingresar_pemdas.grid(row=0, column=0, padx=5, pady=5)
        self.ent_resolv.grid(row=0, column=1, padx=5, pady=25)

        # -------frm 4--------
        self.boton_ecuacion = ttk.Button(
            frm4,
            text="Ingrese Respuesta",
            command=self.jugarbinario_pemdas,
            cursor="hand2",
            state="normal",
        )
        self.boton_ecuacion.grid(row=1, column=1, padx=5, pady=5)
        # ------frm principal------
        ttk.Style().configure("TButton", padding=5, relief="raised", background="gray")

        self.boton_regresar = ttk.Button(
            self.master, text="Juegos", width=10, command=self.regresar, cursor="hand2"
        )

        self.boton_salir = ttk.Button(
            self.master, text="Salir", width=10, command=self.salir, cursor="hand2"
        )

        self.boton_regresar.place(x=20, y=450)
        self.boton_salir.place(x=300, y=450)

    # ---------------------JUEGO PEMDAS-----------------------------------

    def juego_pemdas(self):
        nivel = self.a.get()  # se obtiene el valor del radio button
        # -----dificultad----
        if nivel == 0:
            x = 0
            y = 5
        elif nivel == 1:
            x = 6
            y = 11
        elif nivel == 2:
            x = 12
            y = 22

        while True:
            try:
                # prints a random value from the list
                list1 = ["*", "**", "/", "+", "-"]
                num = [randint(x, y) for i in range(5)]

                a = [randint(0, 4) for i in range(4)]
                aux = 0
                for element in a:
                    if element == 1 and aux < 3:
                        z = a.index(1, aux) + 1  # indice futuro
                        if element == a[z]:
                            a[z] = choice([i for i in range(0, 5) if i != 1])
                    aux += 1

                b = "0+1+2+3+4-"  # modelo para la creación de paréntesis aleatorio
                cont = 0

                while True:
                    if cont == 0:
                        aux2 = randint(0, len(b) - 1)

                    if cont == 0 and b[aux2].isdigit():
                        cont += 1
                        d = b[:aux2] + "(" + b[aux2:]

                    if cont > 0:
                        c = choice(
                            [i for i in range(len(d)) if i not in range(0, aux2 + 2)]
                        )

                        if not d[c].isdigit():
                            d = d[:c] + ")" + d[c:]
                            break
                b = d[:-1]
                lista_b = list(b)
                aux3 = 0
                aux4 = 0

                for k in lista_b:
                    if k.isdigit():
                        i = lista_b.index(k)
                        lista_b[i] = str(num[aux3])
                        aux3 += 1
                    if k == "+":
                        i = lista_b.index(k)
                        lista_b[i] = list1[a[aux4]]
                        aux4 += 1

                b = "".join(lista_b)
                newlist = list(b)
                za = 0
                c = newlist.count("/")
                for i in range(c):
                    indicex = newlist.index("/", za) + 1
                    if newlist[indicex] == "0":
                        newlist[indicex] = str(
                            choice([i for i in range(x, y + 1) if i != 0])
                        )
                    za = indicex

                b = "".join(newlist)
                if eval(b) >= -5000 and eval(b) <= 5000:
                    g = eval(b)
                    self.mostrar_ec = b.replace("**", "^")
                    break
            except ZeroDivisionError:
                pass
        self.imprimir = str(round(g))

    # ---------------------INTERFAZ JUEGO BINARIO-------------------------
    def abrir6(self):
        # se destruyen los frames de la pestaña anterior
        self.frmx.destroy()
        self.boton_salir.destroy()
        self.boton_regresar.destroy()
        self.frmx = tk.Frame(self.master)
        self.reg_press = 0
        # se crean nuevos frames para la pestaña
        frm1 = tk.Frame(self.frmx)
        frm2 = tk.Frame(self.frmx)
        frm3 = tk.Frame(self.frmx)
        frm4 = tk.Frame(self.frmx)
        self.frm5 = tk.Frame(self.frmx)

        self.frmx.pack(padx=30, pady=10)
        frm1.pack(padx=30, pady=10)
        frm2.pack(padx=30, pady=15)
        frm3.pack(padx=10, pady=15)
        frm4.pack(padx=10, pady=10)
        self.frm5.pack(padx=10, pady=10)

        # ------------frm 1--------
        self.lbl_titulo = tk.Label(frm1, font=("Arial 25"), text="Juego Binario")
        self.lbl_titulo.grid(row=0, column=0, padx=5, pady=5)
        # -------------frm 2--------
        lbl_ecuacion = tk.Label(frm2, font=("Arial 12"), text="Número decimal:")
        lbl_ecuacion.grid(row=0, column=0, padx=5, pady=5)
        # -----dificultad-----
        dificultad = self.b.get()
        if dificultad == 0:  # "facil"
            self.x = int(uniform(0, 10))
        elif dificultad == 1:  # "intermedio"
            self.x = int(uniform(11, 100))
        elif dificultad == 2:  # "dificil"
            self.x = int(uniform(101, 200))

        lbl_ecua_a_resolv = tk.Label(frm2, font=("Arial 14"), text=self.x)
        lbl_ecua_a_resolv.grid(row=0, column=1, padx=5, pady=5)

        # -------frm 3--------
        self.ent_resolv = tk.Entry(frm3, textvariable=tk.IntVar())
        lbl_ingresar_pemdas = tk.Label(
            frm3, font=("Arial 12"), text="Escriba el número binario:"
        )
        lbl_ingresar_pemdas.grid(row=0, column=0, padx=5, pady=5)
        self.ent_resolv.grid(row=0, column=1, padx=5, pady=25)

        # -------frm 4--------
        self.boton_ecuacion = ttk.Button(
            frm4,
            text="Ingrese Respuesta",
            command=self.jugarbinario_pemdas,
            cursor="hand2",
            state="normal",
        )
        self.boton_ecuacion.grid(row=1, column=1, padx=5, pady=5)

        # ------frm principal------
        ttk.Style().configure("TButton", padding=5, relief="raised", background="gray")

        self.boton_regresar = ttk.Button(
            self.master, text="Juegos", width=10, command=self.regresar, cursor="hand2"
        )

        self.boton_salir = ttk.Button(
            self.master, text="Salir", width=10, command=self.salir, cursor="hand2"
        )

        self.boton_regresar.place(x=20, y=450)
        self.boton_salir.place(x=300, y=450)

    # --------------------------Juego Binario----------------------------------------
    # se configura el juego y se comprueba si la respuesta es correcta
    def juego_binario(self):
        self.acertaste = ""
        y = []

        def decimal_a_binario(decimal):
            binario = 0
            multiplicador = 1

            while decimal != 0:
                binario = binario + decimal % 2 * multiplicador
                decimal //= 2
                multiplicador *= 10
            return binario

        acerto = self.ent_resolv.get()
        if acerto.isdigit() is True and int(acerto) == decimal_a_binario(self.x):
            self.cont_gb += 1
            self.acertaste = "¡Enhorabuena, acertaste!"
        else:
            # en caso no acerto se le mostrara la solucion
            # completando los ceros faltantes 0### o 0#######
            # binario tiene un formato de 8 o 4 digitos
            self.cont_pb += 1
            tam = len(str(decimal_a_binario(self.x)))
            while True:
                if tam < 4:
                    y.append("0")
                    tam += 1
                elif tam > 4 and tam < 8:
                    y.append("0")
                    tam += 1
                else:
                    break
            y = "".join(y)
            self.acertaste = (
                f"No acertaste, el número binario de {self.x} es "
                f"{y}{decimal_a_binario(self.x)}"
            )
        # -------frm 5--------
        self.lblcorrecto_binario = tk.Label(
            self.frm5, font=("Arial 10"), text=self.acertaste
        )
        self.lblcorrecto_binario.grid(row=0, column=0, padx=5, pady=5)

    # --------------Interaccion botones para Juego Pemdas,Binario y Ecuacion-----------
    # funcion despues de haber presionado el boton para verificar la respuesta
    # en esta se crea el boton intentar
    # para los dos ultimos juegos se comprueba la respuesta
    # para el primer juego se a ejecutar la funcion juego_binario
    def jugarbinario_pemdas(self):
        self.reg_press = 1  # variable para el retorno para evitar errores
        self.boton_ecuacion["state"] = "disabled"
        self.boton_intentar = ttk.Button(
            self.master,
            text="Intenta otra vez",
            width=20,
            command=self.intentarbinario_pemdas,
            cursor="hand2",
        )
        self.boton_intentar.place(x=130, y=450)
        if self.lbl_titulo["text"] == "Juego Binario":
            self.juego_binario()

        elif self.lbl_titulo["text"] == "Juego Pemdas":
            # --------------------------------
            variable = str(self.ent_resolv.get())
            if variable == self.imprimir:
                self.cont_gp += 1
                acertaste = "¡Enhorabuena, acertaste!"
            else:
                self.cont_pp += 1
                acertaste = f"No acertaste, la respuesta es {self.imprimir}"
            # -------frm 5--------
            self.lblcorrecto_pemdas = tk.Label(
                self.frm5, font=("Arial 12"), text=acertaste
            )
            self.lblcorrecto_pemdas.grid(row=0, column=0, padx=5, pady=5)

        elif self.lbl_titulo["text"] == "Juego Ecuacion":
            self.ent_resolv["state"] = "disabled"
            self.ent_resolv2["state"] = "disabled"
            self.boton_regresar["state"] = "normal"
            self.boton_ecuacion.destroy()
            self.variable = self.ent_resolv.get()
            self.variable2 = self.ent_resolv2.get()
            self.aux = 1
            if self.variable == self.x_1 and self.variable2 == self.x_2:
                self.cont_ge += 1
                acertaste = "¡Enhorabuena, acertaste!"
            else:
                self.cont_pe += 1
                acertaste = "No acertaste"
                self.mostrar_solucion()
            self.lbl_correcto = tk.Label(self.frm5, font=("Arial 11"), text=acertaste)
            self.lbl_correcto.grid(row=2, column=0, sticky="w")

    # funcion para la eliminacion de la respuesta y solucion en los 3 juegos
    # ademas de activar de nuevo los botones
    # funcion enlazada al boton_intentar

    def intentarbinario_pemdas(self):
        self.boton_intentar.destroy()
        if self.lbl_titulo["text"] == "Juego Binario":
            self.boton_ecuacion["state"] = "normal"
            self.ent_resolv.delete(0, tk.END)
            self.lblcorrecto_binario.destroy()
            self.abrir6()
        elif self.lbl_titulo["text"] == "Juego Pemdas":
            self.boton_ecuacion["state"] = "normal"
            self.ent_resolv.delete(0, tk.END)
            self.lblcorrecto_pemdas.destroy()
            self.abrir5()
        elif self.lbl_titulo["text"] == "Juego Ecuacion":
            self.lbl_mostrar.destroy()
            self.lbl_mostrar2.destroy()
            if self.aux == 0:
                self.lbl_raices_correct.destroy()
                self.lbl_raices_correct_d1.destroy()
                self.lbl_raices_correct_d2.destroy()
            self.abrir7()

    # ---------------------INTERFAZ JUEGO ECUACION-------------------------
    def abrir7(self):
        # borrado de los frames de la pestaña anterior
        self.frmx.destroy()
        self.boton_salir.destroy()
        self.boton_regresar.destroy()
        self.reg_press = 0
        self.aux = 0
        # creacion de los frames de la pestaña
        self.frmx = tk.Frame(self.master)
        frm1 = tk.Frame(self.frmx)
        frm2 = tk.Frame(self.frmx)
        self.frm3 = tk.LabelFrame(self.frmx, text="Si o no")
        self.frm4 = tk.Frame(self.frmx)
        self.frm5 = tk.Frame(self.frmx)
        self.reg_press = 0

        self.frmx.pack(padx=30, pady=10)
        frm1.pack(padx=10, pady=10)
        frm2.pack(padx=30, pady=10)
        self.frm3.pack(padx=30, pady=5)
        self.frm4.pack(padx=10, pady=5)
        self.frm5.pack(padx=10, pady=10)

        # --------frm 1--------
        self.lbl_titulo = tk.Label(frm1, font=("Arial 25"), text="Juego Ecuacion")
        self.lbl_titulo.grid(row=0, column=0, padx=5, pady=5)

        lbl_ecu = tk.Label(frm2, font=("Arial 12"), text="Ecuacion:")
        lbl_ecu.grid(row=0, column=0, padx=5, pady=5)

        # -----dificultad-----
        dificultad = self.g.get()  # se obtiene el valor de los radiobuttons
        # ingresados en la pestaña instrucciones
        if dificultad == 0:
            self.dif = [randint(1, 20) for x in range(3)]  # 1-20
        elif dificultad == 1:
            self.dif = [randint(5, 50) for x in range(3)]  # 1-80
        else:
            self.dif = [randint(10, 80) for x in range(3)]  # 1-150
        self.a = self.dif[0]
        self.b = self.dif[1]
        self.c = self.dif[2]
        self.determinante = self.b**2 - 4 * self.a * self.c  # b^2-4ac
        if self.b == 1:
            aux = ""
        else:
            aux = self.b
        if self.a == 1:
            aux2 = ""
        else:
            aux2 = self.a
        # --------frame2------
        # se muestra la ecuacion al usuario
        lbl_ecuacion = tk.Label(
            frm2, font=("Arial 13"), text=f"{aux2}x^2 + {aux}x + {self.c}"
        )
        lbl_ecuacion.grid(row=0, column=1, padx=5, pady=5)

        # --------frm 3--------
        # se muestra la pregunta si posee raices reales
        lbl_ingresar_pemdas = tk.Label(
            self.frm3, font=("Arial 11"), text="¿Tiene raices reales?"
        )
        lbl_ingresar_pemdas.grid(row=0, column=0, padx=1, pady=1)

        # botones si y no
        self.verdad_o_si = ttk.Button(
            self.frm3, text=" Si ", command=self.v_si, cursor="hand2", state="normal"
        )
        self.verdad_o_no = ttk.Button(
            self.frm3, text="No", command=self.v_no, cursor="hand2", state="normal"
        )
        # ubicacón y tamaño del cuadro del frame donde estan los botones
        self.verdad_o_si.grid(row=0, column=1, padx=5, pady=5)
        self.verdad_o_no.grid(row=1, column=1, padx=5, pady=5)
        # ------frm principal------
        # configuracion botones
        ttk.Style().configure("TButton", padding=5, relief="raised", background="gray")
        # boton regresar
        self.boton_regresar = ttk.Button(
            self.master,
            text="Juegos",
            width=10,
            command=self.regresar,
            cursor="hand2",
            state="normal",
        )
        # boton salir
        self.boton_salir = ttk.Button(
            self.master, text="Salir", width=10, command=self.salir, cursor="hand2"
        )

        self.boton_regresar.place(x=20, y=450)
        self.boton_salir.place(x=300, y=450)

    # ----------------Juego Ecuacion---------------
    def v_si(self):
        # se desactivan ambos botones
        self.verdad_o_si["state"] = "disabled"
        self.verdad_o_no["state"] = "disabled"
        # se utiliza verificar si es correcto o no de acuerdo a la pregunta(¿Tiene
        # raices reales?)
        # si no es se mostrara la solucion y un boton de volver a intentar
        # si es correcto se pasara al ingreso de la respuesta(funcion Juego_Ecuacion)
        if self.determinante >= 0:
            self.boton_regresar["state"] = "disabled"
            self.lbl_mostrar = tk.Label(self.frm3, font=("Arial 10"), text="Correcto")
            self.lbl_mostrar.grid(row=1, column=0, padx=1, pady=1)
            self.lbl_mostrar2 = tk.Label(
                self.frm3, font=("Arial 10"), text="Posee raíces reales"
            )
            self.lbl_mostrar2.grid(row=2, column=0, padx=1, pady=1)
            self.ent_resolv = tk.Entry(self.frm4)
            self.ent_resolv.grid(row=0, column=0, padx=5, pady=5)
            self.ent_resolv2 = tk.Entry(self.frm4)
            self.ent_resolv2.grid(row=0, column=1, padx=5, pady=5)
            self.boton_ecuacion = ttk.Button(
                self.frm4,
                text="Ingrese Respuesta",
                command=self.jugarbinario_pemdas,
                cursor="hand2",
            )
            self.boton_ecuacion.grid(row=1, column=0, padx=5, pady=5)
            self.juego_ecuacion()
        else:
            # variable para el retorno, configurado para evitar errores al eliminar
            # el boton intentar
            self.reg_press = 1
            self.cont_pe += 1  # contador puntos perdidos ecuacion
            self.lbl_mostrar = tk.Label(self.frm3, font=("Arial 10"), text="Incorrecto")
            self.lbl_mostrar.grid(row=1, column=0, padx=1, pady=1)
            self.lbl_mostrar2 = tk.Label(
                self.frm3, font=("Arial 10"), text="Posee raíces imaginarias"
            )
            self.lbl_mostrar2.grid(row=2, column=0, padx=1, pady=1)
            self.boton_intentar = ttk.Button(
                self.master,
                text="Intenta otra vez",
                width=20,
                command=self.intentarbinario_pemdas,
                cursor="hand2",
            )
            self.boton_intentar.place(x=130, y=450)
            self.mostrar_solucion()

    # Funcion cuando se presione el boton no

    def v_no(self):
        # se desactivan ambos botones
        self.verdad_o_si["state"] = "disabled"
        self.verdad_o_no["state"] = "disabled"
        # se utiliza verificar si es correcto o no
        # si no es se mostrara la solucion y un boton de volver a intentar
        # si es correcto se pasara al ingreso de la respuesta(funcion Juego_Ecuacion)
        if self.determinante >= 0:
            self.reg_press = 1
            self.cont_pe += 1
            self.lbl_mostrar = tk.Label(self.frm3, font=("Arial 10"), text="Incorrecto")
            self.lbl_mostrar.grid(row=1, column=0, padx=1, pady=1)
            self.lbl_mostrar2 = tk.Label(
                self.frm3, font=("Arial 10"), text="Posee raíces reales"
            )
            self.lbl_mostrar2.grid(row=2, column=0, padx=1, pady=1)
            self.boton_intentar = ttk.Button(
                self.master,
                text="Intenta otra vez",
                width=20,
                command=self.intentarbinario_pemdas,
                cursor="hand2",
            )
            self.boton_intentar.place(x=130, y=450)
            self.mostrar_solucion()
        else:
            self.boton_regresar["state"] = "disabled"
            self.lbl_mostrar = tk.Label(self.frm3, font=("Arial 10"), text="Correcto")
            self.lbl_mostrar.grid(row=1, column=0, padx=1, pady=1)
            self.lbl_mostrar2 = tk.Label(
                self.frm3, font=("Arial 10"), text="Posee raíces imaginarias"
            )
            self.lbl_mostrar2.grid(row=2, column=0, padx=1, pady=1)
            self.ent_resolv = tk.Entry(self.frm4)
            self.ent_resolv.grid(row=0, column=0, padx=10, pady=5)
            self.ent_resolv2 = tk.Entry(self.frm4)
            self.ent_resolv2.grid(row=0, column=1, padx=10, pady=5)
            self.boton_ecuacion = ttk.Button(
                self.frm4,
                text="Ingrese Respuesta",
                command=self.jugarbinario_pemdas,
                cursor="hand2",
            )
            self.boton_ecuacion.grid(row=1, column=0, padx=5, pady=5)
            self.juego_ecuacion()

    # muestra la solucion del juego ecuacion al equivocarse
    def mostrar_solucion(self):
        self.juego_ecuacion()
        self.lbl_raices_correct = tk.Label(
            self.frm5, font=("Arial 11"), text="Las raices son:"
        )
        self.lbl_raices_correct.grid(row=0, column=0, pady=5, sticky="w")
        self.lbl_raices_correct_d1 = tk.Label(
            self.frm5, font=("Arial 11"), text=f"x1={self.x_1}"
        )
        self.lbl_raices_correct_d1.grid(row=1, column=0, pady=5, sticky="w")
        self.lbl_raices_correct_d2 = tk.Label(
            self.frm5, font=("Arial 11"), text=f"x2={self.x_2}"
        )
        self.lbl_raices_correct_d2.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    # se usa para la configuracion del Juego Ecuacion
    # retorna el resultado de la ecuacion dada
    def juego_ecuacion(self):
        # se verifica que existen raices reales
        if self.determinante > 0:
            self.x_1 = -self.b + sqrt(self.b ** 2 - 4 * self.a * self.c) / (
                2 * self.a
            )
            self.x_2 = -1 * self.b - sqrt(self.b**2 - 4 * self.a * self.c) / (
                2 * self.a
            )
        # se verifica que existe 1 raiz real
        elif self.determinante == 0:
            self.x_1 = -1 * self.b / (2 * self.a), 3
            self.x_2 = ""

        # se verifica que existen raices imaginarias
        else:
            self.b = -1 * self.b
            self.x_1 = sqrt(4 * self.a * self.c - self.b**2) / (2 * self.a)
            self.x_2 = sqrt(4 * self.a * self.c - self.b**2) / (2 * self.a)

            if isinstance(self.x_1) == float:
                self.x_1 = round(self.x_1, 3)
            if isinstance(self.x_2) == float:
                self.x_2 = round(self.x_2, 3)

            self.x_1 = self.x_1 * 1j
            self.x_2 = self.x_2 * 1j

            self.x_1 = f"{self.b}+{self.x_1}"
            self.x_2 = f"{self.b}-{self.x_2}"

        if isinstance(self.x_1) == float:
            self.x_1 = round(self.x_1, 3)
        if isinstance(self.x_2) == float:
            self.x_2 = round(self.x_2, 3)

    # --------------Regresar funcion-------------
    # esta funcion sirve para el regreso a la pestaña anterior
    # se usa en los botones de los juegos e instrucciones para
    # regresar a la pestaña donde esta la seleccion de juegos

    def regresar(self):
        if self.lbl_titulo["text"] != "Instrucciones" and self.reg_press == 1:
            self.boton_intentar.destroy()
        self.frmx.destroy()
        self.boton_salir.destroy()
        self.boton_regresar.destroy()
        self.abrir()

    # funcion para guardar en el excel los datos recaudados
    # de los nombres, dni , partidas ganadas y perdidas de cada juego

    def hacer_dataframe(self):
        # se condiciona la creacion del dataframe para reconocer cuando
        # el usuario es nuevo o antiguo
        # Con esto al usuario antiguo solo se le sumara el puntaje mas no se reemplazará
        # y cuando es nuevo se guardara todos sus datos ingresados

        if self.vacio == 1:
            self.df = self.df.append(
                pd.Series(
                    [
                        int(self.dni_reg),
                        self.nombre_reg,
                        self.cont_gp,
                        self.cont_pp,
                        self.cont_gb,
                        self.cont_pb,
                        self.cont_ge,
                        self.cont_pe,
                    ],
                    index=self.columnas,
                ),
                ignore_index=True,
            )
            self.vacio = 0
        else:
            # ingresa cuando el usuario es antiguo para acumular el puntaje en
            # cada juego
            self.df.loc[self.guardar_indice, "Partidas Pemdas Ganadas"] += self.cont_gp
            self.df.loc[self.guardar_indice, "Partidas Pemdas Perdidas"] += self.cont_pp
            self.df.loc[self.guardar_indice, "Partidas Binario Ganadas"] += self.cont_gb
            self.df.loc[
                self.guardar_indice, "Partidas Binario Perdidas"
            ] += self.cont_pb
            self.df.loc[
                self.guardar_indice, "Partidas Ecuacion Ganadas"
            ] += self.cont_ge
            self.df.loc[
                self.guardar_indice, "Partidas Ecuacion Perdidas"
            ] += self.cont_pe
            self.cont_gp = 0
            self.cont_pp = 0
            self.cont_gb = 0
            self.cont_pb = 0
            self.cont_ge = 0
            self.cont_pe = 0

        self.df.to_excel("base_datos.xlsx", index=False)

    # Funcion para guardar en el dataframe y salir
    def salir(self):
        self.hacer_dataframe()
        self.master.destroy()


# Programa principal
root = tk.Tk()
app = Juegos(root)
root.mainloop()
