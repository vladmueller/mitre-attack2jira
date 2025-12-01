# Readme

Die Tactics und Techniques von [Tactics - Enterprise | MITRE ATT&CK®](https://attack.mitre.org/tactics/enterprise/) sollen in Jira importiert werden,
so dass diese in einem entsprechenden Custom field (Cascading List) ausgewählt werden können.

## Projektstruktur

```
|── data/
│   ├── raw/                   # Originale Excel-Dateien
│   ├── interim/               # Zwischenergebnisse (optionale CSV-Formate zur Prüfung)
│   └── output/                # Endgültige CSV-Dateien für Jira-Import
├── transforms/
│   ├── __init__.py
│   ├── clean_data.py          # z.B. Normalisierung, Umbenennungen, Typkorrekturen
│   ├── map_fields.py          # z.B. Excel-Spalten → Jira-Felder
│   └── generate_outputs.py    # Aufteilung in verschiedene Asset-Typen etc.
├── utils/
│   └── file_io.py             # Wiederverwendbare Lese-/Schreibfunktionen mit csvkit
├── tests/
│   └── test_transformations.py
├── main.py                    # Einstiegspunkt, orchestriert alles
├── requirements.txt           # Abhängigkeiten wie csvkit, pandas etc.
└── README.md                  # Projektbeschreibung, Nutzung, Beispiele
```

## Initial: Python virtuelle Umgebung anlegen und Dependencies installieren

```shell
python3 -m venv venv

.\venv\Scripts\activate

pip install -r .\requirements.txt
```

## CSV-Import in Jira

**Vorbereitung**: In Jira muss manuell ein "Import-Ticket" angelegt werden, welches wir im Jira CSV-Importer verwenden müssen.

z.B.: DETE-1 CSV-IMPORT
