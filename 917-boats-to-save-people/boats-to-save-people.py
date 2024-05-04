class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        l, r = 0, len(people) - 1
        people.sort()

        while l < r:
            if people[r] == limit:
                r -= 1
                boat += 1
            else:
                s = people[l] + people[r]
                if s <= limit:
                    l += 1
                    r -= 1
                else:
                    r -= 1
                boat += 1
            if l == r and people[r] <= limit:
                boat += 1

        return boat
