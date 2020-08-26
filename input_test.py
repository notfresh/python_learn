class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        length = len(croakOfFrogs)
        flag = [False for i in range(length)]
        the_str = 'croak'
        len2 = len(the_str)
        i = 0
        j = 0
        count = 0
        is_valid = True

        while i < length:
            for item in flag:
                is_valid = is_valid and item
            if is_valid:
                break
            while i< length and j < len2:
                if flag[i] == True:
                    i += 1
                    continue
                elif croakOfFrogs[i] == the_str[j]:
                    flag[i] = True
                    i += 1
                    j += 1
                elif croakOfFrogs[i] != the_str[j]:
                    i += 1
            if j < len2:
                return -1
            if i % len2 == 0:
                if count == 0:
                    count += 1
            else:
                i = 0
                count += 1
            j = 0
            is_valid = True

        if is_valid == False:
            return -1
        return count



s = 'ccroakroak'
res= Solution().minNumberOfFrogs(s)
print(res)