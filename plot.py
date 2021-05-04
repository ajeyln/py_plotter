from matplotlib import pyplot as plt
from matplotlib import style
import pandas
import os
from fpdf import FPDF
import numpy as np

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

def create_histogram():
    age_employee = sorted_gender["Age"].tolist()
    bins = []
    [bins.append(x) for x in range(20,65,5)]
    plt.hist(age_employee, bins, histtype='bar', rwidth=0.3)
    plt.title('Age Info')
    plt.ylabel('Count')
    plt.xlabel('Age')
    plt.legend(loc ="upper right", prop={"size":10})
    filepath = os.path.join(FILE_NAME, "03_histogram")
    plt.savefig(filepath)

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
    width = 0.2
    [join_year.append(x) for x in year_of_join if x not in join_year]
    join_year_female = np.arange(len(join_year))
    join_year_male = [ i+width for i in join_year_female ]
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
    plt.bar(join_year_female,Average_salary_female, label="Female",color='m', width=width)
    plt.bar(join_year_male,Average_salary_male, label="Male", color='r', width=width)
    plt.xticks(join_year_female, join_year)
    create_plot('Average Salary(Based on join Year)', 'Year', 'Average Salary', "02_bar_graph")
def create_scatter_plot():
    gender_female = sorted_gender[sorted_gender["Gender"] == "Female"]
    gender_male = sorted_gender[sorted_gender["Gender"] == "Male"]
    age_female = gender_female["Age_in_Company"].tolist()
    age_male = gender_male["Age_in_Company"].tolist()
    salary_female = gender_female["Salary"].tolist()
    salary_male = gender_male["Salary"].tolist()
    plt.scatter(salary_female, age_female, label='Female',color='r')
    plt.scatter(salary_male, age_male,label='Male',color='b')
    plt.title('Salary Info(Male vs Female)')
    plt.ylabel('Salary')
    plt.xlabel('Age Of Experience')
    plt.legend(loc ="upper right", prop={"size":10})
    filepath = os.path.join(FILE_NAME, "04_scatter_plot")
    plt.savefig(filepath)

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
    filepath = os.path.join(FILE_NAME, '05_pie_chart')
    plt.savefig(filepath)

def create_pdf():
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    pdf.cell(225, 10, txt= "Statistical Report", ln = 1, align = "C")
    pdf.multi_cell(200, 10, txt= "The line graph shows Employee count with respect to their joining year and there are two lines, one reprsents to Female and another to Male in a company.", align = "l")
    file_image1 = os.path.join(FILE_NAME, "01_line_plot.png")
    pdf.image(file_image1, x = None, y = None, w=700/5, h=450/5, type = '')
    pdf.cell(200, 10, txt= "In this task, The Bar graph shows the Average salary of the Female and Male based on their joing years.", ln = 4, align = "l")
    file_image2 = os.path.join(FILE_NAME, "02_bar_graph.png")
    pdf.image(file_image2, x = None, y = None, w=700/5, h=450/5, type = '')
    pdf.cell(200, 10, txt= "In this section, we are plotting the graph based on Employees age with duration of 5 Years.", ln = 6, align = "l")
    file_image3 = os.path.join(FILE_NAME, "03_histogram.png")
    pdf.image(file_image3, x = None, y = None, w=700/5, h=450/5, type = '')
    pdf.cell(200, 10, txt= "The scatter graph shows the salary of Male and Female based on their experience on company.", ln = 8, align = "l")
    file_image4 = os.path.join(FILE_NAME, "04_scatter_plot.png")
    pdf.image(file_image4, x = None, y = None, w=700/5, h=450/5, type = '')
    pdf.cell(200, 10, txt= "In the Piechart, we can find the agewise employee percentage of company.",ln = 10, align = "l")
    file_image5 = os.path.join(FILE_NAME, "05_pie_chart.png")
    pdf.image(file_image5, x = None, y = None, w=700/5, h=450/5, type = 'png', link = '')
    pdf_path = os.path.join(CURRENT_DIR, "statistics")
    pdf_file = os.path.join(pdf_path, "Statistic.pdf")
    pdf.output(pdf_file,'F')

if __name__ == "__main__":
    create_histogram()
    create_line_graph()
   create_bar_graph()
    create_scatter_plot()
    create_pie_chart()
    create_pdf()
