from src.sorting import sort_by

jobs = [
    {
        "min_salary": 12000,
        "max_salary": 24000,
        "date_posted": "2022-10-21",
    },
    {
        "min_salary": 28000,
        "max_salary": 38000,
        "date_posted": "2022-12-23",
    },
    {
        "min_salary": 20000,
        "max_salary": 29000,
        "date_posted": "2022-11-22",
    },
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == 12000

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == 38000

    sort_by(jobs, "date_posted")
    assert jobs[0]["date_posted"] == "2022-12-23"
