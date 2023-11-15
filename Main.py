'''
Universidad del Valle de Guatemala
Proyecto Final - Matemática Discreta
Sistema de encriptación RSA
 ---> Menú principal

Fabiola Contreras 22787
María José Villafuerte 22129
'''
import tkinter as tk # Libreria para creacion de interfaz grafica
import Calculos

def clear_frame():
    for widgets in Main_page.winfo_children():
      widgets.destroy()

def main():
    clear_frame()
    tk.Label(Main_page, text = "\nProyecto Final - Matemática Discreta", font="Times 10 italic").pack()
    tk.Label(Main_page, text = "Fabiola Contreras 22787\tMaría José Villafuerte 22129\n", font="Times 10 italic").pack()
    tk.Label(Main_page, text = "¿Qué deseas realizar?", font="Times 15 italic").pack()

    tk.Label(Main_page, text = "\t Encriptar mensaje", font="Times 15").place(x=5, y=130)
    tk.Button(text ="▷", command= encriptar).place(x=270, y=128)

    tk.Label(Main_page, text = "\t Desencriptar mensaje", font="Times 15").place(x=5, y=160)
    tk.Button(text ="▷", command = desencriptar).place(x=270, y=158)

def encriptar():
    clear_frame()
    tk.Label(Main_page, text = " \nEncriptar mensaje", font="Times 20").pack()

    tk.Label(Main_page, text = "Ingresa el mensaje a encriptar", font="Times 8").place(x=10, y=60)
    Mensaje = tk.StringVar()
    tk.Entry(textvariable=Mensaje).place(x=10,y=80)

    tk.Label(Main_page, text = "Ingresa el valor de p", font="Times 8").place(x=10, y=100)
    numP = tk.IntVar()
    tk.Entry(textvariable=numP).place(x=10,y=120)

    tk.Label(Main_page, text = "Ingresa el valor de q", font="Times 8").place(x=10, y=140)
    numQ = tk.IntVar()
    tk.Entry(textvariable=numQ).place(x=10,y=160)

    tk.Label(Main_page, text = "Ingresa el valor de e --> Recuerda que e>1", font="Times 8").place(x=10, y=180)
    numE = tk.IntVar()
    tk.Entry(textvariable=numE).place(x=10,y=200)

    def Call_calculation():
        mensajeObtenido = Calculos.encriptado(Mensaje.get(), numP.get(), numQ.get(), numE.get())
        show_Results(Mensaje.get(), mensajeObtenido, 0, 1)

    Boton_listo = tk.Button(text ="Listo", command= Call_calculation)
    Boton_listo.place(x=15, y=230)

    Boton_atras = tk.Button(text ="Regresar", command= main)
    Boton_atras.place(x=105, y=230)

def desencriptar():
    clear_frame()
    tk.Label(Main_page, text = " \nDesencriptar mensaje", font="Times 20").pack()

    tk.Label(Main_page, text = "Ingresa el código de mensaje a desencriptar", font="Times 8").place(x=10, y=60)
    Mensaje = tk.StringVar()
    tk.Entry(textvariable=Mensaje).place(x=10,y=80)

    tk.Label(Main_page, text = "Ingresa el valor de e (para la llave pública)", font="Times 8").place(x=10, y=100)
    numE = tk.IntVar()
    tk.Entry(textvariable=numE).place(x=10,y=120)

    tk.Label(Main_page, text = "Ingresa el valor de n (para la llave pública)", font="Times 8").place(x=10, y=140)
    numN = tk.IntVar()
    tk.Entry(textvariable=numN).place(x=10,y=160)

    def Call_calculation():
        mensajeObtenido, d = Calculos.desencriptado(Mensaje.get(), numE.get(), numN.get())
        show_Results(Mensaje.get(), mensajeObtenido, d, 2)

    Boton_listo = tk.Button(text ="Listo", command= Call_calculation)
    Boton_listo.place(x=15, y=190)

    Boton_atras = tk.Button(text ="Regresar", command= main)
    Boton_atras.place(x=105, y=190)

def show_Results(mensajeO, mensajeR, llave, modo):
    clear_frame()
    tk.Label(Main_page, text = " \nResultado del proceso:", font="Times 20").pack()
    tk.Label(Main_page, text = " \nMensaje original: " + mensajeO, font="Times 18").pack()
    tk.Label(Main_page, text = " \nMensaje obtenido: " + str(mensajeR), font="Times 18").pack()
    if modo == 2:
        tk.Label(Main_page, text = " \nLlave privada: " + str(llave), font="Times 15").pack()
    tk.Button(text ="Menu inicial", command= main).place(x=275, y=290)

Main_page = tk.Tk()
Main_page.geometry("550x450")
main()
Main_page.mainloop()