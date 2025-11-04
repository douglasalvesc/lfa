'''
Disciplina: Linguagens Formais e Autômatos
Alunos: Douglas Alves da Cruz e Guilherme da Silva Carvalho
Professor: Alexandre Rossini
Trabalho 2
'''

import re

# nome: (no máximo 50 símbolos alfabéticos e espaço [a-zA-Z ])
REGEX_NOME = r"^[a-zA-Z ]{1,50}$"

# CPF: (algarismos numéricos no padrão "000.000.000-00")
REGEX_CPF = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"

# e-mail: (usuário: [a-zA-Z0-9_.-]{2,}, @, domínio: [a-zA-Z0-9_.-]{2,}, TLD: [a-z]{3}, país(opcional): (\.[a-z]{2})?)
REGEX_EMAIL_VALIDACAO = r"^[a-zA-Z0-9][a-zA-Z0-9_.-]{1,}@[a-zA-Z0-9][a-zA-Z0-9_.-]{1,}\.[a-z]{3}(?:\.[a-z]{2})?$"

# telefone: (dois formatos: 11 números ou (00)00000-0000)
REGEX_TELEFONE = r"^(\d{11}|\(\d{2}\)\d{5}-\d{4})$"


def validar_campo(texto, padrao_regex):
    """
    Valida um texto de entrada contra um padrão de regex.
    """
    if re.match(padrao_regex, texto):
        return True
    else:
        return False


texto_para_extrair = """
Prezado usuário,

Aqui estão os contatos do nosso time de suporte:

- alice.souza@gmail.com
- suporte_23@empresa-tech.com
- joao99@dominio123.org
- erro.email@.gmail...com

Por favor, envie suas dúvidas para qualquer um dos e-mails válidos acima.

Atenciosamente,

Equipe de Atendimento
"""

REGEX_EMAIL_EXTRACAO = r"[a-zA-Z0-9][a-zA-Z0-9_.-]{1,}@[a-zA-Z0-9][a-zA-Z0-9_.-]{1,}\.[a-z]{3}(?:\.[a-z]{2})?"

def extrair_emails_validos(texto, padrao_regex):
    """
    Encontra todas as ocorrências de um padrão regex em um texto.
    """
    return re.findall(padrao_regex, texto)


if __name__ == "__main__":
    
    print("--- 1. Teste de Validação dos Campos ---")

    # nome
    print("\nValidando Nomes:")
    print(f"'João da Silva': {validar_campo('João da Silva', REGEX_NOME)}")
    print(f"'NomeMuitoLongo... (51 chars)': {validar_campo('a'*51, REGEX_NOME)}")
    print(f"'Nome com 123': {validar_campo('Nome com 123', REGEX_NOME)}")

    # CPF
    print("\nValidando CPFs:")
    print(f"'123.456.789-00': {validar_campo('123.456.789-00', REGEX_CPF)}")
    print(f"'12345678900': {validar_campo('12345678900', REGEX_CPF)}")
    print(f"'123.456.789-ab': {validar_campo('123.456.789-ab', REGEX_CPF)}")

    # e-mail
    print("\nValidando E-mails:")
    print(f"'teste@dominio.com': {validar_campo('teste@dominio.com', REGEX_EMAIL_VALIDACAO)}")
    print(f"'teste.valido@dominio.com.br': {validar_campo('teste.valido@dominio.com.br', REGEX_EMAIL_VALIDACAO)}")
    print(f"'teste@dominio.io': {validar_campo('teste@dominio.io', REGEX_EMAIL_VALIDACAO)} (Falso, '.io' tem 2 letras, regra pede 3)")
    print(f"'t@d.com': {validar_campo('t@d.com', REGEX_EMAIL_VALIDACAO)} (Falso, usuário e domínio < 2 chars)")
    print(f"'erro.email@.gmail...com': {validar_campo('erro.email@.gmail...com', REGEX_EMAIL_VALIDACAO)}")

    # telefone
    print("\nValidando Telefones:")
    print(f"'11987654321': {validar_campo('11987654321', REGEX_TELEFONE)}")
    print(f"'(11)98765-4321': {validar_campo('(11)98765-4321', REGEX_TELEFONE)}")
    print(f"'12345': {validar_campo('12345', REGEX_TELEFONE)}")
    print(f"'(11) 98765-4321': {validar_campo('(11) 98765-4321', REGEX_TELEFONE)} (Falso, contém espaço)")

    print("\n" + "="*40 + "\n")

    print("--- 2. Extração de E-mails Válidos do Texto ---")

    emails_encontrados = extrair_emails_validos(texto_para_extrair, REGEX_EMAIL_EXTRACAO)
    
    print("\nTexto original:")
    print(texto_para_extrair)
    
    print("\nE-mails válidos encontrados:")
    if emails_encontrados:
        for email in emails_encontrados:
            print(f"- {email}")
    else:
        print("Nenhum e-mail válido encontrado.")

