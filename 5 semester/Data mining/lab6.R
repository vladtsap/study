data(mtcars)
summary(mtcars)
colnames(mtcars)

shapiro.test(mtcars[, "mpg"])
shapiro.test(mtcars[, "cyl"])
shapiro.test(mtcars[, "disp"])
shapiro.test(mtcars[, "hp"])
shapiro.test(mtcars[, "drat"])
shapiro.test(mtcars[, "wt"])
shapiro.test(mtcars[, "qsec"])
shapiro.test(mtcars[, "vs"])
shapiro.test(mtcars[, "am"])
shapiro.test(mtcars[, "gear"])
shapiro.test(mtcars[, "carb"])



data(iris)
summary(iris)
colnames(iris)

shapiro.test(iris[, "Sepal.Length"])
shapiro.test(iris[, "Sepal.Width"])
shapiro.test(iris[, "Petal.Length"])
shapiro.test(iris[, "Petal.Width"])
