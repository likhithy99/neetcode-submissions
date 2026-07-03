class Solution:
    def minWindow(self, s: str, t: str) -> str:
     if not t or not s:
        return ""
    
     count_t = {}
     for c in t:
        count_t[c] = count_t.get(c, 0) + 1
    
     need = len(count_t)
     have = 0
     window = {}
     res = ""
     res_len = float('inf')
     left = 0
    
     for right in range(len(s)):
        c = s[right]
        window[c] = window.get(c, 0) + 1
        
        if c in count_t and window[c] == count_t[c]:
            have += 1
        
        while have == need:
            if (right - left + 1) < res_len:
                res_len = right - left + 1
                res = s[left:right+1]
            
            window[s[left]] -= 1
            if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                have -= 1
            left += 1
    
     return res