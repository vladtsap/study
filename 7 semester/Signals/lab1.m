clear;                                % Очищення робочої області
N=300;                            % Кількість дискретних відліків
t=[0:1/N:1];                      % Дискретизація часу
y=cos(2*pi*20*t);              % Цифровий моногармонічний сигнал 
ydft = fft(y);                    % Швидке дискретне перетворення Фур'є FFT
ydft = ydft(1:N/2+1);       % Відліки FFT на півосі позитивних частот 
spec=abs(ydft);                   % Відліки спектру
fs=N/2;                           % Верхнє значення частоти спектру в Гц
freq=0:fs/N*2:fs;                 % Відліки частоти в Гц
plot(freq,spec);                  % Графічне зображення спектру
title('Спектр моногармонічного сигналу');
xlabel('Частота (Hz)');  ylabel('Спектральні відліки');
