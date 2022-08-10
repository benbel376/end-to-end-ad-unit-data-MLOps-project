import json
import pandas as pd


class Ingest:

    def __init__(self):
        pass

    def load_json(self, path):
        """
        loads a json file.
        Args:
            path: path of the file and its name

        Return: 
            Nested_json: the extracted json.
        """
        with open(path) as json_file:
            nested_json = json.load(json_file)
        return nested_json

    def flatten_json(self, nested_json):
        """
        flattens the nested json object into one with just one level
        Args:
            nested_json: a nested json object

        Returns:
            df: a dataframe 
        """
        out = {}
        def flatten(x, name=''):
            if type(x) is dict:
                for a in x:
                    flatten(x[a], name + a + '&')
            else:
                out[name[:-1]] = x
            return out
        try:
            df = pd.Series(flatten(nested_json)).to_frame()
            return df.reset_index()
        except Exception as e:
            print(e)

    def restructure(self, df1):
        """
        Restructures the dataframe into oen with multiple columns

        """
        cols = [[], [], [], [], [], []]
        try:
            for i in range(len(df1)):
                lis = df1.iloc[i,0].split("&")
                for k in range(6):
                    try:
                        cols[k].append(lis[k].strip())
                    except:
                        cols[k].append("NAv")
            df_new = pd.DataFrame()

            df_new["game_key"] = cols[0]
            df_new["request_id"] = cols[1]
            df_new["design_feature"] = cols[2]
            df_new["feature_type"] = cols[3]
            df_new["feature_variety"] = cols[4]
            df_new["sub_feature"] = cols[5]
            df_new["feature_value"] = df1.iloc[:,1].tolist()

            df_new["game_key"] = df_new[["game_key", "request_id"]].apply("/".join, axis=1)
            df_new = df_new.drop('request_id', axis=1)
            return df_new
        except Exception as e:
            print(e)