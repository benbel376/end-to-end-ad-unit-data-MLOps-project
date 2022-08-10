# importing libraries
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
import re
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import io
from PIL import Image
from collections import OrderedDict
from operator import itemgetter
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from mlflow.models.signature import infer_signature
import mlflow
import pickle
import mlflow.sklearn
import datetime
import json
from sklearn import preprocessing
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
warnings.filterwarnings("ignore")

# adding scripts to path
sys.path.append(os.path.abspath("../scripts/python"))

class Modeling_Utils:

    def __init__(self):
        pass
    
    def summ_columns(self, df, unique=True):
        """
        shows columns and their missing values along with data types.
        Args:
            df: a dataframe to sumarrize.
            unique: whether to include uniqe value count

        Returns:
            df2: a summary datafrme.
        """
        df1 = df.copy()
        df2 = df1.isna().sum().to_frame().reset_index()
        df2.rename(columns = {'index':'variables', 0:'missing_count'}, inplace = True)
        df2['missing_percent_(%)'] = round(df2['missing_count']*100/df1.shape[0])
        data_type_lis = df1.dtypes.to_frame().reset_index()
        df2['data_type'] = data_type_lis.iloc[:,1]
        
        if(unique):
            unique_val = []
            for i in range(df2.shape[0]):
                unique_val.append(len(pd.unique(df1[df2.iloc[i,0]])))
            df2['unique_values'] = pd.Series(unique_val)
        
        return df2


    # remove those variables with more than 30% data missing
    def reduce_dim_missing(self, df,limit):
        """
        removes columns with number of missing values greater than the provided limit
        ARgs:
            df: the dataframe to reduce in dimension
            limit: the trushold percentage of missing values to use as a reference for removal
        Returns
            r_df: reduced dataframe.
        """
        temp = self.summ_columns(df)
        rem_lis = []
        for i in range(temp.shape[0]):
            if(temp.iloc[i,2] > limit):
                rem_lis.append(temp.iloc[i,0])
        r_df = df.drop(rem_lis, axis=1) 
        
        print("successfully removed")

        return r_df


    # fill categorical and Integer variables with mode
    def fill_missing_by_mode(self, df, cols=None):
        """
        fills missing values by mode
        ARgs:
            df: the dataframe to fill
        """
        df = df.copy()
        mod_fill_list = []
        if(cols == None):
            temp = self.summ_columns(df)
            for i in range(temp.shape[0]):
                if(temp.iloc[i,3] == "object"):
                    mod_fill_list.append(temp.iloc[i,0])
        else:
            for col in cols:
                mod_fill_list.append(col)
        
        for col in mod_fill_list:
            df[col] = df[col].fillna(df[col].mode()[0])
        
        print("successfully filled")

        return df


    # fill floating point variables with mean
    def fill_missing_by_mean(self, df, cols=None):
        """
        fills missing values by mean
        ARgs:
            df: the dataframe to fill
        Returns: 
            df: a dataframe filled.
        """
        df = df.copy()
        temp = self.summ_columns(df)
        mean_fill_list = []
        
        if cols is None:
            for i in range(temp.shape[0]):
                if(temp.iloc[i,3] == "float64"):
                    mean_fill_list.append(temp.iloc[i,0])
        else:
            for col in cols:
                mean_fill_list.append(col)
        
        for col in mean_fill_list:
            df[col] = df[col].fillna(df[col].median())
        
        print("successfully filled")

        return df

    # remove those with high correlation
    # label encoding
    def labeler(self, df):
        """
        a one hot encoder
        Args: 
            df: the dataframe to encode
        
        Returns
            df: encoded dataframe.
        """
        df = df.copy()
        le = preprocessing.LabelEncoder()
        labelers = []
        for x in df.columns:
            if df[x].dtypes=='object':
                df[x]=le.fit_transform(df[x].astype(str))
                labelers.append(le)
        print("successfully labeled")

        return df, labelers

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


    def remove_correlated(self, df, th):
        """
        removes highly correlated variables from a dataframe.
        Args:
            df: a features dataframe that holds the variables
            th: a threshold correlation value to decide which variables to remove
        Return:
            features_df: a new features dataframe with low correlation values. 
        """
        try:
            df = df.copy()
            df2, le = self.labeler(df)
            corrmat = df2.corr()
            correlated_features = set()
            for i in range(len(corrmat.columns)):
                for j in range(i):
                    if abs(corrmat.iloc[i, j]) > th:
                        colname = corrmat.columns[i]
                        correlated_features.add(colname)

            print(f"number of correlated variables: {len(correlated_features)}")
            print("..................................................")
            print("correlated features: ", correlated_features)

            features_df = df.drop(labels=correlated_features, axis=1)

            #logger.info("correlated variables successfully removed")

            return features_df

        except:
            #logger.warning("could not remove highly correlated variables")
            pass


    def remove_cols(self, df, cols, keep=False):
        """
        a functions that removes specified columns 
        from dataframe or their inverse
        """
        df = df.copy()
        if(keep):
            r_df = df.loc[:,cols]
        else:
            r_df = df.drop(cols, axis=1, errors='ignore')

        print("successfully removed")

        return r_df

    # use nlp on categorical variables to tokenize them
    # first lets proess the text based features


    def clean_text(self, column):
        """
        Proceses text removing unwanted characters
        Args:
            column: the column to remove from
        
        Return:
            processed_feature: cleaned column
        """
        processed_feature = []

        for sentence in column:
            # Remove all the special characters
            processed = re.sub(r'\W', ' ', str(sentence))

            # remove all single characters
            processed= re.sub(r'\s+[a-zA-Z]\s+', ' ', processed)

            # Remove single characters from the start
            processed = re.sub(r'\^[a-zA-Z]\s+', ' ', processed) 

            # Substituting multiple spaces with single space
            processed = re.sub(r'\s+', ' ', processed, flags=re.I)

            # Removing prefixed 'b'
            processed = re.sub(r'^b\s+', '', processed)

            # Converting to Lowercase
            processed = processed.lower()

            processed_feature.append(processed)
        
        print("successfully cleaned")

        return processed_feature


    # automatic object cleaner.
    def process_features(self, df, cols=None):
        """
        fills missing values by mode
        """
        df = df.copy()
        mod_fill_list = []
        if(cols == None):
            temp = self.summ_columns(df)
            for i in range(temp.shape[0]):
                if(temp.iloc[i,3] == "object"):
                    cleaned_feature = self.clean_text(df.iloc[:,i])
                    df[temp.iloc[i,0]] = cleaned_feature
        
        print("successfully processed")
        
        return df   


    # feature importance
    def get_importance(self, model, df):
        """
        it takes a regression model: model
        it takes a dataframe: df
        it returns a dictionary of importance scores: sortedx
        """
        features = df.columns.to_list()
        importance = model.feature_importances_
        imp_dict = {}
        for i in range(len(features)):
            imp_dict[features[i]] = importance[i]

        imp_dict = OrderedDict(sorted(imp_dict.items(), key=itemgetter(1)))
        features_i = list(imp_dict.keys())
        importance2 = list(imp_dict.values())
        plt.figure(figsize=(16,5))
        pal = sns.color_palette("flare", as_cmap=True)
        ax = sns.barplot(features_i, importance2, color="darkgreen")
        ax.invert_xaxis()
        locs, labels = plt.xticks()
        plt.setp(labels, rotation=45)
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        plt.savefig("../models/important_features.png")

        im = Image.open(img_buf)
        im.show(title="My Image")

        img_buf.close()
        imp_dict

        print("successfully returned")

        return img_buf, imp_dict


    def train(self, features, target, max_depth, max_feat, n_estimators):
        """
        :param fpath: Path or URL for the training data used with the model.
        :max_detph: int Max tree depth
        :max_features: float percentage of features to use in classification
        :n_estimators: int number of trees to create
        :return: Trained Model
        """
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=0)
        mod = RandomForestClassifier(max_depth=max_depth, max_features=max_feat, n_estimators=n_estimators, random_state=0)

        mod.fit(X_train, y_train)
        predictions = mod.predict(X_test)

        c_mat = confusion_matrix(y_test,predictions)
        print(classification_report(y_test,predictions))
        acc = accuracy_score(y_test, predictions)

        mlparams = {"max_depth": str(max_depth),
                    "max_features": str(max_feat),
                    "n_estimators": str(n_estimators),
                    }
        

        mlmetrics = {"accuracy": acc}
        
        print("successfully trained and tested")

        return mod, mlparams, mlmetrics


    def ml_track(self, encoder, model, params, metrics):
        artifact_path = "Airline-Demo"
        experiment_name = "adludio_challenge"
        run_name = f'run{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'
        model_name = f'adludio_model{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'
        encoder_name = f'adludio_encoder{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'
        arti_path = "adludio"

        mlflow.set_tracking_uri(uri='sqlite:////tmp/mlflow-db.sqlite')
        try:
            experiment_id = mlflow.create_experiment(name=experiment_name)
        except:
            experiment_id = mlflow.get_experiment_by_name(name=experiment_name).experiment_id
            
        mlflow_run = mlflow.start_run(experiment_id=experiment_id, run_name=run_name)
        with mlflow_run: 
            mlflow.log_params(params)
            mlflow.log_metrics(metrics)            
            mlflow.sklearn.log_model(model, artifact_path=arti_path, registered_model_name=model_name)

        with open(f'../models/{encoder_name}.pkl', "wb") as f: 
            pickle.dump(encoder, f)
        # Save model based on time st
        with open(f'../models/{model_name}.pkl', "wb") as f2:
            pickle.dump(model, f2)

        # Serialize data into file:
        manifest = {"model": model_name, "encoder":encoder_name}
        with open( "../models/manifest.json", 'w' ) as f3:
            json.dump(manifest, f3)

        print("successfully saved")


    def load_model(self):
        # Read data from file:
        manifest = None
        with open( "../models/manifest.json", 'rb' ) as f4:
            manifest = json.load(f4)

        model_name = f"../models/{manifest['model']}.pkl"
        encoder_name = f"../models/{manifest['encoder']}.pkl"

        with open(model_name, 'rb') as f:
            model = pickle.load(f)
        
        with open(encoder_name, 'rb') as f:
            encoder = pickle.load(f)

        print("successfully loaded")

        return model, encoder