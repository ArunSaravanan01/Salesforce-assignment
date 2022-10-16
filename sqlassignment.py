import sqlite3

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('Arun.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from favmovie"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Movie: ", row[0])
            print("Actor: ", row[1])
            print("Actress: ", row[2])
            print("Year: ", row[3])
            print("Director: ", row[4])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSqliteTable()