import psycopg2
from tkinter import *
from tkinter import messagebox
import Interfaces

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# FUNÇÕES RELACIONADAS A USUARIOS ABAIXO - FUNÇÕES RELACIONADAS A USUARIOS ABAIXO -  FUNÇÕES RELACIONADAS A USUARIOS ABAIXO -  FUNÇÕES RELACIONADAS A USUARIOS ABAIXO


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#cadastra usuario e insere no banco de dados
def cadastrarusuario(janela, janelaAnterior):
	widgets = janela.winfo_children()
	login = widgets[2].get(1.0, "end-1c")
	senha = widgets[4].get()
	senha2 = widgets[6].get()
	recupera = widgets[10].get(1.0, "end-1c")
	pergunta = widgets[8].current()
	
	
	#VERIFICAÇÃO DOS DADOS
	validaString(login)

	if (senha != senha2):
		return messagebox.showinfo("Cookner Notes   -   AVISO","Sua senha foi conferida incorretamente")

	validaString(recupera)

	validaString(senha)

	conn = factoryconnection()
	sql = "select * from usuario"
	cur = conn.cursor()
	cur.execute(sql)
	usuarios = cur.fetchall()

	loginusuarios = []
	for usuario in usuarios:
		loginusuarios.append(usuario[0])

	if(login in loginusuarios):
		return messagebox.showinfo("Cookner Notes   -   AVISO","Esse username já existe")

	cur.close()
	conn.close()

	#INSERE NO BANCO DE DADOS
	try:
		conn = factoryconnection()

		recuperar = (str(pergunta)+"-"+str(recupera))
		sqlInsertpessoa = "Insert into usuario values (%s,%s, %s)"
		curInsertPessoa = conn.cursor()
		curInsertPessoa.execute(sqlInsertpessoa,(login, senha, recuperar))
		curInsertPessoa.close()
		conn.commit()
		conn.close()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	
	aoFechar(janelaAnterior,janela, True)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#verifica usuario e extrai suas receitas do BD
def conferelogin(receitas, janela, cont):
	widgets = janela.winfo_children()
	loginuser = widgets[2].get(1.0, "end-1c")
	senha = widgets[4].get()

#VERIFICA AS INFORMAÇÕES INSERIDAS
	conn = factoryconnection()
	sql = "select * from usuario"
	cur = conn.cursor()
	cur.execute(sql)
	usuarios = cur.fetchall()
	cur.close()
	conn.close()

	for usuario in usuarios:
		if usuario[0] == loginuser:
#BLOQUEIA APÓS 5 ERROS
			if senha != usuario[1]:
				widgets[4].delete(0, END)
				messagebox.showinfo("Cookner Notes   -   AVISO","Senha inválida")
				if len(cont) == 4:
					inicializa(receitas, loginuser)
					janela.withdraw()
					return Interfaces.timerBAN(60, receitas)
				return cont.append("x")
#INICIALIZA AS RECEITAS NO SISTEMA
			else:
				inicializa(receitas, loginuser)
				janela.withdraw()
				return Interfaces.menuPrincipal(receitas, janela, loginuser)
				

	messagebox.showinfo("Cookner Notes   -   AVISO","Username inválido")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# FUNÇÕES RELACIONADAS A RECEITAS ABAIXO - FUNÇÕES RELACIONADAS A RECEITAS ABAIXO -  FUNÇÕES RELACIONADAS A RECEITAS ABAIXO -  FUNÇÕES RELACIONADAS A RECEITAS ABAIXO


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#verifica as informações da receita e inclui no banco
def adicionaReceita(janela,receitas,janelaAnterior, loginuser):
	widgets = janela.winfo_children()
	nomeReceita = widgets[1].get(1.0,  "end-1c")
	serveReceita = widgets[3].get(1.0, "end-1c")
	modopreparo = widgets[17].get(1.0, "end-1c")
	validadeReceita = widgets[7].get(1.0, "end-1c")
	conteudoListBox = widgets[9].get(0, END)

