import os
from models import db, Editor, Riddle, Avaliacao, criptografar_senha
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Inicializa banco de dados SQLite
DATABASE_URL = 'sqlite:///riddles.db'
engine = create_engine(DATABASE_URL)
db.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_inicial():
    limpar_tela()
    print("--- RIDDLES APP ---")
    print("1. Login")
    print("2. Criar novo usuário")
    print("3. Resetar senha")
    print("4. Sair")
    return input("Escolha uma opção: ")


def login():
    nome = input("Nome: ")
    senha = input("Senha: ")
    editor = session.query(Editor).filter_by(nome=nome).first()
    if editor:
        if editor.senha == criptografar_senha(senha):
            print("Login realizado com sucesso!")
            return editor
        else:
            print("Senha incorreta.")
    else:
        print("Usuário não encontrado.")
    return None


def criar_usuario():
    nome = input("Nome: ")
    if session.query(Editor).filter_by(nome=nome).first():
        print("Usuário já existe.")
        return
    senha = input("Senha: ")
    novo_editor = Editor(nome=nome, senha=criptografar_senha(senha))
    session.add(novo_editor)
    session.commit()
    print("Usuário criado com sucesso!")


def resetar_senha():
    nome = input("Nome do usuário: ")
    editor = session.query(Editor).filter_by(nome=nome).first()
    if editor:
        nova_senha = input("Digite a nova senha: ")
        editor.senha = criptografar_senha(nova_senha)
        session.commit()
        print("Senha atualizada com sucesso!")
    else:
        print("Usuário não encontrado.")


if __name__ == '__main__':
    while True:
        opcao = menu_inicial()

        if opcao == '1':
            usuario = login()
            if usuario:
                # Aqui vamos depois mostrar o menu principal do sistema
                input("Pressione Enter para continuar...")
        elif opcao == '2':
            criar_usuario()
            input("Pressione Enter para continuar...")
        elif opcao == '3':
            resetar_senha()
            input("Pressione Enter para continuar...")
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
            input("Pressione Enter para tentar novamente...")
