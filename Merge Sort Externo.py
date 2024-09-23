import os
import heapq

def cria_arquivos_ordenados(nome, chunk_size):
    chunk_files = []
    with open(nome, 'r') as file:
        i = 0
        while True:
            lines = file.readlines(chunk_size)
            if not lines:
                break
            lines = [int(line.strip()) for line in lines]
            lines.sort()  
            chunk_file = f'Temp_{i + 1}.txt'
            with open(chunk_file, 'w') as chunk:
                for item in lines:
                    chunk.write(f"{item}\n")
            chunk_files.append(chunk_file)
            i += 1
    return chunk_files

def merge(nome, K):
    open_files = [open(chunk, 'r') for chunk in K]
    with open(nome, 'w') as output:
        min_heap = []
        for i, f in enumerate(open_files):
            line = f.readline()
            if line:
                heapq.heappush(min_heap, (int(line.strip()), i))
        
        while min_heap:
            smallest, i = heapq.heappop(min_heap)
            output.write(f"{smallest}\n")
            next_line = open_files[i].readline()
            if next_line:
                heapq.heappush(min_heap, (int(next_line.strip()), i))
    
    for f in open_files:
        f.close()

    for chunk in K:
        os.remove(chunk)

def merge_sort_externo(nome, chunk_size):
    print(f"Processando arquivo {nome}...")

    chunk_files = cria_arquivos_ordenados(nome, chunk_size)
    K = len(chunk_files)  
    T = sum(1 for _ in open(nome)) // (K + 1) 
    
    print(f"Número de arquivos: {K}")
    print(f"Tamanho médio por bloco: {T}")
    
    os.remove(nome)  
    merge(nome, chunk_files)  

