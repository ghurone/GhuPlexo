"""
GhuPlexo v1.0

Uma biblioteca para manipular numeros complexos
-----------------------------------------------------------
objeto:
    Complexo:
        Todas as operacoes a seguir funcionam entre:
            (Complexos, inteiros e floats)
        
        -> Soma
        -> Subtracao
        -> Divisao
        -> Multiplicacao
        -> Potencia
        -> Bool (somente igualdade eh possivel)
        
dados imbutidos:
    conjugado -> Retorna o conjugado do numero complexo
    
    modulo    -> Retorna o modulo("tamanho") do numero complexo 
    
    angulo    -> Retorna o angulo - em radiano - do numero complexo
    
    real      -> Retorna a parte real do numero complexo
    
    imag      -> Retorna a parte imaginaria do numero complexo

A letra Jota ('j') esta indicando a unidade imaginária
"""
from .complex import Complexo