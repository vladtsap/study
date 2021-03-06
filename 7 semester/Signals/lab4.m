clear;
x1 = dlmread('ekg512');           % Сигнал ЕКГ з файлу ekg512 
x = repmat(x1,1,8);               % Сигнал ЕКГ 8 разів повторений
%plot(x);
x = x + 0.0.*randn(1,length(x)); % Зашумлена ЕКГ
y = fft(x);                       % Швидке перетворення Фур'є FFT
% figure;                           % Графічне вікно
% subplot(2,1,1);  plot(x);          % Графік ЕКГ у верхньому підвікні
%xlabel('Номер відліку'); ylabel('Амплітуда ЕКГ');
%title('Сигнал ЕКГ');  
%subplot(2,1,2); plot(abs(y));     % Графік FFT у нижньому підвікні
%xlabel('Номер коефіцієнту'); ylabel('Величина коефіцієнту');
%title('Коефіцієнти амплітудного спектру ЕКГ');
N=200;                            % Номер вищої суттєвої складової спектру
y(N:length(x)-N) = 0;             % Видалення коефіціентів FFT вище N
xRec = real(ifft(y));             % Відновлення ЕКГ інверсним FFT
figure;                           % Друге графічне вікно
plot(x);  hold on;                % Графік ЕКГ і його зберігання у вікні
plot(xRec,'r');                   % Накладання графіка xRec червоним
xlabel('Номер відліку'); ylabel('Амплітуда ЕКГ');
legend('Оригінальний сигнал ЕКГ','Реконструйований сигнал');
