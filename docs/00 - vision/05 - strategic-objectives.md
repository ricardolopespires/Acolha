# Product Principles

**Status:** 🟢 Contrato arquitetural fechado
**Módulo:** `00 - vision`
**Documento:** `product-principles.md`
**Produto:** ACOLHE — Plataforma de Jornada em Saúde

---

## 1. Propósito

Os princípios de produto definem como o ACOLHE deve ser concebido, construído e evoluído.

Eles transformam a visão e a missão do ACOLHE em regras práticas para decisões de:

* produto;
* experiência;
* domínio;
* arquitetura;
* tecnologia;
* acessibilidade;
* segurança;
* inteligência;
* integração;
* desenvolvimento;
* evolução da plataforma.

Nenhuma decisão técnica deve contrariar os princípios fundamentais do produto.

> **Tecnologia é meio, não fim.**

---

# 2. Princípio Central

## 2.1 Pessoa antes do sistema

O ACOLHE deve ser organizado a partir da realidade da pessoa, e não a partir da estrutura interna da instituição.

O sistema deve perguntar:

> **“Como podemos ajudar?”**

e não:

> “Qual operação você deseja executar?”

A pessoa não deve precisar conhecer:

* setores;
* departamentos;
* sistemas;
* códigos;
* fluxos internos;
* regras administrativas;
* nomenclaturas institucionais;
* responsabilidades organizacionais.

O sistema deve absorver essa complexidade sempre que possível.

### Regra

> **A complexidade interna do sistema não deve ser transferida desnecessariamente para a pessoa.**

---

# 3. Necessidade antes do serviço

A jornada começa pela necessidade da pessoa.

Uma necessidade pode ser:

* clínica;
* administrativa;
* documental;
* logística;
* informacional;
* social;
* educacional;
* relacionada ao acompanhamento;
* relacionada à continuidade do cuidado.

Portanto:

```text
Pessoa
   ↓
Necessidade
   ↓
Contexto
   ↓
Serviço
   ↓
Jornada
   ↓
Ações
   ↓
Resultado
   ↓
Próximo passo
```

O ACOLHE não deve obrigar a pessoa a descobrir previamente qual serviço interno resolve sua necessidade.

---

# 4. Jornada antes do CRUD

O ACOLHE não deve ser projetado como uma coleção de cadastros e operações isoladas.

O objeto principal do produto é a **jornada da pessoa**.

CRUDs podem existir como mecanismos internos, mas não devem definir a experiência nem o domínio principal.

### Regra

> **O cadastro representa um elemento da realidade; a jornada representa a realidade em movimento.**

Exemplo:

Não pensar apenas em:

```text
Consulta
Exame
Prescrição
Documento
Solicitação
```

Mas em:

```text
Necessidade
    ↓
Solicitação
    ↓
Avaliação
    ↓
Agendamento
    ↓
Atendimento
    ↓
Exame
    ↓
Resultado
    ↓
Conduta
    ↓
Acompanhamento
```

---

# 5. O próximo passo deve ser explícito

Uma das responsabilidades centrais do ACOLHE é ajudar a pessoa a compreender:

> **“Qual é o próximo passo da minha jornada?”**

Quando houver uma próxima ação conhecida, o sistema deve procurar torná-la:

* visível;
* compreensível;
* contextualizada;
* acessível;
* executável;
* acompanhável.

O próximo passo pode ser:

* uma ação do paciente;
* uma ação de um profissional;
* uma ação administrativa;
* uma ação de outro serviço;
* uma informação que precisa ser fornecida;
* uma decisão humana que precisa acontecer;
* uma etapa que precisa ser aguardada.

O ACOLHE não deve confundir **próximo passo** com **decisão clínica automática**.

---

# 6. Continuidade antes de fragmentação

A pessoa não deve perder sua jornada porque mudou:

* de canal;
* de profissional;
* de setor;
* de serviço;
* de unidade;
* de instituição participante;
* de modalidade de atendimento.

O contexto relevante da jornada deve acompanhar a pessoa dentro dos limites de acesso autorizados.

```text
Mobile
Web
Presencial
Telefone
Atendimento assistido
Telemedicina
Atendimento domiciliar
        ↓
   MESMA JORNADA
```

