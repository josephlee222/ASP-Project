import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class findCountries:
    data = pd.ExcelFile('IMVA.xls')
    sheet = pd.read_excel(data, 'Sheet1')
    start_year = 1978
    end_year = 1987
    countries = ["Brunei Darussalam", "Indonesia", "Malaysia", "Myanmar", "Philippines", "Thailand", "Vietnam", "China",
                 "Hong Kong SAR", "Taiwan", "Japan", "South Korea", "Bangladesh", "India", "Pakistan", "Sri Lanka", "Iran",
                 "Israel", "Kuwait", "Saudi Arabia", "United Arab Emirates"]
    select_countries = ["Date"] + countries
    sheet = sheet[select_countries]
    countries_total = {"Country": [], "Total": []}
    countries_total_array = []
    years = []
    dates = []

    for x in sheet['Date']:
        date = x.split()
        years.append(int(date[0]))

    sheet.insert(1, "Year", years, True)
    sheet = sheet[sheet.Year >= start_year]
    sheet = sheet[sheet.Year <= end_year]
    sheet.replace("na", 0, inplace=True)

    for x in countries:
        countries_total["Total"].append(sheet[x].sum())
        countries_total["Country"].append(x)

    countries_total = pd.DataFrame.from_dict(countries_total)
    countries_total.sort_values(by=['Total'], inplace=True, ascending=False)
    countries_total.reset_index(drop=True, inplace=True)

    plt.figure(figsize=(10, 5))
    plt.gcf().subplots_adjust(bottom=0.30)
    plt.xticks(range(len(countries_total["Country"].to_list())), countries_total["Country"].to_list(), rotation='vertical')
    plt.bar(countries_total["Country"].to_list(), countries_total["Total"].to_list())
    plt.title('Total Visitors (' + str(start_year) + ' - ' + str(end_year) + ')')
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.show()

    print(countries_total['Country'].head(3).to_list())

    plt.figure(figsize=(10, 5))
    plt.gcf().subplots_adjust(bottom=0.30)
    plt.xticks(range(len(countries_total['Country'].head(3).to_list())), countries_total['Country'].head(3).to_list(), rotation='vertical')
    plt.bar(countries_total['Country'].head(3).to_list(), countries_total['Total'].head(3).to_list())
    plt.title('Top Countries (' + str(start_year) + ' - ' + str(end_year) + ')')
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.show()
    top3_total = sum(countries_total['Total'].head(3).to_list())
    grand_mean = round(np.mean(countries_total['Total'].to_list()))

if __name__ == '__main__':
    findCountries()