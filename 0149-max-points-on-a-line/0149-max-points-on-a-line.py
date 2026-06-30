from collections import defaultdict
import math

class Solution:
    def maxPoints(self, points: list[list[str]]) -> int:
        n = len(points)
        if n <= 2:
            return n
            
        max_points = 1
        
        for i in range(n):
            slopes = defaultdict(int)
            duplicate = 0
            current_max = 0
            
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                if dx == 0 and dy == 0:
                    duplicate += 1
                    continue
                    
                gcd = math.gcd(dx, dy)
                dx //= gcd
                dy //= gcd
                
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = abs(dy)
                    
                slopes[(dx, dy)] += 1
                current_max = max(current_max, slopes[(dx, dy)])
                
            max_points = max(max_points, current_max + duplicate + 1)
            
        return max_points