class Solution:
    def isNumber(self, s: str) -> bool:
        dfa = [
            {"digit": 1, "sign": 2, "dot": 3},
            {"digit": 1, "dot": 4, "exponent": 5},
            {"digit": 1, "dot": 3},
            {"digit": 4},
            {"digit": 4, "exponent": 5},
            {"digit": 7, "sign": 6},
            {"digit": 7},
            {"digit": 7}
        ]
        
        current_state = 0
        
        for char in s:
            if char.isdigit():
                group = "digit"
            elif char in ["+", "-"]:
                group = "sign"
            elif char in ["e", "E"]:
                group = "exponent"
            elif char == ".":
                group = "dot"
            else:
                return False
                
            if group not in dfa[current_state]:
                return False
                
            current_state = dfa[current_state][group]
        
        return current_state in [1, 4, 7]