%% Clean everything
% Clear Command Window
clc

% Remove items from workspace, freeing up system memory
clear

% Close all figures
close all   

%% Math Variables

% Sampling Frequency Fs=1 MHz
Fs = 1e6;
Ts = 1/Fs;

% Frequency of the sine wave 100 kHz
Fc = 125e3;

% Normalized Frequency
F_N = Fc/Fs;

% Number of samples
len = 32;

% n variable
n = linspace(0, len-1, len);

% Sine wave
x = sin(2*pi*F_N*n);

% Discrete Time vector
t = n*Ts;   % seconds
t = t*1e6;  % scaling to obtain micro seconds

%% Figure
figure();

subplot(2,1,1)
plot(n, x, 's-')
title('Sine Wave')          % Title
xlabel('Samples')           % x Label
ylabel('Amplitude')         % y Label
legend('Sine Wave')         % Legend
grid on                     % Grid

subplot(2,1,2)
plot(t, x, 'x-')            % Function to perform the plot
xlabel('Time [\mus]')     % x Label
ylabel('Amplitude')         % y Label
legend('Sine Wave')         % Legend
grid on                     % Grid

