data_ = [
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 1093},
    {"Gender": "Male", "HeightCm": "171", "WeightKg": 1094},
    {"Gender": "Male", "HeightCm": 171, "WeightKg": "1095"},
    {"Gender": "Male", "HeightCm": 180, "WeightKg": 87},
    {"Gender": "Male"},
    {"Gender": "Male", "HeightCm": 180},
    {"Gender": "Male", "WeightKg": 90},
]

evaluate_bmi_outputs = [
    373.790226,
    "Invalid Height",
    "Invalid Weight",
    26.851852,
    "Empty Input",
    "Empty Input",
    "Empty Input",
]

bmi_data_ = [
    {
        "Gender": "Male",
        "HeightCm": 171,
        "WeightKg": 1093,
        "BmiValue": 373.79022605246064,
    },
    {
        "Gender": "Male",
        "HeightCm": "171",
        "WeightKg": 1094,
        "BmiValue": "Invalid Height",
    },
    {
        "Gender": "Male",
        "HeightCm": 171,
        "WeightKg": "1095",
        "BmiValue": "Invalid Weight",
    },
    {"Gender": "Male", "HeightCm": 180, "WeightKg": 87, "BmiValue": 26.85185185185185},
    {
        "Gender": "Male",
        "HeightCm": "nan",
        "WeightKg": "nan",
        "BmiValue": "Invalid Height",
    },
    {
        "Gender": "Male",
        "HeightCm": 180,
        "WeightKg": "nan",
        "BmiValue": "Invalid Weight",
    },
    {"Gender": "Male", "HeightCm": "nan", "WeightKg": 90, "BmiValue": "Invalid Height"},
]

category_health_risk_output = [
    ("Very Severely obese", "Very high risk"),
    ("Invalid data", "Invalid data"),
    ("Invalid data", "Invalid data"),
    ("Overweight", "Enhanced risk"),
    ("Invalid data", "Invalid data"),
    ("Invalid data", "Invalid data"),
    ("Invalid data", "Invalid data"),
]

overweight_data_ = [
    [
        {"Gender": "Male", "HeightCm": 180, "WeightKg": 94},
        {"Gender": "Male", "HeightCm": 180, "WeightKg": 95},
        {"Gender": "Male", "HeightCm": 180, "WeightKg": 96},
        {"Gender": "Male", "HeightCm": 180, "WeightKg": 97},
        {"Gender": "Male", "HeightCm": 180, "WeightKg": 98},
    ],
    bmi_data_,
    [
        {
            "Gender": "Male",
            "HeightCm": 171,
            "WeightKg": 1093,
            "BmiValue": 373.79022605246064,
            "Category": "Very Severely obese",
            "HealthRisk": "Very high risk",
        },
        {
            "Gender": "Male",
            "HeightCm": 171,
            "WeightKg": 1094,
            "BmiValue": 374.13221162066964,
            "Category": "Very Severely obese",
            "HealthRisk": "Very high risk",
        },
        {
            "Gender": "Male",
            "HeightCm": 171,
            "WeightKg": 1095,
            "BmiValue": 374.4741971888787,
            "Category": "Very Severely obese",
            "HealthRisk": "Very high risk",
        },
        {
            "Gender": "Male",
            "HeightCm": 180,
            "WeightKg": 87,
            "BmiValue": 26.85185185185185,
            "Category": "Overweight",
            "HealthRisk": "Enhanced risk",
        },
        {
            "Gender": "Male",
            "HeightCm": 180,
            "WeightKg": 88,
            "BmiValue": 27.160493827160494,
            "Category": "Overweight",
            "HealthRisk": "Enhanced risk",
        },
        {
            "Gender": "Male",
            "HeightCm": 180,
            "WeightKg": 89,
            "BmiValue": 27.469135802469133,
            "Category": "Overweight",
            "HealthRisk": "Enhanced risk",
        },
        {
            "Gender": "Male",
            "HeightCm": 180,
            "WeightKg": 90,
            "BmiValue": 27.777777777777775,
            "Category": "Overweight",
            "HealthRisk": "Enhanced risk",
        },
        {
            "Gender": "Male",
            "HeightCm": 180,
            "WeightKg": 91,
            "BmiValue": 28.086419753086417,
            "Category": "Overweight",
            "HealthRisk": "Enhanced risk",
        },
        {
            "Gender": "Male",
            "HeightCm": 180,
            "WeightKg": 92,
            "BmiValue": 28.39506172839506,
            "Category": "Overweight",
            "HealthRisk": "Enhanced risk",
        },
        {
            "Gender": "Male",
            "HeightCm": 180,
            "WeightKg": 93,
            "BmiValue": 28.703703703703702,
            "Category": "Overweight",
            "HealthRisk": "Enhanced risk",
        },
        {
            "Gender": "Male",
            "HeightCm": 180,
            "WeightKg": 94,
            "BmiValue": 29.012345679012345,
            "Category": "Overweight",
            "HealthRisk": "Enhanced risk",
        },
        {
            "Gender": "Male",
            "HeightCm": 180,
            "WeightKg": 95,
            "BmiValue": 29.320987654320987,
            "Category": "Overweight",
            "HealthRisk": "Enhanced risk",
        },
    ],
]

overweight_output_ = [3, 1, 9]


def test_evaluate_bmi():
    from src.overweight_count.main import evaluate_bmi

    for inp, actual_output in zip(data_, evaluate_bmi_outputs):
        expected_output = evaluate_bmi(inp)
        if type(expected_output) is str:
            assert expected_output == actual_output
        else:
            assert round(expected_output, 6) == actual_output


def test_get_category_health_risk():
    from src.overweight_count.main import get_category_health_risk

    for inp, actual_output in zip(bmi_data_, category_health_risk_output):
        expected_output = get_category_health_risk(inp)

        assert expected_output == actual_output


def test_get_count_of_overweights():
    from src.overweight_count.main import get_count_of_overweights

    for inp, actual_output in zip(overweight_data_, overweight_output_):
        expected_output = get_count_of_overweights(inp)

        assert expected_output == actual_output
