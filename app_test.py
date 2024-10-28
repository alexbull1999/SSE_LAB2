from app import process_query


def test_knows_about_dinosaurs():
    assert (
        process_query("dinosaurs")
        == "Dinosaurs ruled the Earth 200 million years ago"
    )


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_query_about_name():
    assert process_query("what is your name?") == "AlexTim"


def test_addition_two_numbers():
    assert process_query("5 plus 5") == "10"
    assert process_query("7 plus 5") == "12"


def largest_of_three_number():
    assert process_query("largest: 67, 46, 1") == "67"
    assert process_query("largest: 2, 5, 10") == "10"


def multiply_two_numbers():
    assert process_query("5 multiplied 5") == "25"
    assert process_query("7 multiplied multiplied 9") == "63"


def both_square_and_cube():
    assert (
        process_query(
            "square and a cube: 64, 4911, 1261, 3025, 4520, 133, 1000"
        )
        == "64"
    )
    assert (
        process_query(
            "square and a cube: 729, 4911, 1261, 3025, 4520, 133, 1000"
        )
        == "729"
    )


def subtract_two_numbers():
    assert process_query("10 minus 5") == "5"
    assert process_query("20 minus 10") == "10"


def is_prime_numbers():
    assert process_query("primes: 33, 78, 31, 23, 97") == "31, 23, 97"
    assert process_query("primes: 15, 9, 11, 19, 5") == "11, 19, 5"
