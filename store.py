total=int(input("Enter the total number of products : "))
if total <=0 :
    exit()
product_list =[]
for i in range (total ):
  product ={
      "product_name" :input("Enter the name of product : "),
      "product_qty ":int (input("enter the qty : ")),
      "product_price":int (input("enter the price : "))}
  product_list.append(product)

def search (productName,list):
    for i in list :
        if productName in i["product_name"]:
            return i
    return "no product in your search"
search_name = input("Enter name of product to search : ")
print(search(search_name,product_list))