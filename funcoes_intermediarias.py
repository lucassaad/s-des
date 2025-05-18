def ip(plaintext: str):
    bits = [bit for bit in plaintext]
    permutaded_bits = [
        bits[1],
        bits[5],
        bits[2],
        bits[0],
        bits[3],
        bits[7],
        bits[4],
        bits[6]
    ]

    return "".join(permutaded_bits)


def function_k(lh: str, rh: str, sub_key: str):


    s0 = [
        ['01','00','11','10'],
        ['11','10','01','00'],
        ['00','10','01','11'],
        ['11','01','11','10']
    ]

    s1 = [
        ['00','01','10','11'],
        ['10','00','01','11'],
        ['11','00','01','00'],
        ['10','01','00','11']
    ]

    expanded_rh = ep(rh) # expand and permute the right half
    
    xor_result = xor(expanded_rh, sub_key, 8) # aplica XOR entre 8 bits e chave K1
    
    lh_xor = xor_result[0:4] # metade esquerda do primeiro xor
    rh_xor = xor_result[4:8] # metade direita do primeiro xor

    s0_output = sbox(lh_xor, s0) #-> 2 bits 
    s1_output = sbox(rh_xor, s1) #-> 2 bits

    sbox_result = s0_output + s1_output # 4 bits resultantes da concatenação s0 + s1
    
    permutaded_sbox_result = p4(sbox_result) 
    
    result = xor(lh, permutaded_sbox_result, 4) # XOR dos 4 bits de lh com o resultado de p4

    return result


def ip_inversa(block: str):
    bits = [bit for bit in block]
    permutaded_bits = [
        bits[3],
        bits[0],
        bits[2],
        bits[4],
        bits[6],
        bits[1],
        bits[7],
        bits[5]
    ]

    return "".join(permutaded_bits)


# FUNÇÕES DE FK
def ep(half: str): # Expand and permute function 

    expanded_half = [
        # n4, n1, n2, n3, n2, n3, n4, n1
        half[3], half[0], half[1], half[2], half[1], half[2], half[3], half[0]
    ]

    return "".join(expanded_half)

def xor(a: str, b: str, input_len: int): # executa um XOR entre 8 bits e uma subchave
    xor_result = []
    for i in range(input_len):
        bit_xor = (int(a[i]) ^ int(b[i]))
        xor_result.append(str(bit_xor))

    return "".join(xor_result)

def sbox(half: str, sbox_matrix: list[list[str]]):

    row_bin = half[0] + half[3] 
    row = int(row_bin, 2)

    column_bin = half[1] + half[2]
    column = int(column_bin, 2)
    

    return sbox_matrix[row][column]

def p4(input: str):
    bits = [bit for bit in input]
    permutaded_bits = [
       bits[1],
       bits[3],
       bits[2],
       bits[0]
    ]
    return "".join(permutaded_bits)

def permutacao_p10(key: str):

    key_bits = [bit for bit in key]
    
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
    
    return "".join(permutaded_bits)

# deslocamento circular 
def deslocamento_circular(half: str):

    bits = [bit for bit in half]

    aux = bits[0] # salva o primeiro bit

    for i in range(len(bits) - 1):
        
        bits[i] = bits[i + 1]  # desloca o bit em i+1 para a esquerda 

    bits[-1] = aux # desloca o primeiro bit de key_half

    return "".join(bits)


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