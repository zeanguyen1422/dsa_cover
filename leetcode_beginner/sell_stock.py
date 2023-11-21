


prices = [9, 1, 3, 4, 5, 9]

# mua giá 9 bán giá 2 lời 8

prices = [7,1,5,3,6,4]

# là 6 chứ ta


def max_profit(prices):

	min_buy = float('inf')
	max_buy = 0 

	for price in prices:

		if price < min_buy: 
			min_buy = price		

		if price - min_buy > max_buy: 
			max_buy = price - min_buy

		# có value của min buy với max buy rồi thì nó loop hết so sánh liên tục á 
			
	return max_buy 




print(max_profit(prices))




