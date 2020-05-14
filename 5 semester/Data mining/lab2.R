#preload
#install.packages("dplyr")
library(datasets)
library(dplyr)
data(airquality)


#task 1
arr = sample(11:99, 10)
arr
buble = function(arr){
  n = length(arr)
  for (i in 1:n){
    for(j in 1:(n-1))
      if(arr[j]>arr[j+1]){
        tmp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = tmp
      }
  }
  arr
}
buble(arr)


#task 2
random = sample(11:99, 1)
res = 0
find = function(arr,random){
  n = length(arr)
  for(i in 1:n){
    if(arr[i] == random){
      print("Matched! Index is")
      print(i)
      res=1
    }
  }
  if (res == 0){
    print("Nothing found")
  }
}
find(arr, random)


#task 3
table = airquality%>%
  group_by(Month)%>%
  summarise(avg_temp = mean(Temp))
write.table(table, file = "output.txt", sep = " ", eol = "\n", dec = ".", row.names = TRUE, col.names = NA)


#task 4
airquality %>%
  filter(Solar.R > 100) %>%
  summarise(wind = mean(Wind, na.rm = TRUE))


#task 5
ozon = airquality %>%
  group_by(Month)
month_ozon = ozon %>%
  summarise(ozon_mean = mean(Ozone, na.rm = TRUE))
max_ozon = max(month_ozon, na.rm = TRUE)
month_ozon %>%
  filter(ozon_mean == max_ozon) %>%
  print(Month)