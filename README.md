# AI Capex Ledger

Open dataset from [Footnote 13](https://footnote13.substack.com): operating cash flow vs all-in capital spending (incl. finance leases) for Microsoft, Alphabet, Amazon, Meta and Oracle, quarter by quarter, plus leases signed but not yet commenced, debt, credit spreads, backlog and guidance. Neoclouds and chip suppliers are recorded alongside but never added into the Big Five totals.

Live page: https://ledger.footnote13.com

## Files
- `data/ledger-master.csv`: one row per fact (company, metric, calendar and fiscal period, value, unit, basis, source, as-of date, notes). The page reads this file directly.
- `data/ai-capex-ledger.xlsx`: Excel export with formulas (Ledger, Quarterly, Combined, Hidden leases, Companies, Changelog).
- `index.html`: the page (what changed, company summaries, cash ledger, combined ratio, hidden leases, row browser, downloads).
- `tools/public_export.py`: builds the public CSV and the workbook's Ledger sheet from Footnote 13's internal master. Values are copied unchanged; internal workflow remarks are removed from notes.

## Groups
1. Big Five (Microsoft, Alphabet, Amazon, Meta, Oracle): the only rows that feed the cash charts.
2. Neoclouds (CoreWeave, Nebius, IREN): rows say "Layer 2" in notes.
3. Chip and hardware suppliers (Nvidia, AMD, Supermicro, Qualcomm, Arm, Marvell): rows say "Layer 3" in notes.

## Method
Cash gap = operating cash flow − all-in capex. All-in capex = cash capex + finance leases as each company reports them (Microsoft: CFO-stated capex incl. finance leases; Meta: principal payments on finance leases; Amazon: P&E acquired under finance leases; Alphabet, Oracle: cash capex only). Calendar quarters; Oracle's fiscal quarters end one month earlier. Leases not yet commenced are undiscounted future payments from the latest 10-Q/10-K. CDS: latest print from any provider, named per row. Rows are append-only: a revised figure is a new row, the old one is kept.

## Licence
Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit "Footnote 13, AI Capex Ledger". Source figures come from public company filings and the reports named in each row.

## Changelog
- 2026-11-12: 12 rows (352 total): CoreWeave Q3 2026 results, backlog, FY26 revenue and capex guidance, total debt (approx., verify vs 10-Q).
- 2026-11-07 (later): internal workflow remarks removed from notes (66 rows; no values changed); line endings normalised.
- 2026-11-07: 61 rows (340 total): bond spreads, ratings, maturities, latest CDS, Meta debt and JV exposure, Alphabet backstops; neoclouds and chip suppliers added. Page: what-changed panel, company summaries, row browser with filtered CSV download, PNG chart downloads, next-quarter due dates.
- 2026-11-05: 16 rows: bond and share sales, Amazon commitments and backlog, Alphabet purchase commitments, S&P on Meta.
- 2026-10-31: 18 rows: Q3 2026 for Microsoft, Alphabet, Amazon; leases at 30 Sep; guidance, backlog, financing.
- 2026-10-25: 8 rows: Meta guidance and debt, Meta and Oracle CDS, Oracle results date.
- 2026-10-24: launched.
