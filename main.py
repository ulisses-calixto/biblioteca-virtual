class Pessoa:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    def exibir_detalhes (self):
        pass

class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)
        self.livros_emprestados = []
    
    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) >= 3:
            print(f"{self.nome} já atingiu o limite de 3 livros.")
        elif not livro.disponivel:
            print(f"O livro '{livro.titulo}' não está disponível.")
        else:
            self.livros_emprestados.append(livro)
            livro.disponivel = False
            print(f"O livro {livro.titulo} foi emprestado para {self.nome}.")

    def devolucao_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.disponivel = True
            print("O livro {} foi devolvido por {}.".format(livro.titulo, self.nome))
        else:
            print("{} não devolveu o livro {}.".format(self.nome, livro.titulo))

    def exibir_detalhes(self):
        livros_emprestados = [livro.titulo for livro in self.livros_emprestados]
        return "Usuário: {} - Idade: {} - Matricula: {} - Livros Emprestados: {}".format(self.nome, self.idade, self.matricula, livros_emprestados)
    
class Admin(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)
        self.usuarios = []
        self.livros = []

    def cadastro_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuário(a) {usuario.nome} cadastrado(a) com sucesso!")

    def cadastro_livros(self, livro):
        self.livros.append(livro)
        print(f"Livro {livro.titulo} cadastrado com sucesso!")

    def relatorio_livros(self):
        print("\nLivros Disponíveis:")
        for livro in self.livros:
            print(f"{livro.exibir_detalhes()}")

    def relatorio_usuarios(self):
        print("\nUsuários que possuem livros emprestados:")
        for usuario in self.usuarios:
            print(f"{usuario.exibir_detalhes()}")
    
    def exibir_informacoes(self):
        print("Administrador: {}, Matricula: {}".format(self.nome, self.matricula))


class ItemBiblioteca:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def exibir_detalhes(self):
        pass

class Livro(ItemBiblioteca):
    def exibir_detalhes(self):
        if self.disponivel: 
            situacao = "Disponível" 
        else:
            situacao = "Emprestado"
        return "Livro: {} - Autor: {} - Status: {}".format(self.titulo, self.autor, situacao)
    
#nomeação-adm
adm = Admin("Ulisses", 20, "ADM01")

#cadastro-users
usuario01 = UsuarioComum("Gabriel", 24, "UC01")
adm.cadastro_usuario(usuario01)

usuario02 = UsuarioComum("Luisa", 27, "UC02")
adm.cadastro_usuario(usuario02)

#cadastro-books
livro01 = Livro("Dom Casmurro", "Machado de Assis")
adm.cadastro_livros(livro01)

livro02 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")
adm.cadastro_livros(livro02)

livro03 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling")
adm.cadastro_livros(livro03)

livro04 = Livro("Harry Potter e o Prisioneiro de Azkaban", "J. K. Rowling")
adm.cadastro_livros(livro04)

#emprestimos-devoluções
usuario01.emprestar_livro(livro01) #usuario1 empresta os livros 1, 2 e 3.
usuario01.emprestar_livro(livro02)
usuario01.emprestar_livro(livro03)
usuario01.emprestar_livro(livro04) #usuario1 recebe o alerta de que já atingiu o número máximo de livros emprestados.

usuario02.emprestar_livro(livro01) #usuario2 tenta emprestar o livro1 já emprestado.

usuario01.devolucao_livro(livro01) #usuario1 devolve o livro1, possibilitando agora, ao usuario2, emprestar o livro1.
usuario02.emprestar_livro(livro01)

#depois disso os relatórios
adm.relatorio_livros()
adm.relatorio_usuarios()
