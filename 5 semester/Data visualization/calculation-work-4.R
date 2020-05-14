library(neuralnet)
data(iris)

train_num = sample(seq_len(nrow(iris)), size = floor(0.8 * nrow(iris)))
train <- iris[train_num, ]
eval <- iris[-train_num, ]

network=neuralnet(Species~Sepal.Length+Sepal.Width+Petal.Length+Petal.Width, data=train, hidden=c(4, 5, 3))
plot(network)

prediction = compute(network,eval)

View(prediction$net.result)
