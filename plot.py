from matplotlib import pyplot as plt
from matplotlib import style
import pandas
import os

data = pandas.read_csv("data.csv")
sorted_gender = data.sort_values("Gender")
sorted_age = data.sort_values("Age")
sorted_Age_in_Company = data.sort_values("Age_in_Company")
sorted_join_year = data.sort_values("Year of Joining")

def create_plot(title, xlabel, ylabel, filename):
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend()
    plt.grid(True,color='k')
    plt.savefig(filename)
    plt.show()

def create_line_graph():
    style.use('ggplot')
    year_of_join = sorted_join_year["Year of Joining"].tolist()
    join_year = []
    [join_year.append(x) for x in year_of_join if x not in join_year]
    gender_female = sorted_gender[sorted_gender["Gender"] == "Female"]
    gender_male = sorted_gender[sorted_gender["Gender"] == "Male"]
    join_year_female = []
    join_year_male = []
    for i in join_year:
        y = gender_female[gender_female["Year of Joining"] == i].count()["Gender"]
        join_year_female.append(y)
    for j in join_year:
        z = gender_male[gender_male["Year of Joining"] == j].count()["Gender"]
        join_year_male.append(z)
    plt.plot(join_year,join_year_female,'g',label='Female', linewidth=5)
    plt.plot(join_year,join_year_male,'c',label='Male',linewidth=5)
    create_plot('Employee Joining Year', 'Year', 'Count', "line_plot")

def create_bar_graph():
    year_of_join = sorted_join_year["Year of Joining"].tolist()
    join_year = []
    [join_year.append(x) for x in year_of_join if x not in join_year]
    gender_female = sorted_gender[sorted_gender["Gender"] == "Female"]
    gender_male = sorted_gender[sorted_gender["Gender"] == "Male"]
    Average_salary_female = []
    Average_salary_male = []
    for i in join_year:
        y = gender_female[gender_female["Year of Joining"] == i]["Salary"].mean()
        Average_salary_female.append(y)
    for j in join_year:
        z = gender_male[gender_male["Year of Joining"] == j]["Salary"].mean()
        Average_salary_male.append(z)
    plt.bar(join_year,Average_salary_female,
    label="Female",color='m',width=.5)
    plt.bar(join_year,Average_salary_male,
    label="Male", color='r',width=.5)
    create_plot('Average Salary(Based on join Year)', 'Year', 'Average Salary', "bar_graph")

def create_histogram():
    age_employee = sorted_gender["Age"].tolist()
    bins = []
    [bins.append(x) for x in range(20,65,5)]
    plt.hist(age_employee, bins, histtype='bar', rwidth=0.3)
    create_plot('Age Info', 'Age', 'Count', "histogram")

def create_scatter_plot():
    gender_female = sorted_gender[sorted_gender["Gender"] == "Female"]
    gender_male = sorted_gender[sorted_gender["Gender"] == "Male"]
    age_female = gender_female["Age_in_Company"].tolist()
    age_male = gender_male["Age_in_Company"].tolist()
    salary_female = gender_female["Salary"].tolist()
    salary_male = gender_male["Salary"].tolist()
    plt.scatter(salary_female, age_female, label='Female',color='r')
    plt.scatter(salary_male, age_male,label='Male',color='b')
    create_plot('Salary Info(Male vs Female)', 'Age Of Experience', 'Salary', "Scatter Plot")

'''
def create_pie_chart():
    days = [1,2,3,4,5]

    sleeping =[7,8,6,11,7]
    eating = [2,3,4,3,2]
    working =[7,8,7,2,2]
    playing = [8,5,7,8,13]

    plt.plot([],[],color='m', label='Sleeping', linewidth=5)
    plt.plot([],[],color='c', label='Eating', linewidth=5)
    plt.plot([],[],color='r', label='Working', linewidth=5)
    plt.plot([],[],color='k', label='Playing', linewidth=5)

    plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Stack Plot')
    plt.legend()
    plt.show()


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

# year in company using histrogram

# pie chart
gender = data["Gender"].tolist()


slices = [7,2,2,13]
cols = ['m','r']
Sex = gender
plt.pie(slices,
  labels=activities,
  colors=cols,
  startangle=90,
  shadow= True,
  explode=(0,0.1,0,0),
  autopct='%1.1f%%')
 
plt.title('Pie Plot')
plt.show()
'''

if __name__ == "__main__":
    create_line_graph()
    create_bar_graph()
    create_histogram()
    create_scatter_plot()
