#preload
data(airquality)


#task 1
plot(sin,-2*pi,2*pi)

plot(sin,-2*pi,2*pi, lty='dashed', col = "red")
plot(sin,-2*pi,2*pi, lty='dotdash', col = "green")
plot(sin,-2*pi,2*pi, lty='longdash', col = "blue")
plot(sin,-2*pi,2*pi, lty='dotted', col = "cyan")
plot(sin,-2*pi,2*pi, lty='dashed', col = "magenta")

plot(cos,-2*pi,2*pi, lty='dashed', col = "red")
plot(cos,-2*pi,2*pi, lty='dotdash', col = "green")
plot(cos,-2*pi,2*pi, lty='longdash', col = "blue")
plot(cos,-2*pi,2*pi, lty='dotted', col = "cyan")
plot(cos,-2*pi,2*pi, lty='dashed', col = "magenta")


#task 2
first = hist(airquality$Temp[airquality$Month <=7], plot = FALSE)
second = hist(airquality$Temp[airquality$Month >7], plot = FALSE)
plot(first,col = "red", xlab = "Temp")
plot(second, col = "green", add = TRUE)
legend("topright",c("5-7 Months", "8-9 Months"), col = c("red", "green"), lwd = 15)


#task 3
airquality$color[airquality$Month == '5'] = "red"
airquality$color[airquality$Month == '6'] = "green"
airquality$color[airquality$Month == '7'] = "blue"
airquality$color[airquality$Month == '8'] = "cyan"
airquality$color[airquality$Month == '9'] = "magenta"
dotchart(airquality$Temp, labels = airquality$Month, cex = 1, groups = airquality$Month, color = airquality$color, xlab = 'temp')


#task 4
x = runif(15,0,3)
plot.new()
plot(x)
lines(x)
