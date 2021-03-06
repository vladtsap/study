# геометричний

p <- 0.84
q <- 1-p

# матсподівання
m <- 1/p
m

# дисперсія
d <- q/p^2
d

# середнє квадратичне відхилення
s <- sqrt(d)
s


# P(x)
P <- function(k) p*q^(k-1)


# таблиця розподілу
for(k in 1:10){
  print(paste0("k:", k, " p:", P(k)))
}


# імовірнісний многокутник
val = c()
for (i in 1:10)
  val[i] <- P(i)
plot(val, type="o")
