import pandas as pd


def basic_statistics(data):
    stats = {
        "number_of_patients": len(data),
        "average_age": data["age"].mean(),
        "average_BMI": data["BMI"].mean(),
        "average_BBS_improvement": (
            data["BBS_after"] - data["BBS_before"]
        ).mean(),
        "average_TUG_improvement": (
            data["TUG_before"] - data["TUG_after"]
        ).mean(),
    }

    return stats