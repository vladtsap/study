% Порівняльне дослідження неперервного вейвлет-перетворення і 
% віконного (короткого) Фур'є-перетворення 

dt=0.001;  t=0:dt:1-dt;  % Вектор часових відліків
% Сигнал для дослідження
x = cos(2*pi*150*t).*(t>=0.1 & t<0.3)+sin(2*pi*200*t).*(t>0.7);
x = x + 0.04*randn(size(t));  % Додавання шуму
x([222 800]) = x([222 800 ])+[-2 2];  % Додавання збурення

 figure;  plot(t.*1000,x);  % Графік сигналу
xlabel('Мілісекунди'); ylabel('Амплітуда');
figure;  % Графіки фрагментів сигналу зі збуренням
subplot(2,1,1); plot(t(184:264).*1000, x(184:264));
ylabel('Амплітуда'); title('Збурення'); axis tight;
subplot(2,1,2); plot(t(760:840).*1000, x(760:840));
ylabel('Амплітуда'); xlabel('Мілісекунди'); axis tight;

figure;  % Вейвлет-перетворення CWT і його графічне зображення
scales = helperCWTTimeFreqVector(1, 500, 6/(2*pi), 0.001, 32);
cwty = cwtft({x,dt},'wavelet','morl','scales',scales,'padmode','symw');
helperCWTTimeFreqPlot(cwty.cfs,t.*1e3,cwty.frequencies,...
    'contour','Вейвлет-розклад Морле','Мілісекунди','Гц');

figure;  % Віконне Фур'є-перетворення SFT і його графічне зображення
[S,F,T] = spectrogram(x, 75, 40, 128, 1000);
surf(T.*1000, F, 20*log10(abs(S)), 'edgecolor', 'none');  view(0,90);
axis tight;  shading interp;  colorbar;
xlabel('Мілісекунди'), ylabel('Гц'); title('Віконне Фур’є-перетворення')
