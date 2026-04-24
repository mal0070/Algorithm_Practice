def solution(numbers):
    arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i in range(len(arr)):
        numbers = numbers.replace(arr[i], str(i))
    return int(numbers)