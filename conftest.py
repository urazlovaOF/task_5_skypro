import pytest


def calculate_premium(years_worked, year, sick_days_last_year):
    if year:
        years_worked *= 365

    if years_worked >= 3 * 365:
        premium_percentage = 30
    elif years_worked >= 1.5 * 365:
        premium_percentage = 25
    elif years_worked >= 90:
        premium_percentage = 15
    else:
        return 0

    if sick_days_last_year == 0:
        premium_percentage += 3

    return premium_percentage


@pytest.fixture(params=[
    pytest.param((3.1, True, 0, 33), id='3_more_no_sick_leave'),
    pytest.param((3, True, 0, 33), id='3_no_sick_leave'),
    pytest.param((2.9, True, 0, 28), id='less_3_no_sick_leave'),
    pytest.param((1.6, True, 0, 28), id='more_1_5_no_sick_leave'),
    pytest.param((1.5, True, 0, 28), id='1_5_no_sick_leave'),
    pytest.param((1.4, True, 0, 18), id='less_1_5_no_sick_leave'),
    pytest.param((91, False, 0, 18), id='more_90_days_no_sick_leave'),
    pytest.param((90, False, 0, 18), id='90_days_no_sick_leave'),
    pytest.param((89, False, 0, 0), id='less_90_days_no_sick_leave'),
    pytest.param((0, False, 0, 0), id='0_days_no_sick_leave'),

    pytest.param((3.1, True, 1, 30), id='3_more_sick_leave'),
    pytest.param((3, True, 10, 30), id='3_sick_leave'),
    pytest.param((2.9, True, 1.1, 25), id='less_3_sick_leave'),
    pytest.param((1.6, True, 100, 25), id='more_1_5_sick_leave'),
    pytest.param((1.5, True, 365, 25), id='1_5_sick_leave'),
    pytest.param((1.4, True, 1, 15), id='less_1_5_sick_leave'),
    pytest.param((91, False, 1, 15), id='more_90_days_sick_leave'),
    pytest.param((90, False, 1, 15), id='90_days_sick_leave'),
    pytest.param((89, False, 1, 0), id='less_90_days_sick_leave'),
    pytest.param((0, False, 1, 0), id='0_days_sick_leave'),
])
def checks_param(request):
    return request.param
