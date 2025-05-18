"""
bloomberg.py

A set of utility functions for fetching data from Bloomberg using the pdblp library

"""

import pdblp
import pandas as pd
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Set up connection to BLP API
con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con.start()
con.debug = False

# Define function for pulling bbg data
def get_bbg_price_index(tickers, start_date, end_date, ffill=True, ffill_limit=10):
    """Function for fetching price data from bloomberg
    for a specified time period and a specified list
    of tickers

    :param tickers: <list> A list of tickers for which
    to fetch data
    :param start_date: <str/pd.Timestamp> start date
    of the analysis period. If provided as a string,
    use the format 'YYYYMMDD'.
    :param end_data: <str/pd.Timestamp> end date
    of the analysis period. If provided as a string,
    use the format 'YYYYMMDD'.
    :param ffill: <bool> Wether to forward fill for
    missing data or not. Set to True as default
    :param ffill_limit: <int> Maximum number of
    periods for which to forward fill. Default
    is set to 10.
    ::

    :return: <pd.DataFrame> a pandas DataFrame
    containing the requested price data
    """

    # Create DataFrame for storing price data
    price_df = pd.DataFrame()

    # Iterate through tickers
    for ticker in tickers:
        try:
            # Check if the ticker corresponds to a currency or not
            if 'Curncy' in ticker:
                # Fetch PX_LAST for currencies
                ret = con.bdh(ticker, ['PX_LAST'], start_date, end_date)
                # Data Manipulation
                ret = ret[ret.columns[0]]
                price_df[ticker] = ret
            else:
                # If not currency, fetch TOT_RETURN_INDEX_NET_DVDS
                ret = con.bdh(ticker, ['TOT_RETURN_INDEX_NET_DVDS'], start_date, end_date)
                ret = ret[ret.columns[0]]
                price_df[ticker] = ret
        # Flag tickers for which data pull was unsuccessful')
        except Exception as e:
            print(f'Failed to fetch data for {ticker}')
            print(e.message)

    # Check wether to forward fill or not
    if ffill:
        price_df.ffill(inplace=True, limit=ffill_limit)

    # Return the DataFrame of prices
    return price_df