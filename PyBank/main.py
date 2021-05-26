import numpy as np
import pandas as pd

data = pd.read_csv("budget_data.csv")
changes = data.rename(columns={'Profit/Losses': 'Change'})

for index, item in data["Profit/Losses"].items():
    if index == 0:
        continue
    changes["Change"][index] = data["Profit/Losses"][index] - data["Profit/Losses"][index - 1]

changes = changes.iloc[1:]

total_months = len(data)
total = sum(data["Profit/Losses"])
average_change = round(np.average(changes["Change"]), 2)
greatest_increase = np.argmax(changes["Change"])
greatest_decrease = np.argmin(changes["Change"])

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average  Change: ${average_change}")
print("Greatest Increase in Profits: " + f"{changes['Date'][greatest_increase + 1]}" + f" (${changes['Change'][greatest_increase + 1]})")
print("Greatest Decrease in Profits: " + f"{changes['Date'][greatest_decrease + 1]}" + f" (${changes['Change'][greatest_decrease + 1]})")

f = open("output.txt", "w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")
f.write(f"Total Months: {total_months}\n")
f.write(f"Total: ${total}\n")
f.write(f"Average  Change: ${average_change}\n")
f.write("Greatest Increase in Profits: " + f"{changes['Date'][greatest_increase + 1]}" + f" (${changes['Change'][greatest_increase + 1]})\n")
f.write("Greatest Decrease in Profits: " + f"{changes['Date'][greatest_decrease + 1]}" + f" (${changes['Change'][greatest_decrease + 1]})\n")
f.close()