### Regra

> **O canal muda. A jornada não deve ser fragmentada.**

---

# 7. O canal não define o direito de acesso

Uma pessoa pode precisar utilizar diferentes canais para acessar o mesmo serviço.

O ACOLHE deve considerar:

* mobile;
* web;
* atendimento presencial;
* telefone;
* quiosques/totens;
* atendimento assistido;
* outros canais institucionais disponíveis.

A indisponibilidade ou dificuldade de utilização de um canal não deve, por si só, eliminar o acesso ao serviço quando houver outro canal apropriado.

> **O canal define como a pessoa acessa o serviço, não se ela tem direito de acessá-lo.**

---

# 8. Acessibilidade é arquitetura

Acessibilidade não deve ser tratada como uma camada adicionada posteriormente à interface.

Ela deve existir desde o domínio e atravessar:

```text
Domínio
   ↓
Serviços
   ↓
APIs
   ↓
Web
   ↓
Mobile
   ↓
Canais presenciais
   ↓
Comunicação
```

O ACOLHE deve considerar, entre outras situações:

* deficiência visual;
* deficiência auditiva;
* mobilidade reduzida;
* idosos;
* baixa alfabetização digital;
* dificuldades cognitivas;
* dependência de cuidador;
* acesso limitado à internet.

### Regra fundamental

> **Acessibilidade modifica a forma de acesso; não deve ser usada para reduzir direitos.**

---

# 9. Identidade não é autorização

O fato de o sistema reconhecer uma pessoa não significa que ela esteja autorizada a agir em determinado contexto.

A arquitetura deve separar:

```text
Identidade
   ↓
Contexto
   ↓
Nível de acesso
   ↓
Escopo
   ↓
Recurso
   ↓
Ação
   ↓
Validade
   ↓
Auditoria
```

Autenticação responde:

> **“Quem é você?”**

Autorização responde:

> **“O que você pode fazer neste contexto?”**

---

# 10. Acesso deve ser contextual

O ACOLHE não deve trabalhar com permissões genéricas e universais.

O acesso deve considerar:

* quem acessa;
* quem é o paciente;
* relação entre as pessoas;
* contexto;
* função;
* instituição;
* escopo;
* recurso;
* ação;
* finalidade;
* validade;
* regras aplicáveis;
* necessidade de auditoria.

Uma mesma pessoa pode possuir diferentes contextos de acesso.

---

# 11. Acesso delegado deve ser explícito

Familiares, cuidadores, representantes e outras pessoas autorizadas podem atuar em nome do paciente quando houver fundamento para isso.

Esse acesso não deve depender de:

* compartilhamento de senha;
* compartilhamento de conta;
* informalidade;
* confiança implícita.

Deve existir um contexto explícito de representação.

```text
Paciente
   ↓
Pessoa autorizada
   ↓
Escopo
   ↓
Ações permitidas
   ↓
Recursos permitidos
   ↓
Validade
   ↓
Auditoria
```

### Regra

> **Representar alguém não significa tornar-se aquela pessoa.**

---

# 12. Níveis de acesso representam capacidade, não permissão absoluta

O ACOLHE adota uma estrutura conceitual de níveis:

```text
NÍVEL 0 — IDENTIFICAÇÃO

NÍVEL 1 — ACESSO PESSOAL

NÍVEL 2 — AÇÕES DE JORNADA

NÍVEL 3 — DOCUMENTOS E INFORMAÇÕES

NÍVEL 4 — ACESSO DELEGADO

NÍVEL 5 — ACESSO PROFISSIONAL

NÍVEL 6 — ACESSO ESPECIAL
```

O nível não deve ser interpretado isoladamente.

A autorização efetiva depende do contexto e do escopo.

### Regra

> **Nível de acesso é capacidade máxima contextual; autorização efetiva é resultado das regras aplicáveis.**

---

# 13. Uma jornada, múltiplas modalidades de cuidado

O ACOLHE deve permitir que uma jornada transite entre diferentes modalidades quando apropriado.

```text
                 JORNADA
                    │
       ┌────────────┼────────────┐
       ↓            ↓            ↓
 Presencial   Telemedicina   Domiciliar
       └────────────┼────────────┘
                    ↓
             Cuidado clínico
                    ↓
              Continuidade
```

