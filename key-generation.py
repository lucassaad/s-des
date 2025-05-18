# permutação p10

def key_generation_sequence(key: str):

    print("Chave original:", key, end="\n\n")

    chave_permutada = permutacao_p10(key)

    print("1º ETAPA: Permutação P10")
    print("Resultado:", chave_permutada, end="\n\n")
    print("2º ETAPA: Deslocamento circular a esquerda das metades")

    half1 = chave_permutada[0:5]
    print("1º metade:", half1)
    half2 = chave_permutada[5:10]
    print("2º Metade", half2)


    sl_half1 = deslocamento_circular(half1)
    print("1º metade deslocada:", sl_half1)
    sl_half2 = deslocamento_circular(half2)
    print("2º metade deslocada", sl_half2)
    new_key = sl_half1 + sl_half2
    print("Resultado:", new_key, end="\n\n")


    print("3º ETAPA: Permutação P8 para obter a chave K1")
    k1 = permutacao_p8(new_key)
    print("K1:", k1, end="\n\n")

    print("4º ETAPA: Duplo deslocamento circular a esquerda das metades")
    h1 = new_key[0:5]
    print("1º metade", h1)
    h2 = new_key[5:10]
    print("2º metade", h2)


    double_sl_h1 = deslocamento_circular(deslocamento_circular(h1))
    print("1º metade duplamente deslocada:", double_sl_h1)

    double_sl_h2 = deslocamento_circular(deslocamento_circular(h2))
    print("2º metade duplamente deslocada:", double_sl_h2, end="\n\n")

    new_key = double_sl_h1 + double_sl_h2

    print("5º ETAPA: Permutação P8 para obter a chave K2")
    k2 = permutacao_p8(new_key)

    print("K2:", k2)


def permutacao_p10(key: str):
    key_bits = [bit for bit in key]
    # print(key_bits) -> chave original 

    permutaded_bits = [
        key_bits[2],
        key_bits[4],
        key_bits[1],
        key_bits[6],
        key_bits[3],
        key_bits[9],
        key_bits[0],
        key_bits[8],
        key_bits[7],
        key_bits[5],
    ]
    permutaded_key = "".join(permutaded_bits)
    # print(permutaded_key) -> depois da permutação 
    return permutaded_key

# deslocamento circular 
def deslocamento_circular(key_half: str):
    bits = [bit for bit in key_half]

    aux = bits[0]
    # print(bits) -> antes do deslocamento
    for i in range(len(bits) - 1):
        
        bits[i] = bits[i + 1] 

    bits[-1] = aux

    return "".join(bits)
    # print(bits) -> depois do deslocamento 


# permutação p8
def permutacao_p8(key: str):
    bits = [bit for bit in key]

    permutaded_bits = [
        bits[5],
        bits[2],
        bits[6],
        bits[3],
        bits[7],
        bits[4],
        bits[9],
        bits[8]
    ]

    return "".join(permutaded_bits)

# deslocamento circular duplo

# permutação p8

if __name__ == '__main__':
    key_generation_sequence("1010000010")