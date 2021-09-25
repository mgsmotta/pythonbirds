# -*- coding: utf-8 -*-

class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos) # Atributo COMPLEXO

    def cumprimentar(self):
        return f'Olá! {id(self)}'


if __name__ == '__main__':
    mario = Pessoa(nome ='Mario')
    sylvio = Pessoa(mario, nome ='Sylvio')
    print(Pessoa.cumprimentar(sylvio))
    print(id(sylvio))
    print(sylvio.cumprimentar())
    print(sylvio.nome)
    print(sylvio.idade)
    for filho in sylvio.filhos:
        print(filho.nome)
    # Atributo Dinâmico sobrenome (não está na definição do dander init do objeto sylvio da classe Pessoa)
    sylvio.sobrenome = 'Motta'
    print(sylvio.__dict__)
    print(mario.__dict__)
    # Remove um atributo de um objeto
    del sylvio.filhos
    print(sylvio.__dict__)

