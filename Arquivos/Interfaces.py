from tkinter import *
from tkinter import ttk
import Functions
from functools import partial

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#tela de login
def entrar(receitas):
	janela = Tk()
	janela.title("Cookner Notes   -   ENTRAR USUARIO")
	ws = janela.winfo_screenwidth()
	hs = janela.winfo_screenheight()
	x = (ws/2) - (450/2)    
	y = (hs/2) - (320/2)
	janela.geometry('%dx%d+%d+%d' % (450, 320, x, y))

	Label(janela, text = 'Informe seus dados', font = ('Arial', 12, 'bold')).place(x=20,y=10)

	#LOGIN
	Label(janela, text = 'login:', font = 12,).place(x=47,y=40)
	Text(janela, height = 1, width = 30, font = 12).place(x=100,y=40)

	#SENHA
	Label(janela, text = 'senha:', font = 12,).place(x=40,y=70)
	Entry(janela, width = 30, font = 12, show = '*').place(x=100,y=70)

	#ESQUECI A SENHA
	Button(janela, text = "ESQUECI A SENHA", width = 18, height = 1, command = lambda: [janela.withdraw(), recuperauser(janela, receitas)]).place(x=238,y=100)

	#CADASTRO
	Label(janela, text = 'Caso não possua cadastro, clique em "CADASTRAR-SE"', font = ('Arial', 11, 'bold')).place(x=20,y=225)
	Button(janela, text = "CADASTRAR-SE", width = 34, height = 2, command = lambda: [janela.withdraw(), cadastraruser(janela)]).place(x=120,y=250)

	#ENTRAR
	cont = []
	Button(janela, text = "ENTRAR", width = 34, height = 2, command = lambda: [Functions.conferelogin(receitas, janela,cont)]).place(x=120,y=135)

	janela.resizable(0,0)
	janela.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#tela de cadastro
def cadastraruser(janelaAnterior):
	janela = Tk()
	janela.title("Cookner Notes   -   CADASTRA USUARIO")
	ws = janela.winfo_screenwidth()
	hs = janela.winfo_screenheight()
	x = (ws/2) - (650/2)
	y = (hs/2) - (400/2)
	janela.geometry('%dx%d+%d+%d' % (650, 400, x, y))

	Label(janela,text = "Informe o nome de login, senha e palavra-chave desejado seguro para acesso", font = ('Arial', 12, 'bold')).place(x=20,y=10)

	#LOGIN
	Label(janela,text = 'Nome de login:', font = 12).place(x=77,y=60)
	Text(janela, height = 1, width = 30, font = 12).place(x=190,y=60)

	#SENHA
	Label(janela,text = 'senha:', font = 12).place(x=137,y=90)
	Entry(janela, width = 30, font = 12, show="*").place(x=190,y=90)

	#SENHA
	Label(janela,text = 'Confirme sua senha:', font = 12).place(x=40,y=120)
	Entry(janela, width = 30, font = 12, show="*").place(x=190,y=120)

	#PERGUNTA
	Label(janela,text = 'Selecione uma pergunta e responda para sua segurança', font = 12).place(x=20,y=230)
	list_perguntas = ['Qual o nome da escola onde realizou o segundo ano fundamental?','Qual o nome do seu Pai','Qual o nome da sua Mãe','Qual nome do time que você torce', 'Quantos anos você tinha quando aprendeu a andar de bicicleta', 'Qual nome do seu pet', 'Qual o nome do seu Professor favorito da escola']
	perguntas = ttk.Combobox(janela, name = "pergunta", values = list_perguntas, width=60 , state = 'readonly')
	perguntas.place(x=20,y=260)
	perguntas.current(0)
	Label(janela,text = 'Responda a pergunta abaixo por segurança', font = ('Arial', 12, 'bold')).place(x=20,y=180)
	Text(janela, height = 1, width = 60, font = 12).place(x=20,y=290)

	#CADASTRAR
	Button(janela, text = "CADASTRAR", width = 34, height = 2, command = lambda: [Functions.cadastrarusuario(janela, janelaAnterior)]).place(x=180,y=330)

	janela.resizable(0,0)
	janela.protocol("WM_DELETE_WINDOW", partial(Functions.aoFechar, janelaAnterior, janela, False))
	janela.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#tela de bloqueio