#VERIFICAÇÃO
	validaInteger(serveReceita)

	validaString(modopreparo)
	
	validaInteger(validadeReceita)

	validaString(nomeReceita)

	if(conteudoListBox == ()):
		return messagebox.showinfo("Cookner Notes   -   AVISO","Não há ingredientes na receita!")

	try:
		conn = factoryconnection()

		sqlSelectCodigo = "Select codigo from receitas"
		curSelectCodigo = conn.cursor()
		curSelectCodigo.execute(sqlSelectCodigo)
		codigo = curSelectCodigo.fetchall()
		
		if codigo == []:
			codigo = 1
		else:
			codigo = len(codigo) + 1

		curSelectCodigo.close()
		conn.close()
			
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	serveReceita = int(serveReceita)
	validadeReceita = int(validadeReceita)

	ingredientesReceita = list()
	for ingrediente in conteudoListBox:
		ingredienteLista = ingrediente.split(" - ")
		ingredienteLista[0] = ingredienteLista[0][:-1]
		ingredienteLista[2] = int(ingredienteLista[2])
		ingredientesReceita.append(ingredienteLista)
	listaReceita = [nomeReceita, serveReceita,validadeReceita,ingredientesReceita, modopreparo]

	receitas[codigo] = listaReceita

#INCLUI RECEITA NO BD
	try:
		conn = factoryconnection()

		sqlInsertReceitas = "Insert into receitas values (%s,%s,%s,%s,%s,%s)"
		curInsertReceitas = conn.cursor()
		curInsertReceitas.execute(sqlInsertReceitas,(codigo, loginuser, nomeReceita, serveReceita, validadeReceita, modopreparo))
		curInsertReceitas.close()
		conn.commit()

		sqlInsertReceitas_Ingredientes = "insert into receitas_ingredientes values(%s,%s,%s,%s)"
		curInsertReceitas_Ingredientes = conn.cursor()
		for ingrediente in ingredientesReceita:
			nomeIngrediente = ingrediente[0]
			medidaIngrediente = ingrediente[1]
			qtdIngrediente = ingrediente[2]
			curInsertReceitas_Ingredientes.execute(sqlInsertReceitas_Ingredientes,(codigo,nomeIngrediente,medidaIngrediente,qtdIngrediente))
		curInsertReceitas_Ingredientes.close()
		conn.commit()

		conn.close()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	
	aoFechar(janelaAnterior,janela, True)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#verifica informações e atualiza no banco
def alteraReceita(janela,receitas,janelaAnterior, loginuser, ReceitaKey):
	widgets = janela.winfo_children()
	nomeReceita = widgets[1].get(1.0, "end-1c")
	serveReceita = widgets[3].get(1.0, "end-1c")
	modopreparo = widgets[17].get(1.0, "end-1c")
	validadeReceita = widgets[6].get(1.0, "end-1c")
	conteudoListBox = widgets[9].get(0, END)

#VERIFICAÇÕES
	validaInteger(serveReceita)

	validaString(nomeReceita)

	validaString(modopreparo)

	validaInteger(validadeReceita)
	
	if(conteudoListBox == ()):
		return messagebox.showinfo("Cookner Notes   -   AVISO","Não há ingredientes na receita!")

	serveReceita = int(serveReceita)
	validadeReceita = int(validadeReceita)

	ingredientesReceita = list()
	for ingrediente in conteudoListBox:
		ingredienteLista = ingrediente.split(" - ")
		ingredienteLista[0] = ingredienteLista[0][0:len(ingredienteLista[0])-1]
		ingredienteLista[2] = int(ingredienteLista[2])
		ingredientesReceita.append(ingredienteLista)
	listaReceita = [nomeReceita, serveReceita,validadeReceita,ingredientesReceita, modopreparo]
	receitas[ReceitaKey] = listaReceita

