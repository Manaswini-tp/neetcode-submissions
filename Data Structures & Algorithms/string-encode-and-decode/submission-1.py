class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return '黄'
        return '昏'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == '黄':
            return []
        if s == '':
            return ['']
        return s.split('昏')
