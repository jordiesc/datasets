import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import calculos as cal
from sklearn.linear_model import LinearRegression

routa = "COVID 19/ccaa_covid19_hospitalizados.csv"

FECHA = "2020-04-19"
#routa = "COVID 19/ccaa_covid19_casos.csv"



timeseries = pd.read_csv(routa, index_col ="CCAA")
print("printamos todo el DataSet")

for region in timeseries.index:
   cal.print_report(timeseries,region)

#print_country(timeseries,'UK')
print("pinto la suma")

spain = timeseries.sum()
cal.print_report_serie(spain,"SPAIN")


