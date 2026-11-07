# Python Learning Journey 🐍

A structured collection of Python coursework, progressing from introductory functions to data manipulation and exploratory analysis.

## Explore the exercises

| Topic | Exercise | Notes |
| --- | --- | --- |
| Python fundamentals | [Power of two](fundamentals/power_of_two.py) | Small self-contained Python example with [unit tests](tests/test_power_of_two.py) |
| Functional programming (M25) | [lambda, map, reduce, filter](data-analysis/module-25-functional-tools.ipynb) | Original course notebook; saved outputs cleared |
| Pandas basics (M26) | [Country dataset exploration](data-analysis/module-26-pandas-country-data.ipynb) | Original notebook; its external CSV download and environment paths may need updating |
| File formats (M28) | [CSV, Excel and JSON](data-analysis/module-28-file-formats.ipynb) | Original notebook; local file paths and source datasets may need updating |

## Quick start

Python 3.10+ is recommended. To run the introductory example and tests without external libraries:

```bash
python fundamentals/power_of_two.py
python -m unittest discover -s tests -v
```

To explore the notebooks, install Jupyter and the packages used by each exercise. The M26/M28 notebooks include coursework-specific source files and paths, so they have **not** been verified as portable or executable in a clean environment.

## Migration status

- [x] Introductory Python function and tests
- [x] Original coursework notebooks for modules 25, 26 and 28
- [ ] Verify notebook dependencies and replace machine-specific paths
- [ ] Migrate NumPy, data visualization and additional Pandas exercises from Drive
- [ ] Add applied EDA projects (Iris, Titanic, population indicators, video-game sales)
- [ ] Document dataset licenses and reproducibility for each applied project

## Principles

This repository documents genuine coursework and learning progress. Original exercises remain recognizable; limitations are stated instead of presenting every exercise as production-ready. No credentials or private datasets should be committed.

See also [Retail Data Integration & Analysis](https://github.com/SantiagoGlez12/retail-data-integration) for a larger applied data project.
