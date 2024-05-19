from tkinter import *
from datetime import *
from tkinter import messagebox

#Crear ventana

ventana=Tk()
ventana.title("Adivina tu año de nacimiento")
ventana.resizable(False,False)


# Etiqueta y campo de entrada para el nombre
Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = Entry(ventana)
entry_nombre.grid(row=1, column=0, padx=5, pady=5)

# Etiqueta y campo de entrada para la edad
Label(ventana, text="Edad:").grid(row=2, column=0, padx=5, pady=5)
entry_edad = Entry(ventana)
entry_edad.grid(row=3, column=0, padx=5, pady=5)

# Botón para calcular la edad
btn_calcular = Button(ventana, text="Calcular Edad",width=7,height=2, command=lambda:calcular_edad())
btn_calcular.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

btn_Limpiar=Button(ventana,text="Borrar",width=7,height=2,command=lambda:limpiar())
btn_Limpiar.grid(row=1,column=2,columnspan=2,padx=5,pady=5)

btn_Salir=Button(ventana,text="Salir",width=7,height=2,command=lambda:salir())
btn_Salir.grid(row=2,column=2,columnspan=2,padx=5,pady=5)



def calcular_edad():
    nombre=entry_nombre.get()

    #Se obtiene el año actual
    a_actual=datetime.now().year

    #Calcular el año de nacimiento

    try:
        edad=int(entry_edad.get())
        a_nacimiento=a_actual-edad

        # Determinar si es mayor o menor de edad
        if edad >= 18:
         messagebox.showinfo("Resultado", f"{nombre}, eres mayor de edad. Naciste en el año {a_nacimiento}.")
        else:
            messagebox.showinfo("Resultado", f"{nombre}, eres menor de edad. Naciste en el año {a_nacimiento}.")
    except ValueError:
            messagebox.showerror("Error", "Por favor, introduce una edad válida.")


def limpiar():
    entry_edad.delete(0,END)
    entry_nombre.delete(0,END)

def salir():
    ventana.destroy()    


ventana.mainloop()            
