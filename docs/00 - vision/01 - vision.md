# 00 - Vision

## Propósito

O módulo `00 - vision` define a direção fundamental do ACOLHE.

Ele estabelece **por que o ACOLHE existe, onde pretende chegar, quais princípios orientam suas decisões e quais objetivos estratégicos conduzem sua evolução**.

Este módulo é o ponto de partida para todos os demais contratos arquiteturais do projeto.

---

## Estrutura

```text
00 - vision/

├── README.md
├── 🔴 vision.md
├── 🔴 mission.md
├── 🔴 manifesto.md
├── 🔴 product-principles.md
└── 🔴 strategic-objectives.md
```

### Documentos

| Documento                 | Propósito                                                            | Status |
| ------------------------- | -------------------------------------------------------------------- | ------ |
| `vision.md`               | Define a visão de futuro do ACOLHE                                   | 🔴     |
| `mission.md`              | Define a razão de existir e o propósito do ACOLHE                    | 🔴     |
| `manifesto.md`            | Define as crenças, compromissos e posições fundamentais do produto   | 🔴     |
| `product-principles.md`   | Define os princípios que orientam produto, experiência e arquitetura | 🔴     |
| `strategic-objectives.md` | Define os objetivos estratégicos que orientam a evolução do ACOLHE   | 🔴     |

---

## Papel do módulo

O `00 - vision` não define:

* modelos de domínio;
* entidades;
* APIs;
* banco de dados;
* tecnologias;
* implementação;
* fluxos operacionais específicos;
* decisões clínicas.

Esses elementos pertencem aos módulos posteriores.

O módulo define **direção**, não implementação.

---

## Princípio fundamental

> **Tecnologia é meio, não fim.**

O ACOLHE deve utilizar tecnologia para reduzir a complexidade enfrentada pela pessoa ao buscar cuidado e serviços de saúde.

A arquitetura deve servir à realidade da pessoa, e não obrigar a pessoa a compreender a arquitetura do sistema.

---

## Posicionamento

**ACOLHE**

**Categoria:** Plataforma de Jornada em Saúde

**Princípio de interação:**

> **“Deixa eu te ajudar.”**

**Pergunta de entrada:**

> **“Como podemos ajudar?”**

**Foco:**

```text
Pessoa
   ↓
Necessidade
   ↓
Serviço
   ↓
Jornada
   ↓
Cuidado
   ↓
Continuidade
```

---

## Visão arquitetural

O ACOLHE não deve ser concebido como um conjunto de módulos administrativos independentes.

A arquitetura deve representar a jornada real da pessoa.

```text
                    PESSOA
                       │
                       ▼
                  NECESSIDADE
                       │
                       ▼
                    SERVIÇO
                       │
                       ▼
                    JORNADA
                       │
                       ▼
                    CUIDADO
                       │
                       ▼
                 CONTINUIDADE
```

Os módulos do sistema existem para sustentar essa jornada.

---

## Reality-First

A visão do ACOLHE está diretamente ligada ao princípio **Reality-First**.

A evolução do produto deve seguir:

```text
Vida real
    ↓
Observação
    ↓
Documentação
    ↓
Domínio
    ↓
Implementação
    ↓
Backend + Web + Mobile
    ↓
Teste na vida real
    ↓
Aprendizado
    ↓
Refinamento
    ↓
Nova validação
```

O sistema não deve ser considerado correto apenas porque está tecnicamente implementado.

Ele precisa funcionar na realidade das pessoas que utilizarão o serviço.

---

## Desenvolvimento por Vertical Slices

O ACOLHE será desenvolvido através de fatias verticais que atravessam diferentes camadas do produto.

Uma slice pode envolver:

```text
Domínio
   +
Backend
   +
API
   +
Web
   +
Mobile
   +
Testes
   +
Experiência real
```

Uma capacidade só deve ser considerada concluída quando houver coerência entre essas dimensões.

---

## Mobile como instrumento de descoberta

O aplicativo mobile não será tratado apenas como uma interface de apresentação.

Ele também será utilizado como instrumento de:

* descoberta do domínio;
* validação da jornada;
* teste de acessibilidade;
* observação da experiência;
* validação de autenticação;
* validação de contexto de acesso;
* experimentação de fluxos reais.

Por isso, **mobile e backend serão desenvolvidos em paralelo** sempre que uma vertical slice exigir validação prática.

---

## Acessibilidade

A acessibilidade é um princípio estrutural do ACOLHE.

O mesmo serviço deve poder ser utilizado por pessoas com diferentes necessidades de acesso, incluindo:

* deficiência visual;
* deficiência auditiva;
* mobilidade reduzida;
* idosos;
* baixa alfabetização digital;
* dificuldades cognitivas;
* pacientes dependentes de cuidador;
* pessoas sem acesso constante à internet.

A necessidade de acessibilidade deve modificar **a forma de interação**, não reduzir automaticamente os direitos ou permissões da pessoa.

---

## Identidade e acesso

O ACOLHE separa:

```text
Identidade
    ↓
Contexto
    ↓
Nível de acesso
    ↓
Escopo
    ↓
Ação
```

Os níveis fundamentais de acesso definidos para o produto são:

```text
Nível 0 — Identificação
Nível 1 — Acesso Pessoal
Nível 2 — Ações de Jornada
Nível 3 — Documentos e Informações
Nível 4 — Acesso Delegado
Nível 5 — Acesso Profissional
Nível 6 — Acesso Especial
```

O módulo `02 - identity-and-access` será responsável por transformar esses princípios em contratos arquiteturais verificáveis.

---

## Contexto inicial

O ACOLHE nasce orientado à realidade de:

* rede pública de saúde;
* hospital universitário;
* organizações sem fins lucrativos;
* pacientes e famílias;
* profissionais de saúde;
* estudantes e residentes;
* cuidadores e representantes autorizados.

Esse contexto inicial **não limita a visão futura da plataforma**.

A arquitetura deve permitir evolução para diferentes organizações, serviços, unidades e redes de cuidado.

---

## Relação com os demais módulos

O módulo `00 - vision` fornece direção para todos os demais módulos.

```text
00 - vision
      │
      ├── 01 - reality-first
      ├── 02 - identity-and-access
      ├── 03 - domain-blueprint
      ├── 04 - patient-journey
      ├── 05 - patient
      ├── 06 - patient-needs
      ├── 07 - patient-services
      ├── ...
      ├── 25 - cognitive-system
      └── 26 - evaluation
```

Nenhum módulo posterior deve contradizer os contratos estabelecidos em `00 - vision`.

Quando uma decisão posterior exigir mudança de direção, o impacto deve ser explicitamente avaliado e a documentação correspondente deve ser atualizada.

---

## Critério de maturidade

Os documentos deste módulo seguem o padrão:

```text
🔴 Documento não iniciado
🟡 Documento em construção
🟢 Contrato arquitetural fechado
```

Um documento somente deve receber status **🟢** quando seu conteúdo estiver suficientemente definido para orientar decisões posteriores sem ambiguidades fundamentais.

---

## Próximos documentos

A construção deste módulo seguirá:

```text
01. vision.md
       ↓
02. mission.md
       ↓
03. manifesto.md
       ↓
04. product-principles.md
       ↓
05. strategic-objectives.md
```

Após o fechamento do módulo `00 - vision`, avançaremos para `01 - reality-first`.
