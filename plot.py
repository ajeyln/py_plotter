from matplotlib import pyplot as plt
import pandas
import os

data = pandas.read_csv("data.csv")

first = data["First Name"].tolist()
age = data["Age"].tolist()
age_in_company = data["Age_in_Company"].tolist()
salary = data["Salary"].tolist()

print(first)
print(age)
print(age_in_company)
print(salary)

plt.bar(first,age,width=.5)
plt.legend()
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Information')
plt.savefig("bar")
plt.show()