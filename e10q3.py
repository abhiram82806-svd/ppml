class product: 
    def __init__(self,product_id,product_name,price,quantity):
        self.product_id=product_id
        self.product_name=product_name
        self.price = price
        self.quantity = quantity
        self.total_amount=0
    def calculate_total(self):
        self.total_amount=self.price*self.quantity
    