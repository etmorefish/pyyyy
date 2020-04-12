# -*- coding: utf-8 -*-
"""
我这个只能显示线强图，吸收系数和吸光度两个图显示不出来。。。
报错写的是：object of type <class 'numpy.float64'> cannot be safely interpreted as an integer.
TypeError: 'numpy.float64' object cannot be interpreted as an integer
好像是转换的问题
这个要怎么改呀？
"""

from hapi import *
import numpy as np
import matplotlib.pylab as plb
import scipy.constants as C

db_begin('data')
myTableName='H2O_7178~7192'
fetch(myTableName,1,1,7178,7192)
tableList()
describeTable(myTableName)
x, y = getStickXY(myTableName)#线强图
plb.figure()
plb.plot(x, y)
plb.xlabel('wavenumber($cm^{-1}$)')
plb.ylabel('linestrength($cm^{-1}/(molecule\cdot cm^{-2})$)')
plb.title('$H_2O linestrength @ 296K$')
nu,coef=absorptionCoefficient_Voigt(SourceTables=myTableName,HITRAN_units=False)#吸收系数
plb.figure()
plb.plot(nu,coef)
plb.xlabel('wavenumber($cm^{-1}$)')
plb.ylabel('absorption coefficient($cm^{-1}$)')
plb.title('$H_2O absorption coefficient @ 1atm,296K$')
myOpticalL = 5.0
nu, absorp = absorptionSpectrum(nu, coef, Environment={'l':myOpticalL})#吸光度
plb.figure()
plb.plot(nu, absorp)
plb.xlabel('wavenumber($cm^{-1}$)')
plb.ylabel('absorbance')
plb.title('$H_2O absorbance @ 1atm, 296K$')
plb.show()