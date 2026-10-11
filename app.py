def calcular_media(notas):
    """
    Recebe uma lista de notas e retorna a média aritmética.
    Trata o caso de listas vazias para evitar erros de divisão por zero.
    """
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def verificar_status(media, media_minima=6.0):
    """
    Avalia se o aluno foi aprovado ou reprovado.
    Garante que nota igual ou maior que a média mínima aprova o estudante.
    """
    if media >= media_minima:
        return "Aprovado(a)"
    return "Reprovado(a)"


def gerar_relatorio(alunos):
    """
    Processa a lista de alunos, integrando as funções de cálculo 
    e verificação para construir um relatório textual completo.
    """
    relatorio = "=== RELATÓRIO DE DESEMPENHO ESCOLAR ===\n\n"
    
    for aluno in list(alunos):
        # Calcula a média utilizando a função especialista
        media_atual = calcular_media(aluno["notas"])
        
        # Verifica a situação utilizando a regra de negócio flexível
        situacao = verificar_status(media_atual)
        
        # Concatena as informações formatadas no texto do relatório
        relatorio += f"Aluno: {aluno['nome']}\n"
        relatorio += f"Disciplina: {aluno['disciplina']}\n"
        relatorio += f"Média: {media_atual:.1f} -> Status: {situacao}\n"
        relatorio += "-" * 40 + "\n"
        
    return relatorio


# --- bloco de teste do sistema ---
if __name__ == "__main__":
    # Simulação de dados recebidos pelo sistema
    dados_alunos = [
        {"nome": "Paulo Silva", "disciplina": "Desenvolvimento de Sistemas", "notas": [8.0, 7.5, 6.0]},
        {"nome": "Ana Costa", "disciplina": "Banco de Dados", "notas": [5.0, 6.0, 4.5]},
        {"nome": "Carlos Souza", "disciplina": "Lógica de Programação", "notas": [6.0, 6.0, 6.0]}
    ]
    
    # Exibição do resultado final no console
    print(gerar_relatorio(dados_alunos))