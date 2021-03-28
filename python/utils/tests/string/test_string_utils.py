from utils.string.generate_substring import generate_substring


def test_generate_substring():
    sample_input = "daniel"
    expected_result = [
        "d",
        "da",
        "dan",
        "dani",
        "danie",
        "daniel",
        "a",
        "an",
        "ani",
        "anie",
        "aniel",
        "n",
        "ni",
        "nie",
        "niel",
        "i",
        "ie",
        "iel",
        "e",
        "el",
        "l"
    ]

    assert generate_substring(sample_input) == expected_result