Telemedicina e atendimento domiciliar não devem existir como produtos isolados.

São modalidades pelas quais uma mesma jornada pode acontecer, conforme regras e disponibilidade aplicáveis.

---

# 14. O cuidado deve chegar onde a pessoa está

Sempre que a natureza do cuidado e os serviços disponíveis permitirem, o sistema deve procurar reduzir deslocamentos desnecessários.

Isso pode envolver:

* telemedicina;
* acompanhamento remoto;
* atendimento domiciliar;
* coleta ou serviços disponíveis no território;
* canais digitais;
* atendimento assistido.

Isso não significa que todo atendimento possa ou deva ser remoto.

A modalidade deve respeitar:

* necessidade;
* segurança;
* disponibilidade;
* regras do serviço;
* contexto clínico;
* decisão profissional quando aplicável.

---

# 15. Humanidade antes da automação

O ACOLHE pode automatizar processos, mas não deve automatizar indiscriminadamente responsabilidades humanas.

Automação deve reduzir:

* espera desnecessária;
* trabalho repetitivo;
* erros operacionais;
* perda de contexto;
* necessidade de repetir informações;
* complexidade administrativa.

Automação não deve substituir indevidamente:

* autoridade clínica;
* consentimento;
* responsabilidade profissional;
* decisões humanas que exigem julgamento;
* direitos do paciente.

---

# 16. Inteligência deve ajudar, não assumir autoridade

A inteligência artificial e outros mecanismos cognitivos devem atuar como **camada de assistência**.

Podem ajudar a:

* organizar contexto;
* resumir informações;
* identificar informações ausentes;
* preparar atendimentos;
* organizar solicitações;
* acompanhar pendências;
* identificar mudanças relevantes;
* explicar etapas;
* apoiar encaminhamento;
* ajudar na continuidade.

A inteligência não deve assumir automaticamente a autoridade do profissional.

### Regra

> **O sistema pode ajudar a pessoa a pensar e agir; não deve substituir a autoridade humana quando ela é necessária.**

---

# 17. Contexto antes da ação

Antes de apresentar uma ação, o ACOLHE deve procurar compreender o contexto relevante.

```text
Contexto
   ↓
Necessidade
   ↓
Estado da jornada
   ↓
Regras
   ↓
Opções disponíveis
   ↓
Próximo passo
```

A mesma solicitação pode produzir caminhos diferentes dependendo de:

* situação do paciente;
* estágio da jornada;
* serviço disponível;
* instituição;
* autorização;
* urgência;
* modalidade;
* informações existentes.

---

# 18. Evidência antes de conclusões

Informações importantes da jornada devem possuir contexto e origem identificáveis quando necessário.

O sistema deve distinguir:

* informação fornecida pelo paciente;
* informação registrada por profissional;
* documento;
* resultado de exame;
* evento do sistema;
* informação proveniente de integração;
* interpretação;
* recomendação;
* decisão humana.

O ACOLHE não deve transformar automaticamente uma informação em verdade clínica apenas porque ela está armazenada no sistema.

---

# 19. Privacidade por arquitetura

Privacidade não deve ser tratada somente como configuração administrativa.

Ela deve estar presente no desenho do sistema.

O acesso a dados deve considerar:

* finalidade;
* contexto;
* escopo;
* necessidade;
* autorização;
* rastreabilidade;
* retenção;
* compartilhamento;
* governança.

### Regra

> **Ter acesso técnico a um dado não significa ter motivo para acessá-lo.**

---

# 20. Cada acesso relevante deve ser explicável

O ACOLHE deve permitir responder:

* quem acessou;
* qual paciente estava envolvido;
* em qual contexto;
* qual recurso foi acessado;
* qual ação foi realizada;
* quando aconteceu;
* por qual canal;
* sob qual autorização;
* quando aplicável, qual finalidade estava associada.

A auditabilidade deve fazer parte do produto e não ser apenas uma preocupação posterior de infraestrutura.

---

# 21. O paciente não deve repetir o que o sistema já sabe

