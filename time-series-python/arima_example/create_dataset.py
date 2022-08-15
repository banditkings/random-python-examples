"""
Helper file function to load some sample time series data covering the period between Jan 1980 to March 1994.

Some work was required to make sure everything was quarterized and at the same time periods.

    load_wineind: Quarterly Wine Sales in bottles (<=1L) in Australia from 1980:Q1 to 1994:Q3
    load_austres: Quarterly Australian Residents from 1971:Q1 to 1994:Q1
    load_ausbeer: Quarterly Beer Production in Australia (megaliters) from 1956:Q1 to 2008:Q3
"""

import pandas as pd
from datetime import datetime
from pmdarima.datasets import load_wineind, load_austres, load_ausbeer

def load_wine():
    wine = load_wineind(True)  # Jan 1980 to Aug 1994
    df = pd.DataFrame(wine)
    df.columns=["Wine"]
    # Convert to quarters
    df = df.reset_index()
    df.index = [datetime.strptime(i, '%b %Y') for i in df["index"]]
    df["timeperiod"] = df.index.year.astype(str) + df.index.quarter.astype(str)
    df = df[["Wine", "timeperiod"]].groupby(by=["timeperiod"], as_index=False).sum()
    # Filter to Q1 1980 to Q1 1994
    df = df.query("timeperiod <= '19941'")
    return df

def load_residents():
    res = load_austres(True) # Qtrly australian residents from March 1971 to March 1994
    # Filter to (Q1 1980) to March (Q1 1994), so that means filtering out first 4 * 6 periods
    qtrs_until_1980 = (4 * 8) # 4 qtrs * 8 years between Q1 1971 to Q1 1980
    res = res.iloc[qtrs_until_1980:].reset_index(drop=True)
    return res    

def load_beer():
    # Total quarterly beer production in Australia (in megalitres) from 1956:Q1 to 2008:Q3
    beer = load_ausbeer(True)
    # Filter to 1980:Q1 to 1994:Q1

    # qtrs from 1980 to 1956
    p1 = (1980 - 1956) * 4  # 96
    # qtrs from 1980 to 1994
    p2 = p1 + 57 # 153
    beer = beer.iloc[p1:p2].reset_index(drop=True)
    return beer

def load_combined_dataset():
    df = load_wine()
    beer = load_beer()
    res = load_residents()

    # add residents data
    df["Residents"] = res
    df["Beer"] = beer
    return df
