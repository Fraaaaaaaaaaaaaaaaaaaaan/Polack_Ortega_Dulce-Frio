from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox


#fondo guarda el color del fondo de la aplicacion
fondo="floral white"
ventana=Tk()
ventana.geometry("1000x1000")
ventana.iconbitmap("./imagenes/icon.ico")
ventana.title("Bienvenido a Dulce Frío")
ventana["background"]=fondo

#todas estas variables guardan la imagen especificada en file=
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
    #orden guarda el texto de ordenes para procesarlo
    orden=open("./directorio/ordenes.txt", 'a')
    #caja regis hace lo mismo pero con el texto cajas_regis
    caja_regis=open("./directorio/caja_regis.txt",'a')
    #todas estas variables guardan su valor convertido a str para poder escribirlo
    bochas=str(bochas)
    sabores=str(sabores)
    precio=str(precio)
    orden.write(f"Bochas:{bochas},Sabor(es):{sabores.strip(r"n\[']")},Precio:{precio}\n")
    caja_regis.write(f"{precio}\n")
    orden.close()
    caja_regis.close()

def bienvenido():
    limpiar_pantalla()
    
    #guarda el logo de dulce frio
    logo_label=Label(ventana,image=logo_img,bg=fondo)
    logo_label.pack(pady=10,padx=10)

    #guarda el logo en letras
    titulo=Label(ventana,image=letras_img,bg=fondo)
    titulo.pack(anchor="center")

    #guarda el subtitulo
    subtitulo=Label(ventana,text="“No se puede comprar la felicidad, pero se puede comprar helado”",font=("Courier New",20,"italic"),fg="deep pink",bg=fondo)
    subtitulo.pack(padx=20)

    #guarda el boton de inicie su pedido
    pedido=Button(ventana,text="Inicie su pedido!",command=pantalla_menu,font=("Comic Sans MS",15), bg="PaleVioletRed1")
    pedido.pack(pady=10,padx=10)

    #guarda el boton para el ingreso al portal
    empleados=Button(ventana,text="Portal de Empleados",command=entrada_portal,font=("Comic Sans MS",15), bg="aquamarine2")
    empleados.pack(pady=10,padx=10)

def pantalla_menu():
    limpiar_pantalla()
    #guarda el titulo
    titulo=Label(ventana,text="Nuestro Menu",font=("Comic Sans MS",30),fg="hot pink",bg=fondo,compound="left",image=tortita_img)
    titulo.pack()

    with open("./directorio/sabores.txt","r") as helados:
            #guarda el titulo de sabores del menu
            titulo1=Label(ventana,text="Nuestros Sabores",font=("Comic Sans MS",30),fg="hot pink",bg=fondo)
            titulo1.pack()
            for sabor in helados:
                #guarda los sabores
                saborsito=Label(ventana,text=f"★ {sabor}",font=("Courier New",15,"bold"),fg="midnight blue",bg=fondo)
                saborsito.pack(anchor="center")
    helados.close()

    with open("./directorio/precios.txt","r") as precios:
        #guarda el titulo de precios del menu
        titulo2=Label(ventana,text="Nuestros Precios",font=("Comic Sans MS",30),fg="hot pink",bg=fondo)
        titulo2.pack()
        for precio in precios:
                #guarda los precios
                precio=Label(ventana,text=f"★ {precio}",font=("Courier New",15,"bold"),fg="midnight blue",bg=fondo)
                precio.pack(anchor="center")
    precios.close()
    #guarda el boton para empezar a pedir
    continuar=Button(ventana,text="Empezar mi pedido",command=pantalla_pedido,font=("Comic Sans MS",15), bg="PaleVioletRed1")
    continuar.pack(side="right",pady=10,padx=10)
    #guarda el boton para ir atras
    volver=Button(ventana,text="Volver a la pantalla de inicio",command=bienvenido,font=("Comic Sans MS",15), bg="aquamarine2")
    volver.pack(side="left",pady=10,padx=10)


def pantalla_pedido():
    limpiar_pantalla()

    #guarda el titulo de la pagina
    titulo=Label(ventana,text="Haga su pedido",font=("Comic Sans MS",30),fg="deep pink",bg=fondo,compound="left",image=imagen_img)
    titulo.pack(pady=10,padx=10)

    #guarda el subtitulo/instrucciones
    subtitulo=Label(ventana,text="Elija primero el tipo de helado que lleva:",font=("Comic Sans MS",15,"italic"),fg="midnight blue",bg=fondo)
    subtitulo.pack()

    #guarda la variable que se fija si fue elegida la opcion de la bocha
    cantidad_var=IntVar()
    cantidad_var.set=0

    #todas estas variables guardan un boton para elegir el tipo de bocha
    una_bocha=Radiobutton(ventana,text="1 Bocha",variable=cantidad_var,value=1,bg="PaleVioletRed1",font=("Comic Sans MS",15,"bold"),fg="midnight blue")
    una_bocha.pack(pady=10,padx=10)
    
    dos_bocha=Radiobutton(ventana,text="2 Bochas",variable=cantidad_var,value=2,bg="aquamarine2",font=("Comic Sans MS",15,"bold"),fg="midnight blue")
    dos_bocha.pack(pady=10,padx=10)

    tres_bocha=Radiobutton(ventana,text="3 Bochas",variable=cantidad_var,value=3,bg="gold",font=("Comic Sans MS",15,"bold"),fg="midnight blue")
    tres_bocha.pack(pady=10,padx=10)

    #guarda mas instrucciones para el usuario
    subtitulo2=Label(ventana,text="¡Muy bien! ahora elije tus sabores:",font=("Comic Sans MS",15,"italic"),fg="midnight blue",bg=fondo)
    subtitulo2.pack()

    #esta lista guardara el valor 1 (se eligio el sabor) o el valor(no se eligio) 
    vars_si=[]
    #esta lista guardara los sabores sacados del archivo sabores.txt
    sabores=[]
    with open("./directorio/sabores.txt","r") as helados:
            for sabor in helados:
                sabores.append(sabor)
    for sabor in sabores:
            #guarda la variable que verifica si se hizo click sobre el boton
            var=IntVar()
            #guarda el boton con el sabor(son creados mediante la iteracion)
            boton=Checkbutton(ventana, text=sabor, variable=var,font=("Courier New",15),bg=fondo,fg="midnight blue")
            boton.pack(anchor="center")
            vars_si.append(var)
    helados.close()

    def continuar():
        #esta lista enumera vars_si(la lista de verificacion de sabores), se fija cuales son uno y recorre la lista de sabores para
        #relacionar la posicion de vars_si con las posiciones de sabores
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

    #guarda el boton para confirmar el pedido
    confirmar=Button(ventana, text="Confirmar pedido", command=continuar,bg="PaleVioletRed1",font=("Comic Sans MS",15))
    confirmar.pack(side="right")
    #guarda el boton para volver atras
    volver=Button(ventana,text="Atras",command=pantalla_menu,font=("Comic Sans MS",15), bg="aquamarine2")
    volver.pack(side="left")


def pantalla_resumen(cantidad, sabores_elegidos):
    limpiar_pantalla()

    #guarda el llamado a calcular_precio con cantidad
    total=calcular_precio(cantidad)

    #guarda el titulo de la pagina
    titulo=Label(ventana, text="Resumen del pedido", font=("Comic Sans MS", 30), fg="PaleVioletRed1",bg=fondo,compound="right",image=resumen_img)
    titulo.pack(pady=10)

    #guarda el texto para mostrar las bochas
    bochas=Label(ventana, text=f"Bochas: {cantidad}",fg="DeepPink2",bg=fondo,font=("Comic Sans MS",15))
    bochas.pack(pady=10,padx=10)

    #guarda el titulo de mostrar los sabores
    sabores=Label(ventana, text="Sabores:",font=("Comic Sans MS",15),fg="maroon1",bg=fondo)
    sabores.pack(pady=10,padx=10)
    for s in sabores_elegidos:
        #guarda el texto para mostrar los sabores elegidos 
        sabor=Label(ventana, text=f"★ {s}",font=("Comic Sans MS",15,"bold"),fg="midnight blue",bg=fondo)
        sabor.pack(pady=10,padx=10)
    #guarda el texto de total a pagar
    total=Label(ventana,text=f"\nTotal a pagar: ${total}",fg="lime green",bg=fondo,font=("Comic Sans MS",20))
    total.pack(pady=10)

    def confirmar():
        pantalla_final()

    #crea un frame 
    frame=Frame(ventana)
    frame.pack(pady=10)

    #guarda el boton de vuelta
    atras=Button(frame,text="Atrás",command=pantalla_pedido,bg="aquamarine2",fg="midnight blue",font=("Comic Sans MS",15,"bold"))
    atras.pack(side="left",pady=10,padx=10)

    #guarda el boton de confirmar pedido
    confirmar=Button(frame,text="Confirmar pedido",command=confirmar,bg="PaleVioletRed1",fg="midnight blue",font=("Comic Sans MS",15,"bold"))
    confirmar.pack(side="left",pady=10,padx=10)

def pantalla_final():
    limpiar_pantalla()

    #guarda la imagen de despedida
    chau=Label(ventana,image=chau_img,bg=fondo)
    chau.pack()

    #guarda la despedida
    titulo=Label(ventana, text="¡Gracias por elegir Dulce Frio!", bg=fondo,fg="PaleVioletRed1", font=("Comic Sans MS", 30))
    titulo.pack(pady=10)
    #guarda el boton para volver al inicio
    volver=Button(ventana, text="Volver al inicio", command=bienvenido,bg="aquamarine2",font=("Comic Sans MS",15))
    volver.pack()

def entrada_portal():
     limpiar_pantalla()
     #lista que guardara las listas sacadas del archivo de texto contras.txt
     contras_lista=[]

     def abrir_contra():
          with open("./directorio/contras.txt","r") as contras:
               for c in contras:
                    contras_lista.append(c)
          contras.close()

     def confirmar():
        abrir_contra()
        #guarda el valor de contra 
        contrasenia=contra.get()
        if contrasenia in contras_lista:
            #guarda el titulo si el id es valido
            titulo=Label(ventana,text="ID Valido",font=("Comic Sans MS",30),fg="hot pink",bg=fondo)
            titulo.pack(pady=10)
            #guarda el boton para ingresar al portal
            entrar=Button(ventana,text="Ingresar al Portal",command=portal_empresa,bg="gold",font=("Comic Sans MS",15))
            entrar.pack()
        else:
             #guarda el titulo si el id no es valido
             id_no=Label(ventana,text="ID no valido",image=no_img,compound="left",font=("Comic Sans MS",30),fg="hot pink",bg=fondo)
             id_no.pack(pady=10)
    #guarda el texto de titulo de la pagina
     bienvenida=Label(ventana,text="Ingreso al Portal",image=pedido_img,compound="left",bg=fondo,font=("Comic Sans MS",30),fg="hot pink")
     bienvenida.pack()
     #guarda las indicaciones para la contraseña
     contras_texto=Label(ventana, text="Ingrese su ID:",font=("Courier New",15),fg="midnight blue",bg=fondo)
     contras_texto.pack()
     #guarda la contraseña ingresada por el usuario
     contra=Entry(ventana, show="*")
     contra.pack()
     #guarda el boton para ingresar la contraseña al sistema
     entrar=Button(ventana,text="Ingresar",font=("Comic Sans MS",15),bg="hot pink",command=confirmar)
     entrar.pack()
    #guarda el boton de atras
     atras=Button(ventana,text="Atrás",command=bienvenido,bg="aquamarine2",font=("Comic Sans MS",15,))
     atras.pack(pady=10,padx=10)

def portal_empresa():
    limpiar_pantalla()
    #guarda el icono del portal
    imagen=Label(ventana,image=feliz_img,bg=fondo)
    imagen.pack(anchor="center")
    #guarda el titulo de la pagina
    titulo=Label(ventana,text="Bienvenido al Portal",font=("Comic Sans MS",30),fg="hot pink",bg=fondo)
    titulo.pack()
    #guarda las instrucciones
    subtitulo=Label(ventana,text="Aprete el botón de la acción que desea realizar",font=("Comic Sans MS",15),fg="midnight blue",bg=fondo)
    subtitulo.pack()

    #guarda el boton para entrar al historial de pedidos
    pedidos=Button(ventana,text="Historial de Pedidos",command=pedidos_pag,font=("Comic Sans MS",15),bg="PaleVioletRed1")
    pedidos.pack()

    #guarda el boton para entrar a la caja registradora 
    caja=Button(ventana,text="Caja Registradora Digital",command=caja_regis_pag,font=("Comic Sans MS",15),bg="aquamarine2")
    caja.pack(pady=10,padx=10)

    #guarda el boton para volver a la pagina de entrada al portal
    atras=Button(ventana,text="Atrás",command=entrada_portal,bg="gold",font=("Comic Sans MS",15,))
    atras.pack(pady=10,padx=10)

def pedidos_pag():
     limpiar_pantalla()
     #guarda el titulo de la página
     titulo=Label(ventana,text="Historial de Pedidos",image=pedidos_hist_img,compound="left",fg="hot pink",bg=fondo,font=("Comic Sans MS",30))
     titulo.pack(pady=10,padx=10)
     contador=1
     with open("./directorio/ordenes.txt","r") as ordenes:
            for orden in ordenes:
               #guarda la variable orden convertida a str
               orden=str(orden)
               orden.strip(r"n\[']")
               imprimir_orden=Label(ventana,text=f"ORDEN {contador}:{orden}",font=("Comic Sans Ms",15),fg="midnight blue",bg="Ivory2")
               imprimir_orden.pack()
               contador+=1
     #guarda el boton para ir atras
     atras=Button(ventana,text="Atrás",command=portal_empresa,bg="aquamarine2",font=("Comic Sans MS",15,))
     atras.pack(pady=30,padx=30)

    
          
def caja_regis_pag():
     limpiar_pantalla()
     #guarda el ingreso total de todos los pedidos
     totalito=0
     #guarda el titulo de la pagina
     titulo=Label(ventana,text="Caja Registradora Digital",image=caja_img,compound="left",fg="hot pink",bg=fondo,font=("Comic Sans MS",30))
     titulo.pack(pady=10,padx=10)
     with open("./directorio/caja_regis.txt","r") as caja:
          for billete in caja:
            if billete=="\n":
               #guarda el titulo si no hay billetes registrados
               no_ventas=Label(ventana,text="Hoy no hubo ventas :(",font=("Comic Sans Ms",30),fg="red",bg="Ivory2")
               no_ventas.pack()
            else:
               #convierte a billete a int para sumarlo
               billete=int(billete)
               #suma todos los billetes que haya a totalito
               totalito=totalito+billete
               #titulo de ingresos
               ingresos_titulo=Label(ventana,text="Ingresos:",font=("Comic Sans Ms",15),fg="midnight blue",bg=fondo)
               ingresos_titulo.pack()
               #guarda el texto pra mostrar el ingreso
               ingresos=Label(ventana,text=f"${billete}",font=("Comic Sans Ms",10),fg="lime green",bg="Ivory2")
               ingresos.pack()
     caja.close()

    #titulo del total de hoy
     imprimir_total_titulo=Label(ventana,text="Total de hoy:",font=("Comic Sans Ms",20),fg="midnight blue",bg=fondo,image=billete_img,compound="left")
     imprimir_total_titulo.pack()
     #muestra el total de hoy
     total=Label(ventana,text=f"${totalito}",font=("Comic Sans Ms",15),fg="lime green",bg="Ivory2")
     total.pack()
    #guarda el boton para volver atras a la pagina del portal 
     atras=Button(ventana,text="Atrás",command=portal_empresa,bg="aquamarine2",font=("Comic Sans MS",15,))
     atras.pack(pady=30,padx=30)
        

bienvenido()
ventana.mainloop()
