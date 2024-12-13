import json

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        print(f"{self.nome} Ataca {inimigo.nome} e Causa {self.ataque} de Dano!")

    def __str__(self):
        return f"{self.nome} {self.vida}"
    

class Guerreiro(Personagem):
    def especial(self, inimigo):
        dano_especial = 30
        inimigo.vida -= dano_especial
        print(f"{self.nome} usa Golpe Poderoso em {inimigo.nome} e Causa {dano_especial} de Dano!")

class Mago(Personagem):
    def especial(self):
        cura = 25
        self.vida += cura
        print(f"{self.nome} usa Cura e Ganha {cura} Pontos de Vida!")

class Arqueiro(Personagem):
    def especial(self, inimigos):
        dano_especial = 15
        for inimigo in inimigos:
            if inimigo != self:
                inimigo.vida -= dano_especial
        print(f"{self.nome} usa Chuva de Flechas e Causa {dano_especial} de Dano a Todos os Inimigos!")

def importar_personagens(caminho):
    with open(caminho, "r") as file:
        percs = json.load(file)

    personagens = []
    for perc in percs:
        classe = perc['classe']
        if classe == 'Guerreiro':
            personagens.append(Guerreiro(perc['nome'], perc['vida'], perc['ataque']))
        elif classe == 'Mago':
            personagens.append(Mago(perc['nome'], perc['vida'], perc['ataque']))
        elif classe == 'Arqueiro':
            personagens.append(Arqueiro(perc['nome'], perc['vida'], perc['ataque']))

    return personagens, len(personagens)

def ordenar_personagens_por_vida(personagens):
    return sorted(personagens, key=lambda p: p.vida)

personagens, num_personagens = importar_personagens('personagens.json')
print(f"{num_personagens} Personagens Entram em Batalha!")

personagens = ordenar_personagens_por_vida(personagens)

print(personagens[0])
print(personagens[1])
print(personagens[2])

personagens[0].atacar(personagens[1])
print(personagens[1])

personagens[1].atacar(personagens[2])
print(personagens[2])

personagens[2].atacar(personagens[0])
print(personagens[0])

personagens[0].especial()
print(personagens[0])

personagens[1].especial([personagens[0], personagens[1]])
print(personagens[0])
print(personagens[1])

personagens[2].especial(personagens[1])
print(personagens[1])