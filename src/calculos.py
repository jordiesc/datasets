import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

#routa = "COVID 19/ccaa_covid19_confirmados_pcr.csv"

routa = "COVID 19/ccaa_covid19_casos.csv"
FECHA = "2020-04-01"

def print_country(dataset,country_name):
    countrypre = dataset.loc[country_name,:]
    #print(countrypre)
    country = countrypre[FECHA:]
    country_pct = country.pct_change()
    #print(country)
    #print("percentatges"," ",country_name)
    #print(country_pct[-10:])
    country_pct.plot(label=str(country_name))
    return country, country_pct

def get_growth_factor(dataset):
    diferences = dataset.diff()

    #print(diferences[-3:])
    for i in range(2,len(diferences)):
        # print("diferences ..",diferences.iloc[i-1]) 
        if diferences.iloc[i-1] != 0 :
            growth_factor = diferences.iloc[i] / diferences.iloc[i-1] 
            # print(" groth_factor :",diferences.iloc[i]," ",diferences.iloc[i-1])
            diferences.iat[i-1] = growth_factor
    growthfactor = diferences.iloc[:len(diferences)-1]
    return growthfactor
 
#def get_growth_factor(dataset,country_name):
#    countrypre = dataset.loc[country_name,:]
#    country = countrypre[FECHA:]
#    diferences = country.diff()

#    #print(diferences[-3:])
#    for i in range(2,len(diferences)):
#        # print("diferences ..",diferences.iloc[i-1]) 
#        if diferences.iloc[i-1] != 0 :
#            growth_factor = diferences.iloc[i] / diferences.iloc[i-1] 
#            # print(" groth_factor :",diferences.iloc[i]," ",diferences.iloc[i-1])
#            diferences.iat[i-1] = growth_factor
#    growthfactor = diferences.iloc[:len(diferences)-1]
#    return growthfactor
   

def get_r0_factor(dataset):
    diferences = dataset.diff()

    print(diferences[-6:])

    temp = []
    for i in range(6,len(diferences)):
        # print("diferences ..",diferences.iloc[i-1]) 
        if diferences.iloc[i-1] != 0 :
            r0_factor = (diferences.iloc[i] + diferences.iloc[i-1] +diferences.iloc[i-2] )/ (diferences.iloc[i-3] + diferences.iloc[i-4] +diferences.iloc[i-5]) 
            temp.append(r0_factor)
    
    return temp




#def get_r0_factor(dataset,country_name):
#    countrypre = dataset.loc[country_name,:]
#    country = countrypre[FECHA:]
#    diferences = country.diff()

#    print(diferences[-6:])

#    temp = []
#    for i in range(6,len(diferences)):
#        # print("diferences ..",diferences.iloc[i-1]) 
#        if diferences.iloc[i-1] != 0 :
#            r0_factor = (diferences.iloc[i] + diferences.iloc[i-1] +diferences.iloc[i-2] )/ (diferences.iloc[i-3] + diferences.iloc[i-4] +diferences.iloc[i-5]) 
#           # print(r0_factor)
#            # print(" groth_factor :",diferences.iloc[i]," ",diferences.iloc[i-1])
#            #diferences.iat[i-1] = ro_factor
#            temp.append(r0_factor)
    
#    return temp



def print_report(dataset,country_name):

    CRED = '\033[91m'
    CEND = '\033[0m'
    print(CRED + "##########      " + country_name + CEND)
    countrypre = dataset.loc[country_name,:]
    #print(countrypre)
    country = countrypre[FECHA:]
    
    growfactor_autonomia = get_growth_factor(country)
    print('printamos el grow factor')
    print(growfactor_autonomia[-6:])

    r0 = get_r0_factor(country)
    print('printamos el r0 factor')
    print(r0[-1:])

def print_country(dataset,country_name):
    countrypre = dataset.loc[country_name,:]
    #print(countrypre)
    country = countrypre[FECHA:]
    country_pct = country.pct_change()
    #print(country)
    #print("percentatges"," ",country_name)
    #print(country_pct[-10:])
    country_pct.plot(label=str(country_name))
    return country, country_pct

   



def print_report_serie(dataset,country_name):

    CRED = '\033[91m'
    CEND = '\033[0m'
    print(CRED + "##########      " + country_name + CEND)
    #print(countrypre)
    reduced  = dataset[FECHA:]
    
    growfactor_autonomia = get_growth_factor(reduced)
    print('printamos el grow factor')
    print(growfactor_autonomia[-6:])

    r0 = get_r0_factor(reduced)
    print('printamos el r0 factor')
    print(r0[-1:])



 


