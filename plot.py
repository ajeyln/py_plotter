from matplotlib import pyplot as plt
from matplotlib import style
import pandas
import os

data = pandas.read_csv("data.csv")
sorted_gender = data.sort_values("Gender")
sorted_age = data.sort_values("Age")
sorted_Age_in_Company = data.sort_values("Age_in_Company")
sorted_join_year = data.sort_values("Year of Joining")
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(CURRENT_DIR, "plotter_images")

def create_plot(title, xlabel, ylabel, filename):
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend(loc ="upper right", prop={"size":10})
    filepath = os.path.join(FILE_NAME, filename)
    plt.savefig(filepath)
    return

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
    create_plot('Employee Joining Year', 'Year', 'Count', "01_line_plot")

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
    create_plot('Average Salary(Based on join Year)', 'Year', 'Average Salary', "02_bar_graph")
def create_histogram():
    age_employee = sorted_gender["Age"].tolist()
    bins = []
    [bins.append(x) for x in range(20,65,5)]
    plt.hist(age_employee, bins, histtype='bar', rwidth=0.3)
    create_plot('Age Info', 'Age', 'Count', "03_histogram")

def create_scatter_plot():
    gender_female = sorted_gender[sorted_gender["Gender"] == "Female"]
    gender_male = sorted_gender[sorted_gender["Gender"] == "Male"]
    age_female = gender_female["Age_in_Company"].tolist()
    age_male = gender_male["Age_in_Company"].tolist()
    salary_female = gender_female["Salary"].tolist()
    salary_male = gender_male["Salary"].tolist()
    plt.scatter(salary_female, age_female, label='Female',color='r')
    plt.scatter(salary_male, age_male,label='Male',color='b')
    create_plot('Salary Info(Male vs Female)', 'Age Of Experience', 'Salary', "04_scatter_plot")

def create_pie_chart():
    less_than_35 = sorted_age[sorted_age["Age"] <= 35].count()["First Name"]
    between_35_45 = sorted_age[(sorted_age["Age"] > 35) & (sorted_age["Age"] <= 45)].count()["First Name"]
    between_45_55 = sorted_age[(sorted_age["Age"] > 45) & (sorted_age["Age"] <= 55)].count()["First Name"]
    higher_than_65 =sorted_age[sorted_age["Age"] > 55].count()["First Name"]
    slices = [less_than_35, between_35_45, between_45_55, higher_than_65]
    Age_of_Employees = ['less than 35','between 35 and 45','between 45 and 55','higher than 55']
    cols = ['m','y','r','g']
    plt.pie(slices,
    labels= Age_of_Employees,
    colors=cols,
    startangle=90,
    shadow= True,
    autopct='%1.1f%%')

    plt.title('Age of Employees')
    plt.legend()
    plt.savefig('05_pie_chart')

if __name__ == "__main__":
    create_line_graph()
    create_bar_graph()
    create_histogram()
    create_scatter_plot()
    create_pie_chart()

