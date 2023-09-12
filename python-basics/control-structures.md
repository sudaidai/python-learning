# Python Control Structures

In Python, control structures are used to control the flow of a program. They allow you to make decisions, repeat actions, and perform different actions based on certain conditions.

## Conditional Statements

### if Statement

The `if` statement is used to execute a block of code if a specified condition is true.

```python
if condition:
    # code to execute if the condition is true
```

### else Statement
The else statement is used to execute a block of code if the condition in the if statement is false.

```python
if condition:
    # code to execute if the condition is true
else:
    # code to execute if the condition is false
```

### elif Statement
The elif statement is used to specify multiple conditions. If the condition in the if statement is false, Python will check the conditions in the elif statements in order and execute the code block associated with the first true condition.

```python
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true
else:
    # code to execute if neither condition1 nor condition2 is true
```

## Looping Statements

### for Loop
The for loop is used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence.

```python
for item in sequence:
    # code to execute for each item
```

### while Loop
The while loop is used to repeatedly execute a block of code as long as a specified condition is true.

```python
while condition:
    # code to execute while the condition is true
```

### break and continue Statements

- The `break` statement is used to exit the loop prematurely.
- The `continue` statement is used to skip the rest of the current iteration and move to the next iteration of the loop.

```python
for item in sequence:
    if condition:
        break  # exit the loop
    if another_condition:
        continue  # skip the rest of this iteration and continue with the next
```
