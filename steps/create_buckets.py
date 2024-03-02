import logging
from typing import List
import networkx as nx
import pandas as pd


def get_hash_collisions_from_signatures_for_band(
        df: pd.DataFrame,
        signature_column_name: str,
        band_size: int,
        band_no: int,
):
    hashes = {}
    for index, row in df.iterrows():
        start_index = band_size * band_no
        end_index = start_index + band_size - 1
        # hash such that the value of the tuple can be compared against other in O(1)
        signature = row[signature_column_name].split(",")
        hash_val = hash(tuple(signature[start_index:end_index]))
        if hash_val not in hashes:
            hashes[hash_val] = set()
        hashes[hash_val].add(index)
    return hashes


def get_buckets(
        band_size: int,
        signature_column_name: str,
        signature_size: int,
        df: pd.DataFrame,
        column_names: List[str],
):
    num_bands = signature_size // band_size
    G = nx.Graph()

    # for i in range(signature_size - band_size):
    for band_no in range(num_bands):
        logging.info("Processing Band no {}".format(band_no))
        buckets = get_hash_collisions_from_signatures_for_band(
            df=df,
            signature_column_name=signature_column_name,
            band_size=band_size,
            band_no=band_no,
        )
        # form a helper data structure.
        for i, (key, similar_indexes) in enumerate(buckets.items()):
            prev_vertex = None
            for index in similar_indexes:
                if prev_vertex is None:
                    prev_vertex = index
                    G.add_node(prev_vertex)
                else:
                    G.add_edge(prev_vertex, index)
                    prev_vertex = index

    connected_components_list = nx.connected_components(G)
    out = []
    bucket_id = 0
    max_cluster_size = 0
    for connected_components in connected_components_list:
        bucket_id = bucket_id + 1
        max_cluster_size = max(len(connected_components), max_cluster_size)
        for index in connected_components:
            cur_row = df.iloc[index][column_names].values.tolist()
            cur_row.append(bucket_id)
            out.append(cur_row)
    print(max_cluster_size)
    column_names.append("bucket_id")
    return pd.DataFrame(
        data=out,
        columns=column_names,
    )
