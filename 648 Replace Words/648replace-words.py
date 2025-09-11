class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        ls = sentence.split(" ")
        ls1 = []

        def find(i):
            index = -1
            min1 = float("inf")

            for j in range(len(dictionary)):
                if ((dictionary[j] <= i) and (i.startswith(dictionary[j])) and (len(dictionary[j]) < min1)):
                    index = j
                    min1 = len(dictionary[j])

            return index

        for i in ls:
            index = find(i)

            if (index != -1):
                ls1.append(dictionary[index])
            else:
                ls1.append(i)
        
        s = " ".join(ls1)

        return s