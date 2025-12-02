import csv
import re
from collections import defaultdict

def parse_csv_to_tactic_map(path):
    tactic_map = defaultdict(set)

    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tactic = row["Tactics"].strip()

            # Hole erste MITRE-ID wie TXXXX oder TXXXX.YYY
            match = re.search(r"T(\d{4})", row["MITRE"])
            if not match:
                continue

            technique_num = match.group(1)   # z.B. "1016"
            tactic_map[tactic].add(technique_num)

    # Ausgabe als gewünschte Zeichenketten
    result = {}
    for tactic, ids in tactic_map.items():
        sorted_ids = sorted(ids)
        regex_group = "(" + "|".join(sorted_ids) + ")"
        result[tactic] = regex_group

    return result


if __name__ == "__main__":
    mapping = parse_csv_to_tactic_map("data/output/mitre_values.csv")

    for tactic, regex_group in mapping.items():
        print(f"{tactic} -> {regex_group}")
