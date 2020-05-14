# нормальний

a <- -1
sigma <- -1
alpha <- 0
beta <- 9

# матсподівання
M <- a

# дисперсія
d <- sigma^2


# f(x) та графік
f <- function(x) dnorm(x, mean=M, sd=abs(sigma))
x <- seq(-10, 10, 0.01)
y=x
for(i in 1:length(x)){
  y[i]=f(x[i])
}
plot(x, y)


# графік F(X)
x <- seq(-5, 5, 0.01)
y <- pnorm(x, mean = M, sd = abs(sigma))
plot(x,y)


# P(alpha < X < beta)
pnorm(beta, mean = M, sd = abs(sigma))-pnorm(alpha, mean = M, sd = abs(sigma))

integrate(f, lower = alpha, upper = beta)$value
