# Power BI Dashboard Specification

## Page 1 — Asset Overview
- KPI cards: Total Assets, Total Asset Cost, In-Use Assets, Stale Assets.
- Bar chart: Asset count by department.
- Donut chart: Asset status distribution.
- Matrix: Asset type by location, with count and total cost.
- Slicers: Department, location, asset type, status, criticality.

## Page 2 — Lifecycle & Data Quality
- Table: asset ID, owner, department, last seen, status, days since last seen.
- Conditional formatting: stale records and missing owner/location.
- Trend: asset purchases by year/month.
- Drill-through: asset detail page.

## Refresh and governance
- Confirm data owner and refresh permissions before scheduling.
- Document definitions for “stale”, “in use”, and “asset cost”.
- Reconcile totals against the source workbook after every schema change.
- Keep PII to the minimum necessary; use role-based access where required.
