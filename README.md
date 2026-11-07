# Python Learning Journey 🐍

[![Python portfolio checks](https://github.com/SantiagoGlez12/python-learning-journey/actions/workflows/python-checks.yml/badge.svg)](https://github.com/SantiagoGlez12/python-learning-journey/actions/workflows/python-checks.yml)

A collection of Python programming and data-analysis coursework, from basic functions to data manipulation, visualizations and exploratory analysis.

## Contents

| Module | Exercise | Status |
| --- | --- | --- |
| Fundamentals | [Power-of-two function](fundamentals/power_of_two.py) and [tests](tests/test_power_of_two.py) | Self-contained |
| M24 | [Population indicators](data-analysis/population-2020/README.md) | Locally executed; 3 figures and 2 CSV reports published; original and portable notebooks retained |
| M25 | [lambda, map, reduce, filter](data-analysis/module-25-functional-tools.ipynb) | Original notebook |
| M26 | [Pandas country data](data-analysis/module-26-pandas-country-data.ipynb) | Original notebook; external CSV dependency |
| M27 | [Debugging and error handling](data-analysis/module-27-coursework.ipynb) | Original notebook; local paths may apply |
| M28 | [CSV, Excel and JSON file handling](data-analysis/module-28-file-formats.ipynb) | Original notebook; local input files required |
| M29 | [Web and API data](data-analysis/module-29-coursework.ipynb) | Original notebook; network access required |
| M30 | [Data manipulation with Pandas](data-analysis/module-30-coursework.ipynb) | Original notebook; input dataset required |
| M31 | [DataFrames, groupby and statistics](data-analysis/module-31-coursework.ipynb) | Original notebook; input dataset required |
| M32 | [FIFA dashboard wireframe and charts](data-analysis/module-32-coursework.ipynb) | Original notebook; input dataset required |
| M33 | [Video-game sales EDA](data-analysis/video-game-eda/README.md) | Original + portable notebooks, 11 charts and 11 CSV summaries; local analysis verified |

**Migration note:** Original notebook outputs were cleared to keep the Git history focused on source. Their source code is preserved, but not all notebooks have been retested in a clean environment. Some exercises contain local paths or downloads that must be adjusted before rerunning.

## Portable coursework

[Portable M24, M26, M27, M28, M29, M30, M31 and M32 notebooks](data-analysis/portable/README.md) now run with project-relative file paths. See the [data-source and verification register](data-analysis/source-data-status.md) for remaining dependencies; adaptation is not the same as successful execution.

## Featured analysis: UN population indicators (2020)

The [M24 report](data-analysis/population-2020/README.md) includes original graphs, verified correlation tables and reproduction instructions.

![Infant mortality vs. life expectancy](data-analysis/population-2020/figures/01_dispersion_mortalidad_esperanza.png)

## Featured analysis: video-game sales

The [video-game EDA project](data-analysis/video-game-eda/README.md) includes a portable notebook, 11 saved figures and 11 derived tables from the coursework.

![Video-game sales by year](data-analysis/video-game-eda/figures/01_ventas_por_anio.png)

## Git/GitHub course practice

A beginner [power-of-two notebook and guided VS Code workflow](github-practice/README.md) is prepared for the pending academic submission. The required local edit, Git commands and screenshots must be completed by the student.

## Quick start

Use Python 3.10+:

```bash
python fundamentals/power_of_two.py
python -m unittest discover -s tests -v
```

For the notebooks, install Jupyter and check each notebook for its dependencies. Common data-science packages include `pandas`, `numpy`, `matplotlib`, `seaborn`, and `openpyxl`; some notebooks require additional packages or data files.

## Remaining improvements

- [x] Replace machine-specific paths in eight adapted notebooks
- [ ] Recover missing third-party datasets for remaining notebooks
- [x] Document dataset/dependency requirements for the known modules
- [x] Add portable copies for M24, M26, M27, M28, M29, M30, M31 and M32
- [ ] Migrate remaining earlier Python and visualization exercises
- [x] Integrate 11 original charts and 11 supporting CSV tables for M33
- [x] Add a project-relative M33 notebook copy
- [x] Validate the M33 analysis locally with its original dataset and compare eleven CSV outputs
- [ ] Validate M33 execution in a clean CI environment
- [x] Execute the M24 source analysis locally, with matching saved CSV results
- [ ] Validate the remaining notebooks end to end where input files are available
- [ ] Complete the Git/GitHub coursework evidence with an actual local notebook edit and screenshots

## Related project

[Retail Data Integration & Analysis](https://github.com/SantiagoGlez12/retail-data-integration) presents a larger SQL and Pandas coursework project.
