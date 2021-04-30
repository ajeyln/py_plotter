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
    print(Average_salary_female)
    print(Average_salary_male)

'''




data_ages_comp = data.sort_values("Age_in_Company")
data_ages_company = data_ages_comp["Age_in_Company"].tolist()

join_year = []
[join_year.append(x) for x in year_of_join if x not in join_year]
count_age_in_company = []
for i in age_in_company:
   y = data[data["Age_in_Company"] == i].count()["Age_in_Company"]
   count_age_in_company.append(y)
plt.bar(age_in_company,count_age_in_company,width=.5)
plt.xlabel('Age')
plt.ylabel('count of employees')
plt.title('Experience in comapany')
plt.savefig("Histogram")


def create_histogram():
    population_age = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
    bins = [0,10,20,30,40,50,60,70,80,90,100]
    plt.hist(population_age, bins, histtype='bar', rwidth=0.8)
    plt.xlabel('age groups')
    plt.ylabel('Number of people')
    plt.title('Histogram')
    plt.show()

def create_scatter_plot():
    x = [1,1.5,2,2.5,3,3.5,3.6]
    y = [7.5,8,8.5,9,9.5,10,10.5]
    
    x1=[8,8.5,9,9.5,10,10.5,11]
    y1=[3,3.5,3.7,4,4.5,5,5.2]
    
    plt.scatter(x,y, label='high income low saving',color='r')
    plt.scatter(x1,y1,label='low income high savings',color='b')
    plt.xlabel('saving*100')
    plt.ylabel('income*1000')
    plt.title('Scatter Plot')
    plt.legend()
    plt.show()

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
