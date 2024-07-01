pip install Django
class Usuario:
    def __init__(self, nome, idade, senha):
        self.nome = nome
        self.idade = idade
        self.senha = senha
        self.biblioteca = []
        self.dicionario = {}
        self.figurinhas = 0

    def adicionar_livro(self, livro):
        self.biblioteca.append(livro)
        self.figurinhas += 1
        print("Livro adicionado à sua biblioteca!")

    def adicionar_palavra(self, palavra, significado):
        self.dicionario[palavra] = significado
        print("Palavra adicionada ao seu dicionário!")

    def ver_lista_de_livros(self):
        if not self.biblioteca:
            print("Sua biblioteca está vazia.")
        else:
            print("Sua Biblioteca de Livros:")
            for livro in self.biblioteca:
                print(f"Nome: {livro['Nome']}, Autor: {livro['Autor']}, Nota: {livro['Nota']}")

    def ver_lista_de_palavras(self):
        if not self.dicionario:
            print("Seu dicionário está vazio.")
        else:
            print("Seu Dicionário de Palavras:")
            for palavra, significado in self.dicionario.items():
                print(f"Palavra: {palavra}, Significado: {significado}")

class BibliotecaVirtual:
    def __init__(self):
        self.usuarios = {}
        self.usuario_logado = None

    def cadastrar_usuario(self, nome, idade, senha):
        if nome not in self.usuarios:
            self.usuarios[nome] = Usuario(nome, idade, senha)
            print("Usuário cadastrado com sucesso!")
        else:
            print("Nome de usuário já existe. Escolha outro nome.")

    def fazer_login(self, nome, senha):
        if nome in self.usuarios and self.usuarios[nome].senha == senha:
            self.usuario_logado = self.usuarios[nome]
            print("Login bem-sucedido.")
        else:
            print("Nome de usuário ou senha incorretos.")

    def menu_principal(self):
        while True:
            if self.usuario_logado:
                print("\n=== Biblioteca Virtual ===")
                print("1. Adicionar Livro")
                print("2. Ver Lista de Livros")
                print("3. Adicionar Palavra")
                print("4. Ver Lista de Palavras")
                print("5. Sair (Logout)")
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    nome_livro = input("Nome do livro: ")
                    autor = input("Autor: ")
                    nota = input("Nota para o livro (de 0 a 10): ")
                    livro = {
                        "Nome": nome_livro,
                        "Autor": autor,
                        "Nota": nota
                    }
                    self.usuario_logado.adicionar_livro(livro)
                elif escolha == "2":
                    self.usuario_logado.ver_lista_de_livros()
                elif escolha == "3":
                    palavra = input("Palavra: ")
                    significado = input("Significado: ")
                    self.usuario_logado.adicionar_palavra(palavra, significado)
                elif escolha == "4":
                    self.usuario_logado.ver_lista_de_palavras()
                elif escolha == "5":
                    print("Logout bem-sucedido.")
                    self.usuario_logado = None
                else:
                    print("Opção inválida. Tente novamente.")
            else:
                print("\n=== Biblioteca Virtual ===")
                print("1. Cadastro")
                print("2. Login")
                print("3. Sair")
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    nome = input("Nome de usuário: ")
                    idade = input("Idade: ")
                    senha = input("Senha: ")
                    self.cadastrar_usuario(nome, idade, senha)
                elif escolha == "2":
                    nome = input("Nome de usuário: ")
                    senha = input("Senha: ")
                    self.fazer_login(nome, senha)
                elif escolha == "3":
                    print("Saindo da Biblioteca Virtual. Até logo!")
                    break
                else:
                    print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    biblioteca = BibliotecaVirtual()
    biblioteca.menu_principal()