
from key_generation import key_generation_sequence
from funcoes_intermediarias import *

def decriptation_sequence(key: str, ciphertext: str):

    sub_keys = key_generation_sequence(key)

    k1 = sub_keys[0]
    k2 = sub_keys[1]


    permutaded_block = ip(ciphertext) # IP(block)
    
    left_ip_half = permutaded_block[0:4] # 4 primeiros bits de IP(block)
    right_ip_half = permutaded_block[4:8] # 4 ultimos bits de IP(block)

    first_fk_result = function_k(left_ip_half, right_ip_half, k2) # FK(L, R, K1)

    second_fk_result = function_k(right_ip_half, first_fk_result, k1) # FK(R, Resultado da FK anterior, K2)
    
    fks_result = second_fk_result + first_fk_result

    final_result = ip_inversa(fks_result)

    return final_result


if __name__ == "__main__":
# teste da função de criptografia:
    key = "1010000010"
    bloco = "10101000"

    print("Bloco original:", bloco)

    result = decriptation_sequence(key, bloco)

    print("Bloco encriptado:", result)# key = "1010000010"
