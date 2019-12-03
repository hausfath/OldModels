# Evaluating the performance of past climate model projections

These notebooks, scripts, and data correspond to the analysis in Hausfather, Drake, Abbott, and Schmidt (2019), Evaluating the performance of past climate model projections, *Geophysical Research Letters*, https://doi.org/10.1029/2019GL085378.

The `environment.yml` file contains the python dependencies necessary to run the data processing notebooks. Figures 1, 2, S1, S2, S3, S4, and S5 were produced offline using the plotting software *STATA* based on the raw data in `data/raw` and the interim data files in `data/interim` produced by the notebook `Obs forcing analysis.ipynb` and saved in `data/processed`. Figures 3 and S6 were produced using the python notebooks `plot_temperature_forcing_spaghetti.ipynb` and `plot_temperature_forcing_FAR_spaghetti.ipynb` based on the data in `data/processed/`.

Example: Figure 3 shows the Hansen et al. 1988 projections compared with observations on a temperature vs. time
basis (top) and temperature vs external forcing (bottom). The dashed grey line in the top panel
represent the start of the projection period. The transparent blue lines in the lower panel
represent 500 random samples of the 5000 combinations of the 5 temperature observation
products and the 1000 ensemble members of estimated forcings (the full ensemble is
subsampled for visual clarity). The dashed blue lines show the 95% confidence intervals for the
5000 member ensemble (see supplementary text S1.4 for details). Anomalies for both
temperature and forcing are shown relative to a 1958-1987 pre-projection baseline.

https://github.com/hausfath/OldModels/blob/master/figures/temperature_forcing_spaghetti.png

