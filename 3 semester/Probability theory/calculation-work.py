
# coding: utf-8

# In[1]:


s = [15,17,13,20,19,17,25,10,18,40,21,35,11,25,30,29,35,34,25,18,27,45,36,22,28,38,46,47,24,11,14,16,27,61,52,33,35,48,16,27,26,48,51,50,60,62,54,58,25,27,35,42,47,45,55,38,70,61,47,44,34,36,35,61,65,70,53,54,54,56,47,11,21,22,24,53,52,53,70,62,61,21,18,11,21,18,27,24,25,26,22,12,11,22,23,33,35,41,18,11]


# In[2]:


len(s)


# In[3]:


s.sort()


# In[4]:


print(s)


# In[5]:


from collections import Counter
from fractions import Fraction
import operator
from matplotlib import pyplot as plt
import math

d = Counter(s)
d.keys()


# In[7]:


for i in d.keys():
    print('{0}, {2}, {1}'.format(d[i], i, Fraction(d[i], 100)))


# In[8]:


print('Мода {0}, Медіана {1}, Розмах {2}'.format(max(d, key=d.get), (s[49]+s[50])/2, s[99]-s[0]))


# In[9]:


plt.figure(figsize=(20, 10))
plt.grid()
plt.plot(d.keys(), d.values())
plt.xticks(s)


# In[10]:

plt.figure(figsize=(20, 10))
plt.bar(d.keys(), d.values())
plt.xticks(s)
plt.show(s)


# In[21]:


interv = []
suma = 0
t = 10
for i in range(20,90,10):
    for j in d.keys():
        if j < i and j >= t:
            suma += d[j]
    interv.append(((t,i),suma, Fraction(suma,100)))
    suma = 0
    t = i


# In[22]:


interv


# In[35]:


ser = 0
for i in d.keys():
    ser += i*d[i]
    
print('Середнє вибіркове {0}'.format(ser/100))


# In[36]:


ser = 0
for i in interv:
    ser+=(i[0][1]+i[0][0])/2 * i[1]

ser_int = ser/100
print('Середнє вибіркове {0}'.format(ser_int))


# In[47]:


dispersion = 0

for i in interv:
    dispersion += ((i[0][1]+i[0][0])/2)**2 * i[1]

dispersion /= 100

dispersion -= ser_int**2

ser_quad = math.sqrt(dispersion)
print('Дисперсія {0}, Середньоквадратичне відхилення {1}'.format(dispersion, ser_quad))


# In[48]:


print('Коефіцієнт варіації {0}'.format(ser_quad/ser_int))


# In[49]:


emp3 = 0
emp4 = 0

for i in interv:
    emp3 += ((i[0][1]+i[0][0])/2 - ser_int)**3 * i[1]
    emp4 += ((i[0][1]+i[0][0])/2 - ser_int)**4 * i[1]

emp3 /= 100
emp4 /= 100

print('Центральні емпіричні моменти 3-го {0} і 4-го порядків {1}'.format(emp3, emp4))


# In[50]:


print('Асиметрія {0} і Ексцес {1}'.format(emp3/(ser_quad**3), emp4/(ser_quad**4)-3))