Quando uma informação válida já estiver disponível e puder ser reutilizada legitimamente, o sistema deve evitar exigir que a pessoa a forneça novamente sem necessidade.

Isso reduz:

* esforço;
* erros;
* frustração;
* inconsistências;
* abandono da jornada.

### Regra

> **Informação útil deve acompanhar a jornada dentro dos limites de acesso permitidos.**

---

# 22. O profissional também merece uma jornada simples

O princípio de pessoa antes do sistema não se aplica apenas ao paciente.

Profissionais também não devem precisar lutar contra o sistema para realizar seu trabalho.

O ACOLHE deve procurar:

* apresentar contexto relevante;
* reduzir duplicidade de registros;
* diminuir tarefas administrativas desnecessárias;
* preservar continuidade;
* tornar pendências visíveis;
* facilitar colaboração;
* respeitar responsabilidades profissionais.

Um sistema que simplifica a experiência do paciente transferindo toda a complexidade para o profissional também falha no princípio de cuidado.

---

# 23. Cuidado, ensino e pesquisa coexistem com governança própria

No contexto de hospital universitário, o ACOLHE deve reconhecer que existem diferentes finalidades legítimas:

```text
CUIDADO
ENSINO
PESQUISA
```

Essas finalidades podem compartilhar infraestrutura e contexto, mas não devem compartilhar automaticamente todos os direitos de acesso.

Cada finalidade deve possuir:

* contexto;
* regras;
* responsabilidades;
* permissões;
* governança;
* rastreabilidade.

---

# 24. A realidade vem antes do código

O ACOLHE deve seguir o princípio:

> **Reality-First Development.**

Antes de construir uma solução, deve-se procurar compreender:

* como a pessoa realmente chega ao serviço;
* o que ela precisa;
* onde encontra dificuldade;
* quem participa;
* quais informações existem;
* quais informações faltam;
* quais regras realmente são aplicadas;
* quais exceções acontecem;
* como o trabalho realmente ocorre.

A documentação deve representar a realidade suficientemente bem para que o software possa ser construído sobre ela.

---

# 25. Documentação antes da implementação

O ACOLHE deve seguir:

```text
Realidade
   ↓
Observação
   ↓
Documentação
   ↓
Contrato
   ↓
Domínio
   ↓
Backend
   ↓
API
   ↓
Mobile/Web
   ↓
Teste
   ↓
Realidade
```

Código não deve ser usado como substituto de decisão arquitetural.

Antes da implementação relevante, devem existir:

* contexto;
* objetivo;
* contrato;
* regras;
* invariantes;
* fluxos;
* critérios de aceitação;
* estratégia de validação.

---

# 26. Mobile, backend e web evoluem em paralelo

O mobile não deve ser tratado como uma etapa posterior.

Ele é também um instrumento de descoberta e validação da realidade.

Uma vertical slice deve procurar conectar:

```text
Domínio
   ↓
Backend
   ↓
API
   ↓
Mobile
   ↓
Web
   ↓
Teste real
```

A implementação deve permitir que a equipe experimente jornadas reais o mais cedo possível.

---

# 27. Vertical Slice antes de grandes camadas isoladas

O ACOLHE deve preferir construir jornadas verticais completas em vez de desenvolver grandes blocos técnicos isolados.

Uma vertical slice deve atravessar, quando aplicável:

* domínio;
* aplicação;
* infraestrutura;
* API;
* autenticação;
* autorização;
* mobile;
* web;
* testes;
* observabilidade;
* experiência real.

### Regra

> **Uma pequena jornada funcionando na realidade vale mais que uma grande infraestrutura sem jornada executável.**

---

# 28. Contratos antes de implementação

Cada contexto relevante deve possuir contratos claros antes da implementação.

Um contrato deve estabelecer, conforme aplicável:

* propósito;
* responsabilidades;
* entradas;
* saídas;
* invariantes;
* regras;
* eventos;
* estados;
* permissões;
* erros;
* auditoria;
* critérios de aceitação.

Isso reduz decisões implícitas escondidas no código.

---

# 29. O sistema deve absorver a complexidade

Quando uma jornada exige interação entre vários serviços, a pessoa não deve precisar coordenar manualmente todos eles sempre que o sistema puder fazer isso de maneira segura.

