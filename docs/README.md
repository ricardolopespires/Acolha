# ACOLHE - Documentação Arquitetural

> O ACOLHE organiza o sistema de saúde ao redor da jornada da pessoa,
> transformando necessidades em serviços, serviços em ações e ações em
> continuidade de cuidado.

## Princípio estrutural

    Pessoa
      -> Necessidade
      -> Serviço
      -> Jornada
      -> Cuidado
      -> Continuidade

## Eixos arquiteturais

| Faixa | Eixo |
|-------|------|
| 00-04 | Fundamentos |
| 05-06 | Entrada da necessidade |
| 07-17 | Rede e cuidado |
| 18-19 | Universidade e pesquisa |
| 20-24 | Plataforma e governança |
| 25    | Cognitive System |
| 26    | Evaluation |

## Princípios arquiteturais

1. Pessoa antes do sistema.
2. Jornada antes do CRUD.
3. Necessidade antes do serviço.
4. Contexto antes da permissão.
5. Permissão antes da ação.
6. Acessibilidade como capacidade transversal.
7. O canal não define o direito de acesso.
8. Autenticação não é autorização.
9. Acesso delegado possui escopo, validade e auditoria.
10. Decisões clínicas permanecem sob autoridade profissional.
11. Ensino e pesquisa possuem governança própria.
12. Tecnologia é meio, não fim.
13. Mobile, web e atendimento presencial devem expressar a mesma jornada.
14. A realidade do paciente valida a arquitetura.
15. Docs before code.
16. Cada vertical slice deve atravessar domínio, backend, experiência e validação real.
