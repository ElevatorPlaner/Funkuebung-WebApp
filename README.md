# Funkübung ELW (Feuerwehr Aidlingen)

- `funkuebung.html`: die App für den ELW-PC (eine Datei, offline lauffähig, wird nicht veröffentlicht)
- `standalone.html`: abgeleitete Fassung ohne Technikfragen per QR-Code und Handy und ohne Übungsleiter-App (eigener Speicherschlüssel `funks_settings`). Wird parallel zur App weiterentwickelt, `funkuebung.html` bleibt das Hauptprojekt.
- `uebungsleiter.html`: Tablet-App für den Übungsleiter (Live-Kontrolle, Fragen und Antworten je Einheit, Dienstabend). Entsteht aus `uebungsleiter.template.html` per `python3 tools/build_uebungsleiter.py`, der Fragenpool wird dabei aus `fragen.html` übernommen. Nur Änderungen an der Vorlage machen, nicht an der erzeugten Datei.
- `fragen.html`: Handy-Seite für die Technikfragen, wird per GitHub Pages unter https ausgeliefert
- Der Fragenpool (`fragen:` im `DATA`-Block) muss in `funkuebung.html`, `fragen.html` und `uebungsleiter.html` identisch sein (`tests/chk.py` prüft das).

## Regel für Änderungen

Jede Änderung an Spiellogik, Modulen, Layout, PDFs oder Texten wird in `funkuebung.html` gemacht und dann in `standalone.html` nachgezogen. Ausnahme: alles rund um Technikfragen (`tq*`, QR-Codes, Kanal, Handy-Seite) gibt es nur in der Hauptversion.

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
    python3 smoke_standalone.py  # Grundablauf der Standalone-Variante
    python3 pdfall.py     # PDFs werden erzeugt, ohne Gedankenstriche
