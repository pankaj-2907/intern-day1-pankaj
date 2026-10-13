def find_largest(numbers):    
        if not numbers:
             return None

        # Initialize largest with the first element of the list
        largest = number[0]    
         
        for number in numbers:
            # Check if current number is Greater than largest    
            if number > largest:    
                largest = number    
         
        return largest    

# Test Cases
print(find_largest([10,6,15,30,27]))
print(find_largest([3]))
