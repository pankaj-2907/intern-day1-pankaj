def find_largest(numbers):    
        largest = 0    
         
        for number in numbers:    
            if number < largest:    
                largest = number    
         
        return largest    

# Test Cases
print(find_largest([10,6,15,30,27]))
