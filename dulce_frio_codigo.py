from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
#frans notes

#add all the variables values in comments


fondo="floral white"
ventana=Tk()
ventana.geometry("1000x1000")
ventana.iconbitmap("./imagenes/icon.ico")
ventana.title("Bienvenido a Dulce Frío")
ventana["background"]=fondo

logo_img=PhotoImage(file="./imagenes/logo_letras.png")
pedido_img=PhotoImage(file="./imagenes/otratorta.png")
letras_img=PhotoImage(file="./imagenes/letras.png")
chau_img=PhotoImage(file="./imagenes/chau.png")
resumen_img=PhotoImage(file="./imagenes/resumen.png")
imagen_img=PhotoImage(file="./imagenes/imagen.png")
tortita_img=PhotoImage(file="./imagenes/cake.png")
feliz_img=PhotoImage(file="./imagenes/feliz.png")
pedidos_hist_img=PhotoImage(file="./imagenes/pedido.png")
caja_img=PhotoImage(file="./imagenes/caja.png")
billete_img=PhotoImage(file="./imagenes/billete.png")
no_img=PhotoImage(file="./imagenes/no.png")


def limpiar_pantalla():
    for widget in ventana.winfo_children():
        widget.destroy()

def calcular_precio(cantidad):
    if cantidad == 1:
        return 700
    elif cantidad == 2:
        return 1200
    elif cantidad == 3:
        return 1600
    else:
        return 0
    
