#!/usr/bin/env python3
"""
ACOLHE — Script de criação da estrutura arquitetural oficial (v2).

Compatível com Windows, Linux e macOS.
Sem emojis para evitar UnicodeEncodeError em terminais cp1252.
"""

import argparse
import sys
import traceback
from pathlib import Path


# ============================================================
# ESTRUTURA OFICIAL DO ACOLHE
# ============================================================

ESTRUTURA_ACOLHE = [
    ("00 - vision",                 "Propósito, visão e contrato central", "Fundamentos (00-04)"),
    ("01 - reality-first",          "Realidade antes da arquitetura",      "Fundamentos (00-04)"),
    ("02 - domain-blueprint",       "Linguagem, domínio e blueprint",      "Fundamentos (00-04)"),
    ("03 - patient-journey",        "Jornada da pessoa como eixo",         "Fundamentos (00-04)"),
    ("04 - patient",                "O paciente como sujeito central",     "Fundamentos (00-04)"),
    ("05 - patient-needs",          "Entrada da necessidade",              "Entrada da necessidade (05-06)"),
    ("06 - patient-services",       "Serviços que respondem às necessidades", "Entrada da necessidade (05-06)"),
    ("07 - healthcare-network",     "Rede de saúde e conexões",            "Rede e cuidado (07-17)"),
    ("08 - professional",           "Profissionais e suas autoridades",    "Rede e cuidado (07-17)"),
    ("09 - scheduling",             "Agendamento e coordenação temporal",  "Rede e cuidado (07-17)"),
    ("10 - reception-and-access",   "Recepção e controle de acesso",       "Rede e cuidado (07-17)"),
    ("11 - clinical-care",          "Assistência clínica",                 "Rede e cuidado (07-17)"),
    ("12 - medical-record",         "Prontuário e registro clínico",       "Rede e cuidado (07-17)"),
    ("13 - clinical-documents",     "Documentos clínicos",                 "Rede e cuidado (07-17)"),
    ("14 - exams",                  "Exames e resultados",                 "Rede e cuidado (07-17)"),
    ("15 - medication",             "Medicação e prescrição",              "Rede e cuidado (07-17)"),
    ("16 - referrals-and-continuity", "Encaminhamentos e continuidade",    "Rede e cuidado (07-17)"),
    ("17 - hospitalization",        "Internação e cuidado hospitalar",     "Rede e cuidado (07-17)"),
    ("18 - education",              "Ensino e formação",                   "Universidade e pesquisa (18-19)"),
    ("19 - research",               "Pesquisa",                            "Universidade e pesquisa (18-19)"),
    ("20 - interoperability",       "Interoperabilidade entre sistemas",   "Plataforma e governança (20-24)"),
    ("21 - identity-and-access",    "Identidade, autenticação e autorização", "Plataforma e governança (20-24)"),
    ("22 - data-platform",          "Plataforma de dados",                 "Plataforma e governança (20-24)"),
    ("23 - notifications",          "Notificações e comunicações",         "Plataforma e governança (20-24)"),
    ("24 - governance",             "Governança institucional",            "Plataforma e governança (20-24)"),
    ("25 - cognitive-system",       "Assistência cognitiva",               "Camada cognitiva (25)"),
    ("26 - evaluation",             "Avaliação do sistema",                "Avaliação (26)"),
]


# ============================================================
# CONTEÚDOS
# ============================================================

README_ACOLHE = """# ACOLHE - Documentação Arquitetural

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
"""

README_VISAO = """# 00 - Vision

## Propósito

Definir o propósito, a visão e o contrato central do ACOLHE.

## Contrato central

> O ACOLHE organiza o sistema de saúde ao redor da jornada da pessoa,
> transformando necessidades em serviços, serviços em ações e ações em
> continuidade de cuidado.

## Documentos deste contexto

- [ ] visao.md - visão de longo prazo
- [ ] contrato-central.md - contrato arquitetural
- [ ] principios.md - princípios arquiteturais
- [ ] glossario.md - linguagem ubíqua inicial
- [ ] nao-objetivos.md - o que o ACOLHE não é

## Critério de conclusão

Este contexto está fechado quando os contratos fundamentais estão
documentados e validados antes de avançar para `01 - reality-first`.
"""


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def log(msg: str) -> None:
    """Print seguro contra UnicodeEncodeError."""
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode("ascii", "replace").decode("ascii"))


