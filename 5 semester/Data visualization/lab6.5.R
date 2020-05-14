# показниковий

N <- 400
T <- 350

l = 1/T


# ймовірність
exp(1)^(-(N)/(T))


# f(x)
f <- function(x){
  if(x>0){
    return(l*exp(1)^(-l*x))
  }
  else{
    return(0)
  }
}
