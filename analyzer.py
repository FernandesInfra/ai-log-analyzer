import os
import sys
from openai import OpenAI

# Inicializa o cliente usando a chave da variável de ambiente
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analisar_log(caminho_log):
    if not os.path.exists(caminho_log):
        print(f"Erro: Arquivo {caminho_log} não encontrado.")
        return

    with open(caminho_log, 'r') as file:
        conteudo_log = file.read()

    print("⚡ Analisando logs e gerando diagnóstico via IA...\n")

    prompt_sistema = (
        "Você é um Engenheiro de Infraestrutura e Especialista em Segurança Sênior. "
        "Analise o trecho de log fornecido, identifique o erro exato, a causa raiz "
        "e sugira um passo a passo objetivo para a solução técnica."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": f"Analise estes logs:\n\n{conteudo_log}"}
            ],
            temperature=0.2
        )

        diagnostico = response.choices[0].message.content
        print("=== RELATÓRIO DE DIAGNÓSTICO ===")
        print(diagnostico)

    except Exception as e:
        print(f"Erro ao conectar com a API: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analisar_log(sys.argv[1])
    else:
        print("Uso: python analyzer.py <caminho_do_log>")
