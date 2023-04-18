
"""
Created on Sat Apr 15 17:25:52 2023

@author: erica
"""


class Distance():
          # Calculate the Euclidean distance between (x0, y0) and (x1, y1)#
              # Functions to calculate the distance between each agent#
        def get_distance(x0, y0, x1, y1):
            """
            Calculates difference between input x0,y0 and x1,y1 coordinates
            
            Parameters
            ----------
            x0 : Number
                The x-coordinate of the first coordinate pair
            y0 : Number
                The y-coordinate of the first coordinate pair
            x1 : Number
                The x-coordinate of the second coordinate pair
            y1 : Number
                The y-coordinate of the second coordinate pair
        
            Returns:
                Euclidean distance between coordinates (x0, y0) and (x1,y1)
            """
    
            # Calculate the difference in the x coordinates.
            dx = x0 - x1
            # Calculate the difference in the y coordinates.
            dy = y0 - y1
            # Square the differences, add the squares, calculate square root
            distance = ((dx * dx) + (dy * dy)) ** 0.5
            return distance
          
       
# =============================================================================
#         def get_both_distance():
#             """
#             Finds the largest maximum distance and lowest minimum between all the agents'
#            
#             Returns
#                 minimum and maximum distance between all the agents
#             """
#             max_distance = 0
#             min_distance = math.inf
#             for i in range(len(agents)):
#                 a = agents[i] #reassign a to first variable's position in range calculation
#                 for j in range(len(agents)):
#                     b = agents[j]
#                     #print("i", i, "j", j)
#                     distance = get_distance(a.x, a.y, b.x, b.y)
#                     #print("distance between", a, b, distance)
#                     max_distance = max(max_distance, distance)
#                     #print("max_distance", max_distance)
#                     min_distance = min(min_distance, distance)
#                     #print("min_distance", min_distance)
#             return min_distance, max_distance
#             #return max_distance
# =============================================================================
