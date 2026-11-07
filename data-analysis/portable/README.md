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
| [M28 file handling](module-28-file-formats.ipynb) | Read/write files under `data-analysis/datasets/module-28/` | FIFA, books and Game of Thrones JSON inputs are not bundled |
| [M30 FIFA Pandas](module-30-fifa-pandas.ipynb) | Use `data-analysis/datasets/fifa/` | Requires original `fifa_eda.csv` or `fifa_eda(1).csv` |
| [M31 FIFA groupby](module-31-fifa-groupby.ipynb) | Use `data-analysis/datasets/fifa/` | Requires original FIFA input CSV |
| [M32 FIFA dashboard](module-32-fifa-dashboard.ipynb) | Use `data-analysis/datasets/fifa/` | Requires original FIFA input CSV |

These editions preserve their original learning level and exercises, including descriptive text about the original Mac workflows. Output folders are ignored by Git. No end-to-end run is claimed.

The remaining bottleneck for M28 and M30–M32 is **missing source datasets**, not absolute local paths. Notebook instructions mentioning Downloads are historical text from the original submission; run the code using the paths described in this document. The files were not executed end to end as part of this adaptation.
