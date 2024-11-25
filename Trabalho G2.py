class Jogo:
    def _init_(self, jogo_id, titulo, desenvolvedor, preco, generos):
        self.jogo_id = jogo_id
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos 

class NoJogo:
    def _init_(self, jogo):
        self.jogo = jogo
        self.esquerda = None
        self.direita = None

class ArvoreJogos:
    def _init_(self):
        self.raiz = None

    def inserir(self, jogo):
        if self.raiz is None:
            self.raiz = NoJogo(jogo)
        else:
            self._inserir_recursivo(self.raiz, jogo)

    def _inserir_recursivo(self, no, jogo):
        if jogo.preco < no.jogo.preco:
            if no.esquerda is None:
                no.esquerda = NoJogo(jogo)
            else:
                self._inserir_recursivo(no.esquerda, jogo)
        else:
            if no.direita is None:
                no.direita = NoJogo(jogo)
            else:
                self._inserir_recursivo(no.direita, jogo)

    def buscar_por_preco(self, preco):
        return self._buscar_por_preco_recursivo(self.raiz, preco)

    def _buscar_por_preco_recursivo(self, no, preco):
        if no is None:
            return []
        elif no.jogo.preco == preco:
            return [no.jogo]
        elif preco < no.jogo.preco:
            return self._buscar_por_preco_recursivo(no.esquerda, preco)
        else:
            return self._buscar_por_preco_recursivo(no.direita, preco)

    def busca_por_faixa_preco(self, preco_minimo, preco_maximo):
        jogos = []
        self._busca_por_faixa_preco_recursivo(self.raiz, preco_minimo, preco_maximo, jogos)
        return jogos

    def _busca_por_faixa_preco_recursivo(self, no, preco_minimo, preco_maximo, jogos):
        if no is None:
            return
        if preco_minimo <= no.jogo.preco <= preco_maximo:
            jogos.append(no.jogo)
        if preco_minimo < no.jogo.preco:
            self._busca_por_faixa_preco_recursivo(no.esquerda, preco_minimo, preco_maximo, jogos)
        if preco_maximo > no.jogo.preco:
            self._busca_por_faixa_preco_recursivo(no.direita, preco_minimo, preco_maximo, jogos)

class HashGeneros:
    def _init_(self):
        self.genero_para_jogos = {}

    def adicionar_jogo(self, jogo):
        for genero in jogo.generos:
            if genero not in self.genero_para_jogos:
                self.genero_para_jogos[genero] = []
            self.genero_para_jogos[genero].append(jogo)

    def obter_jogos(self, genero):
        return self.genero_para_jogos.get(genero, [])

class MotorBuscaJogos:
    def _init_(self):
        self.catalogo_jogos = ArvoreJogos()
        self.generos = HashGeneros()

    def adicionar_jogo(self, jogo):
        self.catalogo_jogos.inserir(jogo)
        self.generos.adicionar_jogo(jogo)

    def buscar_por_preco(self, preco):
        return self.catalogo_jogos.buscar_por_preco(preco)

    def busca_por_faixa_preco(self, preco_minimo, preco_maximo):
        return self.catalogo_jogos.busca_por_faixa_preco(preco_minimo, preco_maximo)

    def buscar_por_genero(self, genero):
        return self.generos.obter_jogos(genero)

def menu():
    motor = MotorBuscaJogos()

    while True:
        print("\n--- Menu ---")
        print("1. Adicionar Jogo")
        print("2. Buscar Jogo por Preço")
        print("3. Buscar Jogo por Faixa de Preço")
        print("4. Buscar Jogo por Gênero")
        print("5. Sair")
        
        escolha = input("Escolha uma opção (1-5): ")

        if escolha == "1":
            jogo_id = int(input("Digite o ID do jogo: "))
            titulo = input("Digite o título do jogo: ")
            desenvolvedor = input("Digite o nome do desenvolvedor: ")
            preco = int(input("Digite o preço do jogo: "))
            generos = input("Digite os gêneros do jogo (separados por vírgula): ").split(",")
            generos = [genero.strip() for genero in generos] 

            jogo = Jogo(jogo_id, titulo, desenvolvedor, preco, generos)
            motor.adicionar_jogo(jogo)
            print(f"Jogo '{titulo}' adicionado com sucesso!")

        elif escolha == "2":
            preco = int(input("Digite o preço do jogo: "))
            jogos = motor.buscar_por_preco(preco)
            if jogos:
                print("Jogos encontrados:")
                for jogo in jogos:
                    print(f"{jogo.titulo} - R${jogo.preco}")
            else:
                print("Nenhum jogo encontrado com esse preço.")

        elif escolha == "3":
            preco_minimo = int(input("Digite o preço mínimo: "))
            preco_maximo = int(input("Digite o preço máximo: "))
            jogos = motor.busca_por_faixa_preco(preco_minimo, preco_maximo)
            if jogos:
                print("Jogos encontrados na faixa de preço:")
                for jogo in jogos:
                    print(f"{jogo.titulo} - R${jogo.preco}")
            else:
                print("Nenhum jogo encontrado nessa faixa de preço.")

        elif escolha == "4":
            genero = input("Digite o gênero do jogo: ")
            jogos = motor.buscar_por_genero(genero)
            if jogos:
                print(f"Jogos encontrados no gênero '{genero}':")
                for jogo in jogos:
                    print(f"{jogo.titulo} - R${jogo.preco}")
            else:
                print(f"Nenhum jogo encontrado no gênero '{genero}'.")

        elif escolha == "5":
            break

        else:
            print("Opção inválida!Escolha uma opção de 1 a 5.")

menu()


# ID: 1  
# Título: The Witcher 3  
# Desenvolvedor: CD Projekt Red  
# Preço: 100  
# Gêneros: RPG, Ação  

# ID: 2  
# Título: Stardew Valley  
# Desenvolvedor: ConcernedApe  
# Preço: 50  
# Gêneros: Simulação, Indie  

# ID: 3  
# Título: Dark Souls 3  
# Desenvolvedor: FromSoftware  
# Preço: 120  
# Gêneros: RPG, Ação  

# ID: 4  
# Título: Celeste  
# Desenvolvedor: Maddy Makes Games  
# Preço: 60  
# Gêneros: Plataforma, Indie  

# ID: 5  
# Título: Hollow Knight  
# Desenvolvedor: Team Cherry  
# Preço: 80  
# Gêneros: Metroidvania, Indie  

# ID: 6  
# Título: Portal 2  
# Desenvolvedor: Valve  
# Preço: 70  
# Gêneros: Puzzle, Aventura