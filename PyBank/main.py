# Dependencies
import os
import csv


# Create output file name
file_output_name = ("budget_data.csv")

# Months of Financial Data
num_months = 86
import datetime
x = datetime.datetime(Feb-2012)
starting_date = datetime.add(months=-num_months)

# % of months that are positive vs negative (Change as needed)
gain_loss_weights = [0.85, 0.15]

# Range of profits or losses 
range_revenue = [1926159, -2196167]

# Iteratively build every month between start and current date
tracked_months = [86]
current_month = starting_date
revenues = []

for x in range(0, num_months + 1):

    # Generate a list of formatted months
    current_month = current_month.add(month=1)
    current_month_string = current_month.date.strftime("%b-%Y")
    tracked_months.append(current_month_string)

    # Generate a random revenue for each month
    random_revenue = random.randrange(range_revenue[0], range_revenue[1])
    revenues = revenues + [random_revenue]

# Convert a set amount of revenues to be negative
neg_months = int(num_months * gain_loss_weights[1])

for x in range(neg_months):
    revenues[x] = -1 * revenues[x]

# Shuffle the revenues so the negatives appear sporadically
random.shuffle(revenues)

# Assemble the months and revenues into a single list
fin_data = zip(tracked_months, revenues)

# Print the financial data to terminal
print(fin_data)

# Export a csv of the generated financial data
with open(file_output_name, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Date", "Revenue"])
    writer.writerows(fin_data)
