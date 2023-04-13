---
name: "Bond pricer"
about: The script allows you to calculate the present value of any type of bond given a set of inputs.
labels: Quantitative Finance

---

## Description
The bond_pricer() function is a Python script for calculating the price of a bond given a set of parameters. Here is the documentation for each of the input parameters:

par: The face value of the bond.

c: The coupon rate of the bond, represented as a decimal.

r: The number of coupon payments per year.

t: The number of years to maturity.

ytm: The yield to maturity of the bond, represented as a decimal.\

bond_type: A string representing the type of bond. It can be one of the following: 'plain_vanilla', 'callable', 'puttable', or 'convertible'.

freq: The frequency of coupon payments. This is only required for plain vanilla bonds.

maturity: The maturity date of the bond. This is only required for convertible bonds.

call_price: The call price of the bond. This is only required for callable bonds.

call_date: The call date of the bond. This is only required for callable bonds.

put_price: The put price of the bond. This is only required for puttable bonds.

put_date: The put date of the bond. This is only required for puttable bonds.

The function calculates the bond price based on the parameters and returns the present value of the bond. The calculation involves the following steps:

Calculate the semi-annual coupon payment for plain vanilla bonds.

Calculate the discount factor for each coupon payment.

Calculate the present value of each coupon payment.

Calculate the present value of the face value payment.

Calculate the present value of the call option (if applicable).

Calculate the present value of the put option (if applicable).

Calculate the present value of the conversion option (if applicable).

Calculate the total present value.


### Environment
Libraries required:
-numpy 


### Basic example

<img width="826" alt="image" src="https://user-images.githubusercontent.com/129782426/231873137-a5ae532c-fa38-4cf7-a0fd-b861ea264548.png">



