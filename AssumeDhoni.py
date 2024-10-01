'''
Assume Dhoni's current age is 6. After 3 years, Dhoni's mother Devki Devi would be 4 times Dhoni's age. What is Devki Devi's current age? Write a program to determine the same.
Input Format:
First line of input consists of one integer value as age of Dhoni.
Output Format:
Output should display an integer that specifies Devki Devi's current age.
Sample Input and Output1:
6
33
Sample Input and Output2:
3
21
Note: Bold highlighted is the output value.
'''
cAge=int(input())
deviAge =((cAge+3)*4)-3
print(deviAge)
