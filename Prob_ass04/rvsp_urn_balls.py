# -*- coding: utf-8 -*-
"""rvsp_Urn_Balls.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19ixH6YxRQ3k6GuuvF4zwTjKLMsupKrQi
"""

######### Name: Anuradha Uggi
######### Id: EE21RESCH01008
######### Assignment: Probability and Random Variables

##################### Pdf and Cdf for Drawing 6 balls from 16 balls in an Urn ###############
import numpy as np
import matplotlib.pyplot as plt

#### Function definition for Combinations
def nchoosek(n, k):
    if k == 0:
        r = 1
    else:
        r = n/k * nchoosek(n-1, k-1)
    return round(r)
c=0;
d=[];
k=6;
n=6;###Number of balls needs to be picked
#### Probability Mass functoion of red balls
for i in range(7):
    dist=nchoosek(7,i)*nchoosek(9,k)/(nchoosek(16,6));
    d=np.append(d,dist);
    c+=dist;
    k=k-1;
print('validity of pmf of red balls:',c)
print('pmf:',d)
## cdf
c=0;
cdf=[];
#### CDF of red balls
for j in range(7):
    c+=d[j];
    print(c)
    cdf=np.append(cdf,c);


K1=np.linspace(0,6,7);

plt.figure()
plt.stem(K1,d)
plt.xlabel('Number of red balls(r)')
plt.ylabel('P(r)')
plt.title('PMF of red balls')

plt.figure()
plt.plot(K1,cdf)
plt.xlabel('Number of Red balls(r)')
plt.ylabel('CDF of r')
plt.title('CDF')
plt.show()