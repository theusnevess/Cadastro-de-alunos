#Importando dependencias do tkinter 
from tkinter.ttk import * 
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

#importando pillow
from PIL import ImageTk, Image

#tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

#importando main
from main import * 

#cores
cor0 = "#2e2d2b"  # Preta
cor1 = "#13293D"  #azul    
cor2 = "#C1E8FF"  # grey
cor3 = "#5483b3"  # linha selecionada
cor4 = "#E8F1F2"   # letra
cor6 = "#021024"   # azul escuro
cor7 = "#ef5350"   # vermelha
cor8 = "#263238"   # + verde
cor9 = "#e9edf5"   # + verde


#Criando janela 
janela = Tk()
janela.title("")
janela.geometry('810x565')
janela.configure(background=cor1)
janela.resizable(width=False, height=False)

style = Style(janela)
style.theme_use("clam")

#Criando frames 
frame_logo = Frame(janela, width=850, height=52, bg=cor6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=cor1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_detalhes = Frame(janela, width=800, height=100, bg=cor1, relief=SOLID)
frame_detalhes.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=800, height=100, bg=cor1, relief=SOLID)
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

#Trabalhando no frame logo --------------------------------------------------
global imagem, imagem_string, l_imagem

app_lg = Image.open('logo.png')
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="  Sistema de cadastro de alunos", width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=cor6, fg=cor4)
app_logo.place(x=5, y=0)

#Abrindo a imagem
imagem = Image.open('logo.png')  # Abre a imagem escolhida
imagem = imagem.resize((130, 130))  # Redimensiona para 130x130 pixels
imagem = ImageTk.PhotoImage(imagem)  # Converte a imagem para o formato compatível com Tkinter

# Atualiza o label com a nova imagem
l_imagem = Label(frame_detalhes, image=imagem, bg=cor1)
l_imagem.place(x=390, y=20)  # Posiciona a imagem na tela (ajustei para um valor visível)

#----------------------------------- Criando funçoes para CRUD --------------------------------
#função adicionar 
def adicionar():
    global imagem, imagem_string, l_imagem

    #obtendo os valores 
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sexo = c_sexo.get()
    data = data_nascimento.get()
    endereco = e_endereco.get()
    turno = c_turno.get()
    img = imagem_string

    lista = [nome, email, tel, sexo, data, endereco, turno, img]

    #verificando se a lista contem valor vazio
    for i in lista:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    
    #registrando os valores 
    sistema_de_registro.registrar_estudante(lista)

    #limpando os campos de entradas
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_turno.delete(0, END)

    #mostrando os valores na tabela
    mostrar_alunos()

#funcao procurar
def procurar(): 
    global imagem, imagem_string, l_imagem

    #obtendo o id
    id_aluno = int(e_procurar.get())

    #procurando aluno 
    dados = sistema_de_registro.buscar_estudante(id_aluno)

    #limpando os campos de entradas
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_turno.delete(0, END)

    #inserindo valores os campos de entradas
    e_nome.insert(END, dados[1])
    e_email.insert(END, dados[2])
    e_tel.insert(END, dados[3])
    c_sexo.insert(END, dados[4])
    data_nascimento.insert(END, dados[5])
    e_endereco.insert(END, dados[6])
    c_turno.insert(END, dados[7])

    imagem = dados[8]
    imagem_string = imagem

    imagem = Image.open(imagem)  
    imagem = imagem.resize((130, 130))  
    imagem = ImageTk.PhotoImage(imagem)  
    l_imagem = Label(frame_detalhes, image=imagem, bg=cor1)
    l_imagem.place(x=390, y=20)  

