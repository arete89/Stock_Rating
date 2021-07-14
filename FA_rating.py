import FundamentalAnalysis as fa
import pandas as pd

#put your own key
api_key = ""
#put your desired stock ticker
ticker = "TSLA"

rating_df = fa.rating(ticker, api_key)
rating_df['ratingDetailsPBRecommendation']

#Export the gathered data to an Excel spreadsheet
rating_df.to_excel('TSLA_ratings.xlsx')