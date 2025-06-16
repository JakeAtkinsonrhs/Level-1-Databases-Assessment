"""This program will make a user interface for people who want to access and use the nightreign_bosses.db database."""

# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'nightreign_bosses.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()
menu_choice = ''
while menu_choice != 'Z':
    menu_choice = input('\nWelcome to the database of bosses from ELDEN RING: NIGHTREIGN.\n'
                        'This database was created for the databases assessment for NCEA Level 1 Digital Technologies.\n\n'
                        'Please enter the corresponding letter for which data you wish to access.\n'
                        'A: All Information.\n'
                        'B: \n'
                        'C: \n'
                        'D: \n'
                        'E: \n'
                        'F: \n'
                        'G: \n'
                        'H: \n'
                        'I: \n'
                        'J: \n'
                        'Z: Exit Database.\n\n'
                        'Please input your chosen letter here: ')