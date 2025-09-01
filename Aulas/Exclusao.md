O Que é Exclusão Mútua?
  Em um sistema distribuído, múltiplos processos podem tentar acessar um mesmo recurso compartilhado, como um banco de dados, um arquivo ou uma impressora. Esse recurso é chamado de Região Crítica.

  A exclusão mútua é a garantia de que, a qualquer momento, apenas um único processo pode estar dentro da região crítica. O objetivo é evitar a corrupção de dados ou resultados inconsistentes causados por acessos concorrentes.

Tipos de Algoritmos para Exclusão Mútua

  Abordagem Centralizada Princípio: Um processo é eleito como "coordenador" ou "servidor de exclusão mútua". Todos os outros processos enviam suas requisições de acesso para ele. O coordenador gerencia uma fila e concede o acesso um de cada vez.
  
  Vantagens: Simples de implementar e entender.

  Desvantagens: O coordenador é um ponto único de falha (se ele falhar, todo o sistema de exclusão mútua para) e pode se tornar um gargalo de desempenho.

  Abordagem Distribuída Princípio: Não há um coordenador central. Os processos comunicam-se entre si para decidir quem pode entrar na região crítica.
  
  Vantagens: Tolerante a falhas (não há ponto único de falha).

  Desvantagens: Alto custo de mensagens. O tráfego de rede é alto (requisições e respostas).

  Abordagem Baseada em Ficha (Token) Princípio: Uma "ficha" (token) é um objeto especial que circula entre os processos em um anel lógico. Apenas o processo que possui a ficha tem o direito de entrar na região crítica. Quando ele sai, passa a ficha para o próximo processo no anel.
  
  Vantagens: Sem starvation (um processo esperando indefinidamente) ou deadlock (impasse).

  Desvantagens: O sistema pode parar se a ficha for perdida. Detectar a perda e gerar uma nova ficha é um problema complexo.
