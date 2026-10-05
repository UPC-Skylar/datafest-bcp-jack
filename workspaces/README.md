# Espacios individuales

Cada integrante trabaja solo dentro de su carpeta:

```
workspaces/antony/
workspaces/vitaly/
workspaces/jack/
workspaces/gabriela/
workspaces/luis/
```

## Reglas

- Nadie edita carpetas ajenas ni `src/common.py`.
- Datos en `data/raw/` (no se suben). Entregas en `submissions/` (no se suben).
- Rama propia: `git switch -c <tu-nombre>`.
- `SEED = 42`.

## Comparación

Todos se evalúan con el mismo protocolo, definido en `src/common.py`:

- Entrenamiento: `mes <= 202610`
- Validación: `mes == 202611`
- Métrica: Gini = 2 * AUC - 1

```python
import sys; sys.path.insert(0, "../../src")
from common import load_data, temporal_split, gini, check_submission, SEED

train, test, sample = load_data()
fit, valid = temporal_split(train)
# ... tu modelo ...
print(gini(valid["objetivo"], pred_valid))
```

Entrega final: CSV `id_cliente,prediccion` validado con `check_submission(submission, test)`.
