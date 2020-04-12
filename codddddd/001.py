# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 09:41:29 2020

@author: 秦凤
"""

from hapi import *
from pylab import show, plot, subplot, xlim, ylim, title, legend, xlabel, ylabel


def convolveSpectrum(Omega, CrossSection, Resolution=0.1, AF_wing=10., SlitFunction=SLIT_RECTANGULAR, Wavenumber=None):
    if Wavenumber: Omega = Wavenumber
    step = Omega[1] - Omega[0]
    if step >= Resolution: raise Exception('step must be less than resolution')
    # x = arange(-AF_wing,AF_wing+step,step)
    x = arange_(-AF_wing, AF_wing + step, step)  # fix
    slit = SlitFunction(x, Resolution)
    # FIXING THE BUG: normalize slit function
    slit //= sum(slit) * step  # simple normalization
    left_bnd = len(slit) // 2
    right_bnd = len(Omega) - len(slit) // 2
    # CrossSectionLowRes = convolve(CrossSection,slit,mode='valid')*step
    CrossSectionLowRes = convolve(CrossSection, slit, mode='same') * step
    # return Omega[left_bnd:right_bnd],CrossSectionLowRes,left_bnd,right_bnd,slit
    return Omega[left_bnd:right_bnd], CrossSectionLowRes[left_bnd:right_bnd], left_bnd, right_bnd, slit


db_begin('data')
fetch('O3', 3, 1, 3900, 4050)
x, y = getStickXY('O3')  # 使用函数绘制谱
plot(x, y);
show()
plot(x, y, '.');
xlim([4020, 4035]);
show()  # 放大光谱区域
# 计算并绘制Voigt与Lorentzian线型的差分
wn = arange(3002, 3008, 0.01)  # 获取研究的谱线范围
voi = PROFILE_VOIGT(3005, 0.1, 0.3, wn)[0]  # 计算VOIGT
lor = PROFILE_LORENTZ(3005, 0.3, wn)  # 计算洛伦兹
diff = voi - lor  # calc difference 计算差分
subplot(2, 1, 1)  # upper panel两行一列上面的图
plot(wn, voi, 'red', wn, lor, 'blue')  # plot both profiles
legend(['Voigt', 'Lorentz'])  # show legend
title('Voigt and Lorentz profiles')  # show title
subplot(2, 1, 2)  # lower panel
plot(wn, diff)  # plot difference
title('Voigt-Lorentz residual')  # show title
show()  # show all figures
# 利用Voigt剖面计算和绘制臭氧吸收系数
nu1, coef1 = absorptionCoefficient_Voigt(((3, 1),), 'O3',
                                         OmegaStep=0.01, HITRAN_units=False, GammaL='gamma_self',
                                         Environment={'p': 1, 'T': 296.})
nu2, coef2 = absorptionCoefficient_Voigt(((3, 1),), 'O3',
                                         OmegaStep=0.01, HITRAN_units=False, GammaL='gamma_self',
                                         Environment={'p': 5, 'T': 296.})
nu3, coef3 = absorptionCoefficient_Voigt(((3, 1),), 'O3',
                                         OmegaStep=0.01, HITRAN_units=False, GammaL='gamma_self',
                                         Environment={'p': 1, 'T': 500.})
nu4, coef4 = absorptionCoefficient_Voigt(((3, 1),), 'O3',
                                         OmegaStep=0.01, HITRAN_units=False, GammaL='gamma_self',
                                         Environment={'p': 5, 'T': 500.})
subplot(2, 2, 1);
plot(nu1, coef1);
title('O3 k(w): p=1 atm, T=296K')
subplot(2, 2, 2);
plot(nu2, coef2);
title('O3 k(w): p=5 atm, T=296K')
subplot(2, 2, 3);
plot(nu3, coef3);
title('O3 k(w): p=1 atm, T=500K')
subplot(2, 2, 4);
plot(nu4, coef4);
title('O3 k(w): p=5 atm, T=500K')
show()
# 计算并绘制1 atm和296K的吸收、透射和辐射光谱。路径长度设置为10 m
nu, absorp = transmittanceSpectrum(nu1, coef1, Environment={'l': 1000.})
nu, transm = absorptionSpectrum(nu1, coef1, Environment={'l': 1000.})
nu, radian = radianceSpectrum(nu1, coef1, Environment={'l': 1000., 'T': 296.})
subplot(2, 2, 1);
plot(nu1, coef1, 'r');
title('O3 k(w): p=1 atm, T=296K')
subplot(2, 2, 2);
plot(nu, absorp, 'g');
title('O3 absorption: p=1 atm, T=296K')
subplot(2, 2, 3);
plot(nu, transm, 'b');
title('O3 transmittance: p=1 atm, T=296K')
subplot(2, 2, 4);
plot(nu, radian, 'y');
title('O3 radiance: p=1 atm, T=296K')
show()
# 计算并比较理想迈克尔逊干涉仪的仪器功能卷积的低分辨率光谱和O3的高分辨率光谱。
nu_, trans_, i1, i2, slit = convolveSpectrum(nu, transm, SlitFunction=SLIT_MICHELSON, Resolution=1.0, AF_wing=20.0)
plot(nu, transm, 'red', nu_, trans_, 'blue');
legend(['HI-RES', 'Michelson'])
show()
