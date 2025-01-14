import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           nome TEXT NOT NULL,
                           email TEXT NOT NULL,
                           tel TEXT NOT NULL,
                           sexo TEXT NOT NULL,
                           data_nascimento TEXT NOT NULL,
                           endereco TEXT NOT NULL,
                           turno TEXT NOT NULL,
                           picture TEXT NOT NULL)''')

    def registrar_estudante(self, estudante):
        try:
            self.c.execute("INSERT INTO estudantes(nome, email, tel, sexo, data_nascimento, endereco, turno, picture) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                           estudante)
            self.conn.commit()
            messagebox.showinfo('Sucesso', 'Registro realizado com sucesso!')
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao registrar: {e}')

    def visualizar_todos_estudantes(self):
        self.c.execute("SELECT * FROM estudantes")
        dados = self.c.fetchall()

        return dados

    def buscar_estudante(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
        dados = self.c.fetchone()
        return dados

    def atualizar_estudante(self, novos_valores):
        try:
            query = "UPDATE estudantes SET nome=?, email=?, tel=?, sexo=?, data_nascimento=?, endereco=?, turno=?, picture=? WHERE id=?"
            self.c.execute(query, novos_valores)
            self.conn.commit()
            messagebox.showinfo('Sucesso', f'Estudante com ID: {novos_valores[8]} foi atualizado!')
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao atualizar: {e}')

    def deletar_estudante(self, id):
        try:
            self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
            self.conn.commit()
            messagebox.showinfo('Sucesso', f'Estudante com ID: {id} foi deletado!')
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao deletar: {e}')

    def fechar_conexao(self):
        self.conn.close()

# Criando uma instância do sistema de registro
sistema_de_registro = SistemaDeRegistro()

# Informações 
#estudante = ('Elena', 'elena@gmail.com', '64988888888', 'F', '16/07/2000', 'Rua 2', 'Matutino', 'imagem2.png')
#sistema_de_registro.registrar_estudante(estudante)

#Ver estudantes 
#todos_alunos = sistema_de_registro.visualizar_todos_estudantes()

#Procurar aluno
#aluno_pesquisar = sistema_de_registro.buscar_estudante(2)

#Atualizar aluno
#estudante = ('Elena', 'elena@gmail.com', '64988888888', 'F', '16/07/2001', 'Rua 2', 'Matutino', 'imagem2.png', 2)
#aluno_atualizar = sistema_de_registro.atualizar_estudante(estudante)

#Deletar aluno
#sistema_de_registro.deletar_estudante(1)