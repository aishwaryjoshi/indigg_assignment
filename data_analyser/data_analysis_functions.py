from typing import List
import os

from pyspark.sql import functions as F, DataFrame
import matplotlib.pyplot as plt

from data_analyser.dataframe_models import TableData


def _sales_per_platform(df: DataFrame) -> DataFrame:
    """
    Function performs aggregation on the input DataFrame
    to calculate the total sales per platform. Then plot
    the results using Matplotlib and saves the plot
    as a PDF file in the "plotted_graphs" directory.
    """
    # Aggregate the sales columns using the sum function
    sales_aggregated = df.groupBy("platform").agg(
        F.sum("global_sales").alias("total_global_sales"),
    )

    # Convert the aggregated data to Pandas DataFrame
    sales_pandas = sales_aggregated.toPandas()
    plt.figure(figsize=(60, 10))
    plt.bar(sales_pandas["platform"], sales_pandas["total_global_sales"])
    plt.xlabel("Platform")
    plt.ylabel("Total Sales")
    plt.title("Total Sales by Platform")
    save_dir = "./plotted_graphs"
    os.makedirs(save_dir, exist_ok=True)
    plt.savefig(f"{save_dir}/sales_per_platform.pdf")


def perform_analysis(df: DataFrame) -> DataFrame:
    """
    Wrapper/helper function to invoke above function, which performs sales analysis
    """
    _sales_per_platform(df)
