# Top 5 Correlations to a Name or a Row in a Time Series Data Set

This function draws a correlation chart of the top "x" rows of a data frame that are highly correlated to a selected row in the dataframe. You can think of the rows of the input dataframe as containing stock prices or fund flows or product sales and the columns     should contain time series data of prices or flows or sales over multiple time periods. <b>CAUTION: MAKE SURE YOU DIFFERENCE THIS TIME SERIES DATA BEFORE DOING CORRELATIONS. OTHERWISE, YOU'LL GET SPURIOUS CORRELATIONS!!</b>
<br>
<br>Now this program will allow you to select the top 5 or 10 rows that are highly correlated to a given row selected by the column: column_name and using a search string "searchstring". The    program will search for the search string in that column column_name and return a list of 5 or 10 rows that are the most correlated to that selected row. If you give "top" as a float ratio then it will use the ratio as the cut off point in the correlation coefficient to select rows.
<br>
<br>
<b>Usage<br></b>
    top_correlation_to_name(stocks, column_name, searchstring, top=5)
<br>
<br>
<b>Arguments <br></b>

stocks: name of the dataframe that contains your time series data in this format: <br>
1. rows = each stock ticker or productname or country or whatever that list of things that represents this data
1. columns = time series data. For example, monthly sales, daily stock prices or monthly CPI for each country
<br><b>CAUTION: MAKE SURE YOU DIFFERENCE THIS TIME SERIES DATA BEFORE DOING CORRELATIONS. OTHERWISE, YOU'LL GET SPURIOUS CORRELATIONS!!</b><br>
<br>column_name: name of the column in which the rows have a name. For example, stock tickers or country names, etc should be in this column.
<br>
search_string: name of the stock or country that you are searching for in the column_name above
<br>
top: the top "n" number of rows that is highly correlated to your country or stock or whatever you are comparing. It can be either:
    integer: this will mean that you want the top 5 or 10 rows that correlate well to your search name
    fraction: this will mean that you want any rows that have a correlation higher than this fraction to be displayed in your chart.
<br>
<br>
<b>Example<br></b>
    top_correlation_to_name(df,'index','MSFT',5)