#ATUALIZAÇÃO NO BD
	try:
		conn = factoryconnection()

		sqlUpdateReceitas = f"update receitas set nome = {'%s'}, serve = {'%s'}, validade = {'%s'} , modo_preparo = {'%s'} where codigo = {'%s'} and fk_USUARIO_login = '{loginuser}'"
		curUpdateReceitas = conn.cursor()
		curUpdateReceitas.execute(sqlUpdateReceitas,(nomeReceita,serveReceita,validadeReceita,modopreparo,ReceitaKey))
		curUpdateReceitas.close()
		conn.commit()

		sqlDeleteReceitas_Ingredientes = f"delete from receitas_ingredientes where fk_receitas_codigo = '{ReceitaKey}'"
		curDeleteReceitas_Ingredientes = conn.cursor()
		curDeleteReceitas_Ingredientes.execute(sqlDeleteReceitas_Ingredientes)
		curDeleteReceitas_Ingredientes.close()
		conn.commit()

		sqlInsertReceitas_Ingredientes = "insert into receitas_ingredientes values(%s,%s,%s,%s)"
		curInsertReceitas_Ingredientes = conn.cursor()
		for ingrediente in ingredientesReceita:
			nomeIngrediente = ingrediente[0]
			medidaIngrediente = ingrediente[1]
			qtdIngrediente = ingrediente[2]
			curInsertReceitas_Ingredientes.execute(sqlInsertReceitas_Ingredientes,(ReceitaKey,nomeIngrediente,medidaIngrediente,qtdIngrediente))
		curInsertReceitas_Ingredientes.close()
		conn.commit()

		conn.close()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	aoFechar(janelaAnterior,janela, True)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#exclui receita no banco de dados
def excluiReceita(janela,receitas,janelaAnterior, loginuser, ReceitaKey):

	widgets = janela.winfo_children()

	del receitas[ReceitaKey]

	try:
		conn = factoryconnection()

		comboBoxSelecNome = widgets[1].get()
		sqlDeleteReceitas_Ingredientes = f"delete from receitas_ingredientes where fk_receitas_codigo = '{ReceitaKey}'"
		curDeleteReceitas_Ingredientes = conn.cursor()
		curDeleteReceitas_Ingredientes.execute(sqlDeleteReceitas_Ingredientes)
		curDeleteReceitas_Ingredientes.close()
		conn.commit()

		sqlDeleteReceitas = f"delete from receitas where codigo ='{ReceitaKey}' and  fk_USUARIO_login = '{loginuser}'"
		curDeleteReceitas = conn.cursor()
		curDeleteReceitas.execute(sqlDeleteReceitas, loginuser)
		curDeleteReceitas.close()
		conn.commit()

		conn.close()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	aoFechar(janelaAnterior,janela, True)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# FUNÇÕES RELACIONADAS A INGREDIENTES ABAIXO - FUNÇÕES RELACIONADAS A INGREDIENTES ABAIXO -  FUNÇÕES RELACIONADAS A INGREDIENTES ABAIXO -  FUNÇÕES RELACIONADAS A INGREDIENTES ABAIXO


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#adiciona informações do ingrediente na listbox
def adicionaIngrediente(janela):
	widgets = janela.winfo_children()
	nomeIngrediente = widgets[11].get(1.0,END)
	medidaIngrediente = widgets[15].get()
	qtdIngrediente = widgets[13].get()

#VERIFICA AS INFORMAÇÕES
	validaString(nomeIngrediente)
		
	validaInteger(qtdIngrediente)

#INSERE NA LISTBOX
	widgets[9].insert(END,nomeIngrediente+" - "+medidaIngrediente+" - "+qtdIngrediente)

	widgets[11].delete(1.0,END)
	widgets[13].delete(0, END)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#atualiza ingrediente na listbox
def AlteraIngrediente(janela):
	widgets = janela.winfo_children()
	nomeIngrediente = widgets[11].get(1.0, END)
	medidaIngrediente = widgets[15].get()
	qtdIngrediente = widgets[13].get()

#VERIFICA AS INFORMAÇÕES
	validaString(nomeIngrediente)
		
	validaInteger(qtdIngrediente)

	if(widgets[9].curselection() == ()):
		return messagebox.showinfo("Cookner Notes   -   AVISO","Nenhum ingrediente foi selecionado!")

#ATUALIZA NA LISTBOX
	selecionado = widgets[9].curselection()
	widgets[9].delete(selecionado)
	widgets[9].insert(selecionado, nomeIngrediente +" - "+medidaIngrediente+" - "+qtdIngrediente)

#LIMPA CAIXAS DE TEXTO
	widgets[11].delete(1.0,END)
	widgets[13].delete(0, END)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#exclui ingrediente da listbox
