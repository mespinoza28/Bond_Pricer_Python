# Bond pricer in Python

# Import necessary libraries
import numpy as np


# Define the function to calculate bond price
def bond_pricer(par, c, r, t, ytm, bond_type, freq, maturity, call_price, call_date,
                put_price, put_date):
    """
    par = face value of the bond
    c = coupon rate
    r = number of coupon payments per year
    t = number of years to maturity
    ytm = yield to maturity
    bond_type = type of bond (plain_vanilla, callable, puttable, convertible)
    freq = frequency of coupon payments (only required for plain_vanilla bonds)
    maturity = maturity date (only required for convertible bonds)
    call_price = call price (only required for callable bonds)
    call_date = call date (only required for callable bonds)
    put_price = put price (only required for puttable bonds)
    put_date = put date (only required for puttable bonds)
    """

    # Calculate the semi-annual coupon payment for plain_vanilla bonds
    if bond_type == 'plain_vanilla':
        coupon = par * c / freq
        total_payments = freq * t
    # For all other bonds, coupon payment is assumed to be fixed
    else:
        coupon = par * c
        total_payments = t

    # Calculate the discount factor for each coupon payment
    discount_factors = [(1 + ytm / r) ** (-i) for i in range(1, total_payments + 1)]

    # Calculate the present value of each coupon payment
    pv_coupons = np.dot(discount_factors, coupon * np.ones(total_payments))

    # Calculate the present value of the face value payment
    pv_face_value = par * (1 + ytm / r) ** (-total_payments)

    # Calculate the present value of the call option (if applicable)
    if bond_type == 'callable' and call_date is not None and call_price is not None:
        call_discount_factor = (1 + ytm / r) ** (-(call_date * r))
        call_value = call_price * call_discount_factor
        pv_call = np.sum(discount_factors[:call_date * r]) * call_value
    else:
        pv_call = 0

    # Calculate the present value of the put option (if applicable)
    if bond_type == 'puttable' and put_date is not None and put_price is not None:
        put_discount_factor = (1 + ytm / r) ** (-(put_date * r))
        put_value = put_price * put_discount_factor
        pv_put = np.sum(discount_factors[:put_date * r]) * put_value
    else:
        pv_put = 0

    # Calculate the present value of the conversion option (if applicable)
    if bond_type == 'convertible' and maturity is not None:
        conversion_discount_factor = (1 + ytm / r) ** (-(maturity * r))
        conversion_value = par / freq
        pv_conversion = np.sum(discount_factors[:maturity * r]) * conversion_value * conversion_discount_factor
    else:
        pv_conversion = 0

    # Calculate the total present value
    pv_total = pv_coupons + pv_face_value - pv_call + pv_put + pv_conversion

    return pv_total

###Example

print(bond_pricer(1000,7,1,10,9, bond_type= 'plain_vanilla', freq= 1))



