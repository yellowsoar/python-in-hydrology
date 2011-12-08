# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:45:50 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
import scipy.stats as st

# one random variable and mean
rvs1 = st.norm.rvs(loc=5,scale=10,size=1000)

t, p = st.ttest_1samp(rvs1,5)
print(p)

# for two  independent  
rvs1 = st.norm.rvs(loc=5,scale=10,size=1000)
rvs2 = st.norm.rvs(loc=5,scale=10,size=1000)

t, p = st.ttest_ind(rvs1,rvs2)
print(p)

# for two related
rvs1 = st.norm.rvs(loc=5,scale=10,size=1000)
rvs2 = st.norm.rvs(loc=5,scale=10,size=1000)

t, p = st.ttest_rel(rvs1,rvs2)
print(p)