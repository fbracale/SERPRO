palavra_magica = "perfume"
palavra_tentativa = ""
palavra_final = ""
tentativas = 0

while True:
    chute = input("Digite uma letra: ").lower()
        
    if chute == "" or len(chute)>1:
        print("Digite apenas uma letra!")
        continue
    
    tentativas += 1
    i = 0
    palavra_tentativa = ""

    for letra in palavra_magica:
        if tentativas > 1 and palavra_final[i] != "*":
            palavra_tentativa += palavra_final[i]
            i += 1
            continue
        elif letra == chute:
            palavra_tentativa += letra
        else:
            palavra_tentativa += "*"
        i += 1
    
    palavra_final = palavra_tentativa
    print(palavra_final)

    if  "*" not in palavra_final:
        break
    
print(palavra_final)
print(f"Parabén, você acertou com {tentativas} tentativas")
