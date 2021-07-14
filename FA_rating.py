import FundamentalAnalysis as fa
import pandas as pd

#put your own key
api_key = ""
#put your desired stock ticker
ticker = "TSLA"

rating_df = fa.rating(ticker, api_key)
print(rating_df)
#slice a specific recommendation from the dataframe
rating_df['ratingDetailsPBRecommendation']

#Export the gathered data to an Excel spreadsheet
rating_df.to_excel('TSLA_ratings.xlsx')
