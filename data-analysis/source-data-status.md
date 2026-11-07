# Data sources and execution status

Status checked 7 November 2026. **File presence is not execution verification.**

| Module | Required input or service | Repository status | Next verification |
| --- | --- | --- | --- |
| M24 | UN population/fertility/mortality CSV, 2020 subset | Original CSV retrieved and key Pandas transformations separately checked on 7 Nov 2026: 185 country records and Pearson r = -0.915; original M24 code executed locally with supplied CSV; all three figures and two tables generated; both regenerated tables match saved coursework CSVs exactly | Check fresh GitHub Actions run of portable edition with dataset |
| M25 | Python standard library | Original notebook retained | Run notebook examples |
| M26 | Country heights CSV (course Drive ID) | Source CSV accessible from the original course Drive link; portable edition prepared | Execute notebook and verify summary statistics |
| M27 | Temporary `test.txt` and deliberate exceptions | Portable edition writes temporary files locally | Run cells individually; confirm exceptions are expected |
| M28 | FIFA CSV, Amazon books XLSX and JSON samples | Inputs not fully bundled | Locate and verify original supporting files |
| M29 | Public website and API endpoints | Portable edition redirects output | Confirm live endpoints/response structure |
| M30 | `fifa_eda.csv` | Source not present | Recover input before executing |
| M31 | `fifa_eda.csv` | Source not present | Recover input before executing |
| M32 | FIFA data source | Source not present | Recover input before executing |
| M33 | Public video-game sales CSV | Original source CSV retrieved; local execution generated eleven charts and eleven derived CSV tables, with all eleven CSV tables matching saved coursework outputs | Validate notebook execution in a clean GitHub Actions environment |

The repository does not claim portable notebooks are executed simply because their paths were modified. It also does not redistribute third-party datasets without verifying suitability. The larger retail project has its own validation record in [retail-data-integration](https://github.com/SantiagoGlez12/retail-data-integration/blob/main/docs/validation.md).

## M24 data validation details (7 November 2026)

The original CSV from the course folder was retrieved, decoded with `latin1` and read using `skiprows=1` (6,756 raw data records, seven columns). Repeating the notebook's cleaning and 2020 exclusion logic independently produced **185 country rows**, seven indicators and **185 complete infant-mortality/life-expectancy pairs**. Pearson's correlation was **-0.915** (rounded to three decimals). These observations verify the core data transformation against the retrieved dataset, **not** an end-to-end notebook or visualization execution. The source CSV is not redistributed in the GitHub repository.

### M24 local run update

The original M24 script was executed locally with a file-path-only adjustment, producing three figures and two CSV tables. Both regenerated CSVs match the original saved tables exactly (the correlation matrix is 7×8 including its label column; the pairwise ranking is 21×4). Figures and saved CSVs are now published in [population-2020](population-2020/). This does not establish that the external `gdown` source is accessible to anonymous users or that every notebook is portable.
