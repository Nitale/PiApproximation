# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 14:47:12 2019

@author: Mathieu
"""
import math
from Monte_Carlo import MonteCarlo
import xlsxwriter

def ReachPrecisionMonteCarlo(eps):
    workbook = xlsxwriter.Workbook('D:\Boulot\MT79\Approximation du nombre PI\monteCarloAverage.xlsx')
    worksheet = workbook.add_worksheet('Sheet2')
    listResult = []
    for k in range (0, 1000):
        i = 1
        while (abs(math.pi - MonteCarlo(i)) > eps):
            i += 1
        worksheet.write_number(101 + k, 2 , i)
    workbook.close()
    return listResult

ReachPrecisionMonteCarlo(10**-4)