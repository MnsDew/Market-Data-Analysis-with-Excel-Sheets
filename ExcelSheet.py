#MGcode
# HEY GUYS, WE HAVE HERE OUR SCRIPT OF EXCEL SHEET READING AND AND CALCULATE TOTAL OF OCCURRENCE... in our two EXCEELSHEET files we have fruits market data
# SECONDLY TOTAL AMOUNT , THEN THE AVERAGE FROM EXCELSHEET  
# MORE THAN ONE EXCELSHEET By CSV FILE TYPE AND CSV LIPRARY 


#First of all we import the csv library , if you don't have csv librarly , write in terminal pip3 install csv.
import csv

# Specify the CSV file names
csv_file1 = "excelsheet.csv"
csv_file2 = "excelsheet2.csv"

# Then we initialize variables to store product names, occurrences, and total amounts
products = []
total_occurrences = {}
total_amount = {}

# Here we have function to calculate statistics for a given CSV file
def calculate_statistics(csv_file):
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = row["Product"]
            if product not in products:
                products.append(product)
                total_occurrences[product] = 0
                total_amount[product] = 0
            total_occurrences[product] += 1
            total_amount[product] += int(row["Amount"])

# Calculate statistics for both CSV files
calculate_statistics(csv_file1)
calculate_statistics(csv_file2)

# In the end print the results for each product
for product in products:
    print(f"Total occurrences of '{product}': {total_occurrences[product]}")
    print(f"Total amount for '{product}': {total_amount[product]}")
    print(f"Average amount per occurrence for '{product}': {total_amount[product] / total_occurrences[product] if total_occurrences[product] != 0 else 0}")
    print()

#MGcode
