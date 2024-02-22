nickname = "TURURU"
qtd_XP = 10000
elo_heroi = ""

if qtd_XP == 1000:
    elo_heroi = "Ferro"
elif qtd_XP >= 1001 and qtd_XP <= 2000:
    elo_heroi = "Bronze"
elif qtd_XP >= 2001 and qtd_XP <= 6000:
    elo_heroi = "Prata"
elif qtd_XP >= 6001 and qtd_XP <= 7000:
    elo_heroi = "Ouro"
elif qtd_XP >= 7001 and qtd_XP <= 8000:
    elo_heroi = "Platina"
elif qtd_XP >= 8001 and qtd_XP <= 9000:
    elo_heroi = "Ascendente"
elif qtd_XP >= 9001 and qtd_XP <= 10000:
    elo_heroi = "Imortal"
else:
    elo_heroi = "Radiante"

match elo_heroi:
    case "Ferro":
        print(f"O heroi de nome {nickname} está no nível {elo_heroi}")
    case "Bronze":
        print(f"O heroi de nome {nickname} está no nível {elo_heroi}")
    case "Prata":
        print(f"O heroi de nome {nickname} está no nível {elo_heroi}")
    case "Ouro":
        print(f"O heroi de nome {nickname} está no nível {elo_heroi}")
    case "Platina":
        print(f"O heroi de nome {nickname} está no nível {elo_heroi}")
    case "Ascendente":
        print(f"O heroi de nome {nickname} está no nível {elo_heroi}")
    case "Imortal":
        print(f"O heroi de nome {nickname} está no nível {elo_heroi}")
    case "Radiante":
        print(f"O heroi de nome {nickname} está no nível {elo_heroi}")
    case _:
        print("valor invalido")