def excluiIngrediente(janela):
	
	widgets = janela.winfo_children()

	if (widgets[9].curselection() == ()):
		return messagebox.showinfo("Cookner Notes   -   AVISO","Nenhum ingrediente foi selecionado!")

	widgets[9].delete(widgets[9].curselection())
	widgets[11].delete(1.0,END)
	widgets[15].current(0)
	widgets[13].delete(0, END)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# FUNCOES RELACIONADAS A SENHA ABAIXO - FUNCOES RELACIONADAS A SENHA ABAIXO - FUNCOES RELACIONADAS A SENHA ABAIXO - FUNCOES RELACIONADAS A SENHA ABAIXO - FUNCOES RELACIONADAS A SENHA ABAIXO


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#atualiza label a cada segundo
def atualizalabel(count, janela, receitas):
	label = Label(janela, text = count, width=4)
	label.place(x=260, y=70)
	if count > 0:
		janela.after(1000, atualizalabel, count-1, janela, receitas)
		
	else:
		janela.destroy()
		Interfaces.entrar(receitas)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#verifica login
def recuperarsenha(janela, receitas):
	widgets = janela.winfo_children()
	login = widgets[2].get(1.0,  "end-1c")

	validaString(login)

	conn = factoryconnection()
	sql = "select * from usuario"
	cur = conn.cursor()
	cur.execute(sql)
	usuarios = cur.fetchall()

	dic = {}
	for usuario in usuarios:
		pergunta = usuario[2].split('-')
		dic[usuario[0]] = pergunta[0]
	
	cur.close()
	conn.close()

	if(login in dic):
		janela.withdraw()
		return Interfaces.recuperandosenha(login, dic[login], receitas, janela)

	else:
		return messagebox.showinfo("Cookner Notes   -   AVISO","Este login não existe")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#verifica palavra-chave e mostra a senha
def recuperasenha(login, janela, receitas):
	widgets = janela.winfo_children()
	palavra = widgets[2].get(1.0,  "end-1c")

#VERIFICAÇAO
	validaString(palavra)

	conn = factoryconnection()
	sql = "select * from usuario"
	cur = conn.cursor()
	cur.execute(sql)
	usuarios = cur.fetchall()

	for usuario in usuarios:
		if usuario[0] == login:
			senha = usuario[1]
			pergunta = usuario[2].split('-')
#MOSTRA A SENHA
			if palavra == pergunta[1]:
				janela.withdraw()
				return Interfaces.mostrasenha(login, senha, janela, receitas)
			else:
				return messagebox.showinfo("Cookner Notes   -   AVISO","Palavra-chave errada")
		
	cur.close()
	conn.close()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#atualiza senha
def mudasenha(login, janela,receitas):
	widgets = janela.winfo_children()
	senha = widgets[1].get()
	confirmacao = widgets[3].get()

#VERIFICAÇÃO DA SENHA
	validaString(senha)

	validaString(confirmacao)

	if(senha == confirmacao):

