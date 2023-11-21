


def max_profit(prices):

	min_buy = float('inf')
	max_buy = 0 

	for price in prices:
		min_buy = min(price, min_buy) 


		max_buy = max(max_buy, price - min_buy)
	

	return max_buy 




prices = [7,1,5,3,6,4] # clm đúng r mua 7 bán 1 là lỗ 6 chứ có lời đâu :) 


print(max_profit(prices))



