from tkinter import *
import tkinter.messagebox
import matplotlib.pyplot as plt
import numpy as np

#Main window config
root=Tk()
root.geometry("400x525")
labelmain=root.title("Calculadora de Pensiones para Nicaragua")
img = tkinter.PhotoImage(file = r'C:\\\nic.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.resizable(width=False, height=False)

#Mensaje inicial
labelmen=Label(root,text="Este ejercicio usa las reglas vigentes de la seguridad social \n para darle un estimado de su futura pensión mensual.\nSe sugiere que el usuario lea el tutorial referido en el menú de ayuda\npara insertar correctamente los parámetros solicitados.", justify=LEFT, relief=RIDGE, fg="blue")
labelmen.grid(row=0, column=0, columnspan=2, sticky=W,pady=(5,5),padx=(5,0))

#Menus
def Acerca():
    tkinter.messagebox.showinfo("Acerca","Esta Calculadora fue diseñada para fines académicos.\n\nCopyright © Alvaro Altamirano Montoya, 2018.\n\nComentarios/sugerencias: ajaltamiranomontoya@gmail.com")

def Acerca2():
    tkinter.messagebox.showinfo("Tutorial","En el siguiente site puede encontrar la información\nnecesaria para introducir correctamente los parámetros solicitados:\n\nhttps://alvaroaltamirano.wordpress.com/")

menu=Menu(root)
root.config(menu=menu)
submenu=Menu(menu)
menu.add_cascade(label="Archivo", menu=submenu)
submenu.add_command(label="Salir", command=root.destroy)
submenu.add_separator()
editmenu=Menu(menu)
menu.add_cascade(label="Ayuda", menu=editmenu)
editmenu.add_command(label="Acerca",command=Acerca)
editmenu.add_command(label="Tutorial", command=Acerca2)

#Entries
labeledad=Label(root,text="Ingrese su edad actual (p. ej. 45):", justify=LEFT)
entryedad=Entry(root)
labeledad.grid(row=1, sticky=W,pady=(5,5),padx=(5,5))
entryedad.grid(row=1, column=1)

labelw=Label(root,text="Ingrese su salario actual (p. ej. C$15000):", justify=LEFT)
entryw=Entry(root)
labelw.grid(row=2, sticky=W,pady=(0,5),padx=(5,5))
entryw.grid(row=2, column=1)

labelc=Label(root,text="Total de años que espera cotizar \ndurante su vida laboral (p. ej. 15):", anchor="nw", justify=LEFT)
entryc=Entry(root)
labelc.grid(row=3, sticky=W+S,pady=(0,5),padx=(5,5))
entryc.grid(row=3, column=1)

labelmw=Label(root,text="Salario mínimo legal (manufactura)\n(p. ej. C$5074 en 2017):", anchor="nw", justify=LEFT)
entrymw=Entry(root)
labelmw.grid(row=4, sticky=W+S,pady=(0,5),padx=(5,5))
entrymw.grid(row=4, column=1)

labelcs=Label(root,text="Crecimiento salarial anual esperado\n(p. ej. 0.02=2% cada año):", anchor="nw", justify=LEFT)
entrycs=Entry(root)
labelcs.grid(row=5, sticky=W+S,pady=(0,5),padx=(5,5))
entrycs.grid(row=5, column=1)

labelcambio=Label(root,text="Tipo de cambio actual (C$ x US$):", anchor="nw", justify=LEFT)
entrycambio=Entry(root)
labelcambio.grid(row=6, sticky=W+S,pady=(0,5),padx=(5,5))
entrycambio.grid(row=6, column=1)

labeltc=Label(root,text="Supuesto de devaluación cambiaria\n(Obs. 5% anual desde 2004):", anchor="nw", justify=LEFT)
entrytc=Entry(root)
labeltc.grid(row=7, sticky=W+S,pady=(0,10),padx=(5,5))
entrytc.grid(row=7, column=1)

#####################################
#############Calculadora#############
    #2.Ecuaciones
def printpension(event):
    edad=int(str(entryedad.get()))
    crectc=float(str(entrytc.get()))
    cambio1=float((entrycambio.get()))
    cambio=(cambio1*(1+crectc)**((60-edad)-1))
    maxima=cambio*1500
    cotizados=int(str(entryc.get()))
    crecsal=float(str(entrycs.get()))
    wmin=int(str(entrymw.get()))
    if (cotizados*50)>1000 and (cotizados*50)<1250:
        anosbase=4
    elif (cotizados*50)>=1250:
            anosbase=3
    else:
                anosbase=5
    #Proyecciones
    reduc1=(1910*((1+crecsal)**((60-edad)-1)))
    reduc2=(2356*((1+crecsal)**((60-edad)-1)))
    reduc3=(2884*((1+crecsal)**((60-edad)-1)))
    reduc4=(3290*((1+crecsal)**((60-edad)-1)))
    reduc5=(3656*((1+crecsal)**((60-edad)-1)))
    
    salarioreferencia1=(int(entryw.get())*(1+crecsal)**((60-edad)-1))
    salarioreferencia=(salarioreferencia1*(1+(1+crecsal)**(-anosbase+1))/2)
    wmin=(wmin*(1+crecsal)**((60-edad)-1))
    if salarioreferencia>=(wmin*2) and (0.37+((0.0115)*(int(entryc.get())-150/50)))<.8:
        pension=salarioreferencia*(0.37+((0.0115)*(int(entryc.get())-150/50)))    
    elif salarioreferencia>=(wmin*2) and (0.37+((0.0115)*(int(entryc.get())-150/50)))>=.8:
            pension=salarioreferencia*.8

    if salarioreferencia<(wmin*2) and (0.45+((0.01591)*(int(entryc.get())-150/50)))<1:
        pension=salarioreferencia*(0.45+((0.01591)*(int(entryc.get())-150/50)))    
    elif salarioreferencia<(wmin*2) and (0.45+((0.01591)*(int(entryc.get())-150/50)))>=1:
            pension=salarioreferencia

    if pension>maxima:
        pension=maxima

    if (cotizados*52)>=250 and (cotizados*52)<=349:
	    pension=reduc1
    if (cotizados*52)>=350 and (cotizados*52)<=449:
	    pension=reduc2
    if (cotizados*52)>=450 and (cotizados*52)<=549:
	    pension=reduc3
    if (cotizados*52)>=550 and (cotizados*52)<=649:
	    pension=reduc4
    if (cotizados*52)>=650 and (cotizados*52)<=749:
	    pension=reduc5

    TdR=(pension/salarioreferencia)*100
    dollar=(pension/cambio)
    
    output.insert(END, "Su pensión estimada es de C$""{:0,.0f}".format(pension)+", equivalente a {:0,.1f}% de su último salario.".format(TdR)+" En US$: {:0,.0f}.".format(dollar))

    objects = ('Pensión mínima \n(pensión reducida con \nmínimo de 5 años)', 'Su pensión', 'Pensión máxima del sistema\nUS$ 1,500')
    y_pos = np.arange(len(objects))
    performance = [int(reduc1),int(pension),int(maxima)]
    colors = ['g', 'b', 'k']
    plt.bar(y_pos, performance, align='center', alpha=0.8, color=colors)
    plt.xticks(y_pos, objects)
    plt.ylabel('Nivel de la pension')
    plt.title('Rangos del beneficio pensional')
    plt.show()
           
#Botón de calculo
button=Button(root,text="Calcular",bg="white", fg="blue")
button.bind("<Button-1>",printpension)
button.grid(row=8,column=0,pady=(5,0),ipady=3)
button.config( height =1, width =7)

#Text output box
labelresultado=Label(root,text="Resultado:", anchor="nw", justify=LEFT)
labelresultado.grid(row=8, sticky=W+N,pady=(0,5),padx=(5,5))
output=Text(root, width=15, height=8, wrap=WORD, background='light gray')
output.grid(row=8, column=1, sticky=W+E)

def clear(event):
    output.delete(1.0,END)

clearbutton=Button(root, text="Borrar resultado",bg="White", fg="black", command=print(""))
clearbutton.grid(row=9, column=1,pady=(5,5),ipady=3)
clearbutton.bind("<Button-1>",clear)

#Quit button
quitbutton=Button(root, text="Cerrar",bg="White", fg="black", command=root.destroy)
quitbutton.grid(row=9, column=0,pady=(5,5),ipady=3)
quitbutton.config( height =1, width =7)

root.mainloop()
