#Finial Calculator function

def monthly_installment(principal, period, interest_rate):
    """
    The monthly_installment function takes the following arguments:

    Principal = Initial principal or loan amount
    interest_rate = Interest rate per period
    period = Total number of payments or periods

    return:

    monthly_installment

    Example:

    Precise took R150 000 loan at 7.5% annual interest rate for 5 years after a R15 000 down payment

    ` A = P(r(1+r)^n)/((1+r)^n-1)`

    - P = R150 000
    - r = 7.5% per year / 12 monts = 0.625% per period (0.00625 on your calculator)
    - n = 5 years x 12 months = 60 total periods

    - A = R 150 000 ( 0.00625 x(1+0.00625)^6)/((1+00625))^(60-1) 
    - A = R150 000 (0.00625 x 1.45329)/(1.45329 -1)
    - A = R150 000 (0.00908306/0.45329)
    - A = R 150 000 (0.02003808)
    - A = R 3005.71

    """
    #convert inputs to manageable format
    principal = float(principal)
    period = float(period)
    interest_rate = float(interest_rate)


    interest_rate = (interest_rate/12)/(100)
    period = period*12
    monthly_installment = principal *(interest_rate *(1+interest_rate)**period) / ( (1+interest_rate)**period -1 )
    monthly_installment = round(monthly_installment,2)

    return monthly_installment