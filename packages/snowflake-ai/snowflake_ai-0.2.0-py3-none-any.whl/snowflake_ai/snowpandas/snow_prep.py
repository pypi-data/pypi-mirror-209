# Copyright (c) 2023, Tony Liu
#
# Licensed under the Apache License, Version 2.0 (the "License");
# Use, reproduction and distribution of this software in source and 
# binary forms, with or without modification, are permitted provided that
# the License terms and conditions are met; you may not use this file
# except in compliance with the License. See the LICENSE file for details.

"""
This module contains SnowEDA and SnowPrep class specific for 

"""

__author__ = "Tony Liu"
__email__ = "tony.liu@yahoo.com"
__license__ = "Apache License 2.0"
__version__ = "0.2.0"


from typing import (
    Dict, Union, Optional, List
)

from pandas import DataFrame as DF
import json
from sklearn.preprocessing import LabelEncoder
from snowflake.snowpark.functions import udf
from snowflake.snowpark.types import IntegerType

from snowflake.snowpark import DataFrame as SDF
from snowflake.snowpark.functions import col, object_construct, CaseExpr
from snowflake.snowpark.functions import lit, array_agg, to_varchar, when
from snowflake.snowpark.functions import sql_expr, iff

from snowflake_ai.snowpandas import EDA, DataPrep, SnowSetup



class SnowEDA(EDA):
    """
    This class extends EDA for Snowflake specific data exploration.

    To use this class, instantiate SnowEDA with SnowSetup as follows:

        from snowflake_ai.common import SnowConnect
        from snowflake_ai.snowpandas import SnowSetup

        conn: SnowConnect = SnowConnect()
        setup: SnowSetup = SnowSetup(conn)
        eda: SnowEDA = SnowEDA(setup)
    
    """
    def __init__(
        self, 
        setup: SnowSetup,
        dfs: Optional[Dict[str, SDF]] = None
    ):
        super().__init__(setup)
        self._sdf = SDF()
        if dfs is not None and isinstance(dfs, Dict):
            for _, value in dfs.items():
                if not isinstance(value, SDF):
                    raise TypeError(
                        f"Dictionary values must be DataFrames, "
                        f"but got {type(value)} instead!"
                    )
            self._data = dfs


    def all_dfs(self) -> Dict[str, SDF]:
        """
        Get all dataframes for exploration.

        Returns:
            Dict: dictionary of dataframes
        """
        return self._data
    

    def active_df(
        self, 
        df_name: Optional[str] = None,
        df: Optional[SDF] = None
    ) -> SDF:
        """
        Get active Snowflake dataframe for exploration.

        Args:
            df_name (str): Snowflake Dataframe name.
            df (DataFrame): set the Snowflake dataframe as active

        Returns:
            DataFrame: active snowflake dataframe for exploration
        """
        if df_name is not None :
            try:
                if df_name in self._data.keys():
                    self._sdf = self._data[df_name]
            except:
                raise ValueError(
                    f"Dictionary of DataFrame doesn't have the key: {df_name}"
                )
            if df is not None:
                self._sdf = df
                self._data[df_name] = df
        elif df is not None:
            self._sdf = df
            self._data[EDA.T_DEFAULT_DF] = df            
        return self._sdf
    

    @staticmethod
    def top_df(df: SDF, n: int = 10, by_col: str = None,
        is_asc: bool = False
    ) -> DF:
        """
        Return pandas dataframe of top n rows from snowflake dataframe
        ordered by one column

        Args:
            df (DataFrame): Snowflake dataframe
            n (int): top n rows
            by_col (str): name of the column ordered by
            is_asc (bool): True if it is ascending order; default False
         
        Returns:
            DataFrame: Pandas Dataframe.
        """
        if by_col is None:
            return df.limit(n).to_pandas()
        else:
            sorted_sdf = df.sort(col(by_col), ascending=is_asc)
            return sorted_sdf.limit(n).to_pandas()
        

    def desc(self, df_name: Optional[str] = None):
        """
        Describe the dataframe by dataframe name.

        Args:
            df_name (str): dataframe name. if emptry, the current
                active dataframe desc is called.
         
        Returns:
            Series or DataFrame: Summary statistics of the Series or
                Dataframe provided.
        """
        if df_name is None:
            return self._df.describe()
        elif df_name is not None and isinstance(self._data, Dict):
            return self._data[df_name].describe()
        else:
            raise TypeError(
                f"df_name or initialization of dataframe is required"
            )