O ACOLHE deve procurar atuar como coordenador da jornada.

```text
Pessoa
  ↓
Necessidade
  ↓
ACOLHE
  ├── Serviço A
  ├── Serviço B
  ├── Serviço C
  └── Profissional
  ↓
Jornada coordenada
```

A complexidade operacional deve ser tratada internamente sempre que isso não comprometer segurança, transparência ou autonomia.

---

# 30. Transparência sem sobrecarregar

O sistema deve esconder complexidade operacional, mas não deve esconder decisões relevantes.

A pessoa deve conseguir compreender:

* o que está acontecendo;
* por que uma etapa existe, quando necessário;
* o que precisa fazer;
* o que o sistema está aguardando;
* quem precisa agir;
* qual é o próximo passo;
* quando houver impedimento, qual é sua natureza.

### Regra

> **Esconder complexidade não significa esconder informação importante.**

---

# 31. Autonomia com apoio

O ACOLHE deve permitir que a pessoa faça o máximo que conseguir sozinha, sem transformar autonomia em abandono.

A experiência deve combinar:

```text
Autonomia
    +
Orientação
    +
Acessibilidade
    +
Apoio humano
```

Quando a pessoa não consegue concluir uma etapa sozinha, o sistema deve procurar oferecer caminhos de apoio.

---

# 32. Falhas devem possuir caminho de recuperação

Uma jornada não termina porque uma operação falhou.

O sistema deve considerar:

* erro técnico;
* indisponibilidade de serviço;
* documento ausente;
* informação inconsistente;
* autorização insuficiente;
* falta de vaga;
* cancelamento;
* mudança de contexto;
* abandono temporário.

Quando possível, deve apresentar:

```text
O que aconteceu
      ↓
O que foi preservado
      ↓
O que precisa acontecer
      ↓
Como continuar
```

---

# 33. Segurança não pode destruir a experiência

Segurança deve proteger a pessoa sem criar obstáculos desnecessários.

O ACOLHE deve procurar equilíbrio entre:

* proteção;
* privacidade;
* autenticação;
* autorização;
* acessibilidade;
* simplicidade;
* continuidade.

A solução de segurança deve considerar o contexto da jornada, e não apenas a conveniência técnica.

---

# 34. Integração deve preservar contexto

Quando o ACOLHE se integrar com outros sistemas, não deve tratar integração apenas como troca de dados.

Uma integração deve preservar, quando aplicável:

* identidade;
* paciente;
* contexto;
* origem;
* finalidade;
* temporalidade;
* estado;
* proveniência;
* autorização.

### Regra

> **Interoperabilidade sem contexto pode transportar dados sem transportar significado.**

---

# 35. Dados devem possuir significado

O ACOLHE não deve considerar dado como simples campo armazenado.

Um dado relevante deve poder ser compreendido em relação a:

* quem;
* o quê;
* quando;
* onde;
* contexto;
* origem;
* finalidade;
* estado;
* relacionamento com a jornada.

O valor de um dado está também no contexto que permite interpretá-lo corretamente.

---

# 36. Evoluir sem perder a história

A jornada é temporal.

O sistema deve preservar, quando necessário, a distinção entre:

* estado atual;
* estados anteriores;
* eventos;
* decisões;
* documentos;
* alterações;
* responsáveis.

Não se deve simplesmente sobrescrever a realidade anterior quando sua preservação for necessária para continuidade, auditoria ou segurança.

---

# 37. Aprender com a realidade

O ACOLHE deve evoluir a partir da observação da utilização real.

```text
Vida real
   ↓
Observação
   ↓
Evidência
   ↓
Aprendizado
   ↓
Ajuste
   ↓
Nova validação
```

Feedback de pacientes, profissionais e operadores deve ser tratado como insumo para evolução do produto.

O objetivo não é construir uma arquitetura perfeita no papel, mas uma plataforma que melhore continuamente sem perder seus contratos fundamentais.

---

# 38. Tecnologia é meio, não fim

Nenhuma tecnologia deve ser adotada simplesmente porque é nova, popular ou sofisticada.

A pergunta principal deve ser:

> **“Qual problema real da jornada isso resolve?”**

