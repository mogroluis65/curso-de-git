import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import bdfacturas2
import form_fact

class aplicacion:
    def __init__(self):
        self.root=tk.Tk()
        self.barramenu=tk.Menu(self.root)
        self.root.config(menu=self.barramenu,width=450,height=400)
#--------------------------barra de herramientas--------
        self.archivofactura=tk.Menu(self.barramenu,tearoff=0)
        self.archivoproducto=tk.Menu(self.barramenu,tearoff=0)
        self.archivocliente=tk.Menu(self.barramenu,tearoff=0)
        self.archivobbdd=tk.Menu(self.barramenu,tearoff=0)
        self.archivoayuda=tk.Menu(self.barramenu,tearoff=0)
    # ---------------------lista desplegable Producto--------------
        self.archivoproducto.add_command(label="Movimientos  ")#,command=nuevo_prod)
        self.barramenu.add_cascade(label="BBDD",menu=self.archivobbdd)
        self.barramenu.add_cascade(label="Factura",menu=self.archivofactura)
        self.barramenu.add_cascade(label="Producto",menu=self.archivoproducto)
        self.barramenu.add_cascade(label="Cliente",menu=self.archivocliente)
        self.barramenu.add_cascade(label="Ayuda",menu=self.archivoayuda)

        self.root.mainloop()
    def productos(self):
       pass 
class botones_aplicacion:
    def __init__(self,producto)
       self.producto=producto
            
aplicacion1=aplicacion() 
print    
