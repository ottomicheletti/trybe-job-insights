from src.counter import count_ocurrences

path = "src/jobs.csv"


def test_counter():
    assert (
        count_ocurrences(path, "Python") == 1639
    ), "Expected 1639 entries for the word Python"
    assert (
        count_ocurrences(path, "Java") == 676
    ), "Expected 676 entries for the word Java"
    assert (
        count_ocurrences(path, "React") == 141
    ), "Expected 141 entries for the word React"
