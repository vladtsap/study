# довідка lm() та nls()
?lm
?nls

# завантажуємо дані до task 2
library(datasets)
data(airmiles)
data(freeny)
data(pressure)
data(uspop)

#task 2.1
summary(airmiles)
plot(airmiles)
airm = lm(airmiles ~ ., data = airmiles) 
airm
summary(airm)

#task 2.2
summary(freeny)
plot(freeny$y)
plot(freeny$lag.quarterly.revenue)
plot(freeny$price.index)
plot(freeny$income.level)
plot(freeny$market.potential)
freenym = lm(y ~ ., data = freeny) 
freenym

#task 2.3
summary(pressure)
cor(pressure$temperature, pressure$pressure)
plot(pressure)
xdata = pressure$temperature
ydata = pressure$pressure
result=nls(ydata~a*exp(xdata)+b,start=list(a=1,b=1))
result

#task 2.4
summary(uspop)
plot(uspop)
uspopm = lm(uspop ~ ., data = uspop) 
uspopm


# task 3
x=c(1,3,6,8,9,10,11,12,14,16,17,18,20,22,23,24,25,27,29,30)
y=c(-26,-18,-6,2,6,10,14,18,26,34,38,42,50,58,62,66,70,78,86,90)
plot(x, y)
cor(x, y)
lm(x~y)
