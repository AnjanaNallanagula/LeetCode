class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        s = ""
        ls = []

        def binarySearch(s):
            low = 0
            high = len(products) - 1
            index = -1

            while (low <= high):
                mid = low + (high - low) // 2

                if (products[mid] >= s):
                    index = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            return index

        for i in range(len(searchWord)):
            s += searchWord[i]
            index = binarySearch(s)
            ls1 = []
            
            if (index == -1):
                ls.append(ls1)
                continue
            
            count = 0
            while (index < len(products) and count < 3):
                if (products[index].startswith(s) == True):
                    ls1.append(products[index])
                    index += 1
                    count += 1
                else:
                    break
            
            ls.append(ls1)
        
        return ls