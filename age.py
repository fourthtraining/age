#IF雙層架構
driving = input('請問你有沒開過車?')

#直接判斷輸入有或沒有，之後才會繼續問問題
#if driving != '有' and driving != '沒有':  
	#print('只能輸入 有/沒有')
	#raise SystemExit

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:    #如果大於18歲，印出以下字串
		print('你通過測驗了')
	else:            #如果沒有大於18歲，印出以下字串
		print('奇怪 你怎麼會有開過車')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了，怎麼還不去考')
	else:
		print('很好，再過幾年就可以考駕照了')
else:
	print('只能輸入 有/沒有')