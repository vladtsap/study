x=c(1,3,6,8,9,10,11,12,14,16,17,18,20,22,23,24,25,27,29,30)
y=c(-26,-18,-6,2,6,10,14,18,26,34,38,42,50,58,62,66,70,78,86,90)

cor(x,y, method = "pearson")
cor(x,y, method = "kendall")
cor(x,y, method = "spearman")

cor.test(x,y)
