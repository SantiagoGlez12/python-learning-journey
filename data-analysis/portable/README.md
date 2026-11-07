# Portable notebook editions

These notebooks are **adapted copies** of coursework notebooks in `../`. The originals are retained for provenance. The adaptations primarily replace absolute macOS paths with repository-relative paths and do not rewrite the exercise logic.

Run Jupyter from the **repository root** so `Path.cwd()` points to the right directory:

```bash
python -m pip install -r data-analysis/portable/requirements.txt
jupyter lab
```

| Notebook | Change | Remaining limitations |
| --- | --- | --- |
| [M24 population](module-24-population-indicators.ipynb) | Download dataset to `data-analysis/datasets/population-2020/` if absent | Requires internet and access to public course CSV; not yet executed here |
| [M26 heights](module-26-pandas-country-data.ipynb) | Download course CSV to `data-analysis/datasets/country-heights/` | Requires working course Drive link and network; not yet executed |
| [M27 debugging](module-27-error-handling.ipynb) | Save temporary files to `data-analysis/generated/error-handling/` | **Intentional exceptions** are part of the lesson; do not use Run All without inspecting them |
| [M29 web/APIs](module-29-web-apis.ipynb) | Export CSVs under `data-analysis/generated/web-api/` | Requires external websites and APIs; failures may occur if endpoints change |

These editions preserve their original learning level and exercises, including descriptive text about the original Mac workflows. Output folders are ignored by Git. No end-to-end run is claimed.

Other notebooks still need source CSV/Excel/JSON inputs or adaptation. In particular, M28, M30, M31 and M32 reference `fifa_eda.csv` or other files that are not bundled with this repository.
