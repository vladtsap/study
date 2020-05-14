# пуасона

p <- 0.00024
n <- 40000


# матсподівання
m <- n*p
m

# дисперсія
d <- n*p
d

# середнє квадратичне відхилення
s <- sqrt(d)
s


# закон розподілу
l = n*p
p <- function(k) ((l^k)*exp(1)^(-l))/factorial(k)

for(i in 0:10){
  print(paste0("i:", i, " p:", p(i)))
}
