def funcao_transicao(estado, caractere):
    """
    Implementa a função de transição (δ).
    """
    if estado == 'q0':
        if caractere == 'a':
            return 'q1'
        elif caractere == 'b':
            return 'q0'
    elif estado == 'q1':
        if caractere == 'a':
            return 'q2'
        elif caractere == 'b':
            return 'q3'
    elif estado == 'q2':
        if caractere == 'a':
            return 'q4'
        elif caractere == 'b':
            return 'q5'
    elif estado == 'q3':
        if caractere == 'a':
            return 'q6'
        elif caractere == 'b':
            return 'q7'
    elif estado == 'q4':
        if caractere == 'a':
            return 'q4'
        elif caractere == 'b':
            return 'q5'
    elif estado == 'q5':
        if caractere == 'a':
            return 'q6'
        elif caractere == 'b':
            return 'q7'
    elif estado == 'q6':
        if caractere == 'a':
            return 'q2'
        elif caractere == 'b':
            return 'q3'
    elif estado == 'q7':
        if caractere == 'a':
            return 'q1'
        elif caractere == 'b':
            return 'q0'
    return "ESTADO_DE_ERRO"

def funcao_transicao_estendida(estado, palavra):
    """
    Implementa a função de transição estendida (δ̂ ).
    """
    if not palavra:
        return estado

    prefixo_x = palavra[:-1]
    ultimo_simbolo_a = palavra[-1]
    estado_intermediario = funcao_transicao_estendida(estado, prefixo_x)
    estado_final = funcao_transicao(estado_intermediario, ultimo_simbolo_a)
    return estado_final


if __name__ == "__main__":
    
    estados_finais = {'q4', 'q5', 'q6'}
    estado_inicial = 'q0'

    # --- Teste 1 ---
    palavra1 = "aba"
    resultado1 = funcao_transicao_estendida(estado_inicial, palavra1)
    if resultado1 in estados_finais:
        status1 = "Aceita"
    else:
        status1 = "Não Aceita"
    print(f"Palavra: '{palavra1}' | Estado Final: {resultado1} | Status: {status1}")

    # --- Teste 2 ---
    palavra2 = "ababa"
    resultado2 = funcao_transicao_estendida(estado_inicial, palavra2)
    if resultado2 in estados_finais:
        status2 = "Aceita"
    else:
        status2 = "Não Aceita"
    print(f"Palavra: '{palavra2}' | Estado Final: {resultado2} | Status: {status2}")

    # --- Teste 3 ---
    palavra3 = "bbbaaa"
    resultado3 = funcao_transicao_estendida(estado_inicial, palavra3)
    if resultado3 in estados_finais:
        status3 = "Aceita"
    else:
        status3 = "Não Aceita"
    print(f"Palavra: '{palavra3}' | Estado Final: {resultado3} | Status: {status3}")

    # --- Teste 4 (palavra rejeitada) ---
    palavra4 = "ab"
    resultado4 = funcao_transicao_estendida(estado_inicial, palavra4)
    if resultado4 in estados_finais:
        status4 = "Aceita"
    else:
        status4 = "Não Aceita"
    print(f"Palavra: '{palavra4}' | Estado Final: {resultado4} | Status: {status4}")