# рівномірний

a <- 3
b <- 10

# матсподівання
m <- (a+b)/2
m

# дисперсія
d <- ((b-a)^2)/12
d

# середнє квадратичне відхилення
s <- sqrt(d)
s


# f(x)
f <- function(x){
  if(x>a && x<=b){
    return(1/(b-a))
  }
  else{
    return(0)
  }
}


# F(x)
F <- function(x) {
  if(x>a && x<=b){
    return((x-a)/(b-a))
  }
  else if(x>b){
    return(1)
  }
  else{
    return(0)
  }
}
