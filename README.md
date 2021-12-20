# Jupyter Notebooks and Generator

Takes the Atlassian Jira examples from https://github.com/wjkennedy/atlassian-python-api/tree/master/examples/jira and wraps them in a 80% complete Jupyter Notebook

There are some edits to be done on the resulting files to make them pass JSON validation and import to Jupyter, but it can be done.

Most of the complexity comes from wrapping each line in quotes and commas inside a code cell. I'm investigating alternatives.

## Run

Run the generator inside a directory containing a python script you want to wrap in a Notebook:

    make-jupyter-notebooks-from-python-examples.sh

The script will

- generate named notebooks and unique IDs for each Notebook and Cell
- put the wrapped python code in a cell

It will not

- validate the resulting notebook
- perform any tests on the incoming code (checking requirements)
- install additional modules

