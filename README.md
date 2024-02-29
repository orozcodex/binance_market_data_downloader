# Binance Market Data Download Script

## Description
This Python script facilitates downloading historical market data from the Binance exchange. It is designed for market analysis, trading strategy backtesting, academic research, and any application requiring historical cryptocurrency data.

## How to Use the Data
Data is saved in CSV files, one for each year and specified cryptocurrency, following the format `SYMBOL_TIMEFRAME_market_data_YEAR.csv`, where:
- `SYMBOL` denotes the cryptocurrency symbol (e.g., BTCUSDT).
- `TIMEFRAME` specifies the data interval (e.g., 1m, 1h).
- `YEAR` represents the year of the data included.

### Dataset Structure
Each CSV file contains columns for:
- `Open Time`: Unix timestamp of the interval start.
- `Open`: Opening price.
- `High`: Highest price during the interval.
- `Low`: Lowest price during the interval.
- `Close`: Closing price.
- `Volume`: Traded volume.
- `Close Time`: Unix timestamp of the interval end.
- Additional metrics: `Quote Asset Volume`, `Number of Trades`, `Taker Buy Base Asset Volume`, `Taker Buy Quote Asset Volume`, `Ignore`.

## How to Contribute
Feel free to open a pull request or issue to share Binance datasets or suggest improvements. Ensure to follow GitHub best practices and provide a clear description of your contributions.

## Responsible Data Use
This repository is provided for educational and research purposes. Users are responsible for adhering to Binance API policies and using the data ethically and legally. Please see [Binance Terms of Use](https://www.binance.com/en/terms) for more information.

## License
This project is licensed under the [MIT License](LICENSE). Please review the `LICENSE` file for details.

## Contact
For questions or comments about this repository, please feel free to contact the repository owner via [GitHub Issues](https://github.com/orozcodex/binance_market_data_downloader/issues).

---
