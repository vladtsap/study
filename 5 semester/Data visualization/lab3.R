library(dplyr)
library(ggplot2)

setwd("~/Drive/Study/Візуалізація/")
youtube <- read.csv("USvideos.csv", stringsAsFactors=FALSE, encoding="UTF-8")

# youtube$likes_to_views <- youtube$likes/youtube$views

summary(youtube)

youtube = youtube %>%
  filter(category_id==25)

cor(youtube$views, youtube$likes)
cor(youtube$views, youtube$dislikes)
cor(youtube$views, youtube$comment_count)
cor(youtube$likes, youtube$comment_count)
cor(youtube$likes, youtube$dislikes)
cor(youtube$dislikes, youtube$comment_count)

lm1 <- lm(data=youtube, views~likes)
lm1$fitted.values
lm1$residuals

summary(lm1)

ggplot(data=youtube, aes(x=likes, y=views)) + geom_point(col="lightblue") +
  geom_smooth(method="lm", se=FALSE)

ggplot(data=youtube, aes(x=likes, y=views, col=category_id)) +
  geom_point()

ggplot(data=youtube, aes(x=likes, y=views)) + geom_point(col="lightblue") +
  geom_smooth(method="lm", se=FALSE) + facet_wrap(~category_id)



qqnorm(lm1$residuals, col="orange", pch=20) 
qqline(lm1$residuals, col = "blue") 
















set.seed(1);
z = rnorm (100)
qqnorm(z)