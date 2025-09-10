import numpy as np


# update/add code below ...
Exercise 1
def ways(n):
    '''
    This functions returns the number of ways you can change n cents
    using only pennies (1 cent) and nickels (5 cents).
    '''
    return int((n // 5) + 1)

# Test cases
print(ways(12))  # should give 3
print(ways(20))  # 5
print(ways(3))   # 1
print(ways(0))   # 1


Optional Variation
def ways(cents, coin_types=[1, 5]):
    '''
    This function returns the number of ways to make 'cents' using the given coin_types.
    '''
    dp = [0] * (cents + 1)
    dp[0] = 1  # 1 way to make 0 cents

    for coin in coin_types:
        for amount in range(coin, cents + 1):
            dp[amount] += dp[amount - coin]

    return dp[cents]

# Test given case
ways(100, [25, 10, 5, 1])  # gives 242


Exercise 2
Part 1
names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])

def lowest_score(names, scores):
    '''
    Returns the name of the student alongwith the lowest score.
    '''
    # index of lowest score
    idx = np.argmin(scores)  
    return str(names[idx]), int(scores[idx])
    
# Test Case
print(lowest_score(names, scores))  # gives ('Mauve', 62)

Part 2

def sort_names(names, scores):
    '''
    Returns the names of students sorted by descending test score.
    '''
    idx = np.argsort(scores)[::-1]   # indices for descending order
    return names[idx]                # apply ordering to names

# Test Case
print("Sorted names by scores:", sort_names(names, scores)) 

