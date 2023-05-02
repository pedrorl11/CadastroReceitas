#---------------------------------------------------------------------------------------------------------------------------------------------------
# ANOTAÇÕES ABAIXO - ANOTAÇÕES ABAIXO - ANOTAÇÕES ABAIXO - ANOTAÇÕES ABAIXO - ANOTAÇÕES ABAIXO - ANOTAÇÕES ABAIXO - ANOTAÇÕES ABAIXO - ANOTAÇÕES ABAIXO -
#---------------------------------------------------------------------------------------------------------------------------------------------------

'''
- manual com todas funções:
    #funcao cadastrar usuario
        verificamos se o login, a senha e a resposta da pergunta selecionada foram preenchidas
        verificamos se a senha foi conferida corretamente
        verificamos se o login já existe no banco de dados
        inserimos os valores no banco de dados

    #funcao de recuperar senha
        verificamos se o login foi preenchido e existe no banco de dados
        inserimos a pergunta escolhida pelo usuario no momento de cadastro
        verificamos se a resposta da pergunta foi preenchida e se ela corresponde à mesma cadastrada
        informamos a senha do usuario dando a opção de alterá-la
        verificamos se os campos de senha foram preenchidos e se foram confirmados corretamente, atualizamos a senha
    
    #funcao de alterar senha
        verificamos se os campos foram preenchidos
        verificamos se a senha foi confirmada corretamente
        atualizamos a senha

    #funcao de conferir login
        verificamos se o login realmente existe no banco de dados
        verificamos se a senha informada corresponde a senha cadastrada para aquele login
        caso o usuário informe a senha errada 5 vezes ele fica bloqueado durante 60 segundos de tentar entrar no sistema
        após informar a senha correta abrimos o menu de gerenciamento de receitas

    #funcao inicializa
        adicionamos as informações guardadas no banco de dados no sistema

    #funcao de cadastra receita
        - adicionareceita
          verificamos se os dias de validade e qtd pessoas serve são inteiros ou floats(usando .) e preenchidos
          verificamos se o nome da receita e o modo de preparo são strings e preenchidos
          verificamos se o usuario cadastrou ingredientes para receita
          cadastramos a receita e os ingredientes no banco de dados

        - adicionaIngrediente
          verificamos se a qtd do ingrediente usada é inteiro ou floats(usando .) e preenchida
          verificamos se o nome do ingrediente é string e foi preenchido
          inserimos as informações do ingrediente em uma list

        - excluiIngrediente
          excluimos o ingrediente selecionado

        - alteraIngrediente
          verificamos se a qtd do ingrediente usada é inteiro ou floats(usando .) e preenchida
          verificamos se o nome do ingrediente é string e foi preenchido
          verificamos se um ingrediente foi selecionado
          atualizamos as informações do ingrediente selecionado na list

    #funcao de editar receita
        - exclui receita
          excluimos a receita selecionada do banco de dados

        - altera receita selecionada
          verificamos se os dias de validade e qtd pessoas serve atualizados são inteiros ou floats(usando .) e preenchidos
          verificamos se o modo de preparo é string e foi preenchido
          verificamos se o usuario cadastrou ingredientes para receita
          atualizamos os dados da receita e dos ingredientes no banco de dados

    #funcao de consultar receita
        verificamos se existe receita cadastrada para aquele login
        mostramos as informações da receita selecionada pelo usuário
    
    #funcao de fechar janelas ao apertar no x voltando para janela anterior

'''
#código de nosso Banco de Dados
'''
drop table if exists receitas, receitas_ingredientes, usuario;

create table usuario(
login varchar(50) primary key,
senha varchar(30),
palavra_chave varchar(30)
);

create table receitas(
codigo integer primary key,
fk_USUARIO_login varchar(50) references usuario(login),
nome varchar(50),
serve integer,
validade integer,
modo_preparo varchar(200)
);

create table receitas_ingredientes(
fk_RECEITAS_codigo integer references receitas(codigo),
nome_ingrediente varchar(50),
medida_ingrediente varchar(50),
qtd_ingrediente integer
);
'''
