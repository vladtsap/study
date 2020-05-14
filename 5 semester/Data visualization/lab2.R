library(dplyr)
library(ggplot2)

setwd("~/Drive/Study/Візуалізація/")

youtube <- read.csv("USvideos.csv", stringsAsFactors=FALSE, encoding="UTF-8")

youtube$likes_to_views <- youtube$likes/youtube$views

str(youtube)

summary(youtube)

ggplot(youtube, aes(x=likes_to_views)) + 
  geom_histogram(bins=20, color="grey", fill="lightblue")

cmean <- mean(youtube$likes_to_views)
cmean
csd <- sd(youtube$likes_to_views)
csd

set.seed(900)
likes_to_views_simulation <- rnorm(n=nrow(youtube), mean = cmean, sd = csd)

str(likes_to_views_simulation)
summary(likes_to_views_simulation)

youtube$likes_to_views_simulation <- likes_to_views_simulation

ggplot(youtube, aes(x=likes_to_views_simulation)) + 
  geom_histogram(bins=20, color="grey", fill="lightblue")

ggplot(youtube, aes(sample = likes_to_views)) + 
  stat_qq()

ggplot(youtube, aes(sample = likes_to_views_simulation)) + 
  stat_qq()

