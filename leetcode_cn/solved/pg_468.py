class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            return self.validIPv4(queryIP)
        elif ':' in queryIP:
            return self.validIPv6(queryIP)
        else:
            return 'Neither'

    def validIPv4(self, queryIP: str) -> str:
        if queryIP.count('.') != 3:
            return 'Neither'
        for i in queryIP.split('.'):
            if not i or i.count('.') or not i.isdigit() or int(i) > 255 or (i[0] == '0' and len(i) > 1):
                return 'Neither'
        return 'IPv4'

    def validIPv6(self, queryIP: str) -> str:
        if queryIP.count(':') != 7:
            return 'Neither'
        for i in queryIP.split(':'):
            if len(i) > 4 or not all(c in '0123456789abcdefABCDEF' for c in i) or (int(i)==0 and len(i)>1):
                return 'Neither'
        return 'IPv6'