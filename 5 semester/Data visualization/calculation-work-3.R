library(datasets)
library(e1071)
data(iris)
iris[2] = NULL
iris[3] = NULL

plot(iris$Petal.Length, iris$Sepal.Length, col=iris$Species, pch=20)
legend(1.5,7.5,unique(iris$Species),col=1:length(iris$Species),pch=19)

x1 = 1.9
y1 = 5.2
points(x1,y1,pch=19, col="blue")
iris = add_row(iris, Petal.Length=1.9, Sepal.Length=5.2, Species='setosa')

x2 = 6.2
y2 = 4.9
points(x2,y2,pch=19, col="blue")
iris = add_row(iris, Petal.Length=6.2, Sepal.Length=4.9, Species='virginica')

model <- svm(Species ~ Sepal.Length + Petal.Length, iris, kernel = "linear")
plot(model, iris, Sepal.Length ~ Petal.Length)
