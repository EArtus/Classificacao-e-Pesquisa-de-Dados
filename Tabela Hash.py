class Arquivo:
    def __init__(self, nome, caminho, tamanho):
        self.nome = nome
        self.caminho = caminho
        self.tamanho = tamanho

    def __repr__(self):
        return f"{self.nome} ({self.tamanho} KB)"

class TabelaHash:
    def __init__(self, tamanho=10):
        self.tabela = [[] for _ in range(tamanho)]

    def _funcao_hash(self, chave):
        return sum(ord(c) for c in chave) % len(self.tabela)

    def adicionar_arquivo(self, arquivo):
        indice = self._funcao_hash(arquivo.nome)
        for item in self.tabela[indice]:
            if item.nome == arquivo.nome:
                return "Arquivo já existe."
        self.tabela[indice].append(arquivo)

    def buscar_arquivo(self, nome):
        indice = self._funcao_hash(nome)
        for arquivo in self.tabela[indice]:
            if arquivo.nome == nome:
                return arquivo
        return None

    def remover_arquivo(self, nome):
        indice = self._funcao_hash(nome)
        for i, arquivo in enumerate(self.tabela[indice]):
            if arquivo.nome == nome:
                del self.tabela[indice][i]
                return True
        return False

    def listar_arquivos(self):
        return [arquivo for lista in self.tabela for arquivo in lista]

def menu():
    tabela = TabelaHash()
    
    while True:
        print("\n1. Adicionar arquivo")
        print("2. Buscar arquivo")
        print("3. Remover arquivo")
        print("4. Listar arquivos")
        print("5. Sair")
        
        escolha = input("Escolha: ")
        
        if escolha == "1":
            nome = input("Nome do arquivo: ")
            caminho = input("Caminho do arquivo: ")
            tamanho = int(input("Tamanho em KB: "))
            tabela.adicionar_arquivo(Arquivo(nome, caminho, tamanho))
            print(f"Arquivo '{nome}' adicionado.")
        
        elif escolha == "2":
            nome = input("Nome do arquivo: ")
            arquivo = tabela.buscar_arquivo(nome)
            if arquivo:
                print(f"Arquivo encontrado: {arquivo}")
            else:
                print("Arquivo não encontrado.")
        
        elif escolha == "3":
            nome = input("Nome do arquivo: ")
            if tabela.remover_arquivo(nome):
                print(f"Arquivo '{nome}' removido.")
            else:
                print("Arquivo não encontrado.")
        
        elif escolha == "4":
            arquivos = tabela.listar_arquivos()
            if arquivos:
                print("Arquivos:")
                for arquivo in arquivos:
                    print(arquivo)
            else:
                print("Nenhum arquivo armazenado.")
        
        elif escolha == "5":
            break
        else:
            print("Opção inválida.")

menu()


# Gerenciamento de Arquivos em Memória Secundária com Tabela Hash

# Uma empresa de tecnologia está desenvolvendo um sistema de gerenciamento de arquivos
# armazenados em memória secundária (discos rígidos ou SSDs). Os arquivos possuem as
# seguintes informações:

# - Nome do arquivo (ex.: "relatorio.pdf")
# - Caminho completo no sistema de arquivos (ex.: "/documentos/relatorio.pdf")
# - Tamanho do arquivo (em KB)

# A empresa quer implementar uma tabela hash para organizar os arquivos com base no nome
# do arquivo como chave. O sistema deve permitir as seguintes operações:

# 1. Adicionar arquivos à tabela hash.
# 2. Buscar arquivos pelo nome.
# 3. Remover arquivos pelo nome.
# 4. Listar todos os arquivos armazenados.

# Como requisito, o sistema precisa tratar colisões utilizando encadeamento separado
# (ou seja, cada posição da tabela armazena uma lista de arquivos no caso de colisão).

# Exemplo de Uso
# Considere os seguintes arquivos armazenados:
# 1. Nome: "relatorio.pdf", Caminho: "/documentos/relatorio.pdf", Tamanho: 1024 KB
# 2. Nome: "foto.jpg", Caminho: "/imagens/foto.jpg", Tamanho: 2048 KB
# 3. Nome: "dados.csv", Caminho: "/planilhas/dados.csv", Tamanho: 512 KB
# 4. Nome: "backup.zip", Caminho: "/backup/backup.zip", Tamanho: 4096 KB

# Com esses arquivos, o sistema deve ser capaz de realizar as seguintes operações:

# 1. Adicionar os arquivos à tabela hash.
# 2. Buscar pelo arquivo "dados.csv" e retornar suas informações.
# 3. Remover o arquivo "foto.jpg".
# 4. Listar todos os arquivos restantes armazenados na tabela hash.

# Regras:
# 1. A tabela hash deve ser implementada com um tamanho fixo inicial (ex.: 10 posições).
# 2. A função hash deve ser baseada no nome do arquivo, convertendo-o para um índice dentro
#    do intervalo da tabela.
# 3. Caso dois arquivos gerem o mesmo índice (colisão), o sistema deve tratá-los utilizando
#    encadeamento separado.
