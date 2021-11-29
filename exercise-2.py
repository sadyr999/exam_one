final_sum = int(input("Enter Final amount: "))
start_sum = int(input("Enter Beginning amount: "))
percent_annual = int(input("Enter Annual percent rate: "))

current_amount = start_sum
percent_monthly = percent_annual/12/100
counter = 0
while current_amount < final_sum:
    counter += 1
    current_amount = percent_monthly*current_amount+current_amount
print(f"It will take {counter} months to raise deposit to {current_amount}")