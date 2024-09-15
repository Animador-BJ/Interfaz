import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk  # Asegúrate de importar esto
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img

class FormularioMaestroDesign(tk.Tk):

    def __init__(self):
        super().__init__()
        self.logo = ImageTk.PhotoImage(Image.open("D:/USUARIO/Music/python/Modern GUI/imagenes/Logo.png"))
        self.perfil = ImageTk.PhotoImage(Image.open("D:/USUARIO/Music/python/Modern GUI/imagenes/Perfil.png"))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()
    
    def config_window(self):
        self.title('Eye System')
        self.iconbitmap("D:/USUARIO/Music/python/Modern GUI/imagenes/Logo.ico")
        w, h = 1800, 900       
        util_ventana.centrar_ventana(self, w, h)        

    def paneles(self):        
        self.barra_superior = tk.Frame(
        self, bg=COLOR_BARRA_SUPERIOR, width=250)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=500)
        self.menu_lateral.pack(side=tk.LEFT, fill='both') 
        
        self.cuerpo_principal = tk.Frame(
            self, bg=COLOR_CUERPO_PRINCIPAL, width=150)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="Eye System")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)
    
    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
         
         # Etiqueta de perfil
        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        # Botones del menú lateral
        
        self.buttonIniciarSecion = tk.Button(self.menu_lateral)        
        self.buttonCrearCuenta = tk.Button(self.menu_lateral)        
        self.buttonTomarDatos = tk.Button(self.menu_lateral)
        self.buttonDashBoard = tk.Button(self.menu_lateral)        
        self.buttonSalir= tk.Button(self.menu_lateral)

        buttons_info = [
            ("Iniciar Secion", "\uf109", self.buttonIniciarSecion),
            ("Crear Cuenta", "\uf007", self.buttonCrearCuenta),
            ("Tomar Datos", "\uf03e", self.buttonTomarDatos),
            ("Panel De Datos", "\uf129", self.buttonDashBoard),
            ("Salir", "\uf013", self.buttonSalir)
        ]

        for text, icon, button in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu)                    
    
    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        label = tk.Label(self.cuerpo_principal, image=self.logo,
                         bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')