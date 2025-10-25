
transactionLog = [
    {'orderId': 1001, 'customerId': 'cust_Ahmed', 'productId': 'prod_10'},
    {'orderId': 1001, 'customerId': 'cust_Ahmed', 'productId': 'prod_12'},
    {'orderId': 1002, 'customerId': 'cust_Bisma', 'productId': 'prod_10'},
    {'orderId': 1002, 'customerId': 'cust_Bisma', 'productId': 'prod_15'},
    {'orderId': 1003, 'customerId': 'cust_Ahmed', 'productId': 'prod_15'},
    {'orderId': 1004, 'customerId': 'cust_Faisal', 'productId': 'prod_12'},
    {'orderId': 1004, 'customerId': 'cust_Faisal', 'productId': 'prod_10'},
]

productCatalog = {
    'prod_10': 'Wireless Mouse',
    'prod_12': 'Keyboard',
    'prod_15': 'USB-C Hub',
}

def processTransactions(transactionsList) :
    d1 = {}

    for x in transactionsList:
        customer = x['customerId']
        product = x['productId']

        if customer not in d1:
            d1[customer] = set()
        
        d1[customer].add(product)

    return d1


def findFrequentPairs(customerData):
    customer_products = {}
    for x in customerData:
        customer = x['customerId']
        product = x['productId']

        if customer not in customer_products:
            customer_products[customer] = set()
        customer_products[customer].add(product)

    pairs = {}

    for products in customer_products.values():
        products_list = list(products)
    
        for x in range(len(products_list)):
            for y in range(x + 1, len(products_list)):
                p1 = products_list[x]
                p2 = products_list[y]

                if p1 < p2:
                    pair_key = (p1, p2)

                else:
                    pair_key = (p2, p1)

                if pair_key in pairs:
                    pairs[pair_key] += 1
                else:
                    pairs[pair_key] = 1

    return pairs

def getRecommendations(targetProductId, frequentPairs):
    recommendations = {}
    
    for pair, count in frequentPairs.items():
        p1 , p2 = pair

        if targetProductId == p1:
            other = p2

        elif targetProductId == p2:
            other = p1

        else:
            continue

        if other in recommendations:
            recommendations[other] += count

        else:
            recommendations[other] = count

    ranked = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return ranked

        
def generateReport(targetProductId, recommendations, catalog):


    if not recommendations:
        print("No co-purchase data available.")
        return
    product_ids, counts = zip(*recommendations)

    for i, (pid, count) in enumerate(zip(product_ids, counts), start=1):
        print(f"{i}. {catalog.get(pid, pid)} (co-purchased {count} times)")    





result = processTransactions(transactionLog)
print(result)

pairs = findFrequentPairs(transactionLog)
print(pairs)

recommendations = getRecommendations('prod_15', pairs)
print("Recommnendations for product 15: ", recommendations)

recommend = [('prod_12', 2), ('prod_15', 2)]

generateReport('prod_12', recommend, transactionLog)

        