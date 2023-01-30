from random import randint # aleatório

# Aceitar uma entrada dizendo quantos números o jogador quer fazer por jogo
# Aceitar uma entrada dizendo quantos jogos ao todo o jogador quer gerar
# Os jogos devem ser gerados em ordem crescente


class MegaSena():
    def __init__(self, qtde_jogos: int, qtde_numeros_por_jogo: int) -> None: # Inicializador
        self.qtde_jogos = qtde_jogos
        self.qtde_numeros_por_jogo = qtde_numeros_por_jogo

    def gerar_numeros_mega_sena(self):
        qtde_jogos = self.qtde_jogos
        qtde_numeros_por_jogo = self.qtde_numeros_por_jogo

        if (qtde_numeros_por_jogo < 6 or qtde_numeros_por_jogo > 15):
            raise("Um jogo da mega sena não pode ter menos que 6 numeros e mais do que 15 números")

        num_jogo_atual = 1
        lista_jogos = []
        while num_jogo_atual <= qtde_jogos: # Enquanto nao gerei todos jogos que foram pedidos, rode comandos abaixo
            posicao_numero_atual = 1 # Inicializando que devo começar o jogo pela posicao 1
            meu_jogo_atual = []
            while posicao_numero_atual <= qtde_numeros_por_jogo: # Gera os números dos jogos
                meu_numero_gerado = randint(1, 60) # Gera um número aleatório entre 1 e 60
                if meu_numero_gerado not in meu_jogo_atual: # Valida se o número gerado já não foi gerado anteriormente para o jogo
                    meu_jogo_atual.append(meu_numero_gerado) # caso o número nao seja repetido ira inseri-lo a uma lista para o jogo
                    posicao_numero_atual += 1 # incrementar a posição do número gerado

            meu_jogo_atual.sort() # Ordena os números de forma crescente
            if meu_jogo_atual not in lista_jogos: # Valida que o jogo gerado não está duplicado com nenhum jogo anterior
                lista_jogos.append(meu_jogo_atual)
                num_jogo_atual += 1
    
        return lista_jogos


app = MegaSena(5, 6)
resultado = app.gerar_numeros_mega_sena()

for jogo in resultado:
    print(jogo)