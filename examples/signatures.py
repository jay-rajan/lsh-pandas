import pandas as pd

from lsh import assign_signatures
from scipy import spatial


def create_df():
    column_names = ["item_name"]

    data = {
        "item_name": [
            "Organic Hass Avocados",
            "Free-Range Chicken Thighs",
            "Artisan Multigrain Bread",
            "Multigrain Bread",
            "Cold-Pressed Olive Oil",
            "Quinoa Grain Mix",
            "Belgian Dark Chocolate",
            "Dry Roasted Macadamia Nuts",
            "Kale and Baby Spinach Mix",
            "Dry Roasted Mix",
            "Cage-Free Brown Eggs",
            "Brown Eggs",
            "Aged Gouda Cheese",
            "Blue Cheese"
        ],
    }

    # Create the DataFrame
    df = pd.DataFrame(data, columns=column_names)
    return df


if __name__ == "__main__":
    cdf = create_df()
    signature_df = assign_signatures(
        df=cdf,
        hash_columns=["item_name"],
        ngrams_size=2,
        signature_size=100)
    print(signature_df.to_string())

    for i in range(len(signature_df)):
        for j in range(i + 1, len(signature_df)):
            print(f"Similarity between {signature_df.iloc[i]['item_name']} "
                  f"and {signature_df.iloc[j]['item_name']}: "
                  f"{1 - spatial.distance.cosine(signature_df.iloc[i]['signature'],
                                                 signature_df.iloc[j]['signature'])}")