def criar_pasta(caminho: Path, dry_run: bool = False) -> bool:
    """Cria uma pasta (e pais) se não existir. Retorna True/False."""
    if dry_run:
        log(f"  [dry-run] [DIR] {caminho}")
        return True
    try:
        caminho.mkdir(parents=True, exist_ok=True)
        return True
    except OSError as e:
        log(f"  [ERRO] Falha ao criar pasta {caminho}: {e}")
        return False


def criar_arquivo(caminho: Path, conteudo: str, dry_run: bool = False,
                  sobrescrever: bool = False) -> bool:
    """Cria um arquivo com conteúdo. Retorna True/False."""
    if dry_run:
        log(f"  [dry-run] [FILE] {caminho}")
        return True
    if caminho.exists() and not sobrescrever:
        return True  # silencioso: já existe
    try:
        caminho.write_text(conteudo, encoding="utf-8")
        return True
    except OSError as e:
        log(f"  [ERRO] Falha ao criar arquivo {caminho}: {e}")
        return False


# ============================================================
# FUNÇÃO PRINCIPAL
# ============================================================

def criar_estrutura(base: Path, dry_run: bool = False) -> int:
    """Cria a árvore completa do ACOLHE. Retorna contagem de erros."""
    erros = 0

    log("=" * 60)
    log("  ACOLHE - Criando estrutura arquitetural oficial")
    log("=" * 60)
    log(f"\n  Base: {base.absolute()}\n")

    # Garantir que a base existe
    if not base.exists():
        if dry_run:
            log(f"  [dry-run] [DIR] {base}")
        else:
            try:
                base.mkdir(parents=True, exist_ok=True)
            except OSError as e:
                log(f"  [ERRO] Não foi possível criar a base {base}: {e}")
                return 1

    docs = base / "docs"

    # 1. Pasta raiz docs/
    log("[1/4] Criando pasta raiz 'docs/'...")
    if not criar_pasta(docs, dry_run):
        erros += 1

    # 2. README raiz
    log("[2/4] Criando README principal...")
    if not criar_arquivo(docs / "README.md", README_ACOLHE, dry_run):
        erros += 1

    # 3. Cada contexto
    log(f"\n[3/4] Criando {len(ESTRUTURA_ACOLHE)} contextos...\n")

    eixo_atual = None
    for nome, descricao, eixo in ESTRUTURA_ACOLHE:
        if eixo != eixo_atual:
            eixo_atual = eixo
            log(f"  -- {eixo_atual} --")

        pasta = docs / nome
        if not criar_pasta(pasta, dry_run):
            erros += 1
            continue

        conteudo = (
            f"# {nome}\n\n"
            f"## Descrição\n\n{descricao}\n\n"
            f"## Eixo\n\n{eixo}\n"
        )
        if not criar_arquivo(pasta / "README.md", conteudo, dry_run):
            erros += 1

    # 4. README detalhado de 00 - vision (sobrescreve)
    log("\n[4/4] Aplicando README detalhado de '00 - vision'...")
    if not criar_arquivo(
        docs / "00 - vision" / "README.md",
        README_VISAO,
        dry_run,
        sobrescrever=True,
    ):
        erros += 1

    # Resumo
    log("\n" + "=" * 60)
    if erros == 0:
        log("  [OK] Estrutura criada com sucesso!")
    else:
        log(f"  [AVISO] Concluído com {erros} erro(s).")
    log("=" * 60)
    log(f"\n  Total de contextos: {len(ESTRUTURA_ACOLHE)}")
    log(f"  Local: {docs.absolute()}")
    log(f"\n  Próximo passo: abrir '00 - vision/' e preencher os contratos.\n")

    return erros


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Cria a estrutura arquitetural oficial do ACOLHE."
    )
    parser.add_argument(
        "--base",
        type=Path,
        default=Path.cwd(),
        help="Diretório base onde 'docs/' será criado (padrão: atual)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Apenas mostra o que seria criado",
    )
    args = parser.parse_args()

    try:
        erros = criar_estrutura(args.base, dry_run=args.dry_run)
        return 0 if erros == 0 else 1
    except KeyboardInterrupt:
        log("\n[INTERROMPIDO] Cancelado pelo usuário.")
        return 130
    except Exception:
        log("\n[ERRO FATAL]")
        traceback.print_exc()
        return 2


if __name__ == "__main__":
    sys.exit(main())