def timerBAN(count, receitas):
	janela = Tk()
	janela.title("BLOQUEADO")
	ws = janela.winfo_screenwidth()
	hs = janela.winfo_screenheight()
	x = (ws/2) - (450/2)
	y = (hs/2) - (180/2)
	janela.geometry('%dx%d+%d+%d' % (500, 180, x, y))

	Label(janela,text = "Voce digitou sua senha errada 5 vezes", font = 12).place(x=20,y=10)

	Label(janela,text = 'Insira seus dados novamente em', font = 12).place(x=20,y=70)

	Label(janela,text = 'segundos', font = 12).place(x=300,y=70)

	Functions.atualizalabel(count, janela, receitas)

	janela.resizable(0,0)
	janela.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#tela de verificação do usuario a recuperar
def recuperauser(janelaAnterior, receitas):
	janela = Tk()
	janela.title("Cookner Notes   -   RECUPERAR SENHA")
	ws = janela.winfo_screenwidth()
	hs = janela.winfo_screenheight()
	x = (ws/2) - (400/2)    
	y = (hs/2) - (150/2)
	janela.geometry('%dx%d+%d+%d' % (400, 150, x, y))
	
	Label(janela, text = 'Informe seus dados para recuperação de senha', font = ('Arial', 12, 'bold')).place(x=20,y=10)

	#LOGIN
	Label(janela, text = 'login:', font = 12,).place(x=20,y=60)
	Text(janela, height = 1, width = 30, font = 12).place(x=65,y=60)

	#PRÓXIMO
	Button(janela, text = "PRÓXIMO", width = 18, height = 1, command = lambda: [Functions.recuperarsenha(janela, receitas)]).place(x=200,y=100)

	janela.resizable(0,0)
	janela.protocol("WM_DELETE_WINDOW", partial(Functions.aoFechar, janelaAnterior, janela, False))
	janela.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#tela de verificação da pergunta
def recuperandosenha(login, perguntar, receitas, janelaAnterior):
	janela = Tk()
	janela.title("Cookner Notes   -   RECUPERAR SENHA")
	ws = janela.winfo_screenwidth()
	hs = janela.winfo_screenheight()
	x = (ws/2) - (600/2)    
	y = (hs/2) - (200/2)
	janela.geometry('%dx%d+%d+%d' % (600, 200, x, y))

	pergunta_user = ''
	if perguntar == '0':
		pergunta_user = 'Qual o nome da escola onde realizou o segundo ano fundamental' 

	elif perguntar == '1':
		pergunta_user = 'Qual o nome do seu Pai'

	elif perguntar == '2':
		pergunta_user = 'Qual o nome da sua Mãe' 

	elif perguntar == '3':
		pergunta_user = 'Qual nome do time que você torce' 

	elif perguntar == '4':
		pergunta_user = 'Quantos anos você tinha quando aprendeu a andar de bicicleta' 

	elif perguntar == '5':
		pergunta_user = 'Qual nome do seu pet' 

	elif perguntar == '6':
		pergunta_user = 'Qual o nome do seu Professor favorito da escola' 

	#PERGUNTA
	Label(janela, text = 'Informe seus dados para recuperação de senha', font = ('Arial', 12, 'bold')).place(x=20,y=10)
	Label(janela, text = pergunta_user, font = 12,).place(x=20,y=60)
	Text(janela, height = 1, width = 40, font = 12).place(x=20,y=90)

	#RECUPERAR SENHA
	Button(janela, text = "RECUPERAR SENHA", width = 18, height = 1, command = lambda: [Functions.recuperasenha(login, janela, receitas)]).place(x=250,y=120)

	janela.resizable(0,0)
	janela.protocol("WM_DELETE_WINDOW", partial(Functions.aoFechar, janelaAnterior, janela, False))
	janela.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#tela que mostra a senha
def mostrasenha(login, senha, janelaAnterior, receitas):
	janela = Tk()
	janela.title("Cookner Notes   -  MOSTRA SENHA")
	ws = janela.winfo_screenwidth()
	hs = janela.winfo_screenheight()
	x = (ws/2) - (300/2)
	y = (hs/2) - (200/2)

	janela.geometry('%dx%d+%d+%d' % (300, 200, x, y))
	Label(janela, text = senha, width=10).place(x=140, y=20)
	Label(janela, text = 'Sua senha é:', font = 12).place(x=30, y=20)
	Label(janela, text = 'Deseja mudar sua senha?', font = 12).place(x=30, y=70)

	#NÃO MUDA SENHA
	Button(janela, text = "NÃO", width = 15, height = 1, command = lambda: [janela.withdraw(), entrar(receitas)]).place(x=160,y=100)

	#MUDA SENHA
	Button(janela, text = "SIM", width = 15, height = 1, command = lambda: [janela.withdraw(), alterarsenha(login, janelaAnterior, receitas)]).place(x=20,y=100)

	janela.resizable(0,0)
	janela.protocol("WM_DELETE_WINDOW", partial(Functions.aoFechar, janelaAnterior, janela, False))
	janela.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#tela de alteração de senha
