class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + len(current_line) > maxWidth:
                for i in range(maxWidth - current_length):
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                res.append("".join(current_line))
                
                current_line = []
                current_length = 0
                
            current_line.append(word)
            current_length += len(word)
            
        last_line = " ".join(current_line)
        last_line += " " * (maxWidth - len(last_line))
        res.append(last_line)
        
        return res