class SnowPrep(DataPrep):
    """
    This class extends EDA for Snowflake specific data exploration.

    To use this class, instantiate SnowEDA with SnowSetup as follows:

        >>> from snowflake_ai.common import SnowConnect
        >>> from snowflake_ai.snowpandas import SnowSetup
        ... 
        >>> conn: SnowConnect = SnowConnect()
        >>> setup: SnowSetup = SnowSetup(conn)
        >>> eda: SnowEDA = SnowEDA(setup)
    
    """

    def __init__(
        self, 
        setup: SnowSetup,
        dfs: Optional[Union[SDF, Dict[str, SDF]]] = None
    ):
        super().__init__(setup)

    
    @property
    def data_setup(self) -> SnowSetup:
        if isinstance(self.data_setup, SnowSetup):
            return self.data_setup
        else:
            raise TypeError(
                "SnowPrep.data_setup: The datasetup should be SnowSetup"
            )    


    @staticmethod
    def check_input_columns(df:SDF, input_columns):
        """
        Checks and formats the input_columns parameter.

        If input_columns is None, it defaults to using all columns 
        in the DataFrame. If input_columns is not a list (i.e., it's a
        single column name), it wraps it in a list.

        Parameters:
            df (DataFrame): The DataFrame whose columns are to be checked.
            input_columns (None, str, list): The columns to check. This 
            could be None, a single column name, or a list of column names.

        Returns:
            list: A list of column names from the DataFrame.
        """
        if not input_columns:
            input_columns = df.columns
        else:
            if not isinstance(input_columns, list):
                input_columns = [input_columns]

        return input_columns


    @staticmethod
    def get_columns_unique_categories(
            df: SDF, 
            categories : Dict = {}, 
            cat_cols: List = []
    ):
        """
        Generate a dictionary containing unique categories for each specified
        column in the DataFrame.
        
        Parameters:
        df (DataFrame): The DataFrame to extract categories from.
        categories (str, dict): Parameter to determine whether to automatically 
            generate categories. If empty, unique categories are computed for each
            column. If it's a dictionary, it's assumed that the unique categories 
            for each column are already defined.
        cat_cols (list): The list of column names to extract categories from.
        
        Returns:
            dict: A dictionary where keys are column names and values are lists of
            unique categories.
        """
        if categories == "":
            obj_const_args = []
            
            for c in cat_cols:
                # Get a sorted list of unique string values in the column
                unique_values_agg = array_agg(to_varchar(c), is_distinct=True)\
                    .within_group(to_varchar(col(c)).asc())
                # Add column name and unique values to the argument list
                obj_const_args.extend([lit(c), unique_values_agg])
            
            # Create a DataFrame with one row and one column named "cats",
            # containing a dictionary of unique categories for each column
            df_cats = df.select(
                    object_construct(*obj_const_args).alias("cats")
                )

            cats_dict = json.loads(df_cats.collect()[0]["cats"])
        else: 
            cats_dict = categories

        return cats_dict



