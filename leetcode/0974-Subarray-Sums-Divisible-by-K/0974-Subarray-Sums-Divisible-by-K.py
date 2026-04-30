count = {0: 1}
        prefix = 0
        result = 0
        
        for num in nums:
            prefix += num
            remainder = prefix % k
            if remainder < 0:
                remainder += k
            
            result += count.get(remainder, 0)
            count[remainder] = count.get(remainder, 0) + 1
        
        return result