def alterarsenha(login, janelaAnterior, receitas):
	janela = Tk()
	janela.title("Cookner Notes   -  ALTERAR SENHA")
	ws = janela.winfo_screenwidth()
	hs = janela.winfo_screenheight()
	x = (ws/2) - (300/2)
	y = (hs/2) - (300/2)
	janela.geometry('%dx%d+%d+%d' % (300, 300, x, y))

	#SENHA
	Label(janela,text = 'Informe a nova senha desejada:', font = 12,).place(x=30,y=10)
	Entry(janela, width = 25, font = 12, show="*").place(x=30,y=40)

	#SENHA
	Label(janela,text = 'Confirme sua nova senha:', font = 12,).place(x=30,y=90)
	Entry(janela, width = 25, font = 12, show="*").place(x=30,y=120)

	#ALTERAR
	Button(janela, text = "ALTERAR", width = 34, height = 2, command = lambda: [Functions.mudasenha(login, janela, receitas)]).place(x=30,y=170)

	janela.resizable(0,0)
	janela.protocol("WM_DELETE_WINDOW", partial(Functions.aoFechar, janelaAnterior, janela, False))
	janela.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#tela para gerenciamento das receitas
def menuPrincipal(receitas, janelaAnterior, loginuser):

	janela = Tk()
	janela.title("Cookner Notes   -   MENU PRINCIPAL")
	ws = janela.winfo_screenwidth()
	hs = janela.winfo_screenheight()
	x = (ws/2) - (269/2)    
	y = (hs/2) - (180/2)
	janela.geometry('%dx%d+%d+%d' % (269, 180, x, y))

	#CADASTRAR RECEITAS
	Button(janela, text = "CADASTRAR RECEITAS", width = 34, height = 2, command = lambda: [janela.withdraw(), menuCadastrar(receitas,janela, loginuser)]).grid(column=0, row=0, padx=10, pady=10)

	#EDITAR RECEITAS
	Button(janela, text = "EDITAR RECEITAS", width = 34, height = 2, command = lambda: [janela.withdraw(), menuEditar(receitas,janela, loginuser)]).grid(column=0, row=2, padx=10, pady=10)

	#CONSULTAR RECEITA
	Button(janela, text = "CONSULTAR RECEITAS", width = 34, height = 2, command = lambda: [janela.withdraw(), menuConsultar(receitas,janela)]).grid(column=0, row=4, padx=10, pady=10)

	janela.resizable(0,0)
	janela.protocol("WM_DELETE_WINDOW", lambda: [receitas.clear(), Functions.aoFechar(janelaAnterior, janela, False)])
	janela.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#tela para cadastro das receitas
