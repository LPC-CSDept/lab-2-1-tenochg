def main():
   ##################################################
   # Comlete your code here
   ##################################################
    original_price = int(input('Regular Price: '))
    rate = int(input('Discount Amount:'))
    discount_amount = original_price - original_price * rate/100
    discount_amount_dollar = original_price * rate/100

    print('Regular Price: $',original_price)
    print('Discount Amount: $',discount_amount_dollar)
    print('The Final Sale Price: $',discount_amount)

    
    pass



    

if __name__ == '__main__':
    main()
