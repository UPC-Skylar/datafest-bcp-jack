# Datafest - Propensión de conversión

Predicción de la probabilidad de conversión de clientes. Métrica: Gini (2*AUC-1).
Descripción de los datos: ver `DATASET_DESCRIPTION.md`.

## Requisitos (una sola vez)

1. **Git**: https://git-scm.com/downloads
2. **uv** (gestor de entorno; instala Python por ti):
   - Windows (PowerShell): `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`
   - Mac/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`

## Puesta en marcha

```bash
git clone https://github.com/meLuis/datafest-coding-test
cd datafest-coding-test
uv sync                # crea .venv con las versiones exactas de uv.lock
```

**Los datos NO están en el repo** (son sensibles). Pide los 4 CSV al equipo y colócalos en `data/raw/`:
`train.csv`, `test.csv`, `sample_submission.csv`, `metaData.csv`.

## Uso

```bash
uv run jupyter lab                 # abrir notebooks
uv run python src/<script>.py      # ejecutar un script
uv add <paquete>                   # agregar dependencia (actualiza pyproject.toml y uv.lock)
uv run ruff check . && uv run ruff format .
```

No actives el entorno a mano: `uv run` ya usa `.venv`.

## Estructura

```
data/raw/         datos originales (ignorado por git)
data/processed/   datos derivados (ignorado por git)
notebooks/        EDA y experimentos
src/              código reutilizable (features, entrenamiento, predicción)
submissions/      CSV de entrega (ignorado por git)
reports/          métricas y gráficos de cada experimento
```
# datafest-bcp-jack
