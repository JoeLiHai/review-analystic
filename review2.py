
# 讀取檔案，把內容存成清單
def read_file(filename):
	data = []
	with open(filename, 'r') as f:
		for line in f:
			data.append(line)
	return data

# 印出長度小於某數的留言數量
def word_count_filter(data, amount):
	new = []
	for d in data:
		if len(d) < amount:
			new.append(d)
	print(f'一共有{len(new)}筆留言長度小於{amount}')

# 印出有某個字的留言數量
def key_word_filter(data, keyword):
	new = []
	for d in data:
		if keyword in d:
			new.append(d)
	print(f'一共有{len(new)}筆留言提到{keyword}')

# # list comprehension 清單快寫法
# good = [d for d in data if 'good' in d]         
# print(good)

# 把字和字數建立成字典，讓使用者查字數
def word_count(filename):
	datas = read_file(filename)
	dic = {}
	for data in datas:
		words = data.split()  # words is a list
		for word in words:
			if word in dic:     # word is a word
				dic[word] += 1
			else:
				dic[word] = 1

	while True:
		word = input('請輸入你要查詢的字： ')
		if word == 'q':
			break
		if word in dic:
			print(word, '出現的次數為', dic[word])
		else:
			print('這個字不在字典裡')





