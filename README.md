# SkiFlow — app web de coaching adaptatif

MVP local, responsive et autonome. Aucune installation Node/npm n'est nécessaire pour tester cette version.

## Démarrage ultra simple

### Windows
Double-clique sur `start.bat`.

### macOS / Linux
Lance `./start.sh` dans un terminal.

### Tous systèmes
Dans ce dossier :

```bash
python3 server.py
```

Puis ouvre : **http://localhost:8080**

> Il faut passer par `http://localhost:8080` plutôt que double-cliquer `index.html` pour profiter du manifest et du service worker PWA.

## Parcours de test conseillé

1. Va dans **Planning** et clique sur **Générer un exemple**.
2. Sur la semaine, ouvre une séance du jour depuis le Dashboard et choisis de la décaler, de l'annuler ou de la terminer.
3. Va dans **Forme**, baisse par exemple l'énergie à 4/10 et le sommeil à 5/10, puis clique sur **Enregistrer et réadapter**.
4. Va dans **Coach IA**, clique sur **Exemple**, puis sur **Analyser et adapter**.
5. Dans **Objectifs & cours**, ajoute une compétition ou une grosse journée de cours.
6. Ajoute une **sortie avec des amis** et vérifie qu'elle apparaît dans le micro-cycle.

## Ce que contient le MVP

- Dashboard : forme, charge de la semaine, nombre de séances.
- Planning hebdomadaire responsive.
- Ajout de séances : running, trail, vélo, ski, musculation.
- Sorties sociales comptées comme charge d'entraînement.
- Check-in : sommeil, énergie, courbatures, stress, FC repos.
- Score de forme 0–100.
- Compétitions et priorités A/B/C.
- Contraintes de cours et fatigue scolaire estimée.
- Déplacement, annulation et validation d'une séance.
- Moteur d'adaptation local : baisse d'intensité quand la forme baisse et plafond de 5 séances/semaine.
- Journal des modifications.
- Coach « IA » en mode démo : analyse simple du langage naturel et déclenchement du moteur d'adaptation.
- Stockage local via `localStorage`.
- PWA de base.

## À propos de la vraie IA générative

Cette version n'embarque volontairement aucune clé API dans le navigateur. Le prochain niveau consiste à ajouter un backend sécurisé : l'IA proposerait des actions structurées (JSON), puis le moteur sportif vérifierait les règles avant d'accepter la modification.

## Données

Les données de cette démo restent dans le navigateur. Pour remettre la démo à zéro, efface les données du site `localhost:8080` depuis les réglages du navigateur.
