import os
import csv

title_words = ['Date', 'Shift', 'Start', 'End', 'Engineer', 'Contact', '']

with open("rota.csv", "r+") as file:
    text = csv.reader(file)
    for row in text:
        print(row)
        if title_words == row:
            print("Line to be removed")