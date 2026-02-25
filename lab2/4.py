file = open("transactions.csv", "r", encoding="utf-8")
user_operations = {}
suspicious_transactions = []
total_suspicious = 0
for line in file:
    a = line.strip().split(",")
    user_id = a[0]
    amount = int(a[1].replace('"', ''))
    if amount > 500000:
        suspicious_transactions.append({
            "user_id": user_id,
            "amount": amount
        })
    if user_id not in user_operations:
        user_operations[user_id] = 0
    user_operations[user_id] += 1
file.close()
for i in suspicious_transactions:
    total_suspicious += i["amount"]
b = open("fraud_report.txt", "x", encoding="utf-8")
b.write("Suspicious transactions: "+str(suspicious_transactions) + "\n")
b.write("Total sum of suspicious operations: "+str(total_suspicious) + "\n")
b.close()