def menuCadastrar(receitas,janelaAnterior, loginuser):

	janela = Tk()
	janela.title("Cookner Notes   -   CADASTRAR RECEITAS")
	ws = janela.winfo_screenwidth()
	hs = janela.winfo_screenheight()
	x = (ws/2) - (600/2)    
	y = (hs/2) - (700/2)
	janela.geometry('%dx%d+%d+%d' % (600, 700, x, y))

	#NOME
	Label(janela,text = 'Nome:', font = 12,).place(x=40,y=20)
	Text(janela, height = 1, width = 30, font = 12).place(x=100,y=20)

	#SERVE
	Label(janela, text= 'Serve', font = 12).place(x=40,y=50)
	Text(janela, height = 1, width = 3, font = 12).place(x=100,y=50)
	Label(janela, text= 'pessoas', font = 12).place(x=140,y=50)

	#VALIDADE
	Label(janela, text = 'Validade:', font = 12).place(x=20,y=80)
	Label(janela, text = 'dias', font = 12).place(x=140,y=80)
	Text(janela, height = 1, width = 3, font = 12).place(x=100,y=80)

	#INGREDIENTES
	Label(janela, text= 'Ingredientes', font = 12).place(x=100,y=125)
	listbox = Listbox(janela, height = 10, width =30)
	listbox.place(x=50,y=150)
	listbox.bind('<<ListboxSelect>>', partial(Functions.eventoSelecaoListBox, janela))

	#NOME INGREDIENTE
	Label(janela, text = 'Nome Ingrediente:', font = 12).place(x=250,y=160)
	Text(janela, height = 1, width = 20, font = 12).place(x=390,y=160)

	#QUANTIDADE INGREDIENTE
	Label(janela, text = 'Quantidade:', font = 12).place(x=290,y=190)
	Entry(janela, width = 3, font = 12).place(x=390,y=190)

	#MEDIDA INGREDIENTE	
	Label(janela, text = 'Medida:', font = 12).place(x=317,y=220)
	medidas = ['gr', 'ml', 'unidade', 'L', 'Kg', 'xícara(s)', 'colher(s) de sopa', 'colher(s) de chá', 'bacia']
	combobox = ttk.Combobox(janela, name = "medidaIngrediente", values = medidas, width=15, state = 'readonly')
	combobox.place(x=390,y=220)
	combobox.current(0)

	#MODO DE PREPARO
	Label(janela, text= 'Modo de Preparo:', font = 12).place(x=50,y=335)
	Text(janela, height = 15, width =57, font = 12).place(x=50,y=360)

	#ADICIONA INGREDIENTE
	Button(janela, text = "Adiciona Ingrediente", width = 18, height = 1, command = lambda: [Functions.adicionaIngrediente(janela)]).place(x=270,y=270)

	#EXCLUI INGREDIENTE
	Button(janela, text = "Exclui Ingrediente", width = 18, height = 1, command = lambda : [Functions.excluiIngrediente(janela)]).place(x=440,y=270)

	#ALTERA INGREDIENTE
	Button(janela, text = "Altera Ingrediente", width = 25, height = 1, command = lambda : [Functions.AlteraIngrediente(janela)]).place(x=335,y=300)

	#ADICIONA RECEITA
	Button(janela, text = "Adiciona Receita", width = 25, height = 2, command = lambda: [Functions.adicionaReceita(janela,receitas,janelaAnterior, loginuser)]).place(x=200,y=640)

	janela.resizable(0,0)
	janela.protocol("WM_DELETE_WINDOW", partial(Functions.aoFechar, janelaAnterior, janela, False))
	janela.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#tela de escolha da receita
def menuEditar(receitas,janelaAnterior, loginuser):

	if (not bool(receitas)):
		janelaAnterior.deiconify()
		return Functions.messagebox.showinfo("Cookner Notes   -   AVISO","Não há nenhuma receita cadastrada!")

	janela = Tk()
	janela.title("Cookner Notes   -   ALTERAR RECEITAS")
	ws = janela.winfo_screenwidth()
	hs = janela.winfo_screenheight()
	x = (ws/2) - (300/2)    
	y = (hs/2) - (150/2)
	janela.geometry('%dx%d+%d+%d' % (300, 150, x, y))

	Label(janela, text= 'Receitas', font = 12).place(x=120,y=20)
	receitasNome = []
	receitasKey = []
	for receita in receitas:
		receitasNome.append(receitas[receita][0] + " - " +str(receita))
	receitasCombox = ttk.Combobox(janela, values = receitasNome, width=20, state = 'readonly')
	receitasCombox.place(x=80,y=50)
	receitasCombox.current(0)
	
	#EXCLUI RECEITA
	Button(janela, text = "Exclui Receita", width = 15, height = 1, command = lambda : [Functions.excluiReceita(janela,receitas,janelaAnterior, loginuser, int(receitasCombox.get().split(" - ")[1]))]).place(x=160,y=90)
	
	#EDITA RECEITA
	Button(janela, text = "Editar Receita", width = 15, height = 1, command = lambda: [janela.withdraw(), menuAltera(receitas,int(receitasCombox.get().split(" - ")[1]),janela, loginuser)]).place(x=30,y=90)

	janela.resizable(0,0)
	janela.protocol("WM_DELETE_WINDOW", partial(Functions.aoFechar, janelaAnterior, janela, False))
	janela.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#tela para alterar as receitas
