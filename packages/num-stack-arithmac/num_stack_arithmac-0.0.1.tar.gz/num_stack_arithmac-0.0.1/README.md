# Num Stack Arithmac
Install via:<br>
`pip install num_stack_arithmac`
## Pre-execution
Input is given by specifying the start number.
## Instructions
Here are the different instructions:<br>
`+` increments the number.<br>
`-` decrements the number.<br>
`%` performs reduction modulo 2 on the number.<br>
`^` squares the number.<br>
`r` takes the square root of the number.<br>
`p` prints the decimal representation of the number.<br>
`q` prints the character with the codepoint of the number.<br>
`b` prints the binary representation of the number.<br>
`x` prints the hexadecimal representation of the number.<br>
`o` prints the boolean representation of the number.<br>
`s` halts the programme.<br><br>
All other characters are no-ops. If you use `\\` or `.` in your programme, the compiler will incorrectly think you are specifying the file path if you are typing in raw code.
## Example
Here is an example programme that checks whether a number is even or odd (the number is given by the starting value):<br><br>
`%+%o`