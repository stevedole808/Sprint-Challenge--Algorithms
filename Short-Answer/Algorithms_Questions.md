# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
# find the middle of the floor, mid = len(floor) / 2
# While len(floor) > 1 (The lowest the n-story can be is 1 story high)
# check to see if egg gets cracked 
# if the egg cracks then we set the egg to cracked and decrement the mid value
  # divide mid by half to start next iteration to check if the egg will crack
# else we increment the mid value by 1
  # divide by half and start the next iterations

# 0(log n) because we would use a while loop to check the length of the building the n a nested for loop that access whether the egg is # # # broken or not. Causing us to have to create two sublists in a way to check the mid  value incremented by 1 and decremented by 1 to see if # the egg is broken on that story or not.
