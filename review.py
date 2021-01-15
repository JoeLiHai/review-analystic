data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 ==0:
			print(len(data))
print('檔案讀取完成, 總共有', len(data), '筆資料')

print(data[0])

wc = {}  # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
print(len(wc))

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print('沒有這個字')










# sum = 0
# for i in range(0, len(data)):
# 	sum += len(data[i])
# print('留言的平均長度為: ', sum / len(data))


# sum_len = 0
# for d in data:
# 	sum_len += len(d)
# print('老師版留言的平均長度為', sum_len / len(data))

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('一共有', len(new), '筆留言長度小於100')

# # list comprehension 清單快寫法

# good = [d for d in data if 'good' in d]         
# print(good)

# bad = ['bad' in d for d in data] # 留言有提到bad才會是True
