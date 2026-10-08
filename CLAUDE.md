# Funkübung ELW (Feuerwehr Aidlingen): Regeln für Claude

Privates Projekt von Christian Görlich (Feuerwehr Aidlingen, ELW-Team). Mit Christian per Du, locker, auf Deutsch. Kein Aufzug- oder Firmenvokabular.

## Dateien

- `funkuebung.html`: Hauptprojekt (Funkübung ELW V2, Drive: `Funkuebung_ELW_V2.html`)
- `standalone.html`: Variante ohne Technikfragen per QR-Code und Handy und ohne Übungsleiter-App. Wird parallel zur Hauptversion weiterentwickelt, jede Änderung an Spiellogik, Modulen, Layout, PDFs und Texten dort nachziehen.
- `fragen.html`: Handy-Seite der Einheiten (GitHub Pages)
- `uebungsleiter.template.html` -> `uebungsleiter.html`: Tablet-App des Übungsleiters, per `python3 tools/build_uebungsleiter.py` bauen. Nur die Vorlage bearbeiten.
- Fragenpool in `funkuebung.html`, `fragen.html` und `uebungsleiter.html` muss identisch sein (`tests/chk.py`). Neue Fragen erst mit Christian im Chat abstimmen.
- Tests: siehe `README.md`. Nach jeder Änderung `tests/statisch.py`, `tests/chk.py`, `tests/full.py` und `tests/smoke_standalone.py` laufen lassen.

## Schreibregeln

- Keine Gedankenstriche (weder lang noch kurz), auch nicht in App-Texten und PDFs.
- Keine KI-typischen Muster: keine Floskeln, Superlative, erzwungenen Gegensatzpaare, kein Marketing-Sprech.
- Rolle heißt "Übungsleiter" (nicht Ausbilder). "Kommunikatoren ELW" überall. "Kommunikatoren im ELW" nur als Beschriftung über den Namensfeldern und vor den Namen in der Tablet-Kopfzeile (dort mit Doppelpunkt). Schritt 1 heißt "Rufgruppe und Funkcheck".
- Fahrzeug ist gleich Einheit.

## Gestaltung

- Ausrichtung ist Pflicht, horizontal und vertikal: Pillen, Felder, Buttons und Überschriften in einer Reihe haben dieselbe Höhe, gleiche Breiten bei gleicher Funktion (über Kästen hinweg) und bündige Kanten. Vor jedem Commit mit Screenshot prüfen.
- Pillen: `.hpill` 30 px hoch, mindestens 96 px breit (Abstand in der Kopfzeile der Kästen 8 px, sonst läuft sie bei 4 Einheiten über). Fahrzeug-Pille `.tp` 30 px hoch, 220 px breit, gelb. TMO blau, DMO grün (`.mp`).
- Module: identische Ausrichtung der Felder, Überschriften, Hilfetexte und roten Buttons. Hilfetexte klein unter den roten Buttons.
- Neue visuelle Ideen erst als Bild oder Mockup zeigen, dann einbauen. Christian entscheidet gern zwischen Varianten.
- PDFs auf möglichst wenig Seiten, Fließtext im Blocksatz, in neuem Tab öffnen.
- Schwebende Scrollbars. Bei mehreren Einheiten scrollt nur der Einheiten-Bereich, nie die Kopfzeile.
- Das Tablet-Design (Übungsleiter) muss der Haupt-App sehr ähnlich sehen (Kopfzeile, Pillen, Kästen).

## Arbeitsweise

- Fragen im Chat kurz beantworten, Vorschläge mit Empfehlung, bei Unklarheit nachfragen statt raten.
- Das private Google Drive darf in diesem Projekt als Quelle dienen, im Geschäftskontext (Die Aufzugsplaner GmbH) niemals. Drive-Dateien kann ich nur lesen, nicht überschreiben: Christian holt sich neue Fassungen per `raw.githubusercontent.com`-Link aus dem Repo.
- Anleitungen oder Prompts für Claude gibt Christian als `.md`-Datei aus.
- Die Auswertung wird nicht in der App korrigiert. Fehler bespricht der Übungsleiter mündlich mit den Einheiten, die erfassten Daten bleiben unverändert.
