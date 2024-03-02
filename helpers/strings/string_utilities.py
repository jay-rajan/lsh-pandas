from typing import List, Set

from nltk import ngrams


def ngrams_strings(string: str, n):
    n_grams_tuples = ngrams(string.lower(), n)
    n_grams_set = set()
    for n_grams_tuple in n_grams_tuples:
        n_grams_set.add("".join(n_grams_tuple))
    return n_grams_set


def ngrams_set(company_names: List[str], n: int = 5):
    the_universal_set: Set[str] = set()
    for company_name in company_names:
        if company_name is None:
            continue
        split_company_names = company_name.split()
        for split_company_name in split_company_names:
            the_universal_set = the_universal_set.union(
                ngrams_strings(split_company_name, n)
            )
    return [x for x in the_universal_set]
