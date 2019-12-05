## Evaluating the performance of past climate model projections

<img src="extra/extra_figures/projectionstripes.png" width="100%">

**This repository contains the notebooks, scripts, and data that correspond to the analysis in the paper by Hausfather, Z., Drake, H. F., Abbott, T., Schmidt, G. A. (2019), "Evaluating the performance of past climate model projections", *Geophysical Research Letters*, https://doi.org/10.1029/2019GL085378.**

Please contact henrifdrake@gmail.com if you have any questions or difficulties with using this code.

Play around with the data directly in your browser at [mybinder.org](https://mybinder.org/):  [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hausfath/OldModels/master?filepath=extra%2FBinder_demo.ipynb)

### Attribution

This code is freely available for reuse as described in the MIT License included in this repository. However, if you use this code or any derived data products in an academic publication, you are obliged to provide the following citation:

- Hausfather, Z., Drake, H. F., Abbott, T., Schmidt, G. A. (2019). Evaluating the performance of past climate model projections, *Geophysical Research Letters*, doi:10.1029/2019GL085378.

If you use any of our raw or derived data from this repository, we ask that you also provide direct citations to the original sources that document the individual climate models (or climate model ensembles) and observational data products.

### Description

The `environment.yml` file contains the python dependencies necessary to run the data processing notebooks. Figures 1, 2, S1, S2, S3, S4, and S5 were produced offline using the plotting software *STATA* based on the raw data in `data/raw` and the interim data files in `data/processed`, which are produced by the notebook `notebooks/Obs forcing analysis.ipynb` from the data files in `data/raw`. Figures 3 and S6 were produced using the python notebooks `notebooks/plot_temperature_forcing_spaghetti.ipynb` and `notebooks/plot_temperature_forcing_FAR_spaghetti.ipynb` based on the data in `data/processed/`.

**Note: Two data files have been moved, relative to the live links in the Supplementary Materials:**

https://github.com/hausfath/OldModels/blob/master/Model%20data%20spreadsheet.xlsx ==> https://github.com/hausfath/OldModels/blob/master/references/Model%20data%20spreadsheet.xlsx 
 
https://github.com/hausfath/OldModels/tree/master/forcing_data ==> https://github.com/hausfath/OldModels/tree/master/data/raw/forcing_data


----------

Copyright (c) 2019 Zeke Hausfather and Henri Drake
