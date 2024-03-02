import pandas as pd

from lsh import assign_buckets


def create_test_df() -> pd.DataFrame:
    column_names = [
        "source_record_id",
        "source_name",
        "company_name",
        "doing_business_as",
        "phone_number",
        "domain",
        "address",
        "city",
        "state_code",
        "zip_code",
        "country_code",
    ]
    data = [
        [
            "0012T00001lSJmiQAG",
            "salesforce",
            "jag contractors",
            None,
            None,
            "jagcontractorsinc.com",
            "5649 general washington dr",
            "alexandria",
            "us-va",
            "22312",
            "US",
        ],
        [
            "0012T00001lSJmiQAG_similar",
            "salesforce",
            "jag contractor1s with mistake",
            None,
            None,
            "jagcontractorssinc.com",
            "5649 general  washington dr",
            "alexandria",
            "us-va",
            "22312",
            "US",
        ],
        [
            "0012T00001a9VOcQAM",
            "salesforce",
            "hi tec construccion",
            None,
            None,
            "hitecconstruccion.com",
            "paseo de granada no 3808 col las torres",
            "monterrey",
            None,
            "64930",
            "MX",
        ],
        [
            "0012T00001a9VOcQAM_similar",
            "salesforce",
            "hi tec construction",
            None,
            None,
            "hitecconstruccion.com",
            "paseo de granada extra string no 3808 col las torres",
            "monterrey",
            None,
            "64930",
            "MX",
        ],
        [
            "0012T00001apEgrQAE",
            "salesforce",
            "celano nominees",
            None,
            None,
            None,
            "920 mickleham road",
            "greenvale",
            "au-vic",
            "3059",
            "AU",
        ],
        [
            "0012T00001apEgrQAE_similar",
            "salesforce",
            "celano nominees",
            None,
            None,
            None,
            "920 mickleham road in one ",
            "greenvale",
            "au-vic",
            "3059",
            "AU",
        ],
        [
            "0013400001SH2MAAA1",
            "salesforce",
            "its concretors",
            None,
            None,
            "ultimoconcrete.com.au",
            "12 mcgee place",
            "baulkham hills",
            "au-nsw",
            "2153",
            "AU",
        ],
        [
            "0012T00001lSCtgQAG",
            "salesforce",
            "mildura concrete",
            None,
            None,
            "milduraconcretecompany.com",
            "35 belar ave po box 511",
            "nichols point",
            "au-vic",
            "3501",
            "AU",
        ],
        [
            "0013400001UbshEAAR",
            "salesforce",
            "city of ketchikan public utilities",
            None,
            None,
            "ketchikanpubliclibrary.org",
            "1065 fair st",
            "ketchikan",
            "us-ak",
            "99901",
            "US",
        ],
        [
            "0013400001NZlvUAAT",
            "salesforce",
            "mick olsen corporation",
            None,
            None,
            "mickolsencorp.com",
            "1963 cattail ln",
            "freeland",
            "us-wa",
            "98249",
            "US",
        ],
        [
            "0012T00001jxS24QAE",
            "salesforce",
            "gatco signs",
            None,
            None,
            "gatco.ca",
            "178 rue de varennes",
            "gatineau",
            "ca-qc",
            "J8T 8G3",
            "CA",
        ],
        [
            "0012T00001jxS24QAE_similar",
            "salesforce",
            "gatco signs post",
            None,
            None,
            "gatco.ca",
            "178 rue de varennes",
            "gatineau",
            "ca-qc",
            "J8T 8G3",
            "CA",
        ],
        [
            "0012T00001ZvxkIQAR",
            "salesforce",
            "colorwise and more",
            None,
            None,
            "colorwiseandmore.com",
            "17316 coastal hwy",
            "lewes",
            "us-de",
            "19958",
            "US",
        ],
        [
            "0013400001LxXEwAAN",
            "salesforce",
            "bennetts hvac and electrical",
            None,
            None,
            "ruuddealer.net",
            "951 elma g miles pkwy ste c",
            "hinesville",
            "us-ga",
            "31313-4515",
            "US",
        ],
        [
            "0012T00001iW2kAQAS",
            "salesforce",
            "kocmoc d contracting",
            None,
            None,
            None,
            "po box 85858",
            "dubai",
            None,
            None,
            "AE",
        ],
        [
            "0012T00001iW2kAQAS_similar",
            "salesforce",
            "kocmoc d contracting",
            None,
            None,
            None,
            "post o box 85858",
            "dubai",
            None,
            None,
            "AE",
        ],
        [
            "0012T00001iW35tQAC",
            "salesforce",
            "al areen contracting",
            None,
            None,
            None,
            "po box 55050",
            "dubai",
            None,
            None,
            "AE",
        ],
        [
            "0012T00001iW2PXQA0",
            "salesforce",
            "al khooli contracting",
            None,
            None,
            None,
            None,
            "dubai",
            None,
            None,
            "AE",
        ],
        [
            "0012T00001hYKhrQAG",
            "salesforce",
            "ggj holdings lc",
            None,
            None,
            None,
            "460s evansdale dr",
            "bloomfield hills",
            "us-mi",
            "48304",
            "US",
        ],
        [
            "0012T00001q5tv4QAA",
            "salesforce",
            "msh solutions sdn bhd",
            None,
            None,
            None,
            "lot02 digital sq lvl 3",
            "shah alam",
            None,
            "40000",
            "MY",
        ],
        [
            "0012T00001lSLkuQAG",
            "salesforce",
            "centric parts",
            None,
            None,
            "apcautotech.com",
            "21046s figueroa st",
            "carson",
            "us-ca",
            "90745",
            "US",
        ],
        [
            "0018V00002MSdTYQA1",
            "salesforce",
            "fundacion teleton",
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ],
        [
            "0013400001YazyhAAB",
            "salesforce",
            "sette forbes developments",
            None,
            None,
            None,
            "12a thornton street",
            "eltham",
            "au-vic",
            "3095",
            "AU",
        ],
        [
            "0013400001UR5Y6AAL",
            "salesforce",
            "dddddddd",
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            "AU",
        ],
        [
            "0012T00001aA9FDQA0",
            "salesforce",
            "splenda concrete design",
            None,
            None,
            "splendaconcrete.ca",
            "123 deerwood cres",
            "richmond hill",
            "ca-on",
            "L4E 4B2",
            "CA",
        ],
    ]
    return pd.DataFrame(data=data, columns=column_names)


if __name__ == "__main__":
    cdf = create_test_df()
    lsh_columns = ["company_name", "address"]
    bucketed_df = assign_buckets(cdf, lsh_columns)
    print(bucketed_df)
