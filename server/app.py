#!/usr/bin/env python3
"""Flask routes for looking up contracts and confirming customers."""

from flask import Flask, Response, make_response

# Sample data. Contracts can be shared; customer details are sensitive.
contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]

# Create the Flask application instance; __name__ tells Flask where to find resources.
app = Flask(__name__)


@app.route('/contract/<int:id>')
def get_contract(id: int) -> Response:
    """Return a contract's information (200), or 404 if no contract has that id.

    The `int:` converter makes Flask hand us an integer, so it can be compared
    directly to each contract's numeric id.
    """
    contract = next((c for c in contracts if c["id"] == id), None)
    if contract is None:
        return make_response("Contract not found", 404)
    return make_response(contract["contract_information"], 200)


@app.route('/customer/<customer_name>')
def get_customer(customer_name: str) -> Response:
    """Confirm a customer exists without exposing their data.

    204 (No Content) means the customer exists; the body is intentionally empty.
    404 means no customer by that name.
    """
    if customer_name in customers:
        return make_response("", 204)
    return make_response("Customer not found", 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
