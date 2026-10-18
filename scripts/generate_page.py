"""Met à jour docs/index.html (page GitHub Pages) depuis schema/duerp.yml.

La page fonctionne entièrement dans le navigateur : les réponses ne sont envoyées
nulle part ; le DUERP Excel est produit localement.

Le script remplace, dans docs/index.html, le contenu situé entre les marqueurs
/*SCHEMA*/ ... /*FIN_SCHEMA*/ et /*USAGE*/ ... /*FIN_USAGE*/.

Usage : python scripts/generate_page.py
"""
from __future__ import annotations

import json
import pathlib
import re

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = ROOT / "docs" / "index.html"

# Suivi d'utilisation (facultatif) : None = désactivé.
# Pour l'activer, créer un formulaire Jotform « FEMAS HDF – Suivi d'utilisation du DUERP »
# (champs « structure » et « type de structure ») puis renseigner, par exemple :
# USAGE = {
#     "formId": "<ID du formulaire>",
#     "submitUrl": "https://eu-submit.jotform.com/submit/<ID du formulaire>/",
#     "fields": {"structure": "q2_structure", "type": "q3_typestructure"},
# }
USAGE = None


def inject(html: str, tag: str, value) -> str:
    data = json.dumps(value, ensure_ascii=False)
    new, n = re.subn(rf"/\*{tag}\*/.*?/\*FIN_{tag}\*/", lambda m: f"/*{tag}*/{data}/*FIN_{tag}*/",
                     html, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f"Marqueur /*{tag}*/ introuvable dans {PAGE}")
    return new


def check(schema: dict) -> None:
    ids = {r["id"] for r in schema["risques"]}
    for u in schema["unites"]:
        unknown = set(u.get("risques", [])) - ids
        if unknown:
            raise SystemExit(f"Unité « {u['nom']} » : risques inconnus {sorted(unknown)}")


def main() -> None:
    schema = yaml.safe_load((ROOT / "schema" / "duerp.yml").read_text(encoding="utf-8"))
    check(schema)
    html = PAGE.read_text(encoding="utf-8")
    html = inject(html, "SCHEMA", schema)
    html = inject(html, "USAGE", USAGE)
    PAGE.write_text(html, encoding="utf-8")
    print(f"Mis à jour : {PAGE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
