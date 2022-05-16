# Os testes aqui feitos tem como objetivo testar algumas extensões do VSCode


#_________________________________________Python Preview _________________________________________________
# Aqui temos Python Preview - onde podemos ter uma noção visual do funcionamento de nosso código
# Para acessar, basta clicar com o botão direito do mouse em cima do documento .py
# e clicar em Open Preview to the Side
nome = "Marcus"

nomes = [nome, nome, nome]

y = nomes


def foo(x):
    y = 1
    return x


z = foo(7)

# _____________________________________________AUTODOCSTRING__________________________________________
# Você deve utilizar 3 aspas simples ou duplas e depois aplicar CTRL + SHIFT + 2
# Teoricamente você pode ir indo de parte em parte utilizando TAB, ainda não consegui fazer funcionar
# https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring


def soma(a, b):
    """_summary_

    Args:
            a (_type_): _description_
            b (_type_): _description_
            """

    return(a+b)


# ___________________________________Python Test Explorer___________________________________________________________
# Utilizar para fazer Debug - funciona melhor com Pytest
# É uma forma melhor de utilizar o DEBUG e entender o que estaria errado durante o seu código


#__________________________________________Pyright__________________________________________________________
# Um forma de você fazer anoptações em Python, principalmente quanto ao tipo da variável: int, strm float
# Essas anotações feitas no código evitam que você faça algum engano e auxiliam na identificação de 
# em um futuro erro, além disso elas não afetam o seu código

 from typing import Dict

 products: Dict[str, int] = {}

 def multiplication(a:int, b:int) -> int:
	 return(a*b)
	
products["Teclado"] = "23"
#_____________________________________________________________________________________________________

