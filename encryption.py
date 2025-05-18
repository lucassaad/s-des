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

def fk(permutaded_bits: str):
    left_half = permutaded_bits[0:5]
    right_half = permutaded_bits[5:10]
    pass

def expand_permute(bits: str, key: str):

    matriz = [
        # n4, n1, n2, n3, n2, n3, n4, n1
        bits[3], bits[0], bits[1], bits[2], bits[1], bits[2], bits[3], bits[0]
    ]

    key_bits = [bit for bit in key]

    xor_result = []
    for i in range(len(key)):
        xor_result[i].append(int(matriz[i]) ^ int(key_bits[i]))


    half1 = xor_result[0:5]
    half2 = xor_result[5:10]

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





a = bin(2)
print(a)