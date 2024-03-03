# Binance Market Data Downloader

## Description

This Python script facilitates downloading historical market data from the Binance exchange. It is designed for market analysis, trading strategy backtesting, academic research, and any application requiring historical cryptocurrency data. By leveraging the Binance API, it provides an efficient way to fetch and organize a vast amount of market data in a structured format, ready for analysis.

## Features

- **`Flexible Data Retrieval`**: Supports downloading data for any cryptocurrency pair available on Binance.
- **Customizable Timeframes**: Allows specification of data interval, ranging from 1 minute to 1 month.
- **Automated File Organization**: Saves data in CSV format, organized by year and cryptocurrency pair.
- **Comprehensive Dataset**: Each record includes detailed trading metrics such as open, high, low, close prices, and volume.

## Dataset Structure

The dataset provided by this script is comprehensive and includes the following fields for each interval:

- **Open Time**: The Unix timestamp indicating the start of the interval.
- **Open**: The opening price of the cryptocurrency in the specified interval.
- **High**: The highest price reached during the interval.
- **Low**: The lowest price during the interval.
- **Close**: The closing price at the end of the interval.
- **Volume**: The total traded volume in the interval.
- **Close Time**: The Unix timestamp indicating the end of the interval.

**Additional Metrics**:
- **Quote Asset Volume**: The total volume of the quote asset traded in the interval.
- **Number of Trades**: The total number of trades that occurred in the interval.
- **Taker Buy Base Asset Volume**: The volume of the base asset bought by takers in the interval.
- **Taker Buy Quote Asset Volume**: The volume of the quote asset bought by takers in the interval.
- **Ignore**: Any additional data that may be ignored for analysis purposes.

Each CSV file is named using the pattern `SYMBOL_TIMEFRAME_market_data_YEAR.csv`, facilitating easy identification and access to historical data for analysis.

## How to Contribute

We welcome contributions from the community! Whether you have enhancements to the code, additional datasets, or other improvements, here's how you can contribute:

1. **Fork the Repository**: Start by forking the repository to your GitHub account.
2. **Clone the Forked Repository**: Clone the repository to your local machine to make your changes.
3. **Create a New Branch**: It's a good practice to create a new branch for each set of changes you wish to contribute.
4. **Make Your Changes**: Add your datasets, enhance the code, or make other improvements.
5. **Commit Your Changes**: Use clear and concise commit messages that explain the changes you've made.
6. **Push Your Changes**: Push your changes to your forked repository on GitHub.
7. **Submit a Pull Request**: Open a pull request from your forked repository to the original repository. Please provide a clear description of the changes and any other relevant information.

**Guidelines**:
- Ensure your code is well-documented and follows the project's coding standards.
- Test your changes thoroughly before submitting a pull request.
- Keep pull requests focused on a single issue or feature for clarity.

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

We look forward to seeing your contributions and thank you for helping to improve the Binance Market Data Downloader!

## Responsible Data Use

This tool is provided for educational and research purposes. Users are expected to comply with Binance API usage policies and employ the data in an ethical and legal manner. Refer to [Binance Terms of Use](https://www.binance.com/en/terms) for detailed information.

## License

This project is open-sourced under the MIT License. See the `LICENSE` file in this repository for more information.

