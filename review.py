data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 ==0:
			print(len(data))
print('檔案讀取完成, 總共有', len(data), '筆資料')

sum = 0
for i in range(0, len(data)):
	sum += len(data[i])
print('留言的平均長度為: ', sum / len(data))


sum_len = 0
for d in data:
	sum_len += len(d)
print('老師版留言的平均長度為', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')

# list comprehension 清單快寫法

good = [d for d in data if 'good' in d]         
print(good)

bad = ['bad' in d for d in data]
# 留言有提到bad才會是True
