from collections import defaultdict, Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = Counter(s)  # Example: {'a': 3, 'b': 2}

        # Step 2: Create a stack (bucket) to hold characters by their frequency
        stack = defaultdict(list)
        for char, freq in count.items():
            stack[freq].append(char)  #neated array

        # Step 3: Build the result string
        res = []
        # Iterate from high frequency to low
        for freq in range(len(s), 0, -1):
            if freq in stack:
                for char in stack[freq]:
                    res.append(char * freq)  # Repeat the character `freq` times

        return ''.join(res)
