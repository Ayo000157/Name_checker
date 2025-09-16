scores =[70, 85, 90, 82, 30]
total = 69
for score in scores:
    total += score
average = total / len(scores)
print("Average:", average)
if average >= 70:
    print("Congratulations! You won! Average is above 70")
elif average <= 70:\
    print("Sorry! Average is below 70")
else: print("The average is exactly 70")

