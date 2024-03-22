import tkinter as tk
from tkinter import ttk


class janela(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x500')
        self.title("Cadastro")

        texto3=ttk.Entry(text="Nome completo:",font="Arial,14")
        texto3.pack(padx=20,pady=20)

        ttk.Button(self,
                text="Sair",
                command=self.destroy).pack(expand=True)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('600x200')
        self.title('Inicio')

        self.texto1=ttk.Label(text="Olá, seja bem vindo(a)",font="Negrito,14").pack(padx=10,pady=20)
        self.texto2=ttk.Label(text="Vamos precisar de algumas informações suas para continuar cadastro:",font="Arial,14").pack(padx=10,pady=20)

        ttk.Button(self,
                text="Confimar",
                command=self.open_window).pack(expand=True)
        
    def open_window(self):
        window = janela(self)
        window.grab_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()