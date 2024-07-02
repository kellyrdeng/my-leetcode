class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 1: #if occupied
                continue

            #if empty, check surroundings and place if valid
            if self.is_valid_placement(flowerbed, i):
                flowerbed[i] = 1
                flowers += 1

        return flowers >= n

    def is_valid_placement(self, flowerbed, i):
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True

        #if left index
        if i == 0 and flowerbed[i + 1] == 0:
            return True

        #if right index
        if i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
            return True

        #if middle
        if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
            return True

        return False
            
