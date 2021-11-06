#二維度清單
#product大清單 裝 name小清單 product小清單

products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
	# p =[]
	# p.append(name)
	# p.append(price)
	# p = [name, price] 快寫法取代以上三行
	# products.append(p) 
print(products)

for p in products:
	print(p)
	print(p[0])
	print(p[1])
	print(p[0],'的價格是',p[1])

products[0][0]
