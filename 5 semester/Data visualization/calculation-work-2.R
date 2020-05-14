library(datasets)
library(dplyr)
data(iris)

plot(iris$Petal.Length, iris$Sepal.Length, col=iris$Species, pch=20)
legend(1.5,7.5,unique(iris$Species),col=1:length(iris$Species),pch=19)

x = 6.2
y = 4.9
points(x,y,pch=19, col="blue")

closest = iris %>%
  filter(Petal.Length < 7.6 & Petal.Length > 4.8 & Sepal.Length > 3.5 & Sepal.Length < 6.3)%>%
  top_n(n=10,Sepal.Length)
points(closest$Petal.Length, closest$Sepal.Length)

distance = 0
for (i in 1:length(closest)) {
  distance[i] = sqrt((x-closest$Petal.Length[i])^2 + (y-closest$Sepal.Length[i])^2)
  segments(x,y,closest$Petal.Length,closest$Sepal.Length, col = "gray")
}

closest[2] = NULL
closest[3] = NULL
closest$distance = distance
closest = closest[order(closest$distance),]
closest

closest %>%
  count(Species)
