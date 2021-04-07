# -*- coding: utf-8 -*-
"""rvsp6_51.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k_HfSZurTbZSAV4gsOXRJ8AtGx9zReHC
"""

#######################   RVSP ASSIGNMENT-PROB  #################################




import numpy as np
import matplotlib.pyplot as plt

## Factorial
def fact(n):
     k=1;
     while(n!=0):
         k=k*n;
         n=n-1;
     return(k)

### Combinations
def nck(n,k):
      ppp=fact(n)/(fact(k)*fact(n-k));
      return (ppp)
## Probability computtation

n=3;
k=2;
prob=nck(n,k)*nck(365,n+1-k)*fact(n+1-k)/(365**n)

print('probability that 2 people among 3 share their birthday :',prob)