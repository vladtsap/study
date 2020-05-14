# Task 1
size = 50; prob = 0.5

binom <- rbinom(50, size, prob) # Біноміальний
hist(binom)

pois <- rpois(size, 2) # Пуассонівський
hist(pois)

geom<-rgeom(size, prob) # Геометричний
hist(geom)

norm <- rnorm(size, mean = 0, sd = 1) # Нормальний
hist(norm)

f<-rf(size, 1, 2, 0.5) # Фішера
hist(f)

t<-rt(size, 1, 0.5) # Стьюдента
hist(t)


# Task 2
ph=numeric(7)
for(i in 0:6)
  ph[i+1]<-dhyper(i,6,14,6)
ph
sum(ph)
barplot(ph,names=as.character(0:6),ylim=c(0,0.4),density= 16)


# Task 3
n = 15
ph = numeric(n)
prob = 0.1

for(i in 0:n-1)
  ph[i+1]<-dgeom(i, prob)

ph
barplot(ph, names=as.character(1:n), ylim = c(0,0.1), density = 16) 
