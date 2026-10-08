# Funkübung ELW (Feuerwehr Aidlingen)

- `funkuebung.html`: die App für den ELW-PC (eine Datei, offline lauffähig, wird nicht veröffentlicht)
- `fragen.html`: Handy-Seite für die Technikfragen, wird per GitHub Pages unter https ausgeliefert
- Der Fragenpool (`fragen:` im `DATA`-Block) muss in beiden Dateien identisch sein.

## Handy-Seite veröffentlichen

1. Repo-Einstellungen, Pages, Source: **GitHub Actions**.
2. Der Workflow `.github/workflows/pages.yml` läuft bei jeder Änderung an `fragen.html` auf dem Standard-Branch.
3. Adresse der Seite (ohne Dateinamen) in der App unter Einstellungen, "Technikfragen: Adresse" eintragen:
   `https://elevatorplaner.github.io/Funkuebung-WebApp/`

## Tests

Voraussetzung: Python mit Playwright (`pip install playwright`) und Chromium, außerdem `node` und `pdftotext`.

    cd tests
    python3 statisch.py   # Gedankenstriche, doppelte IDs, Syntax
    python3 chk.py        # Fragenpool in App und Handy-Seite identisch
    python3 qf.py         # Fragenwahl: pro Einheit 6 verschiedene Fragen
    python3 full.py       # kompletter Ablauf mit 1, 2 und 4 Einheiten
    python3 pdfall.py     # PDFs werden erzeugt, ohne Gedankenstriche
