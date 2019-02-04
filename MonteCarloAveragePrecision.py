# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 14:47:12 2019

@author: Mathieu
"""
import math
from MonteCarlo import MonteCarlo
import xlsxwriter

    # Take the first value of Monte Carlo s method which reach the eps precision
        # eps : precision that you need to reach
        # n : number of Monte Carlo s method simulation
def ReachPrecisionMonteCarlo(eps, n):
    workbook = xlsxwriter.Workbook('ExcelFileRoot')
    worksheet = workbook.add_worksheet('Sheet1')
    listResult = []
    for k in range (0, n):
        i = 1
        while (abs(math.pi - MonteCarlo(i)) > eps):
            i += 1
        worksheet.write_number(k, 2 , i)
    workbook.close()
    return listResult
