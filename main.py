#!/usr/bin/env python

#the Dow stocks are DIS, BA, V, AAPL, NKE, MSFT, AXP, UNH, WMT, HD, GS, MCD, CAT, TRV, JPM, PG, INTC, JNJ, CSCO, KO, MMM, MRK, PFE, WBA, IBM, DOW, CVX, VZ, XOM

import streamlit as st
import pandas as pd
import finviz
from finviz.screener import Screener

st.title('Dogs of the Dow Calculator')
st.write("The stocks of the Dow, their price and dividend yield")

#https://finviz.com/screener.ashx?v=152&f=idx_dji&ft=4&o=-dividendyield

filters = ['idx_dji'] # I only want Dow stocks
dow_jones = Screener(filters=filters, table='Financial', order='-dividendyield')

#for stock in dow_jones:
#    print(stock['Ticker'], stock['Price'], stock['Dividend'])
    #stock_data = pd.DataFrame(data=[stock['Ticker'], stock['Price'], stock['Dividend']], columns=['Ticker', 'Price', 'Dividend'])

st.table(dow_jones)