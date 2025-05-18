# permutação p10
from funcoes_intermediarias import deslocamento_circular, permutacao_p10, permutacao_p8
def key_generation_sequence(key: str):

    chave_permutada = permutacao_p10(key)

    
    lh = chave_permutada[0:5] 
    rh = chave_permutada[5:10]


    sl_left = deslocamento_circular(lh) # deslocamento circular da metade esquerda 
    
    sl_right = deslocamento_circular(rh) # deslocamento circular da metade direita 
    
    first_p8_input = sl_left + sl_right  # input para a primeira execução de P8 que resulta em K1
    
    k1 = permutacao_p8(first_p8_input)

    double_sl_lh = deslocamento_circular(deslocamento_circular(sl_left)) # execução do duplo deslocamento circular na metade esquerda deslocada 

    double_sl_rh = deslocamento_circular(deslocamento_circular(sl_right)) # execução do duplo deslocamento circular na metade direita deslocada 

    second_p8_input = double_sl_lh + double_sl_rh # input para a segunda execução de p9=8 que resulta em k2

    k2 = permutacao_p8(second_p8_input)


    return (k1, k2)




