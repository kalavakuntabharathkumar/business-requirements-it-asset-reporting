# Business Requirements Tracking & IT Asset Reporting Platform

A portfolio-ready reporting project built around sample IT asset data, Power Query transformation guidance, DAX measures, and a requirements traceability register. Power BI Desktop is required to open/edit the PBIX model; a PBIX file is not included because it must be authored in Power BI Desktop.

## Included
- Synthetic 120,000-row asset dataset generator.
- Small CSV preview dataset for quick inspection.
- Requirements traceability matrix and UAT checklist.
- Power Query M transformation template.
- DAX measures for asset counts, stale records, refresh date, and compliance.
- Jira/Confluence/SharePoint workflow guide and dashboard specification.

## Quick start
```bash
python -m venv .venv
# Activate the environment, then:
pip install -r requirements.txt
python scripts/generate_assets.py
```

Open `data/assets_preview.csv` in Excel to inspect the schema. For Power BI Desktop:
1. Get Data → Text/CSV → select `data/assets_preview.csv` or the generated `data/assets_120k.csv`.
2. Open `powerbi/PowerQuery_Transformations.m`.
3. Create measures from `powerbi/Measures.dax`.
4. Build visuals according to `docs/dashboard_spec.md`.

The 120,000 rows are synthetic demo records. The resume figures supplied in the project brief are not verified by the demo implementation and should only be used if they reflect your actual work.
