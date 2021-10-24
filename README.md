# acceleration-consortium-hackaton
Repository for the hackaton at Acceleration Consortium '21

## Requirements

- Python 3.7.4
- `pipenv`

## Install

Run the following commands in a terminal in the current repository:

1. Clone the repository
2. `pipenv sync`
3. ``python -m ipykernel install --user --name=acceleration-consortium-hackaton`

Now it is possible to edit the Jupyter Notebook selecting the project environment.

If you prefer to run the script by console, open a shell in the environment with the following command: `pipenv shell`

## Usage

1. Check port 5432 is available. If it is not, find processes that are using it and kill them.

2. Run: `molarcli install local`

   - Full Name: admin
   - Mail ticona.belu@gmail.com 

3. Create an alembic revision 

   `cd molar`

   `molarcli alembic revision -m "revision_name" --branch-label "revision_name" --head f31 --splice`

