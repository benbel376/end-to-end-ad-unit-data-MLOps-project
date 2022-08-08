import pandas as pd

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

    def summ_columns(self, df, unique=True):
        """
        shows columns and their missing values along with data types.
        """
        df2 = df.isna().sum().to_frame().reset_index()
        df2.rename(columns = {'index':'variables', 0:'missing_count'}, inplace = True)
        df2['missing_percent_(%)'] = round(df2['missing_count']*100/df.shape[0])
        data_type_lis = df.dtypes.to_frame().reset_index()
        df2['data_type'] = data_type_lis.iloc[:,1]
        
        if(unique):
            unique_val = []
            for i in range(df2.shape[0]):
                unique_val.append(len(pd.unique(df[df2.iloc[i,0]])))
            df2['unique_values'] = pd.Series(unique_val)
        return df2