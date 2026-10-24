# AI Capex Ledger

Open dataset from [Footnote 13](https://footnote13.substack.com): operating cash flow vs all-in capital spending (incl. finance leases) for Microsoft, Alphabet, Amazon, Meta and Oracle, quarter by quarter, plus leases signed but not yet commenced.

Live page: https://ledger.footnote13.com

## Files
- `data/ledger-master.csv` — one row per fact: company, metric, calendar and fiscal period, value (USD bn), basis, source, as-of date. The page reads this file directly.
- `data/ai-capex-ledger.xlsx` — Excel export with formulas (Quarterly, Combined, Hidden leases).
- `index.html` — the page.

## Method
Cash gap = operating cash flow − all-in capex. All-in capex = cash capex + finance leases as each company reports them (Microsoft: CFO-stated capex incl. finance leases; Meta: principal payments on finance leases; Amazon: P&E acquired under finance leases; Alphabet, Oracle: cash capex only). Calendar quarters; Oracle's fiscal quarters end one month earlier. Leases not yet commenced are undiscounted future payments from the latest 10-Q/10-K.

## Licence
Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — credit "Footnote 13, AI Capex Ledger". Source figures come from public company filings.

## Changelog
See commit history. 2026-10-24: launched.
