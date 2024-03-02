import pandas as pd

from lsh import assign_buckets


def create_test_df() -> pd.DataFrame:
    column_names = [
        "company_name",
        "address",
        "city",
        "zip_code",
        "state",
        "country_code",
    ]
    data = {
        "company_name": [
            "Prime Building Co.",
            "Prime Building Company",
            "Vertex Constructors",
            "Horizon Infrastructure",
            "Crestview Builders",
            "Skyline Engineering",
            "Blueprint Construction",
            "Foundation Properties",
            "Apex Development",
            "NexGen Constructors",
            "Solid Ground Inc.",
            "StructureCraft Builders",
            "Pinnacle Estate Co.",
            "Cornerstone Construction",
            "Legacy Building Group"
        ],
        "address": [
            "123 Elm St", "123 Elm Street", "789 Pine St", "321 Maple St",
            "654 Cedar St",
            "987 Spruce St", "345 Birch St", "678 Palm St", "890 Aspen St",
            "123 Redwood St",
            "456 Dogwood St", "789 Willow St", "321 Cherry St", "654 Magnolia St",
            "987 Hawthorn St"
        ],
        "city": [
            "Springfield", "Springfield", "Riverside", "Lincoln", "Madison",
            "Clayton", "Clinton", "Franklin", "Jackson", "Lexington",
            "Milford", "Salem", "Georgetown", "Winchester", "Harrison"
        ],
        "zip_code": [str(10000 + i) for i in range(1, 16)],
        "state": [
            "CA", "NY", "TX", "FL", "IL",
            "PA", "OH", "GA", "NC", "MI",
            "NJ", "VA", "WA", "MA", "IN"
        ],
        "country_code": ["US"] * 15,
    }

    # Create the DataFrame
    df = pd.DataFrame(data, columns=column_names)
    return df


if __name__ == "__main__":
    cdf = create_test_df()
    lsh_columns = ["company_name", "address", "city"]
    bucketed_df = assign_buckets(df=cdf,
                                 hash_columns=lsh_columns,
                                 ngrams_size=3,
                                 band_size=5,
                                 signature_size=500)
    print(bucketed_df.to_string())
