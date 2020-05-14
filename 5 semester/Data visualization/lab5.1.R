# коеф А
D(expression((x^2-9)/54),"x")

fa <- function(x) (2 * x)/(54)
integral <- function () { 
  integrate(fa,  lower=3, upper=6)$value 
}

A <- 1/integral()
A


# функція розподілу
F <- function(x) {
  if(x>3 && x<=6){
    return((4 * x)/54)
  }
  else if(x>6){
    return(1)
  }
  else{
    return(0)
  }
}

# щільність розподілу
D(expression((2*(x^2-9))/54),"x")

f <- function(x) {
  if(x>3 && x<=6){
    return((4 * x)/54)
  }
  else{
    return(0)
  }
}


# матсподівання
fm <- function(x) x*f(x)
m <- integrate(fm,  lower=3, upper=6)$value 
m

# дисперсія
fd <- function(x) x^2*f(x)
d <- integrate(fd,  lower=3, upper=6)$value - m^2
d

# ймовірність
i <- integrate(f,  lower=4, upper=5)$value
i


# графік f(x)
x <- seq(1, 10, 0.1)
y=x
for(i in 1:length(x)){
  y[i]=f(x[i])
}
plot(x, y)


# графік F(x)
x <- seq(1, 10, 0.1)
y=x
for(i in 1:length(x)){
  y[i]=F(x[i])
}
plot(x, y)
