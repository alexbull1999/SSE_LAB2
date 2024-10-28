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