#função atualizar 
def atualizar():
    global imagem, imagem_string, l_imagem

    #obtendo o id
    id_aluno = int(e_procurar.get())

    #obtendo os valores 
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sexo = c_sexo.get()
    data = data_nascimento.get()
    endereco = e_endereco.get()
    turno = c_turno.get()
    img = imagem_string

    lista = [nome, email, tel, sexo, data, endereco, turno, img, id_aluno]

    #verificando se a lista contem valor vazio
    for i in lista:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    
    #registrando os valores 
    sistema_de_registro.atualizar_estudante(lista)

    #limpando os campos de entradas
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_turno.delete(0, END)

    #abrindo a imagem
    imagem = Image.open('logo.png')  
    imagem = imagem.resize((130, 130))  
    imagem = ImageTk.PhotoImage(imagem)  
    l_imagem = Label(frame_detalhes, image=imagem, bg=cor1)
    l_imagem.place(x=390, y=20)  

    #mostrando os valores na tabela
    mostrar_alunos()

#função excluir
def excluir():
    global imagem, imagem_string, l_imagem

    #obtendo o id
    id_aluno = int(e_procurar.get())

    #deletando o aluno
    sistema_de_registro.deletar_estudante(id_aluno)

    lista = [nome, email, tel, sexo, data, endereco, turno, img, id_aluno]

    #limpando os campos de entradas
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_turno.delete(0, END)

    e_procurar.delete(0, END)

    #abrindo a imagem
    imagem = Image.open('logo.png')  
    imagem = imagem.resize((130, 130))  
    imagem = ImageTk.PhotoImage(imagem)  
    l_imagem = Label(frame_detalhes, image=imagem, bg=cor1)
    l_imagem.place(x=390, y=20)  

    #mostrando os valores na tabela
    mostrar_alunos()




#Criando os campos de entrada ------------------------------------------------
l_nome = Label(frame_detalhes, text="Nome *", anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_detalhes, width=30, justify='left', relief='solid')
e_nome.place(x=7, y=40)

