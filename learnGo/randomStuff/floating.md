Introduction
A floating-point number is a number with zero or more digits behind the decimal separator. Examples are -2.4, 0.1, 3.14, 16.984025 and 1024.0.

Different floating-point types can store different numbers of digits after the digit separator - this is referred to as its precision.

Go has two floating-point types:

float32: 32 bits (~6-9 digits precision).
float64: 64 bits (~15-17 digits precision). This is the default floating-point type.
As can be seen, both types can store a different number of digits. This means that trying to store PI in a float32 will only store the first 6 to 9 digits (with the last digit being rounded).

By default, Go will use float64 for floating-point numbers, unless the floating-point number is:

assigned to a variable with type float32, or
returned from a function with return type float32, or
passed as an argument to the float32() function.
The math package contains many helpful mathematical functions.

Instructions
In this exercise you'll be working with savings accounts. Each year, the balance of your savings account is updated based on its interest rate. The interest rate your bank gives you depends on the amount of money in your account (its balance):

3.213% for a balance less than 0 dollars (balance gets more negative).
0.5% for a balance greater than or equal to 0 dollars, and less than 1000 dollars.
1.621% for a balance greater than or equal to 1000 dollars, and less than 5000 dollars.
2.475% for a balance greater than or equal to 5000 dollars.
You have four tasks, each of which will deal your balance and its interest rate.

Implement the InterestRate() function to calculate the interest rate based on the specified balance:

InterestRate(200.75)
// => 0.5
Note that the value returned is a float32.


Stuck? Reveal Hints
Opens in a modal
Implement the Interest() function to calculate the interest based on the specified balance:

Interest(200.75)
// => 1.003750
Note that the value returned is a float64.


Stuck? Reveal Hints
Opens in a modal
Implement the AnnualBalanceUpdate() function to calculate the annual balance update, taking into account the interest rate:

AnnualBalanceUpdate(200.75)
// => 201.75375
Note that the value returned is a float64.


Stuck? Reveal Hints
Opens in a modal
Implement the YearsBeforeDesiredBalance() function to calculate the minimum number of years required to reach the desired balance, taking into account that each year, interest is added to the balance. This means that the balance after one year is: start balance + interest for start balance. The balance after the second year is: balance after one year + interest for balance after one year. And so on, until the current year's balance is greater than or equal to the target balance.

balance := 200.75
targetBalance := 214.88
YearsBeforeDesiredBalance(balance, targetBalance)
// => 14