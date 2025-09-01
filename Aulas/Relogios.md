**Relógios Físicos**

  Relógios físicos são aqueles que tentam se aproximar do tempo real, como o tempo universal coordenado (UTC).
  Cada máquina em um sistema distribuído possui seu próprio relógio de hardware.
  O principal desafio é que esses relógios de hardware são imperfeitos. Eles tendem a ter um leve desvio (conhecido como clock drift) e, com o tempo, podem divergir uns dos outros. A sincronização via rede é difícil devido à latência variável das mensagens.

  Essenciais para aplicações que exigem a coordenação com o mundo exterior e a medição do tempo real, como sistemas de transações bancárias ou agendamento de eventos.

  Exemplo de Algoritmo: O NTP (Network Time Protocol) é o protocolo mais comum para sincronizar relógios físicos pela internet, ajustando-os periodicamente para um servidor de tempo de referência.

**Relógios Lógicos**
  Os relógios lógicos não se importam com o tempo real.
  Seu único propósito é capturar a ordem causal dos eventos.
  Eles respondem à pergunta: "O evento A aconteceu antes do evento B?".
  
  Baseiam-se na relação "aconteceu antes" (happened-before).

  Se um evento em um processo pode influenciar um evento em outro, o relógio lógico garante que o timestamp do primeiro será menor que o do segundo.
  São fundamentais para a consistência e a depuração de sistemas distribuídos, permitindo a correta ordenação de eventos e a detecção de concorrência.

**Principais Algoritmos:**

*Relógio de Lamport*: O mais simples. Cada evento incrementa um contador. A sincronização ocorre quando uma mensagem é recebida, ajustando o relógio do receptor para o máximo entre o seu valor e o do remetente.

*Relógio de Vetor (Vector Clock)*: Uma evolução de Lamport. Cada processo mantém um vetor de contadores (um para cada processo do sistema). Isso permite não apenas a ordem causal, mas também a detecção de eventos que são concorrentes (que não têm relação de causa e efeito).
