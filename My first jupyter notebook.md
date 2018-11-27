
# this is my first python notebook
(yes that's how it's spelled and capitalized)

# Heading 1
## Heading 2
### Heading 3 
#### Heading 4
##### Heading 5
I didn't really need that comment.

## This is a bulleted list
* Item 1
* Item 2
    * Item 2a
    * Item 2b
        * Item 2ba
    * Item 2c
* Item 3

# This is a numbered list
1. item 1
3. item 2
7. item 3
17. item 4
    * item 4a
    * item 4b

#### Let's look at Bold and Italics
In this line of text *this item will be in italics* but this won't. Also, _this will be in italics_ but this won't. __This part will be bold__ but this wont. Finally, **this bit will be bold** but this won't.

# My temperature conversion script
In this exercise, I want to enter a temperature in Fahrenheit and have the code calculate degrees in Celsius.


```python
f = 32
c = (f-32)*5/9
c
```




    0.0




```python
f = float(input("Enter the temperature in degrees Fahrenheit? "))
c = (f-32)*5/9
c
print()
print("The temperature " + str(f) + " degrees Fahrenheit is " + str(round((c),2)) + " degrees Celsius.")

```

    Enter the temperature in degrees Fahrenheit? 100
    
    The temperature 100.0 degrees Fahrenheit is 37.78 degrees Celsius.
    


```python
 
```
