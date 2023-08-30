import os
import time


contatos = []


def tela():
    opcao = 10
    while opcao < 0 or opcao > 4:
        os.system("cls")
        print("***** AGENDA TELEFONICA *****")
        print('\nInforme a opção desejada: ')
        print('(1) Inserir um novo contato')
        print('(2) Exibir a lista de contatos')
        print('(3) Editar um contato')
        print('(4) Remover um contato')
        print('(0) SAIR')
        print('\n***************************')
        options()


def inserir_contato():
    os.system("cls")
    novo_contato = []
    print('***** INSERIR UM NOVO CONTATO *****')
    nome = input("Informe o nome: ")
    telefone = input("Informe o telefone:")
    novo_contato.append(nome)
    novo_contato.append(telefone)
    contatos.append(novo_contato)
    print('Contato adicionado com sucesso!\n')
    print('***************************\n')


def mostrar_contatos():
    contador=0
    os.system("cls")
    print('\n ***** CONTATOS CADASTRADOS *****')
    print('Nº:   NOME / NUMERO')
    for elementos in contatos:
        print(contador + 1, ":", elementos)
        contador = contador + 1
    print('\n***************************\n')


def editar_contato():
    contador = 0
    edit_contato = []
    os.system("cls")
    print('***** EDITAR UM CONTATO *****')
    print('Nº:   NOME / NUMERO')
    for elementos in contatos:
        print(contador + 1, ":", elementos)
        contador = contador + 1
    qual = int(input("\nInforme o contato que deseja editar:"))
    if qual-1 < len(contatos):
        nome = input("Informe o nome: ")
        telefone = input("Informe o telefone:")
        edit_contato.append(nome)
        edit_contato.append(telefone)
        contatos[qual - 1] = edit_contato
        print('Contato editado com sucesso!\n')
        print('***************************\n')
    else:
        print("Contato Inexistente!")
        print('***************************\n')


def remover_contato():
    contador = 0
    os.system("cls")
    print('***** REMOVER UM CONTATO ***** ')
    for elementos in contatos:
        print(contador + 1, ":", elementos)
        contador = contador + 1
    qual = int(input("\nInforme o contato que deseja remover:"))
    if qual-1 < len(contatos):
        contatos.pop(qual - 1)
        print("Contato removido com sucesso!\n")
        print('***************************\n')
    else:
        print("Contato Inexistente!")
        print('***************************\n')


def options():
    opcao = int(input("\nInforme a opção desejada: "))
    if opcao == 1:
        inserir_contato()
        time.sleep(2)
        tela()
    if opcao == 2:
        mostrar_contatos()
        time.sleep(5)
        tela()
    if opcao == 3:
        editar_contato()
        time.sleep(2)
        tela()
    if opcao == 4:
        remover_contato()
        time.sleep(2)
        tela()
    if opcao == 0:
        exit()
    

print(tela())