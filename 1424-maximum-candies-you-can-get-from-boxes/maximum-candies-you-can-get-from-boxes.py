class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        total_candy = 0
        visited = set()
        queue = deque()
        can_open = [status[i] == 1 for i in range(len(status))]
        has_box = [0] * len(status)

        for i in initialBoxes:
            has_box[i] = 1
            if can_open[i]:
                queue.append(i)

        while queue:
            q_box = queue.popleft()
            if q_box in visited:
                continue

            visited.add(q_box)
            total_candy += candies[q_box]

            # Add contained boxes
            for box in containedBoxes[q_box]:
                has_box[box] = 1
                if can_open[box] and box not in visited:
                    queue.append(box)

            # Add keys
            for key in keys[q_box]:
                if not can_open[key]:
                    can_open[key] = 1
                    if has_box[key] and key not in visited:
                        queue.append(key)

        return total_candy

# class Solution:
#     def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
#         total_candy = 0
#         visited = set()
#         queue = deque() # open boxes
#         can_open = [status[i] == 1 for i in range(len(status))]
#         has_box = [0] * len(status)

#         for i in initialBoxes:
#             if status[i] == 1:
#                 queue.append(i)
#                 total_candy += candies[i]
#                 visited.add(i)
#                 boxs = containedBoxes[i] # [2]
#                 for box in boxs:
#                     has_box[box] = 1
#                     if can_open[box] == 1:
#                         queue.append(box)
#                 box_keys = keys[i] # [1,2]
#                 for key in box_keys:
#                     can_open[key] = 1
#                     if has_box[key] == 1:
#                         queue.append(key)
#         print(f"queue= {queue}")
#         print(f"visited= {visited}")
#         print(f"total_candy= {total_candy}")
#         print(f"has_box= {has_box}")
#         print(f"can_open= {can_open}")
#         while queue:
#             q_box = queue.popleft()
#             if q_box not in visited:
#                 total_candy += candies[q_box]
#                 visited.add(q_box)
#                 boxs = containedBoxes[q_box] # [3]
#                 for box in boxs:
#                     has_box[box] = 1
#                 box_keys = keys[q_box] # [0]
#                 for key in box_keys:
#                     can_open[key] = 1
#                     if has_box[key] == 1:
#                         queue.append(key)
#         return total_candy

