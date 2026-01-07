import os

caminho = [os.path.join("/run/media/ryan", nome) for nome in os.listdir("/run/media/ryan")]

print(caminho)
