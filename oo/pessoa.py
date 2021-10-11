# -*- coding: utf-8 -*-

class Pessoa:
    olhos = 2  # atributo default ou atributo de classe

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)  # Atributo COMPLEXO

    def cumprimentar(self):
        return f'Olá! meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    mario = Mutante(nome='Mario')
    sylvio = Homem(mario, nome='Sylvio')
    print(Pessoa.cumprimentar(sylvio))
    print(id(sylvio))
    print(sylvio.cumprimentar())
    print(sylvio.nome)
    print(sylvio.idade)

    for filho in sylvio.filhos:
        print(filho.nome)
    # Atributo Dinâmico sobrenome (não está na definição do dander init do objeto sylvio da classe Pessoa)
    sylvio.sobrenome = 'Motta'
    # Remove um atributo de um objeto
    del sylvio.filhos
    sylvio.olhos = 1
    del sylvio.olhos
    print(sylvio.__dict__)
    print(mario.__dict__)
    print(Pessoa.olhos)
    print(sylvio.olhos)
    print(mario.olhos)
    print(id(Pessoa.olhos), id(sylvio.olhos), id(mario.olhos))
    print(Pessoa.metodo_estatico(), sylvio.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), sylvio.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(mario, Pessoa))
    print(isinstance(mario, Homem))
    print(mario.olhos)
    print(sylvio.cumprimentar())
    print(mario.cumprimentar())