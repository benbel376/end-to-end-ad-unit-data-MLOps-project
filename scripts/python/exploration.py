import pandas as pd
import matplotlib.pyplot as plt

class Processing:

    def __init__(self):
        pass

    def find_agg(self, df, group_columns, agg_columns, agg_metrics, new_columns):
        """
        a function that returns a new dataframe with aggregate values of specified columns.
        """
        new_column_dict ={}
        agg_dict = {}
        for i in range(len(agg_columns)):
            new_column_dict[agg_columns[i]] = new_columns[i]
            agg_dict[agg_columns[i]] = agg_metrics[i]

        new_df = df.groupby(group_columns).agg(agg_dict).reset_index().rename(columns=new_column_dict)
        return new_df
    
    def showDistribution(self, df, cols, colors):
        """
        Distribution plotting function.
        """
        for index in range(len(cols)):
            plt.style.use('fivethirtyeight')
            plt.figure(figsize=(8, 4)) 
            sns.displot(data=df, x=cols[index], color=colors[index], kde=True, height=4, aspect=2)
            plt.title(f'Distribution of '+cols[index]+' data volume', size=20, fontweight='bold')
            plt.show()