#Criando os campos de entrada ------------------------------------------------
l_email = Label(frame_detalhes, text="Email *", anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_email.place(x=4, y=70)
e_email = Entry(frame_detalhes, width=30, justify='left', relief='solid')
e_email.place(x=7, y=100)

#Criando os campos de entrada ------------------------------------------------
l_tel = Label(frame_detalhes, text="Telefone *", anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_tel.place(x=4, y=130)
e_tel = Entry(frame_detalhes, width=15, justify='left', relief='solid')
e_tel.place(x=7, y=160)

#Criando os campos de entrada ------------------------------------------------
l_sexo = Label(frame_detalhes, text="Sexo *", anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_sexo.place(x=127, y=130)
c_sexo = ttk.Combobox(frame_detalhes, width=7, font=('Ivy 8 bold'), justify='center')
c_sexo['values'] = ('M', 'F')
c_sexo.place(x=130, y=160)

# Criando os campos de entrada ------------------------------------------------
l_data_nascimento = Label(frame_detalhes, text="Data de nascimento *", anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_data_nascimento.place(x=220, y=10)  # Corrigir a chamada do método place()
data_nascimento = DateEntry(frame_detalhes, width=18, justify='center', background='darkblue', foreground='white', borderwidth=2, year=2025)
data_nascimento.place(x=224, y=40)

#Criando os campos de entrada ------------------------------------------------
l_endereco = Label(frame_detalhes, text="Endereço *", anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_endereco.place(x=220, y=70)
e_endereco = Entry(frame_detalhes, width=15, justify='left', relief='solid')
e_endereco.place(x=224, y=100)

#Criando os campos de entrada ------------------------------------------------
turnos = ['Matutino', 'Vespertino', 'Noturno']
l_turno = Label(frame_detalhes, text="Turno *", anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_turno.place(x=220, y=130)
c_turno = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'), justify='center')
c_turno['values'] = (turnos)
c_turno.place(x=224, y=160)

# Função para escolher imagem 
def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()  # Abre o diálogo de seleção de arquivo
    imagem_string = imagem  # Armazena o caminho da imagem

    imagem = Image.open(imagem)  # Abre a imagem escolhida
    imagem = imagem.resize((130, 130))  # Redimensiona para 130x130 pixels
    imagem = ImageTk.PhotoImage(imagem)  # Converte a imagem para o formato compatível com Tkinter

    # Atualiza o label com a nova imagem
    l_imagem = Label(frame_detalhes, image=imagem, bg=cor1)
    l_imagem.place(x=390, y=20)  # Posiciona a imagem na tela (ajustei para um valor visível)

    botao_carregar['text'] = 'Trocar de foto'  # Altera o texto do botão para 'Trocar de foto'

botao_carregar = Button(frame_detalhes, command=escolher_imagem, text=('Carregar foto').upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=cor1, fg=cor2)
botao_carregar.place(x=390, y=160)

# Tabela Alunos
def mostrar_alunos():

    # creating a treeview with dual scrollbars
    list_header = ['id', 'Nome', 'Email', 'Telefone', 'Sexo', 'Data', 'Endereço', 'Turno']

    # view all students                                                                                    I
    df_list = sistema_de_registro.visualizar_todos_estudantes()

    tree_aluno = ttk. Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
    #horizontal scrollbar
    hsb = ttk.Scrollbar (frame_tabela, orient="horizontal", command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky="nsew")
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "center", "center", "center", "center", "center", "center"]
    h = [40, 150, 150, 70, 70, 70, 120, 100, 100]

    n = 0

    for col in list_header:
        tree_aluno.heading(col, text=col.title(), anchor="w")  # ou "center"
        # adjust the column's width to the header string
        tree_aluno.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in df_list:
        tree_aluno.insert('', 'end', values=item)

    style = Style(janela)
    style.theme_use("clam")
    style.configure("Treeview", 
                    background=cor1,  # Fundo das células
                    foreground=cor2,  # Texto
                    rowheight=25, 
                    fieldbackground=cor1)
    style.map("Treeview", background=[('selected', cor3)])  # Cor da linha selecionada

    # Estilo dos cabeçalhos
    style.configure("Treeview.Heading", 
                    background=cor1,  # Fundo azul para cabeçalhos
                    foreground=cor2,  # Texto branco
                    font=('Helvetica', 10))  # Fonte configurada para negrito


#Procurar aluno -----------------------------------------
frame_procurar = Frame(frame_botoes, width=40, height=50, bg=cor1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text="Procurar aluno [Entra ID]", anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)

e_procurar = Entry(frame_procurar, width=5, justify='center', relief='solid', font=('Ivy 10'))
e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botao_procurar = Button(frame_procurar, command=procurar, text=('Procurar'), width=9, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=cor1, fg=cor2)
botao_procurar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

#botoes ----------------------------------------------------------
app_img_adicionar = Image.open('salvar.png')  
app_img_adicionar = app_img_adicionar.resize((25,25))  
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)  
app_adicionar = Button(frame_botoes, command=adicionar, image=app_img_adicionar, relief=GROOVE, text=('  Adicionar'), width=100, compound=LEFT, font=('Ivy 11'), bg=cor1, fg=cor2)
app_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

app_img_atualizar = Image.open('atualizar.png')  
app_img_atualizar = app_img_atualizar.resize((25,25))  
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)  
app_atualizar = Button(frame_botoes, command=atualizar, image=app_img_atualizar, relief=GROOVE, text=('  Atualizar'), width=100, compound=LEFT, font=('Ivy 11'), bg=cor1, fg=cor2)
app_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

app_img_excluir = Image.open('excluir.png')  
app_img_excluir = app_img_excluir.resize((25,25))  
app_img_excluir = ImageTk.PhotoImage(app_img_excluir)  
app_excluir = Button(frame_botoes, command=excluir, image=app_img_excluir, relief=GROOVE, text=('   Excluir'), width=100, compound=LEFT, font=('Ivy 11'), bg=cor1, fg=cor2)
app_excluir.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)


l_linha = Label(frame_botoes, relief=GROOVE, text=('h'), width=1, height=123, anchor=NW, font=('Ivy 1'), bg=cor1, fg=cor0)
l_linha.place(x=235, y=15)





#chamar a tabela
mostrar_alunos()

janela.mainloop()

