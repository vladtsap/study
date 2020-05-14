#task 1
x<-rnorm(100, mean = 50, sd = 10)
for(i in 1:100){
  x[i] <- as.integer(x[i])
}
x

#task 2
max(x)
which.max(x)

min(x)
which.min(x)

#install.packages("EnvStats")
library(EnvStats)
geoMean(x)

median(x)


#task 3
x1 = vector()
for(num in x){
  if(num < 40 | num > 60){
    x1 <- append(x1, num);
  }
}

x1 = x[x<40 | x>60]
x1

#task 4
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}
getmode(x)


#task 5
first <- matrix(x, nrow=10, ncol=10, byrow=TRUE)
first
second <- matrix(x, nrow=10, ncol=10)
second


#task 6
Ivan = matrix(c(100,TRUE,"100","Відмінно"), nrow=4)
Petro = matrix(c(98,TRUE,"98","Задовільно"), nrow=4)
Stepan = matrix(c(88,TRUE,"88","Добре"), nrow=4)
Mykola = matrix(c(51,FALSE,"51","Незадовільно"), nrow=4)
rating <- data.frame(Ivan, Petro, Stepan, Mykola)
rating


#task 7
A <- matrix(nrow=6, ncol=6,
  c(2.1,1.8,-0.3,2.0,0.4,7.6,
    0.0,1.6,6.8,0.2,-1.0,2.4,
    1.9,2.0,1.3,-0.9,7.2,0.2,
    0.6,5.6,2.4,-0.1,-1.3,0.5,
    6.9,1.2,-1.0,0.3,-1.7,0.7,
    2.0,0.6,0.1,5.7,-0.8,-1.3))
b <- matrix(nrow=6, ncol=1, c(-1.52,10.34,10.61,-1.98,22.74,28.3))
solve(A, b)
