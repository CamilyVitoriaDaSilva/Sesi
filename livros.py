import pandas as pd

dado = pd.read_csv("tabeladelivros.csv")

print(dado)

class Livro:
   def __init__(self, titulo, autor, categoria, ano, ativo):
       self, titulo = titulo
       self.categoria = categoria
       self.ano = ano
       self.ativo = ativo
       self.autor = autor
       
livro0 = Livro("Livro 0", "camily", "progração", 2012,"Sim")
livro1 = Livro("Livro 1", "camily", "progração", 2012,"Sim")
livro2 = Livro("Livro 2", "camily", "progração", 2012,"Sim")
lista_de_livros = [livro0, livro1, livro2]

for livro in lista_de_livros:
    print(livro.titulo)
   