Tecnologia deve ser avaliada por:

* valor para a pessoa;
* segurança;
* confiabilidade;
* manutenção;
* interoperabilidade;
* custo;
* escalabilidade necessária;
* observabilidade;
* impacto operacional;
* capacidade de evolução.

### Regra

> **Se a tecnologia não melhora a realidade da jornada, sua complexidade precisa ser questionada.**

---

# 39. Não construir complexidade antes da necessidade

O ACOLHE deve evitar antecipar abstrações, módulos e infraestrutura sem evidência de necessidade.

A arquitetura deve ser:

* sólida;
* explícita;
* evolutiva;
* orientada ao domínio;
* proporcional à realidade observada.

Isso não significa construir de forma improvisada.

Significa construir com contratos claros e evoluir quando a realidade exigir.

---

# 40. O produto deve ser orientado à confiança

Em saúde, confiança é parte da experiência.

O sistema deve buscar transmitir:

* clareza;
* previsibilidade;
* responsabilidade;
* rastreabilidade;
* segurança;
* respeito à autonomia;
* transparência.

A interface não deve criar falsa certeza quando uma informação é:

* incompleta;
* provisória;
* dependente de validação;
* sujeita a decisão profissional;
* indisponível.

---

# 41. O ACOLHE deve ajudar sem assumir a vida da pessoa

O objetivo do produto não é controlar a jornada da pessoa.

É ajudá-la a compreendê-la e atravessá-la.

Portanto:

```text
ACOLHE
   ↓
Contextualiza
   ↓
Explica
   ↓
Orienta
   ↓
Facilita
   ↓
Acompanha
```

sem transformar isso em:

```text
ACOLHE
   ↓
Decide tudo
   ↓
Age sem autorização
   ↓
Substitui pessoas
```

---

# 42. Regra de ouro

Todos os princípios anteriores podem ser resumidos em uma pergunta:

> **“Estamos tornando a jornada da pessoa mais simples, clara, acessível, segura e contínua?”**

Se uma decisão técnica, funcional ou de produto tornar a jornada significativamente pior sem uma justificativa necessária, a decisão deve ser reavaliada.

---

# 43. Contrato de Produto

Os princípios do ACOLHE estabelecem os seguintes compromissos:

1. **Pessoa antes do sistema.**
2. **Necessidade antes do serviço.**
3. **Jornada antes do CRUD.**
4. **Próximo passo antes da complexidade.**
5. **Continuidade antes da fragmentação.**
6. **O canal não define o direito de acesso.**
7. **Acessibilidade é arquitetura.**
8. **Identidade não é autorização.**
9. **Acesso deve ser contextual.**
10. **Representação deve ser explícita, limitada e auditável.**
11. **Inteligência deve ajudar, não assumir autoridade.**
12. **Evidência e contexto devem preceder conclusões.**
13. **Privacidade deve existir por arquitetura.**
14. **Cuidado, ensino e pesquisa possuem governança própria.**
15. **A realidade vem antes do código.**
16. **Documentação e contratos precedem implementação.**
17. **Mobile, backend e web devem evoluir em conjunto.**
18. **Vertical slices devem validar jornadas reais.**
19. **O sistema deve absorver complexidade sempre que possível.**
20. **Transparência deve acompanhar a simplificação.**
21. **O profissional também deve possuir uma jornada adequada.**
22. **Falhas devem possuir caminhos de recuperação.**
23. **Integrações devem preservar contexto.**
24. **Dados devem possuir significado.**
25. **A evolução deve preservar a história necessária.**
26. **O produto deve aprender com a realidade.**
27. **Tecnologia é meio, não fim.**
28. **O ACOLHE deve ajudar sem assumir a vida da pessoa.**

---

# 44. Princípio final

> **O ACOLHE existe para fazer o sistema trabalhar para a pessoa.**

Quando a pessoa precisa compreender o sistema para conseguir ser cuidada, existe uma oportunidade de melhoria.

Quando o sistema compreende a necessidade, organiza o contexto, reduz a complexidade, mostra o próximo passo e preserva a continuidade, ele está cumprindo seu propósito.

**ACOLHE — Deixa eu te ajudar.**
