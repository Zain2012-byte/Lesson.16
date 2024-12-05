def total_calc(bill_amount,tip_perc):
    #define function to calculate the tip on a bill
    total=bill_amount*(1+0.01*tip_perc)

    #Converts the tip percentage into a decimal value (e.g., 20% becomes 0.20).
    total= round(total,2)
    print(f"please pay ${total}")

    #specify only bill_amount
    
total_calc(150,20)