class SnowEncoder:
    T_PROC_DROP = -1
    T_PROC_SKIP = 0
    T_PROC_GEN = 1

    def __init__(
            self,
            input_cols: Optional[Union[List[str], str]] = None,
            output_cols: Optional[Union[Dict, str]] = None,
            categories: Optional[Dict] = None,
            process_flag: int = 1
    ):
        """
        Encode categorical features using one-hot encoding
        
        Parameters:
            input_cols: name of column or list of columns to encode
            output_cols: name of output column or list of output 
                columns,need to be in the same order as the categories
            categories: {} or specified as a dict: 
                {"COL1": [cat1, cat2, ...], "COL2": [cat1, cat2, ...], ...}
            proc_flags: 
                -1 - drop columns
                 0 - skip columns keeping as it is
                 1 - default to generate matching unknown columns
        """
        self.input_cols = input_cols
        self.output_cols = output_cols
        self.fitted_values = {}
        self.categories = categories
        self.process_flag = process_flag


    def fit(self, df: SDF) -> 'SnowEncoder':
        pass


    def transform(self, df: SDF) -> SDF:
        pass


    def check_fitted(encoder):
        if not hasattr(encoder, "fit"):
            raise TypeError(f"{encoder} is not an encoder instance.")

        fitted = [
            v for v in vars(encoder) if v.endswith("_")
        ]
        if not fitted:
            raise TypeError(f"{type(encoder).__name__} not fitted.")


    def check_columns(columns:List[str], df:SDF):
        df_columns = set(df.columns)
        target_cols = set([col.upper() for col in columns])

        missing_cols = target_cols - df_columns
        if len(missing_cols):
            raise ValueError(
                f"Cannot find columns {missing_cols} in the input dataframe."
            )


    def encode_column_expressions(encoder):
        """
        Builds a list of Column expressions that map categories in columns
        to integer indices. 

        Parameters:
            encoder: An object containing 'input_cols' (columns to be encoded), 
            'fitted_values_' (unique categories per column), 
            and optionally 'handle_unknown' (a strategy to handle unknown 
            categories) and 'unknown_value' (value to replace unknown 
            categories).

        Returns:
            List[Column]: A list of PySpark Column expressions defining the 
                encoding for each column.
        """
        col_exprs = []
        input_cols = encoder.input_cols
        fitted_cats = encoder.fitted_values

        for column in input_cols:
            case_expression = None
            for index, category in enumerate(fitted_cats[column]):
                if isinstance(case_expression, CaseExpr):
                    case_expression = case_expression.when(
                        col(column) == lit(category), lit(index)
                    )
                else:
                    case_expression = when(
                        col(column) == lit(category), lit(index)
                    )

            # set to 'use_encoded_value' if 'handle_unknown' attribute exists
            if hasattr(encoder, 'handle_unknown') and \
                    encoder.handle_unknown == "use_encoded_value":
                case_expression = case_expression.otherwise(
                    lit(encoder.unknown_value)
                )

            col_exprs.append(case_expression)

        return col_exprs


    def decode_column_to_sql_expressions(encoder):
        """
        Generates a list of SQL expressions to map encoded indices back
        to original categories.

        Parameters:
        encoder: An object containing 'output_cols' (columns after encoding),
             'fitted_values_' (unique categories per column), 
            and 'input_cols' (original columns before encoding).

        Returns:
        List[Column]: A list of PySpark SQL expressions defining the decoding 
            for each column.
        """
        input_columns = encoder.input_cols
        output_columns = encoder.output_cols
        fitted_categories = encoder.fitted_values

        # Create tuples of corresponding input and output columns
        column_pairs = list(zip(input_columns, output_columns))
        sql_expressions = []
        
        for input_col, output_col in column_pairs:
            # Convert fitted categories to JSON and create SQL expression
            json_categories = json.dumps(fitted_categories[input_col])
            sql_expression = sql_expr(
                f"AS_CHAR(PARSE_JSON('{json_categories}')[{output_col}])"
            )

            sql_expressions.append(sql_expression)

        return sql_expressions


    def encode_column_names(self):
        """
        Generate encoded column names for categorical variables.
        """

        cat_cols = {}

        if self.output_cols:
            if len(self.output_cols) != len(self.input_cols):
                raise ValueError(
                    f"Number of output columns ({len(self.output_cols)}) "\
                    f"should match number of input columns "\
                    f"({len(self.input_cols)})."
                )

            total_categories = sum(len(self.fitted_values[col]) \
                    for col in self.input_cols)
            total_output_cols = sum(len(self.output_cols[col]) \
                    for col in self.output_cols)

            if total_categories != total_output_cols:
                raise ValueError(
                    f"Total categories ({total_categories}) should match "\
                    f"total output columns ({total_output_cols}).")

            cat_cols = self.output_cols

        else:
            # Generate encoded column names
            for col in self.input_cols:
                cat_cols[col] = [
                    f'{col}_{val}' for val in self.fitted_values[col]
                ]

        total_cols = sum(len(cat_cols[col]) for col in cat_cols)
        if total_cols > 3650:
            raise ValueError("Too many columns; use other encoder instead.")

        return cat_cols


    def fit_transform(self, df: SDF) -> SDF:
        """
        Fit with this encoder and transform the dataframe.

        Parameters:
            df: DataFrame to encode

        Return:
            Encoded DataFrame
        """
        return self.fit(df).transform(df)    


