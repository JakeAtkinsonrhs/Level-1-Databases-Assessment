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
                        'This is an incomplete database, and is very likely to have inaccuracies.\n'
                        'This database was created for the databases assessment for NCEA Level 1 Digital Technologies.\n\n'
                        'Please enter the corresponding letter for which data you wish to access.\n'
                        'A: All Information.\n'
                        'B: All Bosses.\n'
                        'C: All Bosses, Ordered By Returning Bosses.\n'
                        'D: All Expeditions, And The Weakness Of The Corresponding Nightlord.\n'
                        'E: The Damage Type And Weakness Of Every Nightlord.\n'
                        'F: All Bosses Returning From The DARK SOULS Franchise (DARK SOULS Remastered, Scholar Of The First Sin, and 3).\n'
                        'G: Bosses Weak To Fire.\n'
                        'H: Bosses Weak To Lightning.\n'
                        'I: Bosses Weak To Holy.\n'
                        'J: Information About The Nameless King Bossfight.\n'
                        'Z: Exit Database.\n\n'
                        'Please input your chosen letter here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('All Information')
    elif menu_choice == 'B':
        print_query('All Bosses')
    elif menu_choice == 'C':
        print_query('All bosses, returning bosses first')
    elif menu_choice == 'D':
        print_query('Expeditions and weaknesses')
    elif menu_choice == 'E':
        print_query('all nightlords damage type and weakness')
    elif menu_choice == 'F':
        print_query('all returning bosses')
    elif menu_choice == 'G':
        print_query('fire weakness')
    elif menu_choice == 'H':
        print_query('lightning weakness')
    elif menu_choice == 'I':
        print_query('holy weakness')
    elif menu_choice == 'J':
        print_query('nameless king')