import customtkinter as ctk
from utils import *
from PIL import Image

acesso = False

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Janela Principal:
tela_login = ctk.CTk()

tela_login.title('LoveBET: Faça seu Login/Cadastro')
tela_login.geometry('700x400')

# Labels 1
wp = ctk.CTkImage(dark_image=Image.open('wallpaper-login_screen.jpg'), size=(1366, 768))
fundo = ctk.CTkLabel(master=tela_login, image=wp)
fundo.pack()

# Fontes
fonte1 = ctk.CTkFont(family='Century Gothic', size=25, weight="bold", slant="italic", underline=False)
fonte2 = ctk.CTkFont(family='Century Gothic', size=16, weight="normal", slant="italic", underline=False)

# Frame base
frame_base = ctk.CTkFrame(master=tela_login, width=250, height=330, fg_color='#700a36',
                          border_width=2, border_color='black')
frame_base.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Frame 3 - Opções

frame3 = ctk.CTkFrame(master=tela_login, width=70, height=200, fg_color='#313136',
                      border_width=2, border_color='black')
frame3.place(relx=0.269, rely=0.337, anchor=ctk.CENTER)


def botao_login():
    limpar(frame_base)
    # Frame_LOG 2 - Caixa de Dialogo
    frame2 = ctk.CTkFrame(master=frame_base, width=200, height=50, fg_color='#181a1c',
                          border_width=2, border_color='black')

    frame2.place(relx=0.5, rely=0.66, anchor=ctk.CENTER)

    # Labels - Frame Log
    label2 = ctk.CTkLabel(master=frame_base, text='Entre em sua conta:', font=fonte1)
    label2.place(x=5, y=5)

    label3 = ctk.CTkLabel(master=frame_base, text='Login:', font=fonte2)
    label3.place(x=10, y=55)

    label4 = ctk.CTkLabel(master=frame_base, text='Senha:', font=fonte2)
    label4.place(x=5, y=95)

    label5 = ctk.CTkLabel(master=frame2, text='', font=fonte2, text_color='white')
    label5.place(x=5, y=5)

    # Entrada de Dados - Login:
    login = ctk.CTkEntry(frame_base, placeholder_text='Coloque seu email!', height=2,
                         border_width=2, border_color='black', corner_radius=5)
    login.place(x=66, y=60)

    senha = ctk.CTkEntry(frame_base, placeholder_text='Coloque sua senha!', height=2,
                         border_width=2, border_color='black', corner_radius=5)
    senha.place(x=66, y=100)
    frame_base.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    def salvar():
        login.get()
        senha.get()
        x = str(login.get())
        y = str(senha.get())
        verifica = verificar_conta(x, y)
        if x == '' or y == '':
            label5.configure(text='Preencha os quadrados!')
        elif not verifica:
            label5.configure(text='Usuario não encontrado')
        elif verifica:
            label5.configure(text='Usuario encontrado')
            global acesso
            acesso = True
            janela_principal()

    salvar = ctk.CTkButton(frame_base, text='Salvar', command=salvar, fg_color='#a1a1a1',
                           text_color='black', border_width=2, border_color='black')
    salvar.place(x=55, y=295)


botao_login()


# -_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_-

def botao_cadastro():
    limpar(frame_base)
    # Label 1 - Cadastro
    label1 = ctk.CTkLabel(frame_base, text='Faça seu cadastro:', font=fonte1)
    label1.place(x=5, y=5)

    # Label 2 - Email
    label2 = ctk.CTkLabel(frame_base, text='Email:', font=fonte2)
    label2.place(x=10, y=55)

    label2 = ctk.CTkLabel(frame_base, text='Email:', font=fonte2)
    label2.place(x=10, y=155)

    # Label 3 - Senha
    label3 = ctk.CTkLabel(frame_base, text='Senha:', font=fonte2)
    label3.place(x=5, y=95)

    label3 = ctk.CTkLabel(frame_base, text='Senha:', font=fonte2)
    label3.place(x=5, y=195)

    # frame de separar
    linha = ctk.CTkFrame(master=frame_base, width=500, height=5, bg_color='black')
    linha.place(x=2, y=138)

    # Entrada De Dados
    email = ctk.CTkEntry(frame_base, placeholder_text='Coloque seu email!', height=2,
                         border_width=2, border_color='black', corner_radius=5)
    email.place(x=66, y=60)

    conf_email = ctk.CTkEntry(frame_base, placeholder_text='Coloque seu email!', height=2,
                              border_width=2, border_color='black', corner_radius=5)
    conf_email.place(x=66, y=160)

    senha = ctk.CTkEntry(frame_base, placeholder_text='Coloque sua senha!', height=2,
                         border_width=2, border_color='black', corner_radius=5)
    senha.place(x=66, y=100)

    conf_senha = ctk.CTkEntry(frame_base, placeholder_text='Confirme sua Senha!', height=2,
                              border_width=2, border_color='black', corner_radius=5)
    conf_senha.place(x=66, y=200)

    def salvar():
        x = email.get()
        y = conf_email.get()
        a = senha.get()
        b = conf_senha.get()
        if x == y and a == b:
            criar_conta(x, a)

    salvar = ctk.CTkButton(frame_base, text='Salvar', command=salvar, fg_color='#a1a1a1',
                           text_color='black', border_width=2, border_color='black')
    salvar.place(x=55, y=295)


btn_log = ctk.CTkButton(frame3, text='Login   ', command=botao_login, width=80, height=5,
                        border_color='black', fg_color='black', hover_color='#313136')
btn_log.place(relx=0, rely=0.15)

btn_cad = ctk.CTkButton(frame3, text='Cadastro   ', command=botao_cadastro, width=80, height=5,
                        border_color='black', fg_color='black', hover_color='#313136')
btn_cad.place(relx=0, rely=0.27)

# -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

def janela_principal():
    if acesso:
        app = ctk.CTk()
        app.title('Aposte, aposte, APOSTE!')
        app.geometry("400x300")
        app.mainloop()


if __name__ == '__main__':
    tela_login.mainloop()
