import pandas as pd
import pyspark

from spark_dataframe_tools.functions.generator import show_pd_df
from spark_dataframe_tools.functions.generator import show_size_df
from spark_dataframe_tools.functions.generator import show_spark_df
from spark_dataframe_tools.utils import BASE_DIR

pyspark.sql.dataframe.DataFrame.show2 = show_spark_df
pyspark.sql.dataframe.DataFrame.size = show_size_df
pd.DataFrame.show2 = show_pd_df

dataframe_all = ["show_pd_df", "show_spark_df", "apply_dataframe"]

__all__ = dataframe_all
