class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # two arrays 
        # positions = [], positions[i] ith car's position
        # speed = [] ith car's speed
        # target => destination # 10
        # one line cannot pass
# target = 10
# position = [4, 1, 0, 7]
# speed    = [2, 2, 1, 1]

# 0th loc 4 speed 2
# 1th loc 1 speed 2
# 2th loc 0 speed 1
# 3th loc 7 speed 1

# loc [2th,1th,0,0th,0,0,3th,0,0,0]

# oth = (10-4) /2 time? 3
# 1th = 10-1 /2 4.5
# 2th = 10-0 10 
# 3th = 10-7 /1 3
        cars = sorted(zip(position,speed),reverse=True)
        stack= []

        for loc,spd in cars:
            time = (target-loc) /spd

            if not stack or time > stack[-1]:
                # later than the car ahead
                stack.append(time)
        return len(stack)