# -*- coding: utf-8 -*-

class Pessoa:
    olhos = 2  # atributo default ou atributo de classe

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)  # Atributo COMPLEXO

    def cumprimentar(self):
        return f'Olá! {id(self)}'


if __name__ == '__main__':
    mario = Pessoa(nome='Mario')
    sylvio = Pessoa(mario, nome='Sylvio')
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(sylvio.olhos)
    print(mario.olhos)
    print(id(Pessoa.olhos), id(sylvio.olhos), id(mario.olhos))
