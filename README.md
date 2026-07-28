# Retail Demand Forecasting - M5 (Walmart) Dataset

> 🚧 **In progress** - building in public. Follow the commits.

Forecasting daily unit sales for 3,049 products across 10 Walmart stores, using the
[M5 competition dataset](https://www.kaggle.com/competitions/m5-forecasting-accuracy).

**Why this project:** I work in a supermarket. When a demand forecast is wrong, I'm the one
looking at the empty shelf (lost sales) or throwing out short-dated stock (markdown waste).
This project is about closing the gap between forecast error as a metric and forecast error
as a real operational cost.

## Roadmap

- [x] Repo setup and data pipeline
- [ ] Exploratory analysis - sales patterns, seasonality, promotions (SNAP), price effects
- [ ] Baseline models - naive, seasonal naive, moving average
- [ ] ML models - LightGBM with calendar/price/lag features
- [ ] Evaluation - WRMSSE (competition metric) + a "cost of error" translation
- [ ] Findings writeup

## Results

*(coming - this table fills in as models land)*

| Model | WRMSSE | Notes |
|---|---|---|
| Seasonal naive baseline | – | |
| LightGBM | – | |

## Setup

```bash
pip install -r requirements.txt
```

Download the M5 data from [Kaggle](https://www.kaggle.com/competitions/m5-forecasting-accuracy/data)
and place the CSVs in `data/` (not tracked by git - see `data/README.md`).

## Structure

```
notebooks/   analysis notebooks, numbered in order
src/         reusable functions (data loading, features, evaluation)
data/        raw M5 CSVs (gitignored)
results/     saved metrics and figures
```

## Stack

Python · pandas · LightGBM · statsmodels · Matplotlib
