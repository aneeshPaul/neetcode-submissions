class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        sorted_position = sorted(zip(position, speed), key= lambda x:x[0], reverse=True)

        time= [0]*len(position)

        for i in range(len(time)):
            time[i]= (target - sorted_position[i][0])/sorted_position[i][1]

        if time:
            res = time[0:1]
        else:
            return 0

        for t in time[1:]:
            if t>res[-1]:
                res.append(t)

        return len(res)


        


        
        