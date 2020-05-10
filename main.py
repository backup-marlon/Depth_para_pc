def rawDepthToMeters(valor: int) -> float:
    """
    Retorna o valor convertido em profundidade em metros.
    :param valor: Um int entre -1 e 4095
    """
    if valor == -1:
        return 0
    else:
        return 1 / (valor * -0.0030711016 + 3.3309495161)

# Configuracoes Kinect
width = 640
height = 480
skip = 4 # Downsampling

# Abrir arquivo txt com os dados
arquivo = open("Nuvem_teste2.txt").readlines()
arrayDepth = []
for linha in arquivo:
    arrayDepth.append(int(linha))

# Armazenando os valores de profundidade em uma tabela
depthTable = []
for valor in arrayDepth:
    depthTable.append(rawDepthToMeters(valor))

for x in range(width, skip):
    for y in range(height, skip):
        
