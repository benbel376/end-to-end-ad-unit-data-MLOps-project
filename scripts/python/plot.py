"""Plotting script for the results of the simulation."""

import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns

from logger import Logger
from pandas.plotting import scatter_matrix

from pandas_profiling import ProfileReport


class Plot:
    def __init__(self) -> None:
        """Initilize class."""
        try:
            pass
            self.logger = Logger("plot.log").get_app_logger()
            self.logger.info("Successfully Instantiated Preprocessing Class Object")
        except Exception:
            self.logger.exception("Failed to Instantiate Preprocessing Class Object")
            sys.exit(1)

    def plot_profile(self, df: pd.DataFrame, title: str) -> None:
        """Plot the profile of the dataset.
        Args:
            df(pd.DataFrame): Dataframe to be plotted.
            title(str): title of chart.
        """
        profile = ProfileReport(df)
        profile.to_file(output_file=f"{title}.html")
        self.logger.info("Plotting a profile for the dataset: ")
        return profile

    def plot_hist(self, df: pd.DataFrame, column: str, color: str) -> None:
        """Plot the hist of the column.
        Args:
            df(pd.DataFrame): Dataframe to be plotted.
            column(str): column to be plotted.
            color(str): color of the histogram.
        """
        # plt.figure(figsize=(15, 10))
        # fig, ax = plt.subplots(1, figsize=(12, 7))
        sns.displot(data=df, x=column, color=color, kde=True, height=7, aspect=2)
        plt.title(f"Distribution of {column}", size=20, fontweight="bold")
        # self.logger.info(
        #     'Plotting a histogram')
        plt.show()

    def plot_hist_subplot(self, df: pd.DataFrame, columns: list) -> None:
        """Plot multiple displot for the columns.
        Args:
            df(pd.DataFrame): Dataframe to be plotted.
            columns(list): list of columns to be plotted.
        
        Returns:
            None
        """

        # plot the histogram of the columns
        self.logger.info("Plotting multiple histogram")
        sns.set()
        fig, ax = plt.subplots(len(columns), figsize=(20, 15))
        for i, col in enumerate(columns):
            sns.distplot(df[col], ax=ax[i])
            ax[i].set_title(col, size=20)
        plt.show()

    def plot_count(self, df: pd.DataFrame, column: str) -> None:
        """Plot the count of the column.
        Args:
            df(pd.DataFrame): Dataframe to be plotted.
            column(str): column to be plotted.
        """
        sns.set()
        plt.figure(figsize=(12, 7))
        self.logger.info("Plotting a plot_count")
        sns.countplot(data=df, x=column)
        plt.title(f"Countplot of {column}", size=20, fontweight="bold")
        plt.show()

    def plot_bar(
        self,
        df: pd.DataFrame,
        x_col: str,
        y_col: str,
        title: str,
        xlabel: str,
        ylabel: str,
    ) -> None:
        """Plot bar of the column.
        Args:
            df(pd.DataFrame): Dataframe to be plotted.
            x_col(str): column to be plotted.
        """
        plt.figure(figsize=(12, 7))
        sns.barplot(data=df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        plt.xlabel(xlabel, fontsize=16)
        plt.ylabel(ylabel, fontsize=16)
        # self.logger.info(
        #     'Plotting a bar chart')
        plt.show()

    def plot_heatmap2(self, df: pd.DataFrame, title: str, cbar=False) -> None:
        """Plot Heat map of the dataset.
        Args:
            df(pd.DataFrame): Dataframe to be plotted.
            title(str): title of chart.
        """
        # num_cols = df.select_dtypes(include=np.number).columns
        plt.figure(figsize=(12, 7))
        sns.heatmap(
            df,
            annot=True,
            cmap="viridis",
            vmin=0,
            vmax=1,
            fmt=".2f",
            linewidths=0.7,
            cbar=cbar,
        )
        plt.title(title, size=18, fontweight="bold")
        # self.logger.info(
        #     'Plotting a heatmap for the dataset: ')
        plt.show()

    def plot_heatmap(self, df: pd.DataFrame, title: str, cbar=False) -> None:
        """Plot Heat map of the dataset.
        Args:
            df(pd.DataFrame): Dataframe to be plotted.
            title(str): title of chart.
        """
        # Increase the size of the heatmap.
        plt.figure(figsize=(26, 12))
        heatmap = sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True)
        heatmap.set_title(title, fontdict={"fontsize": 8}, pad=12)

    def plot_box(self, df: pd.DataFrame, x_col: str, title: str) -> None:
        """Plot box chart of the column.
        Args:
            df(pd.DataFrame): Dataframe to be plotted.
            x_col(str): column to be plotted.
            title(str): title of chart.
        """
        plt.figure(figsize=(12, 7))
        sns.boxplot(data=df, x=x_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        # self.logger.info(
        #     'Plotting a box plot for Column: ', x_col)
        plt.show()

    def plot_box_multi(
        self, df: pd.DataFrame, x_col: str, y_col: str, title: str
    ) -> None:
        """Plot the box chart for multiple column.
        Args:
            df(pd.DataFrame): Dataframe to be plotted.
            column(str): column to be plotted.
        """
        plt.figure(figsize=(12, 7))
        sns.boxplot(data=df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        # self.logger.info(
        #     'Plotting a multiple box plot: ')
        plt.show()

    def plot_scatter(
        self, df: pd.DataFrame, x_col: str, y_col: str, title: str, hue: str, style: str
    ) -> None:
        """Plot Scatter chart of the data.
        Args:
            df(pd.DataFrame): Dataframe to be plotted.
            column(str): column to be plotted.
        """
        plt.figure(figsize=(12, 7))
        sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, style=style)
        plt.title(title, size=20)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        # self.logger.info(
        #     'Plotting a scatter plot')
        plt.show()

    def plot_pie(self, data, labels, title="") -> None:
        """Plot pie chart of the data.
        Args:
            data(list): Data to be plotted.
            labels(list): labels of the data.
            colors(list): colors of the data.
        """
        # plt.figure(figsize=(12, 7))
        # colors = sns.color_palette("bright")
        # plt.pie(data, labels=labels, colors=colors, autopct="%.0f%%")
        # plt.title(title, size=20)
        # # self.logger.info(
        # #     'Plotting a pie chart')
        # plt.show()
        sns.set()
        fig = go.Figure(
            data=[
                go.Pie(
                    labels=labels, values=data.value_counts(), textinfo="label+percent",
                )
            ]
        )
        fig.update_traces(
            hoverinfo="label+percent",
            textinfo="value",
            textfont_size=20,
            marker=dict(
                colors=["darkorange", "gold"], line=dict(color="#000000", width=2)
            ),
        )
        fig.show()

    # function to get the values in a plot
    def plot_hist_2d(
        self,
        df1: pd.DataFrame,
        df2: pd.DataFrame,
        x_col: str,
        y_col: str,
        title: str,
        label1,
        label2,
    ) -> None:
        """Plot multiple histograms of the data.
        Args:
            df(pd.DataFrame): Dataframe to be plotted.
            x_col(str): column to be plotted.
        """
        sns.set()
        plt.hist(df1[x_col], color="black", alpha=0.3, label=label1)
        plt.hist(df2[y_col], color="red", alpha=0.3, label=label2)
        plt.legend()
        plt.plot()
        plt.title(title, size=20)
        # self.logger.info(
        #     'Plotting multiple histogram')
        plt.show()

    def outliers_plot(self, data, cols) -> None:
        """Plot outliers of the data.
        Args:
            data(pd.DataFrame): Dataframe to be plotted.
        """
        names = cols
        # convert DataFrame to list
        values = []
        for column in data.iloc[:, 5:11].columns:
            li = data[column].tolist()
            values.append(li)
        colors = [
            "gold",
            "mediumturquoise",
            "darkorange",
            "lightgreen",
            "cyan",
            "royalblue",
        ]

        fig = go.Figure()
        for xd, yd, cls in zip(names, values, colors):
            fig.add_trace(
                go.Box(
                    y=yd,
                    name=xd,
                    boxpoints="outliers",
                    jitter=0.5,
                    whiskerwidth=0.2,
                    fillcolor=cls,
                    marker_size=3,
                    line_width=2,
                )
            )
        fig.show()

    def get_value(self, figure):
        """Get values in a plot.
        Args:
            figure(_type_): _description_
        """
        # self.logger.info(
        #     'Getting value for a plot')
        for p in figure.patches:
            figure.annotate(
                format(p.get_height()),
                (p.get_x() + p.get_width() / 2.0, p.get_height()),
                ha="center",
                va="center",
                xytext=(0, 10),
                textcoords="offset points",
            )

    # function to set figure parameters

    def fig_att(self, figure, title, titlex, titley, size, sizexy, weight):
        """Plot chart of the data.
        Args:
            figure(_type_): figure to be plotted.
            title(_type_): title of plot
            titlex(_type_): x axis title
            titley(_type_): y axis title
            size(_type_): size of plot
            sizexy(_type_): size of x and y axis
            weight(_type_): weight of title
        """
        # setting the parameters for the title, x and y labels of the plot
        figure.set_title(title, size=size, weight=weight)
        figure.set_xlabel(titlex, size=sizexy, weight=weight)
        figure.set_ylabel(titley, size=sizexy, weight=weight)
        # self.logger.info(
        #     'set figure parameters')

    # function to change rotation of the x axis tick labels
    def rotate(self, figure, rotation):
        """Rotate the x axis tick labels.
        Args:
            figure(_type_): figure to be plotted.
            rotation(_type_): rotation of x axis tick labels
        """
        # changing the rotation of the x axis tick labels
        # self.logger.info(
        #     'Plotting a chart')
        for item in figure.get_xticklabels():
            item.set_rotation(rotation)

    def sc_matrix(self, df: pd.DataFrame, title: str) -> None:
        """Plot the scatter matrix of the data.
        Args:
            df(pd.DataFrame): Dataframe to be plotted.
            title(str): title of chart.
        """
        plt.figure(figsize=(12, 7))
        sns.pairplot(df)
        plt.title(title, size=20)
        # self.logger.info(
        #     'Plotting a scatter matrix')
        scatter_matrix(df, alpha=0.2, figsize=(12, 7), diagonal="kde")
        # plt.show()

    def plot_subplots(self, x: str, y: str, xtitle: str, ytitle: str) -> None:
        """Plot the subplots of the data.
        Args:
            df(pd.DataFrame): Dataframe to be plotted.
            title(str): title of chart.
        """
        sns.set(style="whitegrid")
        fig, axes = plt.subplots(nrows=1, ncols=2)
        fig.set_size_inches(25, 8)
        x.hist(ax=axes[0], alpha=0.3, color="red", bins=20)
        y.hist(ax=axes[1], alpha=0.3, color="blue", bins=20)
        axes[0].set_title(xtitle, size=20)
        axes[1].set_title(ytitle, size=20)
        # self.logger.info(
        #     'Plotting a subplots')
        plt.show()

    def plot_hist_muli(self, df):
        """Plot multiple Histogram."""
        sns.set()
        num_feats = list(
            df.select_dtypes(include=["int64", "float64", "int32"]).columns
        )
        # self.logger.info("Plotting multiple histogram")
        df[num_feats].hist(figsize=(20, 15))

    def plot_feature_importance(self, importance, names, model_type, path):
        """Feature importance plot."""
        sns.set(style="whitegrid")
        # Create arrays from feature importance and feature names
        feature_importance = np.array(importance)
        feature_names = np.array(names)

        # Create a DataFrame using a Dictionary
        data = {
            "feature_names": feature_names,
            "feature_importance": feature_importance,
        }
        fi_df = pd.DataFrame(data)

        # Sort the DataFrame in order decreasing feature importance
        fi_df.sort_values(by=["feature_importance"], ascending=False, inplace=True)

        # Define size of bar plot
        plt.figure(figsize=(10, 8))
        # Plot Searborn bar chart
        sns.barplot(x=fi_df["feature_importance"], y=fi_df["feature_names"])
        # Add chart labels
        plt.title(model_type + " FEATURE IMPORTANCE")
        plt.xlabel("FEATURE IMPORTANCE")
        plt.ylabel("FEATURE NAMES")
        # Save the chart to path
        plt.savefig(path)
        # plt.show()

    def plot_prediction(self, model, x, y, path):
        """Prediction plot."""
        sns.set(style="whitegrid")
        plt.figure(figsize=(12, 8))
        plt.plot(y[:40], color="blue", label="Actual")
        plt.plot(model.predict(x)[:40], color="red", label="Predicted")
        plt.legend()
        plt.savefig(path)