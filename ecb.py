from funcoes_intermediarias import xor
from encrypt import encryptation_sequence
from decrypt import decriptation_sequence


def encrypt_ecb(key: str, message: str):
    blocks = message.split(" ") # divide a mensagem de blocos de 8 bits
    
    encrypted_blocks = [] # armazena os blocos encriptados 

    for block in blocks:
        encrypted_block = encryptation_sequence(key, block) # para cada bloco de 8 bits da mensagem chama a função para encripta-lo
        encrypted_blocks.append(encrypted_block) # adiciona o bloco encriptado a lista 

    # transforma a lista de blocos encriptados em uma string 
    output = encrypted_blocks[0]
    for i in range(len(encrypted_blocks) - 1):
        output = output + " " + encrypted_blocks[i+1]

    return output # retorna a string 


def decrypt_ecb(key:str, block: str):

    blocks = block.split(" ") # divide a mensagem de blocos de 8 bits
    decrypted_blocks = [] # armazena os blocos encriptados 


    for block in blocks:
        decrypted_block = decriptation_sequence(key, block) # para cada bloco de 8 bits e chamada a função para descripta-lo
        decrypted_blocks.append(decrypted_block) # adiciona o bloco descriptografado a lista 

    output = decrypted_blocks[0]
    for i in range(len(decrypted_blocks) - 1):
        output = output + " " + decrypted_blocks[i+1]

    return output # retorna a string 

if __name__ == "__main__":
# teste encriptar e decriptar modo ECB:
    key = "1010000010"
    message = "11010111 01101100 10111010 11110000"
    
    print("Blocos originais", message)
    result = encrypt_ecb(key, message)
    
    print("Blocos cifrados", result)
    decrypted = decrypt_ecb(key, result)
    print("Blocos decifrados:", decrypted)
    pass