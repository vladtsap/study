%  Spline interpolation and approximation of the Runge function 
clear;
xx=-5:0.01:5;  yy=1./(1+xx.*xx);  % Функція Рунге в 1000 точок 
yy1=-2.*xx./(1+xx.*xx).^2;           % Перша і друга похідні 
yy2=-2./(1+xx.*xx).^2+8.*xx.^2./(1+xx.*xx).^3;
% Функція Рунге з випадковою добавкою 
x=-5:0.05:5;   y=1./(1+x.*x)+1e-4*randn(1,length(x));  % 
%sp=csapi(x,y);              % Кубічний інтерполяційний сплайн
%sp=csaps(x,y,0.999);    % Кубічний апроксимаційний сплайн
sp=spapi(4,x,y);               % Інтерполяційний сплайн 4-го степеня
sp1=fnder(sp);  sp2=fnder(sp1); % Перша і друга похідні сплайна
% Порівняльні графіки фукції Рунге та її сплайнів
%plot(xx,yy,'r', xx,fnval(xx,sp),'b');  pause; % 
%plot(xx,yy1,'r', xx,fnval(xx,sp1),'b');  pause;
plot(xx,yy2,'r', xx,fnval(xx,sp2),'b'); 
er=max(abs(yy2-fnval(xx,sp2)));  title(sprintf('er=%g',er));