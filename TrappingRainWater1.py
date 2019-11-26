class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<= 1:return 0
        water = 0
        self.lever = 1
        def changeZero(x):
            if x == self.lever:
                return 0
            else:
                return x
        while 1:
            if height[0] == 0:
                height.pop(0)
            if len(height)<= 1:
                break
            if height[len(height)-1] == 0:
                height.pop(len(height)-1)
            if height[0] != 0 and height[len(height)-1] != 0:
                if height.count(0) > 0:
                    water = water + height.count(0)
                height = map(changeZero,height)
                self.lever = self.lever + 1
        return water
