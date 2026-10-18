# FEMAS HDF – DUERP en ligne

Outil permettant à chaque MSP / CPTS employeuse de réaliser et mettre à jour son
**document unique d'évaluation des risques professionnels (DUERP)**, sur le modèle de
l'[outil d'évaluation des risques de l'Assurance Maladie – Risques professionnels et de l'INRS](https://www.ameli.fr/artois/entreprise/votre-entreprise/outils-gestion-prevention-risques-professionnels/outil-evaluation-des-risques)
(OiRA), adapté aux postes rencontrés en exercice coordonné (accueil / secrétariat,
coordination, soins salariés, entretien, télétravail, déplacements).

## 👉 Utiliser l'outil

**https://femashdf.github.io/duerp/**

1. **Préparer** : renseignez votre structure (employeur, effectif, SPST, personnes associées)
   et l'organisation générale de la prévention.
2. **Identifier** : ajoutez une fiche par unité de travail (modèles proposés). Les risques les
   plus fréquents pour l'unité sont présélectionnés ; passez en revue les autres.
3. **Hiérarchiser** : pour chaque risque, cochez les mesures déjà en place puis cotez
   gravité × fréquence → criticité et priorité (P1 / P2 / P3).
4. **Plan d'actions** : vos actions prévues + les mesures non encore en place, proposées
   par l'outil, à arbitrer.
5. **Éditer** : cliquez sur **Télécharger le DUERP Excel**.
   Pour la mise à jour : **Importer mon DUERP Excel**, modifiez, re-téléchargez.

## Contenu du fichier Excel

| Feuille | Contenu |
|---|---|
| Synthèse | Structure, rappels réglementaires, organisation de la prévention, tableau par unité, **historique des versions** |
| Inventaire des risques | Une ligne par risque identifié et par unité : situations, salariés exposés, mesures existantes, gravité, fréquence, criticité, priorité |
| Plan d'actions | Liste des actions de prévention (< 50 salariés) ou PAPRIPACT (≥ 50), avec responsable, échéance, coût, date de réalisation |
| Annexe – expositions | Données collectives utiles : unités concernées, salariés exposés, proportion de l'effectif (R.4121-1 CT) |
| Grille de cotation | Matrice gravité × fréquence |
| _donnees (masquée) | Données permettant le ré-import |

## Références

* Code du travail : L.4121-1 à L.4121-3-1, L.4122-1, R.4121-1 à R.4121-4, R.4741-1
* ameli.fr Entreprise : [Le DUERP](https://www.ameli.fr/artois/entreprise/sante-travail/prevention/conseils/piloter/declarer-evaluer-duer)
  · [Outils de gestion et prévention des risques professionnels](https://www.ameli.fr/artois/entreprise/votre-entreprise/outils-gestion-prevention-risques-professionnels)
* INRS : démarche d'évaluation des risques, outil OiRA « Travail de bureau et télétravail »

## Confidentialité

* Les réponses **ne quittent pas le navigateur** : aucune donnée n'est envoyée à GitHub ni
  à FEMAS HDF ; le fichier Excel est généré localement.
* Un brouillon est conservé dans le navigateur (stockage local) ; le bouton
  *Effacer les données de ce navigateur* le supprime (à utiliser sur un poste partagé).
* Aucune donnée de santé concernant un salarié ne doit être saisie.
* Suivi d'utilisation : **désactivé** par défaut (voir USAGE dans scripts/generate_page.py).

## Maintenance (FEMAS HDF)

Les unités de travail, risques, mesures et grilles sont définis dans schema/duerp.yml.
Après modification :

    pip install -r requirements.txt
    python scripts/generate_page.py      # régénère docs/index.html

Publication : GitHub Pages, branche main, dossier /docs.
