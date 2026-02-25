file = open("shop.txt", "r", encoding="utf-8")
unique_users = set()
total_buys = 0
total_sum = 0
user_spending = {}
for line in file:
    parts = line.strip().split(";")
    user_id = parts[1]
    action = parts[2]
    if action == "BUY":
        total_buys += 1
        amount = int(parts[3])
        total_sum += amount
        if user_id not in user_spending:
            user_spending[user_id] = amount
        else:
            user_spending[user_id] += amount
file.close()
max_user = ""
max_spent = 0
for user in user_spending:
    if user_spending[user] > max_spent:
        max_spent = user_spending[user]
        max_user = user
if total_buys > 0:
    average_check = total_sum/total_buys
else:
    average_check = 0
report = open("report.txt", "x", encoding="utf-8")
report.write("Unique users: "+str(len(unique_users)) + "\n")
report.write("Total buys: "+str(total_buys) + "\n")
report.write("Total sum"+str(total_sum) + "\n")
report.write("Max user"+max_user+"\n")
report.write("Average check"+str(average_check)+"\n")
report.close()
print("Report had created successfully")