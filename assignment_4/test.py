import matplotlib.pyplot as plt

original_wave_sample = [0, 3, 7, 14, 18, 24, 23, 29, 28, 30, 32, 35, 31, 34, 32, 30, 25, 25, 24, 23, 18, 14, 15, 14, 12, 12, 7, 8, 10, 9, 5, 8, 8, 8, 8, 5, 6, 4, 2, 2, 3, -1, -5, -4, -9, -9, -14, -16, -17, -18, -23, -24, -25, -25, -23, -20, -20, -16, -17, -11, -7, -7, 0, 3, 6, 8, 15, 18, 19, 24, 27, 24, 28, 25, 29, 27, 26, 22, 20, 16, 13, 13, 11, 7, 4, 0, 0, 0, 0, -3, -6, -6, -7, -6, -5, -7, -6, -6, -6, -6, -7, -9, -13, -11, -17, -16, -22, -24, -23, -27, -29, -30, -34, -33, -34, -37, -34, -32, -33, -28, -28, -23, -18, -13, -10, -8, 0, 3, 10, 12, 15, 22, 22, 27, 29, 31, 31, 29, 31, 27, 26, 27, 24, 20, 17, 17, 14, 11, 12, 8, 6, 5, 8, 6, 3, 6, 7, 4, 7, 6, 7, 6, 5, 4, 2, 0, -2, -3, -6, -7, -12, -14, -16, -15, -18, -21, -22, -23, -26, -26, -22, -23, -21, -18, -13, -9, -8, -3, -1, 6, 10, 12, 17, 20, 23, 25, 28, 30, 30, 30, 27, 25, 26, 24, 19, 18, 17, 12, 12, 8, 7, 4, 0, -2, -2, -1, -1, -6, -4, -4, -3, -5, -7, -8, -5, -5, -7, -10, -10, -12, -17, -17, -22, -21, -25, -29, -29, -32, -35, -34, -32, -33, -33, -33, -33, -28, -24, -22, -18, -15, -9, -6, 0, 6, 9, 11, 16, 22, 22, 24, 25, 29, 30, 31, 28, 29, 27, 22, 22, 20, 16, 17, 15, 14, 10, 10, 6, 8, 4, 4, 7, 4, 7, 7, 6, 6, 3, 7, 2, 2, 4, 1, 0, -2, -3, -7, -8, -13, -14, -16]

for i in range(len(original_wave_sample)):
	original_wave_sample[i]*=1000

def filter_wave(wave,times):
	new_wave = []
	for i in range(0,len(wave)):
		new_wave.insert(i,0) #insert the list with 0s so i can call its index later

	for y in range(0,times-1):
		if y == 0:
			print(f'entering initial loop')
			for i in range(0,len(new_wave)):
				if i == 0:
					print(f' i == {i}')
					new_wave[i] = 0 + wave[i] * 0.6 + wave[i+1] * 0.2
				elif i == len(new_wave)-1:
					print(f' i elif== {i}')

					new_wave[i] = wave[i-1] * 0.2 + wave[i] * 0.6 + 0
				else:
					print(f' i else == {i}')
					new_wave[i] = wave[i-1] * 0.2 + wave[i] * 0.6 + wave[i+1] * 0.2
		else:
			print(f'entering next loop')
			for i in range(0,len(new_wave)):
				if i == 0:
					new_wave[i] = 0 + new_wave[i] * 0.6 + new_wave[i+1] * 0.2
				elif i == len(new_wave)-1:
					new_wave[i] = new_wave[i] + new_wave[i-1] * 0.2 + new_wave[i] * 0.6 + 0
				else:
					new_wave[i] = new_wave[i] + new_wave[i-1] * 0.2 + new_wave[i] * 0.6 + new_wave[i+1] * 0.2
	return new_wave

# plt.plot(original_wave_sample)
# plt.show()

new_wave = filter_wave(original_wave_sample,200)
print(new_wave)
# plt.plot(new_wave)
# plt.show()