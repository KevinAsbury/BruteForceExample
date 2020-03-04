# Reading Authentification Headers

A flask server to read a password input (for a brute force attack).

## Getting Started

### Create a Virutal Enviornment

Follow instructions on the [Pipenv site](https://pipenv-fork.readthedocs.io/en/latest/) to install and run pipenv.
Run 'pipenv shell' to create, install dependencies, and start the virtual environment.

### Run the Server

On first run, execute `export FLASK_APP=server.py`. Then run `flask run --reload` to run the developer server.

### Run the Brute Force Attack

Execute 'python brute_force.py'