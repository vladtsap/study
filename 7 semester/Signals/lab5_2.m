% Фільтрування шуму електрокардіограми швидким перетворенням Уолша-Адамара
clear;
x1 = dlmread('ekg512');           % Сигнал ЕКГ з файлу ekg512
x = repmat(x1,1,8);               % Сигнал ЕКГ 8 разів повторений
x = x + 0.0.*randn(1,length(x)); % Зашумлена ЕКГ
y = fwht(x);                      % Швидке перетворення Уолша-Адамара FWHT
%figure;                           % Графічне вікно
%subplot(2,1,1); plot(x);          % Графік ЕКГ у верхньому підвікні
%xlabel('Номер відліку'); ylabel('Амплітуда ЕКГ');
%title('Сигнал ЕКГ');  
%subplot(2,1,2); plot(abs(y));     % Графік FWHT у нижньому підвікні
%xlabel('Номер коефіцієнту'); ylabel('Величина коефіцієнту');
%title('Коефіцієнти FWHT');
N=500;                           % Номер вищої суттєвої складової спектру
y(N:length(x)) = 0;               % Видалення коефіціентів FWHT вище N 
xRec = ifwht(y);                  % Відновлення ЕКГ інверсним FWHT
figure;                           % Друге графічне вікно
plot(x);  hold on;                % Графік ЕКГ і його зберігання у вікні
plot(xRec,'r');                   % Накладання графіка IFWHT червоним
xlabel('Номер відліку'); ylabel('Амплітуда ЕКГ');
legend('Оригінальний сигнал ЕКГ','Реконструйований сигнал');