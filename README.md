# Funkübung ELW (Feuerwehr Aidlingen)

- `funkuebung.html`: die App für den ELW-PC (eine Datei, offline lauffähig, wird nicht veröffentlicht)
- `fragen.html`: Handy-Seite für die Technikfragen, wird per GitHub Pages unter https ausgeliefert
- Der Fragenpool (`fragen:` im `DATA`-Block) muss in beiden Dateien identisch sein.

## Handy-Seite veröffentlichen

1. Repo-Einstellungen, Pages, Source: **GitHub Actions**.
2. Der Workflow `.github/workflows/pages.yml` läuft bei jeder Änderung an `fragen.html` auf dem Standard-Branch.
3. Adresse der Seite (ohne Dateinamen) in der App unter Einstellungen, "Technikfragen: Adresse" eintragen:
   `https://elevatorplaner.github.io/Funkuebung-WebApp/`