def escribir_orden(bochas,sabores,precio):
    orden=open("./directorio/ordenes.txt", 'a')
    caja_regis=open("./directorio/caja_regis.txt",'a')
    bochas=str(bochas)
    sabores=str(sabores)
    precio=str(precio)
    orden.write(f"Bochas:{bochas},Sabor(es):{sabores.strip(r"n\[']")},Precio:{precio}\n")
    caja_regis.write(f"{precio}\n")
    orden.close()
    caja_regis.close()

def bienvenido():
    limpiar_pantalla()
    
    logo_label=Label(ventana,image=logo_img,bg=fondo)
    logo_label.pack(pady=10,padx=10)

    titulo1=Label(ventana,image=letras_img,bg=fondo)
    titulo1.pack(anchor="center")

    subtitulo=Label(ventana,text="“No se puede comprar la felicidad, pero se puede comprar helado”",font=("Courier New",20,"italic"),fg="deep pink",bg=fondo)
    subtitulo.pack(padx=20)

    pedido=Button(ventana,text="Inicie su pedido!",command=pantalla_menu,font=("Comic Sans MS",15), bg="PaleVioletRed1")
    pedido.pack(pady=10,padx=10)

    empleados=Button(ventana,text="Portal de Empleados",command=entrada_portal,font=("Comic Sans MS",15), bg="aquamarine2")
    empleados.pack(pady=10,padx=10)

def pantalla_menu():
    limpiar_pantalla()
    titulo=Label(ventana,text="Nuestro Menu",font=("Comic Sans MS",30),fg="hot pink",bg=fondo,compound="left",image=tortita_img)
    titulo.pack()

    with open("./directorio/sabores.txt","r") as helados:
            titulo1=Label(ventana,text="Nuestros Sabores",font=("Comic Sans MS",30),fg="hot pink",bg=fondo)
            titulo1.pack()
            for sabor in helados:
                saborsito=Label(ventana,text=f"★ {sabor}",font=("Courier New",15,"bold"),fg="midnight blue",bg=fondo)
                saborsito.pack(anchor="center")
    helados.close()

    with open("./directorio/precios.txt","r") as precios:
        titulo2=Label(ventana,text="Nuestros Precios",font=("Comic Sans MS",30),fg="hot pink",bg=fondo)
        titulo2.pack()
        for precio in precios:
                precio=Label(ventana,text=f"★ {precio}",font=("Courier New",15,"bold"),fg="midnight blue",bg=fondo)
                precio.pack(anchor="center")
    precios.close()
    continuar=Button(ventana,text="Empezar mi pedido",command=pantalla_pedido,font=("Comic Sans MS",15), bg="PaleVioletRed1")
    continuar.pack(side="right",pady=10,padx=10)
    volver=Button(ventana,text="Volver a la pantalla de inicio",command=bienvenido,font=("Comic Sans MS",15), bg="aquamarine2")
    volver.pack(side="left",pady=10,padx=10)


def pantalla_pedido():
    limpiar_pantalla()

    titulo=Label(ventana,text="Haga su pedido",font=("Comic Sans MS",30),fg="deep pink",bg=fondo,compound="left",image=imagen_img)
    titulo.pack(pady=10,padx=10)

    subtitulo=Label(ventana,text="Elija primero el tipo de helado que lleva:",font=("Comic Sans MS",15,"italic"),fg="midnight blue",bg=fondo)
    subtitulo.pack()

    cantidad_var=IntVar()
    cantidad_var.set=0

    una_bocha=Radiobutton(ventana,text="1 Bocha",variable=cantidad_var,value=1,bg="PaleVioletRed1",font=("Comic Sans MS",15,"bold"),fg="midnight blue")
    una_bocha.pack(pady=10,padx=10)
    
    dos_bocha=Radiobutton(ventana,text="2 Bochas",variable=cantidad_var,value=2,bg="aquamarine2",font=("Comic Sans MS",15,"bold"),fg="midnight blue")
    dos_bocha.pack(pady=10,padx=10)

    tres_bocha=Radiobutton(ventana,text="3 Bochas",variable=cantidad_var,value=3,bg="gold",font=("Comic Sans MS",15,"bold"),fg="midnight blue")
    tres_bocha.pack(pady=10,padx=10)

    subtitulo2=Label(ventana,text="¡Muy bien! ahora elije tus sabores:",font=("Comic Sans MS",15,"italic"),fg="midnight blue",bg=fondo)
    subtitulo2.pack()

    vars_si=[]
    sabores=[]
    with open("./directorio/sabores.txt","r") as helados:
            for sabor in helados:
                sabores.append(sabor)
    for sabor in sabores:
            var=IntVar()
            boton=Checkbutton(ventana, text=sabor, variable=var,font=("Courier New",15),bg=fondo,fg="midnight blue")
            boton.pack(anchor="center")
            vars_si.append(var)
    helados.close()

    def continuar():
        seleccionados=[sabores[i] for i, v in enumerate(vars_si) if v.get() == 1]

        if len(seleccionados) == 0:
            messagebox.showwarning("Uy!","Seleccione un sabor para continuar")
            return
        
        if len(seleccionados)>cantidad_var.get():
             messagebox.showwarning("Uy!",f"El limite de sabores para su pedido es de {cantidad_var.get()}")
             return
                  
        pantalla_resumen(cantidad_var.get(), seleccionados)
        total=calcular_precio(cantidad_var.get())
        escribir_orden(cantidad_var.get(),seleccionados,total)


    confirmar=Button(ventana, text="Confirmar pedido", command=continuar,bg="PaleVioletRed1",font=("Comic Sans MS",15))
    confirmar.pack(side="right")
    volver=Button(ventana,text="Atras",command=pantalla_menu,font=("Comic Sans MS",15), bg="aquamarine2")
    volver.pack(side="left")


def pantalla_resumen(cantidad, sabores_elegidos):
    limpiar_pantalla()

    total=calcular_precio(cantidad)

    titulo=Label(ventana, text="Resumen del pedido", font=("Comic Sans MS", 30), fg="PaleVioletRed1",bg=fondo,compound="right",image=resumen_img)
    titulo.pack(pady=10)

    bochas=Label(ventana, text=f"Bochas: {cantidad}",fg="DeepPink2",bg=fondo,font=("Comic Sans MS",15))
    bochas.pack(pady=10,padx=10)

    sabores=Label(ventana, text="Sabores:",font=("Comic Sans MS",15),fg="maroon1",bg=fondo)
    sabores.pack(pady=10,padx=10)
    for s in sabores_elegidos:
        sabor=Label(ventana, text=f"★ {s}",font=("Comic Sans MS",15,"bold"),fg="midnight blue",bg=fondo)
        sabor.pack(pady=10,padx=10)

    total=Label(ventana,text=f"\nTotal a pagar: ${total}",fg="lime green",bg=fondo,font=("Comic Sans MS",20))
    total.pack(pady=10)

    def confirmar():
        pantalla_final()

    frame=Frame(ventana)
    frame.pack(pady=10)

    atras=Button(frame,text="Atrás",command=pantalla_pedido,bg="aquamarine2",fg="midnight blue",font=("Comic Sans MS",15,"bold"))
    atras.pack(side="left",pady=10,padx=10)

    confirmar=Button(frame,text="Confirmar pedido",command=confirmar,bg="PaleVioletRed1",fg="midnight blue",font=("Comic Sans MS",15,"bold"))
    confirmar.pack(side="left",pady=10,padx=10)

def pantalla_final():
    limpiar_pantalla()

    chau=Label(ventana,image=chau_img,bg=fondo)
    chau.pack()

    titulo=Label(ventana, text="¡Gracias por elegir Dulce Frio!", bg=fondo,fg="PaleVioletRed1", font=("Comic Sans MS", 30))
    titulo.pack(pady=10)
    volver=Button(ventana, text="Volver al inicio", command=bienvenido,bg="aquamarine2",font=("Comic Sans MS",15))
    volver.pack()

def entrada_portal():
     limpiar_pantalla()
     contras_lista=[]

     def abrir_contra():
          with open("./directorio/contras.txt","r") as contras:
               for c in contras:
                    contras_lista.append(c)
          contras.close()

     def confirmar():
        abrir_contra()
        contrasenia=contra.get()
        if contrasenia in contras_lista:
            limpiar_pantalla()
            titulo=Label(ventana,text="ID Valido",font=("Comic Sans MS",30),fg="hot pink",bg=fondo)
            titulo.pack(pady=10)
            entrar=Button(ventana,text="Ingresar al Portal",command=portal_empresa,bg="gold",font=("Comic Sans MS",15))
            entrar.pack()
        else:
             id_no=Label(ventana,text="ID no valido",image=no_img,compound="left",font=("Comic Sans MS",30),fg="hot pink",bg=fondo)
             id_no.pack(pady=10)

     bienvenida=Label(ventana,text="Ingreso al Portal",image=pedido_img,compound="left",bg=fondo,font=("Comic Sans MS",30),fg="hot pink")
     bienvenida.pack()

     contras_texto=Label(ventana, text="Ingrese su ID:",font=("Courier New",15),fg="midnight blue",bg=fondo)
     contras_texto.pack()
     contra=Entry(ventana, show="*")
     contra.pack()
     entrar=Button(ventana,text="Ingresar",font=("Comic Sans MS",15),bg="hot pink",command=confirmar)
     entrar.pack()

     atras=Button(ventana,text="Atrás",command=bienvenido,bg="aquamarine2",font=("Comic Sans MS",15,))
     atras.pack(pady=10,padx=10)

def portal_empresa():
    limpiar_pantalla()
    imagen=Label(ventana,image=feliz_img,bg=fondo)
    imagen.pack(anchor="center")
    titulo=Label(ventana,text="Bienvenido al Portal",font=("Comic Sans MS",30),fg="hot pink",bg=fondo)
    titulo.pack()

    subtitulo=Label(ventana,text="Aprete el botón de la acción que desea realizar",font=("Comic Sans MS",15),fg="midnight blue",bg=fondo)
    subtitulo.pack()

    pedidos=Button(ventana,text="Historial de Pedidos",command=pedidos_pag,font=("Comic Sans MS",15),bg="PaleVioletRed1")
    pedidos.pack()

    caja=Button(ventana,text="Caja Registradora Digital",command=caja_regis_pag,font=("Comic Sans MS",15),bg="aquamarine2")
    caja.pack(pady=10,padx=10)

    atras=Button(ventana,text="Atrás",command=entrada_portal,bg="gold",font=("Comic Sans MS",15,))
    atras.pack(pady=10,padx=10)

def pedidos_pag():
     limpiar_pantalla()
     titulo=Label(ventana,text="Historial de Pedidos",image=pedidos_hist_img,compound="left",fg="hot pink",bg=fondo,font=("Comic Sans MS",30))
     titulo.pack(pady=10,padx=10)
     contador=1
     with open("./directorio/ordenes.txt","r") as ordenes:
            for orden in ordenes:
               orden=str(orden)
               orden.strip(r"n\[']")
               imprimir_orden=Label(ventana,text=f"ORDEN {contador}:{orden}",font=("Comic Sans Ms",15),fg="midnight blue",bg="Ivory2")
               imprimir_orden.pack()
               contador+=1

     atras=Button(ventana,text="Atrás",command=portal_empresa,bg="aquamarine2",font=("Comic Sans MS",15,))
     atras.pack(pady=30,padx=30)

    
          
def caja_regis_pag():
     limpiar_pantalla()
     totalito=0
     titulo=Label(ventana,text="Caja Registradora Digital",image=caja_img,compound="left",fg="hot pink",bg=fondo,font=("Comic Sans MS",30))
     titulo.pack(pady=10,padx=10)
     with open("./directorio/caja_regis.txt","r") as caja:
          for billete in caja:
            print(billete)
            if billete=="\n":
               no_ventas=Label(ventana,text="Hoy no hubo ventas :(",font=("Comic Sans Ms",30),fg="red",bg="Ivory2")
               no_ventas.pack()
            else:
               billete=int(billete)
               totalito=totalito+billete
               ingresos_titulo=Label(ventana,text="Ingresos:",font=("Comic Sans Ms",15),fg="midnight blue",bg=fondo)
               ingresos_titulo.pack()
               ingresos=Label(ventana,text=f"${billete}",font=("Comic Sans Ms",10),fg="lime green",bg="Ivory2")
               ingresos.pack()
     caja.close()

     imprimir_total_titulo=Label(ventana,text="Total de hoy:",font=("Comic Sans Ms",20),fg="midnight blue",bg=fondo,image=billete_img,compound="left")
     imprimir_total_titulo.pack()
     total=Label(ventana,text=f"${totalito}",font=("Comic Sans Ms",15),fg="lime green",bg="Ivory2")
     total.pack()

     atras=Button(ventana,text="Atrás",command=portal_empresa,bg="aquamarine2",font=("Comic Sans MS",15,))
     atras.pack(pady=30,padx=30)
        

bienvenido()
ventana.mainloop()