import sqlite3 as sqlite

contas = sqlite.connect('contas.db')
c = contas.cursor()

c.execute("SELECT * FROM contas")
contas_l = c.fetchall()
print(list(conta for conta in contas_l))


contas.close()
