Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> csv.reader(C:\Users\Thiago.DESKTOP-13409IC\Desktop\Midicsv.csv)
SyntaxError: invalid syntax
>>> csv.reader(C\Users\Thiago.DESKTOP-13409IC\Desktop\Midicsv.csv)
SyntaxError: unexpected character after line continuation character
>>> csv.reader(C\Users\Thiago.DESKTOP-13409IC\Desktop\csv.csv)
SyntaxError: unexpected character after line continuation character
>>> csv.reader(C\Users\Thiago.DESKTOP-13409IC\Desktop\csv.csv
	   
SyntaxError: unexpected character after line continuation character
>>> csv.reader('C:\Users\Thiago.DESKTOP-13409IC\Desktop\csv.csv')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> csv.reader('C:\Users\Thiago.DESKTOP-13409IC\Desktop\csv.csv')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> csv.readeer('C:\Users\Thiago.DESKTOP-13409IC\Desktop\csv.csv')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> csv.reader()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    csv.reader()
NameError: name 'csv' is not defined
>>> 
>>> 
>>> import csv
>>> with open('C:\Users\Thiago.DESKTOP-13409IC\Desktop\Midicsv\csv.csv')
SyntaxError: invalid syntax
>>> with open('C:\Users\Thiago.DESKTOP-13409IC\Desktop\Midicsv\csv.csv') as f:
	reader = csv.reader(f, delimiter=',', quiting=csv.QUOTE_NONE)
	
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> with open9("C:\Users\Thiago.DESKTOP-13409IC\Desktop\Midicsv\csv.csv") as f:
	reader = csv.reader(f, delimiter=',', quiting=csv.QUOTE_NONE)
	
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> with open(r'C:\Users\Thiago.DESKTOP-13409IC\Desktop\Midicsv\csv.csv') as f:
	reader = csv.reader(f, delimiter=',', quiting=csv.QUOTE_NONE)
	fir row in reader:
		
SyntaxError: invalid syntax
>>> with open(r'C:\Users\Thiago.DESKTOP-13409IC\Desktop\Midicsv\csv.csv') as f:
	reader = csv.reader(f, delimiter=',', quiting=csv.QUOTE_NONE)
	for row in reader:
		print(row)

		
Traceback (most recent call last):
  File "<pyshell#20>", line 2, in <module>
    reader = csv.reader(f, delimiter=',', quiting=csv.QUOTE_NONE)
TypeError: 'quiting' is an invalid keyword argument for this function
>>> with open(r'C:\Users\Thiago.DESKTOP-13409IC\Desktop\Midicsv\csv.csv') as f:
	reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
	for row in reader:
		print(row)

		
['0', ' 0', ' Header', ' 1', ' 5', ' 1000']
['1', ' 0', ' Start_track']
['1', ' 0', ' Time_signature', ' 4', ' 2', ' 24', ' 8']
['1', ' 0', ' Key_signature', ' 2', ' "major"']
['1', ' 0', ' Tempo', ' 1000000']
['1', ' 0', ' Copyright_t', ' "Direitos autorais © "']
['1', ' 4000', ' Tempo', ' 1000000']
['1', ' 4000', ' Tempo', ' 750000']
['1', ' 4000', ' Time_signature', ' 3', ' 2', ' 24', ' 8']
['1', ' 7000', ' Tempo', ' 750000']
['1', ' 7000', ' Tempo', ' 428571']
['1', ' 7000', ' Time_signature', ' 2', ' 2', ' 24', ' 8']
['1', ' 9000', ' Tempo', ' 2400000']
['1', ' 11000', ' Tempo', ' 1000000']
['1', ' 13000', ' Tempo', ' 1000000']
['1', ' 13000', ' Time_signature', ' 4', ' 2', ' 24', ' 8']
['1', ' 13001', ' End_track']
['2', ' 0', ' Start_track']
['2', ' 0', ' Program_c', ' 0', ' 0']
['2', ' 0', ' Control_c', ' 0', ' 121', ' 0']
['2', ' 0', ' Control_c', ' 0', ' 64', ' 0']
['2', ' 0', ' Control_c', ' 0', ' 91', ' 48']
['2', ' 0', ' Control_c', ' 0', ' 10', ' 63']
['2', ' 0', ' Control_c', ' 0', ' 7', ' 100']
['2', ' 0', ' Note_on_c', ' 0', ' 73', ' 81']
['2', ' 0', ' Control_c', ' 0', ' 121', ' 0']
['2', ' 0', ' Control_c', ' 0', ' 64', ' 0']
['2', ' 0', ' Control_c', ' 0', ' 91', ' 48']
['2', ' 0', ' Control_c', ' 0', ' 10', ' 63']
['2', ' 0', ' Control_c', ' 0', ' 7', ' 100']
['2', ' 0', ' Title_t', ' "Piano"']
['2', ' 4000', ' Note_off_c', ' 0', ' 73', ' 0']
['2', ' 4000', ' Note_on_c', ' 0', ' 71', ' 81']
['2', ' 6000', ' Note_off_c', ' 0', ' 71', ' 0']
['2', ' 6000', ' Note_on_c', ' 0', ' 69', ' 76']
['2', ' 7000', ' Note_off_c', ' 0', ' 69', ' 0']
['2', ' 7000', ' Note_on_c', ' 0', ' 67', ' 84']
['2', ' 7500', ' Note_off_c', ' 0', ' 67', ' 0']
['2', ' 7500', ' Note_on_c', ' 0', ' 66', ' 77']
['2', ' 8500', ' Note_off_c', ' 0', ' 66', ' 0']
['2', ' 8500', ' Note_on_c', ' 0', ' 64', ' 73']
['2', ' 9000', ' Note_off_c', ' 0', ' 64', ' 0']
['2', ' 9000', ' Note_on_c', ' 0', ' 50', ' 81']
['2', ' 9500', ' Note_on_c', ' 0', ' 62', ' 75']
['2', ' 9750', ' Note_off_c', ' 0', ' 62', ' 0']
['2', ' 9750', ' Note_on_c', ' 0', ' 64', ' 77']
['2', ' 10000', ' Note_off_c', ' 0', ' 64', ' 0']
['2', ' 10000', ' Note_on_c', ' 0', ' 66', ' 78']
['2', ' 10500', ' Note_off_c', ' 0', ' 50', ' 0']
['2', ' 10500', ' Note_on_c', ' 0', ' 52', ' 76']
['2', ' 10750', ' Note_off_c', ' 0', ' 52', ' 0']
['2', ' 10750', ' Note_on_c', ' 0', ' 54', ' 77']
['2', ' 11000', ' Note_off_c', ' 0', ' 66', ' 0']
['2', ' 11000', ' Note_off_c', ' 0', ' 54', ' 0']
['2', ' 11000', ' Note_on_c', ' 0', ' 71', ' 81']
['2', ' 11000', ' Note_on_c', ' 0', ' 55', ' 82']
['2', ' 13000', ' Note_off_c', ' 0', ' 71', ' 0']
['2', ' 13000', ' Note_off_c', ' 0', ' 55', ' 0']
['2', ' 13000', ' Note_on_c', ' 0', ' 57', ' 81']
['2', ' 14000', ' Note_off_c', ' 0', ' 57', ' 0']
['2', ' 14000', ' Note_on_c', ' 0', ' 59', ' 77']
['2', ' 15000', ' Note_off_c', ' 0', ' 59', ' 0']
['2', ' 16000', ' Note_on_c', ' 0', ' 59', ' 76']
['2', ' 17000', ' Note_off_c', ' 0', ' 59', ' 0']
['2', ' 17000', ' Note_on_c', ' 0', ' 64', ' 82']
['2', ' 18000', ' Note_off_c', ' 0', ' 64', ' 0']
['2', ' 18000', ' Note_on_c', ' 0', ' 59', ' 75']
['2', ' 19000', ' Note_off_c', ' 0', ' 59', ' 0']
['2', ' 19000', ' Note_on_c', ' 0', ' 60', ' 79']
['2', ' 21000', ' Note_off_c', ' 0', ' 60', ' 0']
['2', ' 21001', ' End_track']
['3', ' 0', ' Start_track']
['3', ' 0', ' Program_c', ' 1', ' 0']
['3', ' 0', ' Control_c', ' 1', ' 121', ' 0']
['3', ' 0', ' Control_c', ' 1', ' 64', ' 0']
['3', ' 0', ' Control_c', ' 1', ' 91', ' 48']
['3', ' 0', ' Control_c', ' 1', ' 10', ' 63']
['3', ' 0', ' Control_c', ' 1', ' 7', ' 100']
['3', ' 0', ' Note_on_c', ' 1', ' 73', ' 81']
['3', ' 0', ' Control_c', ' 1', ' 121', ' 0']
['3', ' 0', ' Control_c', ' 1', ' 64', ' 0']
['3', ' 0', ' Control_c', ' 1', ' 91', ' 48']
['3', ' 0', ' Control_c', ' 1', ' 10', ' 63']
['3', ' 0', ' Control_c', ' 1', ' 7', ' 100']
['3', ' 0', ' Title_t', ' "Piano"']
['3', ' 4000', ' Note_off_c', ' 1', ' 73', ' 0']
['3', ' 4000', ' Note_on_c', ' 1', ' 71', ' 81']
['3', ' 6000', ' Note_off_c', ' 1', ' 71', ' 0']
['3', ' 6000', ' Note_on_c', ' 1', ' 69', ' 76']
['3', ' 7000', ' Note_off_c', ' 1', ' 69', ' 0']
['3', ' 7000', ' Note_on_c', ' 1', ' 67', ' 84']
['3', ' 7500', ' Note_off_c', ' 1', ' 67', ' 0']
['3', ' 7500', ' Note_on_c', ' 1', ' 66', ' 77']
['3', ' 8500', ' Note_off_c', ' 1', ' 66', ' 0']
['3', ' 8500', ' Note_on_c', ' 1', ' 64', ' 73']
['3', ' 9000', ' Note_off_c', ' 1', ' 64', ' 0']
['3', ' 9000', ' Note_on_c', ' 1', ' 50', ' 81']
['3', ' 9500', ' Note_on_c', ' 1', ' 62', ' 75']
['3', ' 9750', ' Note_off_c', ' 1', ' 62', ' 0']
['3', ' 9750', ' Note_on_c', ' 1', ' 64', ' 77']
['3', ' 10000', ' Note_off_c', ' 1', ' 64', ' 0']
['3', ' 10000', ' Note_on_c', ' 1', ' 66', ' 78']
['3', ' 10500', ' Note_off_c', ' 1', ' 50', ' 0']
['3', ' 10500', ' Note_on_c', ' 1', ' 52', ' 76']
['3', ' 10750', ' Note_off_c', ' 1', ' 52', ' 0']
['3', ' 10750', ' Note_on_c', ' 1', ' 54', ' 77']
['3', ' 11000', ' Note_off_c', ' 1', ' 66', ' 0']
['3', ' 11000', ' Note_off_c', ' 1', ' 54', ' 0']
['3', ' 11000', ' Note_on_c', ' 1', ' 71', ' 81']
['3', ' 11000', ' Note_on_c', ' 1', ' 55', ' 82']
['3', ' 13000', ' Note_off_c', ' 1', ' 71', ' 0']
['3', ' 13000', ' Note_off_c', ' 1', ' 55', ' 0']
['3', ' 13000', ' Note_on_c', ' 1', ' 57', ' 81']
['3', ' 14000', ' Note_off_c', ' 1', ' 57', ' 0']
['3', ' 14000', ' Note_on_c', ' 1', ' 59', ' 77']
['3', ' 15000', ' Note_off_c', ' 1', ' 59', ' 0']
['3', ' 16000', ' Note_on_c', ' 1', ' 59', ' 76']
['3', ' 17000', ' Note_off_c', ' 1', ' 59', ' 0']
['3', ' 17000', ' Note_on_c', ' 1', ' 64', ' 82']
['3', ' 18000', ' Note_off_c', ' 1', ' 64', ' 0']
['3', ' 18000', ' Note_on_c', ' 1', ' 59', ' 75']
['3', ' 19000', ' Note_off_c', ' 1', ' 59', ' 0']
['3', ' 19000', ' Note_on_c', ' 1', ' 60', ' 79']
['3', ' 21000', ' Note_off_c', ' 1', ' 60', ' 0']
['3', ' 21001', ' End_track']
['4', ' 0', ' Start_track']
['4', ' 0', ' Program_c', ' 2', ' 0']
['4', ' 0', ' Control_c', ' 2', ' 121', ' 0']
['4', ' 0', ' Control_c', ' 2', ' 64', ' 0']
['4', ' 0', ' Control_c', ' 2', ' 91', ' 48']
['4', ' 0', ' Control_c', ' 2', ' 10', ' 63']
['4', ' 0', ' Control_c', ' 2', ' 7', ' 100']
['4', ' 0', ' Note_on_c', ' 2', ' 73', ' 81']
['4', ' 0', ' Control_c', ' 2', ' 121', ' 0']
['4', ' 0', ' Control_c', ' 2', ' 64', ' 0']
['4', ' 0', ' Control_c', ' 2', ' 91', ' 48']
['4', ' 0', ' Control_c', ' 2', ' 10', ' 63']
['4', ' 0', ' Control_c', ' 2', ' 7', ' 100']
['4', ' 0', ' Title_t', ' "Piano"']
['4', ' 4000', ' Note_off_c', ' 2', ' 73', ' 0']
['4', ' 4000', ' Note_on_c', ' 2', ' 71', ' 81']
['4', ' 6000', ' Note_off_c', ' 2', ' 71', ' 0']
['4', ' 6000', ' Note_on_c', ' 2', ' 69', ' 76']
['4', ' 7000', ' Note_off_c', ' 2', ' 69', ' 0']
['4', ' 7000', ' Note_on_c', ' 2', ' 67', ' 84']
['4', ' 7500', ' Note_off_c', ' 2', ' 67', ' 0']
['4', ' 7500', ' Note_on_c', ' 2', ' 66', ' 77']
['4', ' 8500', ' Note_off_c', ' 2', ' 66', ' 0']
['4', ' 8500', ' Note_on_c', ' 2', ' 64', ' 73']
['4', ' 9000', ' Note_off_c', ' 2', ' 64', ' 0']
['4', ' 9000', ' Note_on_c', ' 2', ' 50', ' 81']
['4', ' 9500', ' Note_on_c', ' 2', ' 62', ' 75']
['4', ' 9750', ' Note_off_c', ' 2', ' 62', ' 0']
['4', ' 9750', ' Note_on_c', ' 2', ' 64', ' 77']
['4', ' 10000', ' Note_off_c', ' 2', ' 64', ' 0']
['4', ' 10000', ' Note_on_c', ' 2', ' 66', ' 78']
['4', ' 10500', ' Note_off_c', ' 2', ' 50', ' 0']
['4', ' 10500', ' Note_on_c', ' 2', ' 52', ' 76']
['4', ' 10750', ' Note_off_c', ' 2', ' 52', ' 0']
['4', ' 10750', ' Note_on_c', ' 2', ' 54', ' 77']
['4', ' 11000', ' Note_off_c', ' 2', ' 66', ' 0']
['4', ' 11000', ' Note_off_c', ' 2', ' 54', ' 0']
['4', ' 11000', ' Note_on_c', ' 2', ' 71', ' 81']
['4', ' 11000', ' Note_on_c', ' 2', ' 55', ' 82']
['4', ' 13000', ' Note_off_c', ' 2', ' 71', ' 0']
['4', ' 13000', ' Note_off_c', ' 2', ' 55', ' 0']
['4', ' 13000', ' Note_on_c', ' 2', ' 57', ' 81']
['4', ' 14000', ' Note_off_c', ' 2', ' 57', ' 0']
['4', ' 14000', ' Note_on_c', ' 2', ' 59', ' 77']
['4', ' 15000', ' Note_off_c', ' 2', ' 59', ' 0']
['4', ' 16000', ' Note_on_c', ' 2', ' 59', ' 76']
['4', ' 17000', ' Note_off_c', ' 2', ' 59', ' 0']
['4', ' 17000', ' Note_on_c', ' 2', ' 64', ' 82']
['4', ' 18000', ' Note_off_c', ' 2', ' 64', ' 0']
['4', ' 18000', ' Note_on_c', ' 2', ' 59', ' 75']
['4', ' 19000', ' Note_off_c', ' 2', ' 59', ' 0']
['4', ' 19000', ' Note_on_c', ' 2', ' 60', ' 79']
['4', ' 21000', ' Note_off_c', ' 2', ' 60', ' 0']
['4', ' 21001', ' End_track']
['5', ' 0', ' Start_track']
['5', ' 0', ' Program_c', ' 3', ' 0']
['5', ' 0', ' Control_c', ' 3', ' 121', ' 0']
['5', ' 0', ' Control_c', ' 3', ' 64', ' 0']
['5', ' 0', ' Control_c', ' 3', ' 91', ' 48']
['5', ' 0', ' Control_c', ' 3', ' 10', ' 63']
['5', ' 0', ' Control_c', ' 3', ' 7', ' 100']
['5', ' 0', ' Note_on_c', ' 3', ' 73', ' 81']
['5', ' 0', ' Control_c', ' 3', ' 121', ' 0']
['5', ' 0', ' Control_c', ' 3', ' 64', ' 0']
['5', ' 0', ' Control_c', ' 3', ' 91', ' 48']
['5', ' 0', ' Control_c', ' 3', ' 10', ' 63']
['5', ' 0', ' Control_c', ' 3', ' 7', ' 100']
['5', ' 0', ' Title_t', ' "Piano"']
['5', ' 4000', ' Note_off_c', ' 3', ' 73', ' 0']
['5', ' 4000', ' Note_on_c', ' 3', ' 71', ' 81']
['5', ' 6000', ' Note_off_c', ' 3', ' 71', ' 0']
['5', ' 6000', ' Note_on_c', ' 3', ' 69', ' 76']
['5', ' 7000', ' Note_off_c', ' 3', ' 69', ' 0']
['5', ' 7000', ' Note_on_c', ' 3', ' 67', ' 84']
['5', ' 7500', ' Note_off_c', ' 3', ' 67', ' 0']
['5', ' 7500', ' Note_on_c', ' 3', ' 66', ' 77']
['5', ' 8500', ' Note_off_c', ' 3', ' 66', ' 0']
['5', ' 8500', ' Note_on_c', ' 3', ' 64', ' 73']
['5', ' 9000', ' Note_off_c', ' 3', ' 64', ' 0']
['5', ' 9000', ' Note_on_c', ' 3', ' 50', ' 81']
['5', ' 9500', ' Note_on_c', ' 3', ' 62', ' 75']
['5', ' 9750', ' Note_off_c', ' 3', ' 62', ' 0']
['5', ' 9750', ' Note_on_c', ' 3', ' 64', ' 77']
['5', ' 10000', ' Note_off_c', ' 3', ' 64', ' 0']
['5', ' 10000', ' Note_on_c', ' 3', ' 66', ' 78']
['5', ' 10500', ' Note_off_c', ' 3', ' 50', ' 0']
['5', ' 10500', ' Note_on_c', ' 3', ' 52', ' 76']
['5', ' 10750', ' Note_off_c', ' 3', ' 52', ' 0']
['5', ' 10750', ' Note_on_c', ' 3', ' 54', ' 77']
['5', ' 11000', ' Note_off_c', ' 3', ' 66', ' 0']
['5', ' 11000', ' Note_off_c', ' 3', ' 54', ' 0']
['5', ' 11000', ' Note_on_c', ' 3', ' 71', ' 81']
['5', ' 11000', ' Note_on_c', ' 3', ' 55', ' 82']
['5', ' 13000', ' Note_off_c', ' 3', ' 71', ' 0']
['5', ' 13000', ' Note_off_c', ' 3', ' 55', ' 0']
['5', ' 13000', ' Note_on_c', ' 3', ' 57', ' 81']
['5', ' 14000', ' Note_off_c', ' 3', ' 57', ' 0']
['5', ' 14000', ' Note_on_c', ' 3', ' 59', ' 77']
['5', ' 15000', ' Note_off_c', ' 3', ' 59', ' 0']
['5', ' 16000', ' Note_on_c', ' 3', ' 59', ' 76']
['5', ' 17000', ' Note_off_c', ' 3', ' 59', ' 0']
['5', ' 17000', ' Note_on_c', ' 3', ' 64', ' 82']
['5', ' 18000', ' Note_off_c', ' 3', ' 64', ' 0']
['5', ' 18000', ' Note_on_c', ' 3', ' 59', ' 75']
['5', ' 19000', ' Note_off_c', ' 3', ' 59', ' 0']
['5', ' 19000', ' Note_on_c', ' 3', ' 60', ' 79']
['5', ' 21000', ' Note_off_c', ' 3', ' 60', ' 0']
['5', ' 21001', ' End_track']
['0', ' 0', ' End_of_file']
>>> import csv
>>> with open(r'C:\Users\Thiago.DESKTOP-13409IC\Desktop\Midicsv\csv.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		print(row)

		
['0', ' 0', ' Header', ' 1', ' 5', ' 1000']
['1', ' 0', ' Start_track']
['1', ' 0', ' Time_signature', ' 4', ' 2', ' 24', ' 8']
['1', ' 0', ' Key_signature', ' 2', ' "major"']
['1', ' 0', ' Tempo', ' 1000000']
['1', ' 0', ' Copyright_t', ' "Direitos autorais © "']
['1', ' 4000', ' Tempo', ' 1000000']
['1', ' 4000', ' Tempo', ' 750000']
['1', ' 4000', ' Time_signature', ' 3', ' 2', ' 24', ' 8']
['1', ' 7000', ' Tempo', ' 750000']
['1', ' 7000', ' Tempo', ' 428571']
['1', ' 7000', ' Time_signature', ' 2', ' 2', ' 24', ' 8']
['1', ' 9000', ' Tempo', ' 2400000']
['1', ' 11000', ' Tempo', ' 1000000']
['1', ' 13000', ' Tempo', ' 1000000']
['1', ' 13000', ' Time_signature', ' 4', ' 2', ' 24', ' 8']
['1', ' 13001', ' End_track']
['2', ' 0', ' Start_track']
['2', ' 0', ' Program_c', ' 0', ' 0']
['2', ' 0', ' Control_c', ' 0', ' 121', ' 0']
['2', ' 0', ' Control_c', ' 0', ' 64', ' 0']
['2', ' 0', ' Control_c', ' 0', ' 91', ' 48']
['2', ' 0', ' Control_c', ' 0', ' 10', ' 63']
['2', ' 0', ' Control_c', ' 0', ' 7', ' 100']
['2', ' 0', ' Note_on_c', ' 0', ' 73', ' 81']
['2', ' 0', ' Control_c', ' 0', ' 121', ' 0']
['2', ' 0', ' Control_c', ' 0', ' 64', ' 0']
['2', ' 0', ' Control_c', ' 0', ' 91', ' 48']
['2', ' 0', ' Control_c', ' 0', ' 10', ' 63']
['2', ' 0', ' Control_c', ' 0', ' 7', ' 100']
['2', ' 0', ' Title_t', ' "Piano"']
['2', ' 4000', ' Note_off_c', ' 0', ' 73', ' 0']
['2', ' 4000', ' Note_on_c', ' 0', ' 71', ' 81']
['2', ' 6000', ' Note_off_c', ' 0', ' 71', ' 0']
['2', ' 6000', ' Note_on_c', ' 0', ' 69', ' 76']
['2', ' 7000', ' Note_off_c', ' 0', ' 69', ' 0']
['2', ' 7000', ' Note_on_c', ' 0', ' 67', ' 84']
['2', ' 7500', ' Note_off_c', ' 0', ' 67', ' 0']
['2', ' 7500', ' Note_on_c', ' 0', ' 66', ' 77']
['2', ' 8500', ' Note_off_c', ' 0', ' 66', ' 0']
['2', ' 8500', ' Note_on_c', ' 0', ' 64', ' 73']
['2', ' 9000', ' Note_off_c', ' 0', ' 64', ' 0']
['2', ' 9000', ' Note_on_c', ' 0', ' 50', ' 81']
['2', ' 9500', ' Note_on_c', ' 0', ' 62', ' 75']
['2', ' 9750', ' Note_off_c', ' 0', ' 62', ' 0']
['2', ' 9750', ' Note_on_c', ' 0', ' 64', ' 77']
['2', ' 10000', ' Note_off_c', ' 0', ' 64', ' 0']
['2', ' 10000', ' Note_on_c', ' 0', ' 66', ' 78']
['2', ' 10500', ' Note_off_c', ' 0', ' 50', ' 0']
['2', ' 10500', ' Note_on_c', ' 0', ' 52', ' 76']
['2', ' 10750', ' Note_off_c', ' 0', ' 52', ' 0']
['2', ' 10750', ' Note_on_c', ' 0', ' 54', ' 77']
['2', ' 11000', ' Note_off_c', ' 0', ' 66', ' 0']
['2', ' 11000', ' Note_off_c', ' 0', ' 54', ' 0']
['2', ' 11000', ' Note_on_c', ' 0', ' 71', ' 81']
['2', ' 11000', ' Note_on_c', ' 0', ' 55', ' 82']
['2', ' 13000', ' Note_off_c', ' 0', ' 71', ' 0']
['2', ' 13000', ' Note_off_c', ' 0', ' 55', ' 0']
['2', ' 13000', ' Note_on_c', ' 0', ' 57', ' 81']
['2', ' 14000', ' Note_off_c', ' 0', ' 57', ' 0']
['2', ' 14000', ' Note_on_c', ' 0', ' 59', ' 77']
['2', ' 15000', ' Note_off_c', ' 0', ' 59', ' 0']
['2', ' 16000', ' Note_on_c', ' 0', ' 59', ' 76']
['2', ' 17000', ' Note_off_c', ' 0', ' 59', ' 0']
['2', ' 17000', ' Note_on_c', ' 0', ' 64', ' 82']
['2', ' 18000', ' Note_off_c', ' 0', ' 64', ' 0']
['2', ' 18000', ' Note_on_c', ' 0', ' 59', ' 75']
['2', ' 19000', ' Note_off_c', ' 0', ' 59', ' 0']
['2', ' 19000', ' Note_on_c', ' 0', ' 60', ' 79']
['2', ' 21000', ' Note_off_c', ' 0', ' 60', ' 0']
['2', ' 21001', ' End_track']
['3', ' 0', ' Start_track']
['3', ' 0', ' Program_c', ' 1', ' 0']
['3', ' 0', ' Control_c', ' 1', ' 121', ' 0']
['3', ' 0', ' Control_c', ' 1', ' 64', ' 0']
['3', ' 0', ' Control_c', ' 1', ' 91', ' 48']
['3', ' 0', ' Control_c', ' 1', ' 10', ' 63']
['3', ' 0', ' Control_c', ' 1', ' 7', ' 100']
['3', ' 0', ' Note_on_c', ' 1', ' 73', ' 81']
['3', ' 0', ' Control_c', ' 1', ' 121', ' 0']
['3', ' 0', ' Control_c', ' 1', ' 64', ' 0']
['3', ' 0', ' Control_c', ' 1', ' 91', ' 48']
['3', ' 0', ' Control_c', ' 1', ' 10', ' 63']
['3', ' 0', ' Control_c', ' 1', ' 7', ' 100']
['3', ' 0', ' Title_t', ' "Piano"']
['3', ' 4000', ' Note_off_c', ' 1', ' 73', ' 0']
['3', ' 4000', ' Note_on_c', ' 1', ' 71', ' 81']
['3', ' 6000', ' Note_off_c', ' 1', ' 71', ' 0']
['3', ' 6000', ' Note_on_c', ' 1', ' 69', ' 76']
['3', ' 7000', ' Note_off_c', ' 1', ' 69', ' 0']
['3', ' 7000', ' Note_on_c', ' 1', ' 67', ' 84']
['3', ' 7500', ' Note_off_c', ' 1', ' 67', ' 0']
['3', ' 7500', ' Note_on_c', ' 1', ' 66', ' 77']
['3', ' 8500', ' Note_off_c', ' 1', ' 66', ' 0']
['3', ' 8500', ' Note_on_c', ' 1', ' 64', ' 73']
['3', ' 9000', ' Note_off_c', ' 1', ' 64', ' 0']
['3', ' 9000', ' Note_on_c', ' 1', ' 50', ' 81']
['3', ' 9500', ' Note_on_c', ' 1', ' 62', ' 75']
['3', ' 9750', ' Note_off_c', ' 1', ' 62', ' 0']
['3', ' 9750', ' Note_on_c', ' 1', ' 64', ' 77']
['3', ' 10000', ' Note_off_c', ' 1', ' 64', ' 0']
['3', ' 10000', ' Note_on_c', ' 1', ' 66', ' 78']
['3', ' 10500', ' Note_off_c', ' 1', ' 50', ' 0']
['3', ' 10500', ' Note_on_c', ' 1', ' 52', ' 76']
['3', ' 10750', ' Note_off_c', ' 1', ' 52', ' 0']
['3', ' 10750', ' Note_on_c', ' 1', ' 54', ' 77']
['3', ' 11000', ' Note_off_c', ' 1', ' 66', ' 0']
['3', ' 11000', ' Note_off_c', ' 1', ' 54', ' 0']
['3', ' 11000', ' Note_on_c', ' 1', ' 71', ' 81']
['3', ' 11000', ' Note_on_c', ' 1', ' 55', ' 82']
['3', ' 13000', ' Note_off_c', ' 1', ' 71', ' 0']
['3', ' 13000', ' Note_off_c', ' 1', ' 55', ' 0']
['3', ' 13000', ' Note_on_c', ' 1', ' 57', ' 81']
['3', ' 14000', ' Note_off_c', ' 1', ' 57', ' 0']
['3', ' 14000', ' Note_on_c', ' 1', ' 59', ' 77']
['3', ' 15000', ' Note_off_c', ' 1', ' 59', ' 0']
['3', ' 16000', ' Note_on_c', ' 1', ' 59', ' 76']
['3', ' 17000', ' Note_off_c', ' 1', ' 59', ' 0']
['3', ' 17000', ' Note_on_c', ' 1', ' 64', ' 82']
['3', ' 18000', ' Note_off_c', ' 1', ' 64', ' 0']
['3', ' 18000', ' Note_on_c', ' 1', ' 59', ' 75']
['3', ' 19000', ' Note_off_c', ' 1', ' 59', ' 0']
['3', ' 19000', ' Note_on_c', ' 1', ' 60', ' 79']
['3', ' 21000', ' Note_off_c', ' 1', ' 60', ' 0']
['3', ' 21001', ' End_track']
['4', ' 0', ' Start_track']
['4', ' 0', ' Program_c', ' 2', ' 0']
['4', ' 0', ' Control_c', ' 2', ' 121', ' 0']
['4', ' 0', ' Control_c', ' 2', ' 64', ' 0']
['4', ' 0', ' Control_c', ' 2', ' 91', ' 48']
['4', ' 0', ' Control_c', ' 2', ' 10', ' 63']
['4', ' 0', ' Control_c', ' 2', ' 7', ' 100']
['4', ' 0', ' Note_on_c', ' 2', ' 73', ' 81']
['4', ' 0', ' Control_c', ' 2', ' 121', ' 0']
['4', ' 0', ' Control_c', ' 2', ' 64', ' 0']
['4', ' 0', ' Control_c', ' 2', ' 91', ' 48']
['4', ' 0', ' Control_c', ' 2', ' 10', ' 63']
['4', ' 0', ' Control_c', ' 2', ' 7', ' 100']
['4', ' 0', ' Title_t', ' "Piano"']
['4', ' 4000', ' Note_off_c', ' 2', ' 73', ' 0']
['4', ' 4000', ' Note_on_c', ' 2', ' 71', ' 81']
['4', ' 6000', ' Note_off_c', ' 2', ' 71', ' 0']
['4', ' 6000', ' Note_on_c', ' 2', ' 69', ' 76']
['4', ' 7000', ' Note_off_c', ' 2', ' 69', ' 0']
['4', ' 7000', ' Note_on_c', ' 2', ' 67', ' 84']
['4', ' 7500', ' Note_off_c', ' 2', ' 67', ' 0']
['4', ' 7500', ' Note_on_c', ' 2', ' 66', ' 77']
['4', ' 8500', ' Note_off_c', ' 2', ' 66', ' 0']
['4', ' 8500', ' Note_on_c', ' 2', ' 64', ' 73']
['4', ' 9000', ' Note_off_c', ' 2', ' 64', ' 0']
['4', ' 9000', ' Note_on_c', ' 2', ' 50', ' 81']
['4', ' 9500', ' Note_on_c', ' 2', ' 62', ' 75']
['4', ' 9750', ' Note_off_c', ' 2', ' 62', ' 0']
['4', ' 9750', ' Note_on_c', ' 2', ' 64', ' 77']
['4', ' 10000', ' Note_off_c', ' 2', ' 64', ' 0']
['4', ' 10000', ' Note_on_c', ' 2', ' 66', ' 78']
['4', ' 10500', ' Note_off_c', ' 2', ' 50', ' 0']
['4', ' 10500', ' Note_on_c', ' 2', ' 52', ' 76']
['4', ' 10750', ' Note_off_c', ' 2', ' 52', ' 0']
['4', ' 10750', ' Note_on_c', ' 2', ' 54', ' 77']
['4', ' 11000', ' Note_off_c', ' 2', ' 66', ' 0']
['4', ' 11000', ' Note_off_c', ' 2', ' 54', ' 0']
['4', ' 11000', ' Note_on_c', ' 2', ' 71', ' 81']
['4', ' 11000', ' Note_on_c', ' 2', ' 55', ' 82']
['4', ' 13000', ' Note_off_c', ' 2', ' 71', ' 0']
['4', ' 13000', ' Note_off_c', ' 2', ' 55', ' 0']
['4', ' 13000', ' Note_on_c', ' 2', ' 57', ' 81']
['4', ' 14000', ' Note_off_c', ' 2', ' 57', ' 0']
['4', ' 14000', ' Note_on_c', ' 2', ' 59', ' 77']
['4', ' 15000', ' Note_off_c', ' 2', ' 59', ' 0']
['4', ' 16000', ' Note_on_c', ' 2', ' 59', ' 76']
['4', ' 17000', ' Note_off_c', ' 2', ' 59', ' 0']
['4', ' 17000', ' Note_on_c', ' 2', ' 64', ' 82']
['4', ' 18000', ' Note_off_c', ' 2', ' 64', ' 0']
['4', ' 18000', ' Note_on_c', ' 2', ' 59', ' 75']
['4', ' 19000', ' Note_off_c', ' 2', ' 59', ' 0']
['4', ' 19000', ' Note_on_c', ' 2', ' 60', ' 79']
['4', ' 21000', ' Note_off_c', ' 2', ' 60', ' 0']
['4', ' 21001', ' End_track']
['5', ' 0', ' Start_track']
['5', ' 0', ' Program_c', ' 3', ' 0']
['5', ' 0', ' Control_c', ' 3', ' 121', ' 0']
['5', ' 0', ' Control_c', ' 3', ' 64', ' 0']
['5', ' 0', ' Control_c', ' 3', ' 91', ' 48']
['5', ' 0', ' Control_c', ' 3', ' 10', ' 63']
['5', ' 0', ' Control_c', ' 3', ' 7', ' 100']
['5', ' 0', ' Note_on_c', ' 3', ' 73', ' 81']
['5', ' 0', ' Control_c', ' 3', ' 121', ' 0']
['5', ' 0', ' Control_c', ' 3', ' 64', ' 0']
['5', ' 0', ' Control_c', ' 3', ' 91', ' 48']
['5', ' 0', ' Control_c', ' 3', ' 10', ' 63']
['5', ' 0', ' Control_c', ' 3', ' 7', ' 100']
['5', ' 0', ' Title_t', ' "Piano"']
['5', ' 4000', ' Note_off_c', ' 3', ' 73', ' 0']
['5', ' 4000', ' Note_on_c', ' 3', ' 71', ' 81']
['5', ' 6000', ' Note_off_c', ' 3', ' 71', ' 0']
['5', ' 6000', ' Note_on_c', ' 3', ' 69', ' 76']
['5', ' 7000', ' Note_off_c', ' 3', ' 69', ' 0']
['5', ' 7000', ' Note_on_c', ' 3', ' 67', ' 84']
['5', ' 7500', ' Note_off_c', ' 3', ' 67', ' 0']
['5', ' 7500', ' Note_on_c', ' 3', ' 66', ' 77']
['5', ' 8500', ' Note_off_c', ' 3', ' 66', ' 0']
['5', ' 8500', ' Note_on_c', ' 3', ' 64', ' 73']
['5', ' 9000', ' Note_off_c', ' 3', ' 64', ' 0']
['5', ' 9000', ' Note_on_c', ' 3', ' 50', ' 81']
['5', ' 9500', ' Note_on_c', ' 3', ' 62', ' 75']
['5', ' 9750', ' Note_off_c', ' 3', ' 62', ' 0']
['5', ' 9750', ' Note_on_c', ' 3', ' 64', ' 77']
['5', ' 10000', ' Note_off_c', ' 3', ' 64', ' 0']
['5', ' 10000', ' Note_on_c', ' 3', ' 66', ' 78']
['5', ' 10500', ' Note_off_c', ' 3', ' 50', ' 0']
['5', ' 10500', ' Note_on_c', ' 3', ' 52', ' 76']
['5', ' 10750', ' Note_off_c', ' 3', ' 52', ' 0']
['5', ' 10750', ' Note_on_c', ' 3', ' 54', ' 77']
['5', ' 11000', ' Note_off_c', ' 3', ' 66', ' 0']
['5', ' 11000', ' Note_off_c', ' 3', ' 54', ' 0']
['5', ' 11000', ' Note_on_c', ' 3', ' 71', ' 81']
['5', ' 11000', ' Note_on_c', ' 3', ' 55', ' 82']
['5', ' 13000', ' Note_off_c', ' 3', ' 71', ' 0']
['5', ' 13000', ' Note_off_c', ' 3', ' 55', ' 0']
['5', ' 13000', ' Note_on_c', ' 3', ' 57', ' 81']
['5', ' 14000', ' Note_off_c', ' 3', ' 57', ' 0']
['5', ' 14000', ' Note_on_c', ' 3', ' 59', ' 77']
['5', ' 15000', ' Note_off_c', ' 3', ' 59', ' 0']
['5', ' 16000', ' Note_on_c', ' 3', ' 59', ' 76']
['5', ' 17000', ' Note_off_c', ' 3', ' 59', ' 0']
['5', ' 17000', ' Note_on_c', ' 3', ' 64', ' 82']
['5', ' 18000', ' Note_off_c', ' 3', ' 64', ' 0']
['5', ' 18000', ' Note_on_c', ' 3', ' 59', ' 75']
['5', ' 19000', ' Note_off_c', ' 3', ' 59', ' 0']
['5', ' 19000', ' Note_on_c', ' 3', ' 60', ' 79']
['5', ' 21000', ' Note_off_c', ' 3', ' 60', ' 0']
['5', ' 21001', ' End_track']
['0', ' 0', ' End_of_file']
>>> import csv
>>> with open(r'C:\Users\Thiago.DESKTOP-13409IC\Desktop\Midicsv\csv.csv') as f:
	reader = csv.reader(f)
	for row in reader(['note_on_c']):
		print(row)

		
Traceback (most recent call last):
  File "<pyshell#31>", line 3, in <module>
    for row in reader(['note_on_c']):
TypeError: '_csv.reader' object is not callable
>>> with open(r'C:\Users\Thiago.DESKTOP-13409IC\Desktop\Midicsv\csv.csv') as f:
	reader = csv.reader(f)
	for row in csv.reader(['note_on_c']):
		print(row)

		
['note_on_c']
>>> #comment
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
	print(w, len(w))

	
cat 3
window 6
defenestrate 12
>>> for w in words[:]:
	if len(w) > 6:
		words.insert(0, w)

		
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
>>> for w in words:
	if len(w) > 6:
		words.insert(0, w)

		
Traceback (most recent call last):
  File "<pyshell#45>", line 3, in <module>
    words.insert(0, w)
KeyboardInterrupt
>>> for w in words[:]:
	if len(w) <= 6:
		words.insert(0, w)

		
>>> for w in words[:]:
	if len(w) > 6:
		words.insert(0, w)

		
Traceback (most recent call last):
  File "<pyshell#49>", line 3, in <module>
    words.insert(0, w)
KeyboardInterrupt
>>> for w in words[:]:
	if len(w) > 6:
		words.insert(0, w)

		
Traceback (most recent call last):
  File "<pyshell#51>", line 3, in <module>
    words.insert(0, w)
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> words = ['cat', 'window', 'defenestrate']
>>> 
>>> for w in words[:]:
	if len(w) > 6:
		words.insert(0, w)

		
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
>>> for w in words[:]:
	if len(w) <= 6:
		words.insert(0, w)

		
>>> words
['window', 'cat', 'defenestrate', 'cat', 'window', 'defenestrate']
>>> words
['window', 'cat', 'defenestrate', 'cat', 'window', 'defenestrate']
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words[:]:
	if len(w) <= 6:
		words.insert(0, w)

		
>>> words
['window', 'cat', 'cat', 'window', 'defenestrate']
>>> num = [1,2,3,4,5,6,7,8,9,10,11,12]
>>> for x in num[0::2]
SyntaxError: invalid syntax
>>> for x in num[0::2]:
	print(x)

	
1
3
5
7
9
11
>>> list = [1,2,3,4,5]
>>> lista = [1,2,3,4,5]
>>> lista.insert(2, 'terceira')
>>> lista
[1, 2, 'terceira', 3, 4, 5]
>>> lista.inser(0, 'primeira')
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    lista.inser(0, 'primeira')
AttributeError: 'list' object has no attribute 'inser'
>>> lista.insert(0, 'primeira')
>>> 
>>> lista
['primeira', 1, 2, 'terceira', 3, 4, 5]
>>> lista.insert(len(lista), 'última')
>>> lista
['primeira', 1, 2, 'terceira', 3, 4, 5, 'última']
>>> lista.insert(len(lista)-1, 'penúltima')
>>> lista
['primeira', 1, 2, 'terceira', 3, 4, 5, 'penúltima', 'última']
>>> lista.remove(2)
>>> lista
['primeira', 1, 'terceira', 3, 4, 5, 'penúltima', 'última']
>>>  words = ['cat', 'window', 'defenestrate']
 
SyntaxError: unexpected indent
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words[:]:
	if len(w) > 6:
		words.insert(0, w)

		
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
>>> x =15
i
>>> id(x)
140734305694400
>>> y = x
>>> x
15
>>> y
15
>>> id(y)
140734305694400
>>> id(words)
2265061967624
>>> a = 1
>>> b = 1
>>> id(a)
140734305693952
>>> id(b)
140734305693952
>>> a
1
>>> b
1
>>> type(a)
<class 'int'>
>>> asdf = None
>>> type(asdf)
<class 'NoneType'>
>>> asdf is True
False
>>> ...
Ellipsis
>>> a
1
>>> 
>>> b
1
>>> c
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> type(range)
<class 'type'>
>>> lista
['primeira', 1, 'terceira', 3, 4, 5, 'penúltima', 'última']
>>> type(insert)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    type(insert)
NameError: name 'insert' is not defined
>>> type(list)
<class 'list'>
>>> x = ["
     
SyntaxError: EOL while scanning string literal
>>> x = ['a','b','c','d','e','f','g','h','i','j']
>>> for posicaopar in range(0,len(x),2)
SyntaxError: invalid syntax
>>> for posicaopar in range(0,len(x),2):
	print x
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> for posicaopar in range(0,len(x),2):
	print(x)

	
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
>>> for posicaopar in range(0,len(x),2):
	print(x[posicaopar])

	
a
c
e
g
i
>>> enumerate(x)
<enumerate object at 0x0000020F60365638>
>>> list(enumerate(x))
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    list(enumerate(x))
TypeError: 'list' object is not callable
>>> y = []
>>> y(enumerate(x))
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    y(enumerate(x))
TypeError: 'list' object is not callable
>>> y(enumerate(x))
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    y(enumerate(x))
TypeError: 'list' object is not callable
>>> u = 1.23432
>>> type(u)
<class 'float'>
>>> asdf = {}
>>> type(asdf)
<class 'dict'>
>>> intervalos = ['1','2','3','4','5']
>>> durações = ['6','7','8','9','10']
>>> for posição in zip(Intervalos, Durações)
SyntaxError: invalid syntax
>>> 
>>> listanota = [73, 71, 69, 67, 66, 64]
>>> for posição in range(len(listana)):
	if posição <= len(listanote)-2:
		listaintervalo.append(listanota[posicao+1] - listana[posição])

		
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    for posição in range(len(listana)):
NameError: name 'listana' is not defined
>>> listaintervalo = []
>>> for posição in range(len(listana)):
	if posição <= len(listanote)-2:
		listaintervalo.append(listanota[posicao+1] - listana[posição])

		
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    for posição in range(len(listana)):
NameError: name 'listana' is not defined
>>> for posição in range(len(listanota)):
	if posição <= len(listanota)-2:
		listaintervalo.append(listanota[posicao+1] - listanota[posição])

		
Traceback (most recent call last):
  File "<pyshell#147>", line 3, in <module>
    listaintervalo.append(listanota[posicao+1] - listanota[posição])
NameError: name 'posicao' is not defined
>>> for posição in range(len(listanota)):
	if posição <= len(listanota)-2:
		listaintervalo.append(listanota[posição+1] - listanota[posição])

		
>>> 
>>> listaintervalo
[-2, -2, -2, -1, -2]
>>> listalocalizacao = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4]]
>>> for posicao1 in range(len(listaintervalo):
		      
SyntaxError: invalid syntax
>>> for posicao1 in range(len(listaintervalo)):
	for posicao2 in range(posicao1, len(listaintervalo)):
		print(listalocalizacao[posicao1], (posicao2+1) - posicao1, listaintervalo[posicao1:posicao2+1])

		
[1, 1] 1 [-2]
[1, 1] 2 [-2, -2]
[1, 1] 3 [-2, -2, -2]
[1, 1] 4 [-2, -2, -2, -1]
[1, 1] 5 [-2, -2, -2, -1, -2]
[1, 2] 1 [-2]
[1, 2] 2 [-2, -2]
[1, 2] 3 [-2, -2, -1]
[1, 2] 4 [-2, -2, -1, -2]
[1, 3] 1 [-2]
[1, 3] 2 [-2, -1]
[1, 3] 3 [-2, -1, -2]
[1, 4] 1 [-1]
[1, 4] 2 [-1, -2]
[2, 1] 1 [-2]
>>> "afa aewawe"
'afa aewawe'
>>> #caecasecasec
>>> #wdeqwed
>>> #deww
>>> intervalos = ['1','2','3','4','5']
>>> durações = ['6','7','8','9','10']
>>> for q, a in zip(Intervalos, Durações):
	print(q, a,))
	
SyntaxError: invalid syntax
>>> for q, a in zip(Intervalos, Durações):
	print(q, a)

	
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    for q, a in zip(Intervalos, Durações):
NameError: name 'Intervalos' is not defined
>>> for q, a in zip(intervalos, durações):
	print(q, a)

	
1 6
2 7
3 8
4 9
5 10
>>> teste = {1:1,2:2,3:3}
>>> typr
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    typr
NameError: name 'typr' is not defined
>>> type(teste))
SyntaxError: invalid syntax
>>> type(teste)
<class 'dict'>
>>> 
