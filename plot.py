from matplotlib import pyplot as plt
import pandas
import os

data = pandas.read_csv("data.csv")

# list files for all fields
first = data["First Name"].tolist()
age = data["Age"].tolist()
age_in_company = data["Age_in_Company"].tolist()
salary = data["Salary"].tolist()

# ploting bargrph,where age is less than 40
name_40 = data[data["Age"] <= 40]["First Name"].tolist()
age_40 =  data[data["Age"] <= 40]["Age"].tolist()
plt.bar(name_40,age_40,width=.5)
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Information')
plt.savefig("bar")

# year in company
data_ages_comp = data.sort_values("Age_in_Company")
data_ages_company = data_ages_comp["Age_in_Company"].tolist()

age_in_company = []
[age_in_company.append(x) for x in data_ages_company if x not in age_in_company]
count_age_in_company = []
for i in age_in_company:
   y = data[data["Age_in_Company"] == i].count()["Age_in_Company"]
   count_age_in_company.append(y)
plt.hist(age_in_company,count_age_in_company,width=.5)
plt.xlabel('Age')
plt.ylabel('count of employees')
plt.title('Experience in comapany')
plt.savefig("Histogram")