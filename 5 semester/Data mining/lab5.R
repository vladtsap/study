set.seed(1)
num = rbinom(100,100,0.8)
num

cut1 = cut(num,breaks = c(-1,59,74,89,100),labels = c("2","3","4","5"))
cut1

mean(num)
sd(num)


table1 = table(cut1)
table1


table2 = table(num)
table2

table(cut1)/length(cut1)

barplot(table1)

par(mfrow=c(1,1))
pie(table1,labels=c('2','3','4','5'),edges=40,radius=1, clockwise=T, init.angle=60,density=c(2,4,6,8),angle=c(15,45,60,75),col =1:4, border=NULL,main='table1')


Fn = ecdf(num);
summary(Fn)

par(mfrow=c(2,2))
plot(Fn)
plot.ecdf(Fn)
plot.ecdf(num)
plot(Fn, verticals=TRUE, col.points="blue", col.hor="red", col.vert="bisque")