def menuAltera(receitas, ReceitaKey, janelaAnterior, loginuser):
	
	janela = Tk()
	janela.title("Cookner Notes   -   EDITAR RECEITA")
	ws = janela.winfo_screenwidth()
	hs = janela.winfo_screenheight()
	x = (ws/2) - (600/2)  
	y = (hs/2) - (700/2)
	janela.geometry('%dx%d+%d+%d' % (600, 700, x, y))

	#NOME
	Label(janela, text = 'Nome:', font = 12).place(x=40,y=20)
	nomeReceita = Text(janela, height = 1, width = 30, font = 12)
	nomeReceita.place(x=100,y=20)
	nomeReceita.insert(END,receitas[ReceitaKey][0])
	
	#SERVE
	Label(janela, text = 'Serve:', font = 12).place(x=40,y=50)
	serveReceita = Text(janela, height = 1, width = 3, font = 12)
	serveReceita.place(x=100,y=50)
	serveReceita.insert(END,receitas[ReceitaKey][1])
	Label(janela, text= 'pessoas', font = 12).place(x=140,y=50)

	#VALIDADE
	Label(janela, text = 'Validade:', font = 12).place(x=20,y=80)
	validadeReceita = Text(janela, height = 1, width = 3, font = 12)
	validadeReceita.place(x=100,y=80)
	validadeReceita.insert(END,receitas[ReceitaKey][2])
	Label(janela, text = 'dias', font = 12).place(x=140,y=80)

	#INGREDIENTES
	Label(janela, text= 'Ingredientes', font = 12).place(x=100,y=125)
	listaIngredientes = receitas[ReceitaKey][3]
	ingredientesListBox = Listbox(janela, height = 10, width =25)
	ingredientesListBox.place(x=50,y=150)
	for ingrediente in listaIngredientes:
		ingredientesListBox.insert(END, ingrediente[0] + "\n - " + ingrediente[1] + " - " + str(ingrediente[2]) + "\n")
	
	ingredientesListBox.bind('<<ListboxSelect>>', partial(Functions.eventoSelecaoListBox, janela))

	#NOME INGREDIENTE
	Label(janela, text = 'Nome Ingrediente:', font = 12).place(x=250,y=160)
	Text(janela, height = 1, width = 20, font = 12).place(x=390,y=160)

	#QUANTIDADE INGREDIENTE
	Label(janela, text = 'Quantidade:', font = 12).place(x=290,y=190)
	Entry(janela, width = 3, font = 12).place(x=390,y=190)
	
	#MEDIDA INGREDIENTE
	Label(janela, text = 'Medida:', font = 12).place(x=317,y=220)
	medidas = ['gr', 'ml', 'unidade', 'L', 'Kg', 'xícara(s)', 'colher(s) de sopa', 'colher(s) de chá']
	combobox = ttk.Combobox(janela, values = medidas, width=15, state = 'readonly')
	combobox.place(x=390,y=220)
	combobox.current(0)

	#MODO DE PREPARO
	Label(janela, text= 'Modo de Preparo:', font = 12).place(x=50,y=335)
	modoPreparoReceita = Text(janela, name = "modoPreparo", height = 15, width =57, font = 12)
	modoPreparoReceita.place(x=50,y=360)
	modoPreparoReceita.insert(END,receitas[ReceitaKey][4])

	#ADICIONA INGREDIENTE
	Button(janela, text = "Adiciona Ingrediente", width = 18, height = 1, command = lambda : [Functions.adicionaIngrediente(janela)]).place(x=270,y=270)
	
	#EXCLUI INGREDIENTE
	Button(janela, text = "Exclui Ingrediente", width = 18, height = 1, command = lambda : [Functions.excluiIngrediente(janela)]).place(x=440,y=270)

	#ALTERA INGREDIENTE
	Button(janela, text = "Altera Ingrediente", width = 25, height = 1, command = lambda : [Functions.AlteraIngrediente(janela)]).place(x=335,y=300)

	#ALTERA RECEITA
	Button(janela, text = "Altera Receita", width = 25, height = 1, command = lambda : [Functions.alteraReceita(janela,receitas,janelaAnterior, loginuser, ReceitaKey)]).place(x=200,y=650)
	
	janela.resizable(0,0)
	janela.protocol("WM_DELETE_WINDOW", partial(Functions.aoFechar, janelaAnterior, janela, False))
	janela.mainloop()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#tela de escolha da receita
