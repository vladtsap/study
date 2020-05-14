?hclust


setwd("~/Drive/Study/ІАД")
ny <- read.csv("ny.gdp.mktp.kd.zg_Indicator_en_csv_v2.csv", stringsAsFactors=FALSE, encoding="UTF-8")
summary(ny)
d <- na.omit(ny$X2007)
matr_D=dist(d, method = "euclidean") #побудова дендрограми за ієрархічним алгоритмом
tree=hclust(matr_D)
plot(tree)
cl=kmeans(matr_D, 5, 10)
cl$cluster
table(cl$cluster)


sl <- read.csv("sl.uem.totl.zs_Indicator_en_csv_v2.csv", stringsAsFactors=FALSE, encoding="UTF-8")
summary(sl)
dsl <- na.omit(sl$X2013)
matr_D_sl=dist(dsl, method = "euclidean") #побудова дендрограми за ієрархічним алгоритмом
tree_sl=hclust(matr_D_sl)
plot(tree_sl)
clsl=kmeans(matr_D_sl, 5, 10)
clsl$cluster
table(clsl$cluster)
