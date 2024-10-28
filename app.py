from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route("/")
def hello_word():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_animal = request.form.get("animal")
    if input_animal == "Goat" or input_animal == "goat":
        return render_template(
            "goat.html", name=input_name, animal=input_animal
        )
    elif input_animal == "Dog" or input_animal == "dog":
        return render_template(
            "dog.html", name=input_name, animal=input_animal
        )
    elif input_animal == "Donkey" or input_animal == "donkey":
        return render_template(
            "donkey.html", name=input_name, animal=input_animal
        )
    elif input_animal == "Cow" or input_animal == "cow":
        return render_template(
            "cow.html", name=input_name, animal=input_animal
        )
    elif input_animal == "Lion" or input_animal == "lion":
        return render_template(
            "lion.html", name=input_name, animal=input_animal
        )
    else:
        return render_template(
            "error.html", name=input_name, animal=input_animal
        )


def process_query(query):
    # Define responses based on the input query
    numbers = extract_numbers_from_query(query)

    if query.lower() == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    if "plus" in query.lower():
        return str(sum(numbers))
    if "largest" in query.lower():
        return str(max(numbers))
    if "multiplied" in query.lower():
        return str(numbers[0] * numbers[1])
    if "name" in query.lower():
        return "AlexTim"
    if "square" in query.lower():
        return str(square_and_cube(numbers))

    return "Unknown"


def square_and_cube(numbers):
    for number in numbers:
        root = round(number ** (1 / 6))
        if root**6 == number:
            return number


def extract_numbers_from_query(query):
    numbers = re.findall(r"\d+", query)
    return list(map(int, numbers))


@app.route("/query", methods=["GET"])
def query():
    # Get the 'q' query parameter from the request
    query_param = request.args.get("q", " ")

    # Process the query using the existing function
    result = process_query(query_param)

    # Return the result as plain text
    return result


if __name__ == "__main__":
    app.run(debug=True)
