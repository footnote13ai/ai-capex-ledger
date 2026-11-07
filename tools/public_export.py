"""Build the public ledger files from the internal master.

Usage: python3 tools/public_export.py MASTER.csv
Writes data/ledger-master.csv and updates the Ledger sheet in data/ai-capex-ledger.xlsx.
Values are never changed; only internal workflow remarks (approvals, queue and
post references, to-do flags) are removed from the notes and source columns.
"""
import csv, re, sys, openpyxl

NOTE_RULES = [
    (r"Approved( by David)?( \d{1,2} [A-Z][a-z]{2})?( \(ledger-pending\))?\.?", ""),
    (r"REFRESH from Q3 10-Q\.?", ""),
    (r"\s*\(rule agreed 7 Nov[^)]*\)", ""),
    (r"Used in published Post #\d+ \([^)]*\)\.?", ""),
    (r"Replaces the >60 figure used in Post #2\.?", ""),
    (r"Refines 883 in the queue\.?", ""),
    (r"Resolves the on-hold \$152bn call figure \(= 130\.5 leases \+ 21\.9 equity-investment funding\), meeting David's verify-vs-10-Q condition of 29 Oct",
     "The $152bn cited on the call = 130.5 leases + 21.9 equity-investment funding"),
]
SOURCE_RULES = [(r"Oracle filings via 3 Nov news log", "Oracle filings, 2-3 Nov 2026")]
INTERNAL = re.compile(r"David|Approved|queue|pending|news log|REFRESH|Post #|rule agreed", re.I)

def tidy(s):
    s = re.sub(r"\s{2,}", " ", s)
    s = re.sub(r"\s+([.;,])", r"\1", s)
    s = re.sub(r"([.;,])\1+", r"\1", s)
    s = re.sub(r"^[\s.;,]+|[\s;,]+$", "", s)
    return s

def clean(text, rules):
    for a, b in rules:
        text = re.sub(a, b, text)
    return tidy(text)

def main(src):
    with open(src, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f)); cols = list(rows[0].keys())
    for r in rows:
        r["notes"] = clean(r["notes"], NOTE_RULES)
        r["source"] = clean(r["source"], SOURCE_RULES)
        left = [c for c in ("notes", "source", "basis") if INTERNAL.search(r[c])]
        if left:
            sys.exit(f"Internal remark left in {left} for {r['company']} {r['metric']}: add a rule")
    with open("data/ledger-master.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n"); w.writeheader(); w.writerows(rows)
    wb = openpyxl.load_workbook("data/ai-capex-ledger.xlsx"); ws = wb["Ledger"]
    assert ws.max_row - 1 == len(rows), "Ledger sheet row count differs from CSV"
    for i, r in enumerate(rows, start=2):
        ws.cell(i, 10).value = r["source"] or None
        ws.cell(i, 12).value = r["notes"] or None
    wb.save("data/ai-capex-ledger.xlsx")
    print(f"{len(rows)} rows written")

if __name__ == "__main__":
    main(sys.argv[1])
