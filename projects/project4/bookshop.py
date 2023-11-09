# Project No.4
# Authos: Ryan Lilleyman, Christian Blanchard
# Description: Bookshop super class

from functools import reduce
from collections import defaultdict 
class BookShop:
    def __init__(self, orders = ()):
        """
        Initializes an instance of the class.

        Parameters:
            orders (list, optional): A list of orders. Defaults to an empty list.
        """
        self.orders = list(orders)
        self.mod=[]
        self.mo = []

    def get_orders(self):
        """
        Get the orders.

        Returns:
            The orders.
        """
        return self.orders

    def set_orders(self, orders):
        """
        Set the orders for the object.

        Parameters:
            orders (list): A list of orders to be set.

        Returns:
            None
        """
        self.orders = orders

    def add_order(self, order):
        """
        Add an order to the list of orders.

        Args:
            order: The order to be added.

        Returns:
            None.
        """
        self.orders.append(order)

  
    def total_price_per_book_order_number(self):
        to_return = []
        for order in self.orders:

            mod = []

            on = order[0]
            mod.append(on)

            bol = order[1:]
            for book in bol:
                
                if book[1]*book[2]<100:
                    mbo = (book[0],(book[1]*book[2])+10)
                    mod.append(mbo)
                else:
                    mbo = (book[0],(book[1]*book[2]))
                    mod.append(mbo)

            to_return.append(mod)

        self.mod = to_return
        return to_return
    

    def filter_lowest(self):
        fl = []
        for order in self.mod:
            tup = [item[1] for item in order[1:]]
            minimum = list(filter(lambda x: x == min(tup),tup))
            minimum = minimum[0]
            bo = ''
            for tup in order[1:]:
                if tup[1] == minimum:
                    bo = tup[0]
            mo = (order[0],bo)
            fl.append(mo)
        return fl
    
    def filter_maximum(self):
        fl = []
        for order in self.mod:
           
            tup = [item[1] for item in order[1:]]
            maximum = list(filter(lambda x: x == max(tup),tup))
            maximum = maximum[0]
            
            bo = ''
            for tup in order[1:]:
                if tup[1] == maximum:
                    bo = tup[0]
                    
            mo = (order[0],bo)
            
            fl.append(mo)
        return fl

        
    def sum_tuple(self):
        fl = []
        for order in self.mod:
            tup = [item[1] for item in order[1:]]
            total = reduce(lambda x,y: x+y ,tup)  
            fl.append((order[0],"{:,.2f}".format(total))) 
        return fl
    
    def max_amount(self):
        to_check = [item[1] for item in self.sum_tuple()]
        return list(filter(lambda x: x == max(to_check),to_check))
    
    def max_order_and_book(self):
        result = [(order[0], sum([item[1] for item in order[1:]])) for order in self.orders]
        res = max([item[1] for item in result])
        something = list(filter(lambda x: x[1] == res,result))
        result = something[0]
        return result
    
    def max_books_decending_list(self):
        result = [(order[0], sum([item[1] for item in order[1:]])) for order in self.orders]
        result = sorted(result, reverse=True)
        return result
    
    def total_quantity_of_all_books(self):
        result = [(order[0], sum([item[1] for item in order[1:]])) for order in self.orders]
        res = [item[1] for item in result]
        return reduce((lambda x,y: x+y), res)

    def most_ordered(self):
        result = [item for item in [order[1:] for order in self.orders]]
        n = defaultdict(str)
        for res in result:
            for item in res:
                key = item[0]
                value = item[1]
        
                if key in n:
                    n[key] += value
                else:
                    n[key] = value
        maximum = max(n.values())
        ls = []
        for k in n:
            if n[k] == maximum:
                ls.append(k)
            
        minimum = min(n.values())
        for k in n:
            if n[k]== minimum:
                ls.append(k)

        return ls
        

    def sub_order_length(self):
        sublist = [item for item in [order[1:] for order in self.orders]]
        lengths = [ len(item) for item in sublist]
        return lengths
                
        
        

        
        

    

    def __str__(self):
        return str(self.orders) 

        

        