class OneHotEncoder(SnowEncoder):

    def fit(self, df: SDF) -> 'OneHotEncoder':
        """
        Fit the OneHotEncoder using df.

        Parameters:
            df: Snowflake DataFrame used for getting the categories for
                each input column
        
        Return: 
            Fitted encoder
        """
        encode_cols = SnowPrep.check_input_columns(df, self.input_cols)
        self.input_cols = encode_cols

        self.fitted_values = SnowPrep.get_columns_unique_categories(
            df, self.categories, encode_cols)

        return self
    

    def transform(self, df: SDF) -> SDF:
        """
        Transform dataframe df using one-hot encoding creating one new 
        column for each category found with fit.

        If process_flag is -1 then the input columns are dropped

        Parameters:
            df: Snowpark DataFrame to transform
        
        Return: 
            Encoded Snowpark DataFrame
        """
        self.check_fitted()
        out_cols = self.encode_column_names()
        self.output_cols = out_cols

        for c in self.input_cols:
            uniq_vals = self.fitted_values[c]
            col_names = out_cols[c]
            df = df.with_columns(
                col_names, 
                [iff(col(c) == val, lit(1), lit(0)) for val in uniq_vals]
            )
            if self.process_flag == self.T_PROC_GEN:
                df = df.with_column(
                    f"{c}__unknown", 
                    iff(~ col(c).in_(uniq_vals), lit(1), lit(0))
                )

            if self.process_flag == self.T_PROC_DROP:
                df = df.drop(c)

        return df



class BinaryEncoder(SnowEncoder):
    """
    A binary encoder that encodes categorical features using a 
    binary scheme.
    """

    def fit(self, df: SDF) -> 'BinaryEncoder':
        """
        Fit the BinaryEncoder using df.

        Parameters:
            df: DataFrame used for getting the categories for each input
                column
        Return: 
            Fitted encoder
        """
        encode_cols = SnowPrep.check_input_columns(df, self.input_cols)
        self.input_cols = encode_cols

        self.fitted_values = {}
        for col in self.input_cols:
            categories = SnowPrep.get_columns_unique_categories(df, None, [col])
            label_encoder = LabelEncoder()
            label_encoder.fit(categories)
            self.fitted_values[col] = label_encoder

        return self


    def transform(self, df: SDF) -> SDF:
        """
        Transform dataframe df using binary encoding, creating new columns for 
        each bit of the binary representation of the category.

        If process_flag is -1 then the input columns are dropped

        Parameters:
            df: DataFrame to transform

        Return: 
            Encoded DataFrame
        """
        self.check_fitted()

        for c in self.input_cols:
            label_encoder:LabelEncoder = self.fitted_values[c]
            
            # Define UDF to apply the label encoder and transform to binary
            encode_udf = udf(
                lambda category: label_encoder.transform([category])[0], 
                IntegerType()
            )
            
            df = df.withColumn(c, encode_udf(df[c]))

            if self.process_flag == self.T_PROC_DROP:
                df = df.drop(c)

        return df


class OrdinalEncoder(SnowEncoder):
    """
    An ordinal encoder that encodes categorical features using an 
    ordinal scheme.
    """

    def fit(self, df: SDF) -> 'OrdinalEncoder':
        """
        Fit the OrdinalEncoder using df.

        Parameters:
            df: DataFrame used for getting the categories for each input
                column
        Return: 
            Fitted encoder
        """
        encode_cols = SnowPrep.check_input_columns(df, self.input_cols)
        self.input_cols = encode_cols

        self.fitted_values = {}
        for col in self.input_cols:
            categories = SnowPrep.get_columns_unique_categories(df, None, [col])
            label_encoder = LabelEncoder()
            label_encoder.fit(categories)
            self.fitted_values[col] = label_encoder

        return self


    def transform(self, df: SDF) -> SDF:
        """
        Transform dataframe df using ordinal encoding, creating new columns 
        for each category in ordinal form.

        If process_flag is -1 then the input columns are dropped

        Parameters:
            df: DataFrame to transform

        Return: 
            Encoded DataFrame
        """
        self.check_fitted()

        for c in self.input_cols:
            label_encoder:LabelEncoder = self.fitted_values[c]
            
            # Define UDF to apply the label encoder
            encode_udf = udf(
                lambda category: label_encoder.transform([category])[0], 
                IntegerType()
            )
            
            df = df.withColumn(c, encode_udf(df[c]))

            if self.process_flag == self.T_PROC_DROP:
                df = df.drop(c)

        return df
