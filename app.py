from flask import Flask, render_template, request

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
    if query.lower() == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    else:
        return "Unknown"


@app.route("/query", methods=["GET"])
def query():
    # Get the 'q' query parameter from the request
    query_param = request.args.get("q")

    # Process the query using the existing function
    result = process_query(query_param)

    # Return the result as plain text
    return result


if __name__ == "__main__":
    app.run(debug=True)
