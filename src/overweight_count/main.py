import pandas as pd


def evaluate_bmi(row):
    """
    BMI(kg/m2) = mass(kg) / height(m)2
    :param row: A dictionary containing values of height, weight
    :return: float if inputs are valid, otherwise str
    """
    try:
        height = row["HeightCm"]
        weight = row["WeightKg"]
    except KeyError:
        return "Empty Input"

    if type(height) is not int:
        return "Invalid Height"
    if type(weight) is not int:
        return "Invalid Weight"
    height = height / 100
    return weight / (height * height)


def get_category_health_risk(row):
    """
    Get bmi category and the health risk associated with it.
    :param bmi_value: A dictionary containing values of height, weight & bmi_value
    :return: Tuple of 2 str (<category_value>, <health_risk_value>) i.e. (str, str)
    """
    try:
        bmi_value = row["BmiValue"]
    except KeyError:
        return "Invalid data", "Invalid data"
    if type(bmi_value) is str:
        return "Invalid data", "Invalid data"
    if bmi_value <= 18.4:
        category = "Underweight"
        health_risk = "Malnutrition risk"
    elif 18.5 <= bmi_value <= 24.9:
        category = "Normal weight"
        health_risk = "Low risk"
    elif 25 <= bmi_value <= 29.9:
        category = "Overweight"
        health_risk = "Enhanced risk"
    elif 30 <= bmi_value <= 34.9:
        category = "Moderately obese"
        health_risk = "Medium risk"
    elif 35 <= bmi_value < 39.9:
        category = "Severely obese"
        health_risk = "High risk"
    else:
        category = "Very Severely obese"
        health_risk = "Very high risk"
    return category, health_risk


def get_count_of_overweights(data_):
    """
    Fetches the count of all the overweight person from the list of data provided
    :param data_: A dictionary containing all the values like height, weight, bmi_value
    :return: int
    """
    df = pd.DataFrame(data_)
    df["BmiValue"] = df.apply(evaluate_bmi, axis=1)
    df[["Category", "HealthRisk"]] = df.apply(get_category_health_risk, axis=1).apply(
        pd.Series
    )
    overweight_count = df.loc[df["Category"] == "Overweight"].shape[0]
    return overweight_count


if __name__ == "__main__":
    get_count_of_overweights(data_=[])
