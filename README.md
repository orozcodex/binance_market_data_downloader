# binance_market_data_downloader
This Python script downloads Binance market data, letting users choose symbol, timeframe, and dates. Saves data in yearly CSVs, including prices and volume.

**Binance Market Data Downloader**

This Python script allows users to download historical market data from the Binance exchange. It offers a simple command-line interface for specifying the cryptocurrency symbol, the data timeframe (e.g., 1 minute, 1 hour), and the desired date range for the data retrieval. The downloaded data includes open, high, low, close prices, volume, and other relevant market information, which are saved into yearly CSV files named according to the symbol, timeframe, and year of the data.

**Features:**
- User-friendly command-line interface for specifying parameters.
- Supports various timeframes (e.g., 1m, 1h, 1d) for flexible data analysis needs.
- Downloads data for a specified date range, allowing for targeted analysis.
- Organizes downloaded data into yearly CSV files for easy management and access.

**Usage:**
1. Run the script from the command line.
2. Enter the desired cryptocurrency symbol (e.g., BTCUSDT) when prompted.
3. Specify the data timeframe (e.g., 1m for one minute).
4. Enter the start and end dates for the data download in YYYY-MM-DD format.
5. The script will retrieve the data and save it into CSV files, one for each year in the specified date range.

**Requirements:**
- Python 3
- Requests library

**Note:**
This script is designed for educational and analytical purposes. Users are responsible for adhering to Binance's API usage policies and guidelines.
