import sqlite3 as sqlite


def limpar(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()


def criar_conta(x, y):
    contas = sqlite.connect('contas.db')
    c = contas.cursor()
    c.execute("INSERT INTO contas (email, senha) VALUES (?, ?)", (x, y))
    contas.commit()
    contas.close()


def verificar_conta(x, y):
    contas = sqlite.connect('contas.db')
    c = contas.cursor()
    c.execute("SELECT * FROM contas WHERE email = ? AND senha = ?", (x, y))
    conta = c.fetchone()
    contas.close()
    if conta:
        return True
    return False
