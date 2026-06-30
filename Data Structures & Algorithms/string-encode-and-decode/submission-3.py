class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = ""
        for string in strs:
            temp = temp + str(len(string)) + "#" + string
        return temp
    def decode(self, s: str) -> List[str]:
        # how to read get the size from the first part
        
        # dont split just iterate
        ans = []
        i = 0
        while i < len(s):
            j = i
            #print(s)
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            #print(i, j, s[i:j])
            i = j + 1
            j = i + length
            #print(i, j, s[i:j])
            ans.append(s[i:j])
            i = j
        
        return ans