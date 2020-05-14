# щільність розподілу
f <- function(x){
  if(x>0 && x<=2){
    return((2*x+1)/6)
  }
  else{
    return(0)
  }
}


# функція розподілу
F <- function(x) {
  if(x>0 && x<=2){
    return(x*(x+1)/6)
  }
  else if(x>2){
    return(1)
  }
  else{
    return(0)
  }
}


# матсподівання
fm <- function(x) x*f(x)
m <- integrate(fm,  lower=0, upper=2)$value 
m


# дисперсія
fd <- function(x) x^2*f(x)
d <- integrate(fd,  lower=0, upper=2)$value - m^2
d


# ймовірність
i <- integrate(f,  lower=1, upper=1.25)$value
i


# графік f
x <- seq(-1, 10, 0.01)
y=x
for(i in 1:length(x)){
  y[i]=f(x[i])
}
plot(x, y)


# графік F
x <- seq(-1, 10, 0.01)
y=x
for(i in 1:length(x)){
  y[i]=F(x[i])
}
plot(x, y)
