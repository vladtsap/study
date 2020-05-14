install.packages("dplyr")
install.packages("ggplot2")

library(dplyr)
library(ggplot2)

setwd("~/Desktop")

youtube <- read.csv("USvideos.csv", stringsAsFactors=FALSE, encoding="UTF-8")

class(youtube)

str(youtube)

summary(youtube)

dim(youtube)

head(youtube, 6)

tail(youtube, 6)

glimpse(youtube)

youtube %>%
  filter(views > 10000000) %>%
  filter(likes > 100000) %>%
  count(channel_title) %>%
  arrange(desc(n))

youtube %>%
  filter(comments_disabled == "True") %>%
  summarise(mean(dislikes ))

ggplot(youtube, aes(x=channel_title)) +
  geom_bar(fill="lightblue", col="grey") +
  ylab('Кількість')

ggplot(youtube, aes(x=views)) +
  geom_histogram(breaks=seq(0, 1000000, by = 10000), fill="lightblue",
                 col="grey") + ylab('Кількість')

ggplot(youtube, aes(x=dislikes, y=likes)) + geom_point()


ggplot(youtube, aes(group=category_id, x=category_id, y=views)) +
  geom_boxplot() +
  coord_flip()+
  ylab("Кількість")


