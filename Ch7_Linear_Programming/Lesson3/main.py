def calculate_profit(num_cakes, num_cookies):
    if (
        num_cakes > 250
        or num_cookies > 200
        or num_cakes + num_cookies > 300
    ):
        return -1
    return (num_cakes * 5) + num_cookies


    
