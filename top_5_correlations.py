######## Finding Top 5 Correlations to a Name or Row ###########################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
###############
def search_string(gr, column, strings_list):
    """
    search for a string in a dataframe specified in columns
    """
    if isinstance(strings_list,str):
        strings_list = [strings_list]
    if isinstance(column, str):
        #### if column is not a list but a string, it means there is only one column to search
        return gr[gr[column].str.contains('|'.join(strings_list),na=False)]
    else:
        gr_df = pd.DataFrame()
        counter = 0
        for col in column:
            if counter == 0:
                gr_df =  gr[gr[col].str.contains('|'.join(strings_list),na=False)]
                counter += 1
            else:
                gr_df.append(gr[gr[col].str.contains('|'.join(strings_list),na=False)])
                counter += 1
        return gr_df
#############
def top_correlation_to_name(stocks, column_name, searchstring, top=5):
    """
    This function draws a correlation chart of the top "x" rows of a data frame that are
    highly correlated to a selected row in the dataframe. You can think of the rows of the
    input dataframe as containing stock prices or fund flows or product sales and the columns
    should contain time series data of prices or flows or sales over multiple time periods.
    Now this program will allow you to select the top 5 or 10 rows that are highly correlated
    to a given row selected by the column: column_name and using a search string "searchstring". The
    program will search for the search string in that column column_name and return a list of 5 or 10
    rows that are the most correlated to that selected row. If you give "top" as a float ratio
    then it will use the ratio as the cut off point in the correlation coefficient to select rows.
    """
    incl = [x for x in list(stocks) if x not in column_name]
    ### First drop all NA rows since they will mess up your correlations.
    stocks.dropna(inplace=True)
    ### Now find the highest correlated rows to the selected row ###
    try:
        index_val = search_string(stocks, column_name,searchstring).index[0]
    except:
        print('Not able to find the search string in the column.')
        return
    ### Bring that selected Row to the top of the Data Frame
    df = stocks[:]
    df["new"] = range(1, len(df)+1)
    df.loc[index_val,"new"] = 0
    stocks = df.sort_values("new").drop("new",axis=1)
    stocks.reset_index(inplace=True,drop=True)
    ##### Now calculate the correlation coefficients of other rows with the Top row
    try:
        cordf = pd.DataFrame(stocks[incl].T.corr().sort_values(0,ascending=False))
    except:
        print('Cannot calculate Correlations since Dataframe contains string values or objects.')
        return
    try:
        cordf = stocks[column_name].join(cordf)
    except:
        cordf = pd.concat((stocks[column_name],cordf),axis=1)
    #### Visualizing the top 5 or 10 or whatever cut-off they have given for Corr Coeff
    if top >= 1:
        top10index = cordf.sort_values(0,ascending=False).iloc[:top,:3].index
        top10names = cordf.sort_values(0,ascending=False).iloc[:top,:3][column_name]
        top10values = cordf.sort_values(0,ascending=False)[0].values[:top]
    else:
        top10index = cordf.sort_values(0,ascending=False)[
            cordf.sort_values(0,ascending=False)[0].values>=top].index
        top10names = cordf.sort_values(0,ascending=False)[
            cordf.sort_values(0,ascending=False)[0].values>=top][column_name]
        top10values = cordf.sort_values(0,ascending=False)[
            cordf.sort_values(0,ascending=False)[0].values>=top][0]
    print(top10names,top10values)
    #### Now plot the top rows that are highly correlated based on condition above
    stocksloc = stocks.iloc[top10index]
    #### Visualizing using Matplotlib ###
    stocksloc = stocksloc.T
    stocksloc = stocksloc.reset_index(drop=True)
    stocksloc.columns = stocksloc.iloc[0].values.tolist()
    stocksloc.drop(0).plot(subplots=True, figsize=(15,10),legend=False,
                         title="Top %s Correlations to %s" %(top,searchstring))
    [ax.legend(loc=1) for ax in plt.gcf().axes]
    plt.tight_layout()
    plt.show()
#######################
