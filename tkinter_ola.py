import tkinter as tk
from tkinter import messagebox

def exibir_mensagem():
# Recuperar informação digitrada no Entry
    nome = campo.get()
    if nome.strip:
        messagebox.showinfo(
        'Bem-Vindo(a)',
        f'Olá {nome}. Se você está vendo essa mensagem, é porque clicou no botão!'
    )
    else:
        messagebox.showwarning(
            'Ops',
            'Primeiro você precisa digitar seu NOME!'
        )

#criando uma janela
janela = tk.Tk()
# inserindo titulo para a janela
janela.title('montando interface com pyton')
#definindo dimensoes
janela.geometry('600x400')


titulo = tk.Label(
    janela,
    text='Olá mundo',
    font=('Arial', 20)
).pack(pady=10)

botao = tk.Button(
    janela,
    text="Clique aqui",
    font=('Arial', 12),
    command=exibir_mensagem
).pack(pady=10)

campo = tk.Entry(
    janela,
    font=('arial', 12),
    width=20
)
campo.pack(pady=10)




janela.mainloop()