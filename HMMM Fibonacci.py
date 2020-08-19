# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name    :Jose de la Cruz  
# Pledge  :I pledge my honor that I have abided by the Stevens Honor System
# Purpose :
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Max:
#  Write a hmmm function that gets two numbers,
#   then prints the larger of the two.
#  Assumptions: Both inputs are any integers
Max = """
00 read r1
01 read r2
02 sub r3 r1 r2
03 jgtzn r3 06 
04 jltzn r3 08
05 jeqzn r3 08
06 write r1
07 halt
08 write r2
09 halt
"""


# Power:
#  Write a hmmm function that gets two numbers,
#   then prints (No.1 ^ No.2).
#  Assumptions: No.1 is any integer, No.2 ≥ 0
Power = """
00 read r1 # Input goes to r1
01 read r2 # Input goes to r2
02 setn r4 1 #sets r4 to 1
03 jeqzn r2 13 # checks if r2 is equal to zero jumps to a line that outputs r4 which is 1 then halts
04 copy r3 r1 # copies r1 to r3
05 jeqzn r2 10 #checks if r2 is 0 jumps to line that outputs r3 and halts
06 jnezn r2 07 #checks if r2 is not 0 jumps to multiply r3 r3 r1
07 mul r3 r3 r1
08 sub r2 r2 r4
09 jumpn 05 #resets multiplication loop
10 div r3 r3 r1
11 write r3 # writes the result in r3
12 halt
13 write r4 # outputs 1
14 halt


"""


# Fibonacci
#  Write a hmmm function that gets one numner,
#   then prints the No.1st fibonacci number.
#  Assumptions: No.1 ≥ 0
#  Hint: You really don't want to implement
#   recursion in hmmm, try to find an
#   iterative method to compute your goal.
#  Tests: f(2) = 1
#         f(5) = 5
#         f(9) = 34
Fibonacci = """
00 read r1
01 setn r2 0
02 setn r3 1
03 setn r4 1

04 jeqzn r1 12
05 add r2 r2 r3
06 sub r1 r1 r4
07 jumpn 08

08 jeqzn r1 14
09 add r3 r2 r3
10 sub r1 r1 r4
11 jumpn 04

12 write r2
13 halt
14 write r3
15 halt

"""


# ~~~~~ Running ~~~~~~
RunThis = Fibonacci
doDebug = False

if __name__ == "__main__" : 
    import hmmm
    hmmm.main(RunThis, doDebug)


