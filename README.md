# Ghana Oil Production/Price Forecasting

## Project Overview

This project aims to forecast Ghana's crude oil production and prices using time series analysis techniques, specifically ARIMA and SARIMA models. The project leverages historical data to train these models and generate future predictions, which can be valuable for decision-making in the energy sector.

## Data Source

The project utilizes historical data on Ghana's oil production and prices. The dataset is in CSV format and is loaded from Google Drive.  You can find similar datasets by searching for "Ghana oil production data" or "Ghana oil price data" online.

## Methodology

1. **Data Loading and Preprocessing:** The data is loaded, missing values are handled using interpolation, and the data is resampled to a monthly frequency.

2. **Exploratory Data Analysis:** The data is visualized to understand trends, seasonality, and potential outliers. Time series decomposition is performed to analyze the underlying components of the data.

3. **Stationarity Check:** The Augmented Dickey-Fuller (ADF) test is applied to assess the stationarity of the time series, which is a crucial assumption for ARIMA and SARIMA models.

4. **ARIMA Model Implementation:** The `auto_arima` function is used to automatically determine the optimal parameters (p, d, q) for the ARIMA model. The model is then trained and used to generate forecasts.

5. **SARIMA Model Implementation:** Similar to ARIMA, `auto_arima` is used to identify the best parameters for the SARIMA model, including seasonal components (P, D, Q, m). The model is trained and used to generate forecasts with confidence intervals.

6. **Model Evaluation:** The performance of both ARIMA and SARIMA models is assessed using metrics such as AIC, BIC, and RMSE. The results are compared to determine the most suitable model for forecasting.

## Dependencies

- Python 3.x
- Libraries: `pandas`, `numpy`, `matplotlib`, `statsmodels`, `pmdarima`, `sklearn`

To install the necessary libraries, run the following commands in your Google Colab environment:
```
!pip install pmdarima 
!pip install --upgrade statsmodels 
```
## Usage

1. Upload your Ghana oil data CSV file to your Google Drive.
2. Update the file path in the code to point to your uploaded data file.
3. Run the code cells in the notebook sequentially.
4. Observe the generated forecasts and model evaluation results.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
