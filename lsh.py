from typing import List, Set

import pandas as pd

from steps.create_buckets import get_buckets
from steps.create_signatures import create_signature
from helpers.strings.string_utilities import ngrams_set
from helpers.math.hash import get_hash_functions


def create_ngrams(df: pd.DataFrame, column_names: List[str], ngrams_size: int):
    universal_set: Set[str] = set()
    for index, row in df.iterrows():
        current_batch_set = ngrams_set(
            df.iloc[index][column_names].values.tolist(), n=ngrams_size
        )
        universal_set = universal_set.union(current_batch_set)

    return universal_set


def assign_buckets(
        df: pd.DataFrame,
        hash_columns: list,
        ngrams_size: int = 2,
        signature_size: int = 100,
        band_size: int = 10,
) -> pd.DataFrame:
    """
    Utilizes the LSH Algorithm to bucket rows on a dataframe
    Args:
        df (pd.DataFrame): the dataframe in question
        hash_columns (list): column names to be used for lsh algorithm
        ngrams_size (int): size of the ngrams(defaults to 2)
        signature_size (int): size of the signature(defaults to 100)
        band_size (int): size of the band used for bucketing

    Returns: the original dataframe with the bucket_id field added to it

    """

    signature_column_name = "signature"
    assign_signatures(
        df=df,
        hash_columns=hash_columns,
        ngrams_size=ngrams_size,
        signature_size=signature_size,
        signature_column_name=signature_column_name,
    )

    bucket_df = get_buckets(
        band_size=band_size,
        signature_column_name=signature_column_name,
        df=df,
        signature_size=signature_size,
        column_names=df.columns.tolist(),
    )
    return bucket_df


def assign_signatures(
        df: pd.DataFrame,
        hash_columns: list,
        ngrams_size: int = 2,
        signature_size: int = 100,
        signature_column_name: str = "signature",
) -> pd.DataFrame:
    """
    Assigns signatures to the dataframe in the column signature_column_name
    Args:
        df (pd.DataFrame): the dataframe in question
        hash_columns (list): column names to be used for lsh algorithm
        ngrams_size (int): size of the ngrams(defaults to 2)
        signature_size (int): size of the signature(defaults to 100)
        signature_column_name (str): name of the column to store the signature
    """
    the_universal_set = create_ngrams(df, hash_columns, ngrams_size)

    hash_functions = get_hash_functions(len(the_universal_set), signature_size)

    column_names = ",".join(hash_columns)
    df = create_signature(
        the_universal_set=the_universal_set,
        companies=df,
        column_names_for_signature=column_names,
        hash_functions=hash_functions,
        signature_column_name_output=signature_column_name,
        selected_ngrams_size=ngrams_size,
        selected_signature_size=signature_size,
    )
    return df
