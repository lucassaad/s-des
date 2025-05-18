from funcoes_intermediarias import xor
from encrypt import encryptation_sequence
from decrypt import decriptation_sequence

def encrypt_cbc(key: str, message: str, iv: str):
    blocks = message.split(" ") # divide a mensagem de blocos de 8 bits
    encrypted_blocks = [] # armazena os blocos encriptados 
    
    xor_chain_input = iv # primeiro vetor de inicialização 

    for block in blocks:
        xor_result = xor(xor_chain_input, block, 8) # xor entre o bloco e um vetor 
        encrypted_block = encryptation_sequence(key, xor_result) # para cada XOR_bloco é chamada a função para encripta-lo
        encrypted_blocks.append(encrypted_block) 
        xor_chain_input = encrypted_block # vetor do XOR = bloco cifrado atual 

    output = encrypted_blocks[0]
    for i in range(len(encrypted_blocks) - 1):
        output = output + " " + encrypted_blocks[i+1]

    return output # retorna a string

def decrypt_cbc(key: str, message: str, iv: str):
    blocks = message.split(" ") # divide a mensagem de blocos de 8 bits
    decrypted_blocks = [] # armazena os blocos encriptados 
    
    xor_chain_input = iv # primeiro vetor de inicialização 

    for block in blocks:
        decrypted_block = decriptation_sequence(key, block) # para cada XOR_bloco é chamada a função para encripta-lo
        xor_result = xor(xor_chain_input, decrypted_block, 8) # xor entre o bloco e um vetor 

        decrypted_blocks.append(xor_result) 
        xor_chain_input = decrypted_block # vetor do XOR = bloco cifrado atual 

    output = decrypted_blocks[0]
    for i in range(len(decrypted_blocks) - 1):
        output = output + " " + decrypted_blocks[i+1]

    return output # retorna a string 


if __name__ == "__main__":
# teste encriptar e decriptar modo ECB:
    key = "1010000010"
    message = "11010111 01101100 10111010 11110000"
    iv = "01010101"
    print("Blocos originais", message)

    result = encrypt_cbc(key, message, iv)
    print("Blocos cifrados", result)

    decrypted = decrypt_cbc(key, result, iv)
    print("Blocos decifrados:", decrypted)
    pass