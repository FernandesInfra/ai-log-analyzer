# 🤖 AI Log Analyzer (Analisador de Logs com IA)

Este projeto é uma ferramenta de automação feita em Python. Ela lê arquivos de log de rede e servidores (aqueles arquivos cheios de mensagens de erro) e usa Inteligência Artificial para traduzir os erros em um relatório simples e com ações de solução.

---

## 🎯 Por que este projeto foi criado?

No dia a dia do suporte técnico e da infraestrutura de TI, quando um servidor dá problema, ele gera centenas de linhas de código e erros brutos. 

Analisar linha por linha manualmente toma muito tempo. Com essa ferramenta, a IA faz a leitura pesada em segundos e já entrega o diagnóstico pronto para o técnico resolver o problema mais rápido (reduzindo o tempo de atendimento / SLA).

---

## ⚙️ Como a solução funciona?

1. **Entrada de Dados:** O programa recebe o arquivo de log do servidor (exemplo: `exemplo_servidor.log`).
2. **Processamento com IA:** O script envia o texto do log para a API da OpenAI com orientações específicas (Engenharia de Prompt) para analisar a causa raiz do problema.
3. **Relatório de Saída:** A IA devolve um resumo direto, explicando o que aconteceu e o que deve ser feito.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem principal para leitura de arquivos e automação.
- **API da OpenAI**: Modelo de IA responsável pela análise inteligente dos dados.
- **Git & GitHub**: Controle de versão e documentação do projeto.

---

## 📄 Exemplo Prático de Funcionamento

### 1. O log bruto lido pelo programa (`exemplo_servidor.log`):

- `2026-10-30 14:22:01 [ERROR] [auth] Failed password for invalid user admin from 192.168.1.105`
- `2026-10-30 14:22:10 [CRITICAL] [kernel] Out of memory: Kill process 1042 (mysqld)`

---

### 2. O relatório que a IA entrega na tela para o técnico:

> 🔍 **Diagnóstico Identificado:**
> - **Falha de Segurança:** Tentativas repetidas de acesso indevido vindas do IP `192.168.1.105` (Ataque de Força Bruta).
> - **Falha de Sistema:** O banco de dados (`mysqld`) caiu por falta de memória RAM no servidor.
>
> 💡 **Ação Recomendada:** 
> 1. Bloquear o IP `192.168.1.105` no Firewall.
> 2. Reiniciar o serviço do banco de dados e verificar o uso de memória do servidor.
