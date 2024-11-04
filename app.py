from flask import Flask, render_template, request
import re
import requests

app = Flask(__name__)


@app.route("/")
def hello_word():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_animal = request.form.get("animal")
    input_gitusername = request.form.get("gitusername")
    if input_gitusername is not None:
        avatar_response = requests.get(
            f"https://api.github.com/users/{input_gitusername}"
        )
        if avatar_response.status_code == 200:
            avatar_data = avatar_response.json()
            avatar_url = avatar_data["avatar_url"]

        response = requests.get(
            f"https://api.github.com/users/{input_gitusername}/repos"
        )
        repos = []
        if response.status_code == 200:
            repos_data = (
                response.json()
            )  # data returned is a list of ‘repository’ entities
            repos = [
                {"name": repo["name"], "updated_at": repo["updated_at"]}
                for repo in repos_data
            ]

            detailed_git = []
            for repo in repos:
                new_data = requests.get(
                    f"https://api.github.com/repos/{input_gitusername}/"
                    f"{repo['name']}/commits"
                )
                if new_data.status_code == 200:
                    commits = new_data.json()

                    if commits:
                        latest_commit = max(
                            commits,
                            key=lambda x: x["commit"]["author"]["date"],
                        )
                        detailed_git.append(
                            {
                                "name": repo["name"],
                                "commit_hash": latest_commit["sha"],
                                "commit_message": latest_commit["commit"][
                                    "message"
                                ],
                                "commit_author": latest_commit["commit"][
                                    "author"
                                ]["name"],
                                "commit_date": latest_commit["commit"][
                                    "author"
                                ]["date"],
                            }
                        )

            return render_template(
                "gitdata.html",
                gitusername=input_gitusername,
                repos=detailed_git,
                avatar=avatar_url,
            )
        return render_template(
            "gitdata.html", gitusername=input_gitusername, repos=[]
        )

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
    if "minus" in query.lower():
        return str(numbers[0] - numbers[1])
    if "largest" in query.lower():
        return str(max(numbers))
    if "multiplied" in query.lower():
        return str(numbers[0] * numbers[1])
    if "divided" in query.lower():
        return str(numbers[0] / numbers[1])
    if "power" in query.lower():
        return str(numbers[0] ** numbers[1])
    if "name" in query.lower():
        return "AlexTim"
    if "square" in query.lower():
        return str(find_perfect_square_and_cube(numbers))
    if "prime" in query.lower():
        return str(find_primes(numbers))
    return "Unknown"


def square_and_cube(number):
    root = round(number ** (1 / 6))
    if root**6 == number:
        return number
    return False


def find_perfect_square_and_cube(numbers):
    perfect_numbers = []  # List to store prime numbers
    for number in numbers:
        if square_and_cube(number):
            perfect_numbers.append(number)  # Add the prime number to the list
    return perfect_numbers


def extract_numbers_from_query(query):
    numbers = re.findall(r"\d+", query)
    return list(map(int, numbers))


def is_prime(num):
    if num <= 1:  # 0 and 1 are not prime numbers
        return False
    if num <= 3:  # 2 and 3 are prime numbers
        return True
    if num % 2 == 0 or num % 3 == 0:  # Eliminate multiples of 2 and 3
        return False

    # Check for factors from 5 to the square root of num
    for i in range(5, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_primes(numbers):
    primes = []  # List to store prime numbers
    for number in numbers:
        if is_prime(number):
            primes.append(number)  # Add the prime number to the list
    return primes


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
