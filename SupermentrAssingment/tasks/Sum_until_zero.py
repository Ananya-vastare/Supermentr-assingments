#10th feb

total_sum = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    
    if num == 0:
        break  # Exit the loop
    
    total_sum += num

print(f"The total sum is: {total_sum}")