import sys
from typing import Set
import pandas
from helpers.strings.string_utilities import ngrams_set
from lsh_types import Vector


def create_signature(
        the_universal_set: Set[str],
        companies: pandas.DataFrame,
        column_names_for_signature: str,
        signature_column_name_output: str,
        hash_functions,
        selected_signature_size: int = 100,
        selected_ngrams_size: int = 2,
):
    """Compute the signature and add the signature to the data frame"""
    apply_signature_function = apply_signature(
        selected_signature_size=selected_signature_size,
        column_names_for_signature=column_names_for_signature,
        selected_ngrams_size=selected_ngrams_size,
        the_universal_set=the_universal_set,
        hash_functions=hash_functions,
    )
    # apply the signature over the parallelized
    companies[signature_column_name_output] = companies.apply(
        apply_signature_function, axis=1
    )
    return companies


def apply_signature(
        selected_signature_size,
        column_names_for_signature,
        selected_ngrams_size,
        the_universal_set,
        hash_functions,
):
    """Helper method to apply on dataframe"""
    # initialize signature to max value
    initial_signature: Vector = []
    for sigi in range(selected_signature_size):
        initial_signature.append(sys.maxsize)

    # Maintain a reverse index of ngram set for easy lookup.
    universal_set_indexes_dict = {}
    for set_index, string in enumerate(the_universal_set):
        universal_set_indexes_dict[string] = set_index

    def inner(
            row,
    ):
        signature = initial_signature.copy()
        col_names = column_names_for_signature.split(",")
        company_name_ngrams: Set[str] = ngrams_set(
            row[col_names].values, selected_ngrams_size
        )
        for company_name_ngram in company_name_ngrams:
            if company_name_ngram in universal_set_indexes_dict:
                row = universal_set_indexes_dict[company_name_ngram]
                for hash_index in range(selected_signature_size):
                    hash_function = hash_functions[hash_index]
                    hash_val = hash_function(row + 1)
                    signature[hash_index] = min(hash_val, signature[hash_index])
        return ",".join(str(v) for v in signature)

    return inner