def menuConsultar(receitas, janelaAnterior):

	if (not bool(receitas)):
		janelaAnterior.deiconify()
		return Functions.messagebox.showinfo("Cookner Notes   -   AVISO","Não há nenhuma receita cadastrada!")

	janela = Tk()
	janela.title("Cookner Notes   -   CONSULTAR RECEITAS")
	ws = janela.winfo_screenwidth()
	hs = janela.winfo_screenheight()
	x = (ws/2) - (300/2)    
	y = (hs/2) - (150/2)
	janela.geometry('%dx%d+%d+%d' % (300, 150, x, y))

	Label(janela, text= 'Receitas', font = 12).place(x=120,y=20)
	receitasKey = []
	for receita in receitas:
		receitasKey.append(receitas[receita][0] +" - "+ str(receita))
	receitasCombox = ttk.Combobox(janela, values = receitasKey, width=20, state = 'readonly')
	receitasCombox.place(x=80,y=50)
	receitasCombox.current(0)

	Button(janela, text = "Consulta Receita", width = 15, height = 1, command = lambda: [janela.withdraw(), menuVerReceitas(receitas,int(receitasCombox.get().split(" - ")[1]),janela)]).place(x=95,y=90) 

	janela.resizable(0,0)
	janela.protocol("WM_DELETE_WINDOW", partial(Functions.aoFechar, janelaAnterior, janela, False))
	janela.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#tela de consultar as receitas
def menuVerReceitas(receitas, receitaKey, janelaAnterior):

	janela = Tk()
	janela.title("Cookner Notes   -   CONSULTAR RECEITAS")
	ws = janela.winfo_screenwidth()
	hs = janela.winfo_screenheight()
	x = (ws/2) - (1100/2)    
	y = (hs/2) - (450/2)
	janela.geometry('%dx%d+%d+%d' % (1100, 450, x, y))

	#NOME
	Label(janela, text= 'Receita de', font = 12).place(x=20,y=40)
	nomeReceitaTextbox = Text(janela, height = 1, width = 30, font = 12)
	nomeReceitaTextbox.insert(END,receitas[receitaKey][0])
	nomeReceitaTextbox.config(state = 'disabled')
	nomeReceitaTextbox.place(x=115,y=40)

	#SERVE
	Label(janela, text= 'Serve', font = 12).place(x=55,y=70)
	serveReceita = receitas[receitaKey][1]
	serveReceitaTextbox = Text(janela, height = 1, width = 3, font = 12)
	serveReceitaTextbox.insert(END, serveReceita)
	serveReceitaTextbox.config(state = 'disabled')
	serveReceitaTextbox.place(x=115,y=70)
	pessoaLabel = Label(janela, text= 'pessoas', font = 12).place(x=155,y=70)

	#VALIDADE
	Label(janela, text= 'Validade', font = 12).place(x=33,y=100)
	validadeReceita = receitas[receitaKey][2]
	validadeReceitaTextbox = Text(janela, height = 1, width = 3, font = 12)
	validadeReceitaTextbox.insert(END, validadeReceita)
	validadeReceitaTextbox.config(state = 'disabled')
	validadeReceitaTextbox.place(x=115,y=100)
	Label(janela, text= 'dias', font = 12).place(x=155,y=100)

	#INGREDIENTES
	Label(janela, text= 'Ingredientes', font = 12).place(x=210,y=130)
	listaIngredientes = receitas[receitaKey][3]
	nomeIngredienteTextbox = Text(janela, height = 15, width = 40, font = 12)
	for ingrediente in listaIngredientes:
		nomeIngredienteTextbox.insert(END, ingrediente[0] +" "+ str(ingrediente[2]) +" "+ ingrediente[1] + '\n')
	nomeIngredienteTextbox.config(state = 'disabled')
	nomeIngredienteTextbox.place(x=60,y=160)

	#MODO DE PREPARO
	Label(janela, text= 'Modo de Preparo', font = 12).place(x=690,y=50)
	modopreparotextbox = Text(janela, name = "modoPreparo", height = 19, width =57, font = 12)
	modopreparotextbox.insert(END,receitas[receitaKey][4])
	modopreparotextbox.config(state = 'disabled')
	modopreparotextbox.place(x=480,y=90)

	janela.resizable(0,0)
	janela.protocol("WM_DELETE_WINDOW", partial(Functions.aoFechar, janelaAnterior, janela, False))
	janela.mainloop()