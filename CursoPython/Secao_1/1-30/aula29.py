"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if (velocidade > RADAR_1):
    print("Passou.")

velocidade_acima_do_radar = (velocidade > RADAR_1)
carro_multado = local_carro >= (LOCAL_1-RADAR_RANGE) and local_carro <= (LOCAL_1+RADAR_RANGE) and velocidade_acima_do_radar

if carro_multado:
    print("Levou multa.")