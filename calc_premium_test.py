from conftest import calculate_premium


def test_calculate_premium(checks_param):
    years_worked, year, sick_days_last_year, expected_result = checks_param
    assert (
            calculate_premium(years_worked, year, sick_days_last_year) ==
            expected_result
    )