#ATUALIZA NO BD
		try:
			conn = factoryconnection()

			sqlUpdateReceitas = f"update usuario set senha = {'%s'} where login = {'%s'}"
			curUpdateReceitas = conn.cursor()
			curUpdateReceitas.execute(sqlUpdateReceitas,(senha, login))
			curUpdateReceitas.close()
			conn.commit()
			conn.close()

		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
	else:
		return messagebox.showinfo("Cookner Notes   -   AVISO","Confirmação inválida")
	janela.destroy()
	messagebox.showinfo("Cookner Notes   -   AVISO","Senha Atualizada")
	return Interfaces.entrar(receitas)
	
	
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# FUNCOES DIVERSAS ABAIXO - FUNCOES DIVERSAS ABAIXO - FUNCOES DIVERSAS ABAIXO - FUNCOES DIVERSAS ABAIXO - FUNCOES DIVERSAS ABAIXO - FUNCOES DIVERSAS ABAIXO - FUNCOES DIVERSAS ABAIXO

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#mostra avisos e fecha janelas
def aoFechar(janelaAnterior,janelaAtual,flag):

	if (janelaAtual.title()  == "Cookner Notes   -   CADASTRAR RECEITAS" and flag):
		messagebox.showinfo("Cookner Notes   -   AVISO","Receita registrada com sucesso")
		janelaAnterior.deiconify()
		janelaAtual.destroy()
	elif (janelaAtual.title() == "Cookner Notes   -   EDITAR RECEITA" and flag):
		messagebox.showinfo("Cookner Notes   -   AVISO","Receita alterada com sucesso")
		janelaAnterior.deiconify()
		janelaAtual.destroy()
	elif (janelaAtual.title() == "Cookner Notes   -   ALTERAR RECEITAS" and flag):
		messagebox.showinfo("Cookner Notes   -   AVISO","Receita excluida com sucesso")
		janelaAnterior.deiconify()
		janelaAtual.destroy()
	elif ( janelaAtual.title() == "Cookner Notes   -   CADASTRA USUARIO" and flag):
		messagebox.showinfo("Cookner Notes   -   AVISO","Usuario cadastrado com sucesso")
		janelaAnterior.deiconify()
		janelaAtual.destroy()
	else: 
		resposta = messagebox.askokcancel("Cookner Notes   -   FECHAR", "Você deseja fechar a janela atual?")
		if(resposta):
			janelaAnterior.deiconify()
			janelaAtual.destroy()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#conexao com o banco de dados
def factoryconnection():
	
	try:
		conn = psycopg2.connect(
		host="kesavan.db.elephantsql.com",
		database="nmhzdful",
		user="nmhzdful",
		password="QnKW9RUERK4L0RCosalwQ7uIcvhBR5yn")
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	return conn

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#
def eventoSelecaoListBox(janela, evt):

	widgets = janela.winfo_children()

	if(widgets[9].curselection() == ()):
		return

	widgets[11].delete(1.0,END)
	widgets[13].delete(0, END)

	ingrediente = widgets[9].get(widgets[9].curselection())
	ingredienteLista = ingrediente.split(" - ")
	widgets[11].insert(1.0,ingredienteLista[0][0:len(ingredienteLista[0])-1])
	qtd = int(ingredienteLista[2])
	qtd = str(qtd)
	widgets[13].insert(0,qtd)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#verifica se informação é inteira/float
def validaInteger(string):

	try:
		float(string)
	except ValueError:
		messagebox.showinfo("Cookner Notes   -   AVISO","Os campos não foram preenchidos corretamente!")
		raise Exception
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#verifica se campo está vazio
def validaString(string):

	naoEstaVazio = string != " " and string != "\n" and string != ""

	if(not naoEstaVazio):
		messagebox.showinfo("Cookner Notes   -   AVISO","Os campos não foram preenchidos corretamente!")
		raise Exception
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#extrai informações do bd e adiciona no sistema
def inicializa(receitas, loginuser):

#VARREDURA NO BD
	try:
		conn = factoryconnection()
		sql = f"select * from receitas where fk_USUARIO_login = '{loginuser}'"
		cur = conn.cursor()
		cur.execute(sql, (loginuser))
		receitasSet = cur.fetchall()
		
		sql1 = "select * from receitas_ingredientes"
		cur1 = conn.cursor()
		cur1.execute(sql1)
		ingredientesSet = cur1.fetchall()

#ATRIBUIÇÃO DAS INFROMAÇÕES NO SISTEMA
		for receita in receitasSet:
			codigoReceita = receita[0]
			nomeReceita = receita[2]
			serveReceita = receita[3]
			validadeReceita = receita[4]
			modoPreparoReceita = receita[5]

			listaIngredientesReceita = list()
			for ingrediente in ingredientesSet:
				if(ingrediente[0] == codigoReceita):
					nomeIngrediente = ingrediente[1]
					medidaIngrediente = ingrediente[2]
					qtdIngrediente = ingrediente[3]
					ingrediente = [nomeIngrediente,medidaIngrediente,qtdIngrediente]
					listaIngredientesReceita.append(ingrediente)

			receitas[codigoReceita] = [nomeReceita, serveReceita, validadeReceita, listaIngredientesReceita, modoPreparoReceita]
			listaIngredientesReceita = list()
			ingrediente = list()
		cur.close()
		cur1.close()
		conn.close()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)