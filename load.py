import csv

def toCSV(data: list) :

    """
    This function load data into CSV file.
    """

    with open("players.csv", "w") as file :

        writer = csv.writer(file, delimiter=",")
        for row in data :
            writer.writerow(row)