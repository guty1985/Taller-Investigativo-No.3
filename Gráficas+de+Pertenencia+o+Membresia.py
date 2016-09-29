
# coding: utf-8

# Funcion Triangular $$f(x) = 
# \begin{cases} 
# 0 & \mbox{si } x<a \\ (x-a) &\mbox{si } a<=x<b\\ (c-x) & \mbox{si } b<=x<=c\\ 0 & \mbox{si } x>=c 
# \end{cases} 
# $$

# In[21]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,100)
a=8
b=50
c=90

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Funcion Triangular')

plt.grid()

def f(x,a,b,c):
    if ((x<a) | (x>=c)):
        ans=0
    if ((a<=x) & (x<b)):
         ans=(x-a)
    if ((b<=x) & (x<=c)):
        ans=(c-x)
    return ans

f_vec = np.vectorize(f)
func=f_vec(x,a,b,c)
plt.plot(x,f_vec(x,a,b,c))


# Funcion Trapezoidal $$f(x) = 
# \begin{cases} 
# 0 & \mbox{si } x<=a \\ \frac {(x-a)}{(b-a)} &\mbox{si } a<=x<=b\\ 1 & \mbox{si } b<=x<=c\\ \frac{(d-x)}{(d-c)} & \mbox{si } c<=x<=d\\ 0 & \mbox{si } x>d
# \end{cases} 
# $$

# Funcion Sigmoidal

# In[10]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,80)

a=30
b=20
c=50
d=20

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Funcion Trapezoidal')

plt.grid()

def f(x,a,b,c,d):
    if ((x<=a) | (x>d)):
        ans=0.8
    if ((a<=x) & (x<=b)):
         ans=(x-a)/(b-a)
    if ((b<=x) & (x<=c)):
        ans=1
    if ((c<=x) & (x<=d)):
         ans=(d-x)/(d-c)
    return ans

f_vec = np.vectorize(f)
func=f_vec(x,a,b,c,d)
plt.plot(x,f_vec(x,a,b,c,d))


# In[83]:

import matplotlib.pyplot as plt
import numpy as np
import math

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Funcion Sigmoidal')


def sigmoid(x):
    a = []
    for item in x:
        a.append(1/(1+math.exp(-item)))
    return a



x = np.arange(-10., 10., 0.2)
sig = sigmoid(x)
plt.plot(x,sig)
plt.show()


# Funcion Tipo Hombro o Saturacion Derecha $$f(x) = 
# \begin{cases} 
# 0 & \mbox{si } x<=\alpha  \\ \frac{(x-\beta)}{(\alpha-\beta)} & \mbox{si } \\ 1 & \mbox{si } x>=\beta
# \end{cases} 
# $$

# In[139]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,100)

alfa=0.935
beta=50

def f(x,alfa,beta):
    if (x<=alfa):
        
        p=0
   
    if (alfa<=x)&(x<=beta):
        p=(x-beta)/(alfa-beta)
    
    if (x>=beta):
        p=1
   
    return p

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Funcion Tipo Hombro o Saturacion Derecha')

f_vec = np.vectorize(f)
func=f_vec(x,alfa,beta)
plt.plot(x,f_vec(x,alfa,beta))


# Funcion Tipo Hombro  o Saturacion Izquierda $$f(x) = 
# \begin{cases} 
# 1 & \mbox{si } x<=\alpha  \\ \frac{(x-\alpha)}{(\beta-\alpha)} & \mbox{si } \\ 0 & \mbox{si } x>=\beta
# \end{cases} 
# $$

# In[5]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,100)

alfa=20
beta=70

def f(x,alfa,beta):
    if (x<=alfa):
        
        p=1
   
    if (alfa<=x)&(x<=beta):
        p=(x-alfa)/(beta-alfa)
    
    if (x>=beta):
        p=0
   
    return p

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Funcion Tipo Hombro  o Saturacion Izquierda')

f_vec = np.vectorize(f)
func=f_vec(x,alfa,beta)
plt.plot(x,f_vec(x,alfa,beta))


# Funcion Tipo Saturacion Izquierda (PI) $$f(x) = 
# \begin{cases} 
# 0 & \mbox{si } x<a \\ \frac {(x-a)}{(b-a)} &\mbox{si } a<=x<=b\\ 1 & \mbox{si } b<=x<=d\\ \frac{(x-d)}{(c-d)} & \mbox{si } d<=x<c\\ 0 & \mbox{si } x>=c
# \end{cases} 
# $$

# In[6]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,100)

a=10
b=30
c=60
d=70

def f(x,a,b,c,d):
    
    if (x<a)|(x>=c):
        m=0;
   
    if (x>=a)&(x<b):
        m=(x-a)/(b-a)
    
    if (x>=b)&(x<d):
        m=1
    
    if (x>=d)&(x<c):
        m=1-(x-d)/(c-d)
    return m

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Funcion Tipo Saturacion Izquierda (PI)')


f_vec = np.vectorize(f)
func=f_vec(x,a,b,c,d)
plt.plot(x,f_vec(x,a,b,c,d))






# Funcion Forma S $$f(x) = 
# \begin{cases} 
# 0 & \mbox{si } x<a \\ 2\frac {(x-a)}{(c-a)} &\mbox{si } a<=x<b\\  1-2\left ( \frac{(x-c)}{(c-a)}\right )^{2} & \mbox{si } b<=x<=c\\ 1 & \mbox{si } x>c
# \end{cases} 
# $$

# In[141]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,100)

a=10
b=30
c=60

def f(x,a,b,c):
    
   
    if (x<a):
        p=0
  
    if (x>=a)&(x<b):
        p=2*(((x-a)/(c-a))**2)
    
    if (x>=b)&(x<=c):
        p=1-2*(((x-c)/(c-a))**2)
   
    if (x>c):
        p=1

    return p

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Funcion Forma S')

f_vec = np.vectorize(f)
func=f_vec(x,a,b,c)
plt.plot(x,f_vec(x,a,b,c))



# In[ ]:



