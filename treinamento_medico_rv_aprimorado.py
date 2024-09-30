#550161 - EDUARDO OSORIO FILHO
#550610 - FABIO HIDEKI KAMIKIHARA
#99696 - LUAN RAMOS TEIXEIRA
#550260 - PEDRO MOURA BARROS
#98896 - RODRIGO FERNANDES DOS SANTOS

# Aprimorando a função de treinamento para fornecer feedback detalhado e ajustar a dificuldade com base no desempenho anterior

def treinamento_medico_aprimorado(procedimento, max_tentativas):
    # Matriz para armazenar os resultados de cada tentativa
    dp = [[0 for _ in range(len(procedimento) + 1)] for _ in range(max_tentativas + 1)]
    feedback = []
    
    # Iteramos sobre as tentativas e os passos do procedimento
    for tentativa in range(1, max_tentativas + 1):
        tent_feedback = []
        for passo in range(1, len(procedimento) + 1):
            # Se o passo foi executado corretamente (simulação)
            if procedimento[passo - 1] == "correto":
                dp[tentativa][passo] = dp[tentativa - 1][passo - 1] + 1
                tent_feedback.append(f"Tentativa {tentativa}: Passo {passo} correto.")
            else:
                # Considera tentativas anteriores para otimizar o procedimento
                dp[tentativa][passo] = max(dp[tentativa - 1][passo], dp[tentativa][passo - 1])
                tent_feedback.append(f"Tentativa {tentativa}: Passo {passo} incorreto.")
        
        feedback.append(tent_feedback)

    # Ajuste de dificuldade com base no desempenho
    desempenho = dp[max_tentativas][len(procedimento)]
    dificuldade = "Fácil" if desempenho / len(procedimento) > 0.8 else "Difícil"

    return dp[max_tentativas][len(procedimento)], feedback, dificuldade


# Simulação de um procedimento médico
procedimento_simulado = ["correto", "erro", "correto", "erro", "correto"]

# Quantidade máxima de tentativas de simulação
max_tentativas = 5

# Executa a função aprimorada de treinamento
resultado_aprimorado, feedback_aprimorado, dificuldade = treinamento_medico_aprimorado(procedimento_simulado, max_tentativas)

# Exibe os resultados do treinamento
print(f"Resultado otimizado: {resultado_aprimorado}")
print(f"Feedback do treinamento: {feedback_aprimorado}")
print(f"Ajuste de dificuldade: {dificuldade}")
