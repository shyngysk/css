file = open("employees.txt", "r", encoding="utf-8")
employees = []
total_salary = 0
for line in file:
    a = line.strip().split(",")
    dep = a[1]
    salary = int(a[2])
    name = a[0]
    employees.append({
        "name": name,
        "dep": dep,
        "salary": salary
    })
    total_salary += salary
file.close()
average_salary = total_salary / len(employees)
highest_paid = employees[0]
for i in employees:
    if i["salary"] > highest_paid["salary"]:
        highest_paid = i
more_than_average_salary = []
for i in employees:
    if i["salary"] > average_salary:
        more_than_average_salary.append(i)
departments = {}
for i in employees:
    dep = i["dep"]
    salary = i["salary"]
    if dep not in departments:
        departments[dep] = []
    departments[dep].append(salary)
dep_averages = {}
for k, v in departments.items():
    average = sum(v)/len(v)
    dep_averages[k] = average
highest_dep = ""
highest_average = 0
for dep, avg in dep_averages.items():
    if avg > highest_average:
        highest_dep = dep
        highest_average = avg
rep = open("high_salary.csv", "x", encoding="utf-8")
rep.write("Average salary: " + str(average_salary) + "\n")
rep.write("Departaments' average salaries"+str(dep_averages)+"\n")
rep.write("Highest salary dep: " + str(highest_dep) + "\n")
rep.write("Highest paid: " + str(highest_paid) + "\n")
rep.write("More than average salary: " + str(more_than_average_salary) + "\n")
rep.close()