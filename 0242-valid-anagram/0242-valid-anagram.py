class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        s_dic={}
        t_dic={}

        for s_al in s:
            s_dic[s_al]=s_dic.get(s_al,0)+1
        for t_al in t:
            t_dic[t_al]=t_dic.get(t_al,0)+1

        return s_dic==t_dic
