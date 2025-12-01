import pandas as pd


# Excel einlesen
df = pd.read_excel("data/raw/enterprise-attack-v18.1-techniques.xlsx", sheet_name="techniques")

# Wir nehmen an:
# df["ID"]  = z.B. "T1595.001"
# df["name"] = z.B. "Active Scanning: Scanning IP Blocks"

# Haupt-Techniques (ohne Punkt)
main = df[~df["ID"].str.contains(r"\.")].copy()

# Subtechniques (mit Punkt)
subs = df[df["ID"].str.contains(r"\.")].copy()

# Numerischen Subteil extrahieren, z.B. aus "T1548.006" → 6
subs["sub_num"] = subs["ID"].apply(lambda x: int(x.split(".")[1]))

# Sortieren nach: Parent-ID, sub_num
subs = subs.sort_values(by=["ID", "sub_num"])

# Mapping von Technique-ID zu (ID, Name)
main_map = {row["ID"]: row["name"] for _, row in main.iterrows()}

rows = []

for _, row in subs.iterrows():
    sub_id = row["ID"]                              # T1595.001
    parent_id = sub_id.split(".")[0]                # T1595
    main_name = main_map.get(parent_id, "UNKNOWN")  # falls Zuordnung fehlt

    # Sub-Name bereinigen: Alles vor dem ersten ":" entfernen
    raw_sub_name = row["name"]
    if ":" in raw_sub_name:
        sub_name = raw_sub_name.split(":", 1)[1].strip()
    else:
        sub_name = raw_sub_name.strip()

    # z.B.: "T1595 Active Scanning -> T1595.001 Scanning IP Blocks"
    mitre_field = f"{parent_id} {main_name} -> {sub_id} {sub_name}"

    rows.append({
        "IssueKey": "DETE-9",          # existierendes Issue
        "Summary": "CSV-IMPORT",       # Jira verlangt die Spalte Summary
        "MITRE": mitre_field           # Custom-Field-Wert
    })

out = pd.DataFrame(rows)
out.to_csv("data/output/mitre_values.csv", index=False)
