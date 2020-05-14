img = imread('X:/Dropbox/Desktop/qwe.jpg');
img = rgb2gray(img);
ent = entropy(img);
disp(ent);
figure, imshow(img);

imgDS2 = downsample(img, 2);
imgDS2 = imrotate(imgDS2, 90);
imgDS2 = downsample(imgDS2, 2);
imgDS2 = imrotate(imgDS2, -90);
figure, imshow(imgDS2);

imgDS4 = downsample(img, 4);
imgDS4 = imrotate(imgDS4, 90);
imgDS4 = downsample(imgDS4, 4);
imgDS4 = imrotate(imgDS4, -90);
figure, imshow(imgDS4);


imgQUANT8 = quantiz(img, [0, 32, 64, 96, 128, 160, 192, 224, 256]);
figure, imshow(imgQUANT8);


imgQUANT16 = quantiz(img, [0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 256]);
figure, imshow(imgQUANT16);

imgQUANT64 = quantiz(img, [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104 ,108, 112, 116, 120, 124, 128, 132, 136, 140, 144, 148, 152, 156, 160, 164, 168, 172, 176, 180, 184, 188, 192 ,196, 200, 204, 208, 212, 216, 220, 224, 228, 232, 236, 240, 244, 248, 252, 256]);
figure, imshow(imgQUANT64);

figure, imhist(imgQUANT8);
figure, imhist(imgQUANT16);
figure, imhist(imgQUANT64);

entDS2 = entropy(imgDS2);
entDS4 = entropy(imgDS4);

entQUANT8 = entropy(imgQUANT8);
entQUANT16 = entropy(imgQUANT16);
entQUANT64 = entropy(imgQUANT64);

disp([entDS2, entDS4]);
disp([entQUANT8, entQUANT16, entQUANT64]);


imgRE = imresize(img3, 2, 'bicubic');
figure, imshow(imgRE);


[height, width] = size(img);
imsize = height*width;
[p, x] = imhist(img);
p = p./imsize;
p = p(p>0);

[heightRE, widthRE] = size(imgRE);
imsizeRE = heightRE*widthRE;
[q, x] = imhist(imgRE);
q = q./imsizeRE;
q = q(p>0);

relativeEntRE=sum(p.*log(p./q))

[heightQUANT8, widthQUANT8] = size(imgQUANT8);
imsizeQUANT8 = heightQUANT8*widthQUANT8;
[q, x] = imhist(imgQUANT8);
q = q./imsizeQUANT8;
q = q(p>0);

relativeEntQUANT8=sum(p.*log(p./q))

[heightQUANT16, widthQUANT16] = size(imgQUANT16);
imsizeQUANT16 = heightQUANT16*widthQUANT16;
[q, x] = imhist(imgQUANT16);
q = q./imsizeQUANT16;
q = q(p>0);

relativeEntQUANT16=sum(p.*log(p./q))

[heightQUANT64, widthQUANT64] = size(imgQUANT64);
imsizeQUANT64 = heightQUANT64*widthQUANT64;
[q, x] = imhist(imgQUANT64);
q = q./imsizeQUANT64;
q = q(p>0);

relativeEntQUANT64=sum(p.*log(p./q))


disp(relativeEntRE);
disp([relativeEntQUANT8, relativeEntQUANT16, relativeEntQUANT64]);