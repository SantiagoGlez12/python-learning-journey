# Data sources and execution status

Status checked 7 November 2026. **File presence is not execution verification.**

| Module | Required input or service | Repository status | Next verification |
| --- | --- | --- | --- |
| M24 | UN population/fertility/mortality CSV, 2020 subset | Portable edition uses course Drive file ID; original CSV not included | Download and run all analytical cells |
| M25 | Python standard library | Original notebook retained | Run notebook examples |
| M26 | Country heights CSV (course Drive ID) | Portable edition attempts external download | Confirm Drive access, CSV schema and stats |
| M27 | Temporary `test.txt` and deliberate exceptions | Portable edition writes temporary files locally | Run cells individually; confirm exceptions are expected |
| M28 | FIFA CSV, Amazon books XLSX and JSON samples | Inputs not fully bundled | Locate and verify original supporting files |
| M29 | Public website and API endpoints | Portable edition redirects output | Confirm live endpoints/response structure |
| M30 | `fifa_eda.csv` | Source not present | Recover input before executing |
| M31 | `fifa_eda.csv` | Source not present | Recover input before executing |
| M32 | FIFA data source | Source not present | Recover input before executing |
| M33 | Public video-game sales CSV | Original figures and derived tables included, portable notebook attempts external download | Run notebook with original CSV and compare generated outputs |

The repository does not claim portable notebooks are executed simply because their paths were modified. It also does not redistribute third-party datasets without verifying suitability. The larger retail project has its own validation record in [retail-data-integration](https://github.com/SantiagoGlez12/retail-data-integration/blob/main/docs/validation.md).
