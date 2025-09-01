O Que é o Problema de Eleição?
  Uma tarefa crítica é atribuída a um único processo, que atua como coordenador ou líder.
  Se esse líder falha ou se o sistema é inicializado, os processos restantes precisam escolher um novo líder de forma cooperativa e consistente.
  O problema de eleição é o processo de designar um único processo entre um grupo como o novo líder, de forma que todos os outros processos concordem com a escolha.

Principais Algoritmos de Eleição Algoritmo do Valentão e o Algoritmo do Anel.

Algoritmo do Valentão (Bully Algorithm) Princípio: A eleição é "vencida" pelo processo com o ID de identificação mais alto. O algoritmo presume que cada processo conhece o ID dos outros.
Como Funciona:

  Um processo percebe que o líder falhou e inicia uma eleição.
  Ele envia mensagens de "ELEIÇÃO" para todos os processos com um ID maior que o seu.
  Se nenhum processo de ID maior responder, ele se proclama o novo líder e envia uma mensagem de "COORDENADOR" para todos.
  Se um processo de ID maior responder, o processo que iniciou a eleição desiste e aguarda. O processo de ID maior que respondeu assume a responsabilidade de continuar a eleição.
  
Vantagens: Simples de entender e robusto. Garante que o processo com o maior ID seja sempre o líder, o que pode ser útil.

Desvantagens: Gera um grande volume de mensagens, especialmente se um processo com um ID baixo inicia a eleição. Pode ser ineficiente.

Algoritmo do Anel (Ring Algorithm) Princípio: Os processos são organizados em uma estrutura de anel lógico, onde cada processo sabe quem é o próximo na sequência.
Como Funciona:

  Um processo percebe que o líder falhou e inicia uma eleição.
  Ele cria uma mensagem de "ELEIÇÃO" com seu próprio ID e a envia para o próximo processo no anel.
  Cada processo que recebe a mensagem adiciona seu próprio ID à lista de IDs na mensagem e a passa adiante.
  Quando a mensagem retorna ao processo que a iniciou (após ter percorrido todo o anel), ele tem uma lista completa de todos os processos ativos.
  O processo iniciador escolhe o maior ID da lista como o novo líder e envia uma segunda mensagem de "COORDENADOR" para todo o anel, informando a todos sobre o resultado.
  
Vantagens: Mais eficiente em termos de mensagens, pois a informação circula em apenas uma direção.

Desvantagens: A falha de um único processo no anel pode interromper a eleição. A topologia de anel precisa ser mantida.

