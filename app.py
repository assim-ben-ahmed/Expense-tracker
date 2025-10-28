from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)
FILE_NAME = "expenses.json"

# Load existing expenses or create new list
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        expenses = json.load(f)
else:
    expenses = []

# Save expenses to file
def save_expenses():
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_expense():
    data = request.json
    name = data.get("name")
    amount = float(data.get("amount", 0))
    category = data.get("category", "Other")
    expense = {"name": name, "amount": amount, "category": category}
    expenses.append(expense)
    save_expenses()
    return jsonify({"status": "success", "expense": expense})

@app.route("/expenses", methods=["GET"])
def get_expenses():
    return jsonify(expenses)

if __name__ == "__main__":
    app.run(debug=True)
