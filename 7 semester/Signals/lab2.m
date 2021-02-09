% Складнощі інтерполяції функції Рунге
clear;
xx=-5:0.01:5; yy=1./(1+xx.*xx); % Функція Рунге в 1000 точок
yy=yy+0.02*randn(size(yy)); % Шумова добавка для апроксимації
for n=2:2:20 % Цикл значень порядку степеневого полінома
    %x=-5:(5-(-5))/(n-1):5; % Точки для інтерполяції
    x=-5:0.05:5; % Точки для апроксимації
    y=1./(1+x.*x); % Функція Рунге в точках інтерп. або апрокс.
    y=y+0.02*randn(size(y)); % Шумова добавка для апроксимації
    [p,s,mu]=polyfit(x,y,n-1); % Обчислення коефіцієнтів поліному
    pol=polyval(p,xx,[],mu); % Значення поліному в точках хх
    er=max(abs(yy-pol)); % Максимальний модуль різниці
    plot(xx,yy,'b', xx,pol,'r'); % Графіки поліному і функції Рунге
    title(sprintf('n=%g er=%g',n,er));
    pause;
end