# **Python_QA_checks**

## Description:
This MVP demos the "QA Checks" exercise that will connect to a local SQLite database for demo purposes and run some test sqls against the channel tables. We are using Python language for this purpose.

It will output the results in a GUI.

#### Database: 
Uses sqlite as the database (Channel.db), included in the application. There is few rows of sample data for demo purposes.

#### Scripts:
1. To create/re-create the tables and infrastructure, run the "create_db.py" that will create the Channel.db file.
2. Common functionality is in the "utils.py" script. It points to the location of the sqlite "channel.db" database file, stored locally. This may need to be changed accordingly for your local.
3. To run the "QA Checks" application, run the "run_qa_checks.py" that outputs the results in a GUI.

#### Application Dependencies:
The main dependencies include:

- Python: Pandas , PandasGUI. Please install using the pip install command in your local python folder.
- SQLite3: Download this and install locally on windows and add the path to windows envionment variable.

#### Application Execution Environment:
This application was designed to run on Windows machine.