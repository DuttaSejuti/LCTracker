class Solution:
    def canInsert(self, key: str, index_dict: dict, cooling_time: int, current_index: int) -> bool:
        return index_dict.get(key) == None or current_index > index_dict[key] + cooling_time

    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dict = dict()
        index_dict = dict()
        
        # create task:freq dictionary 
        for t in tasks:
            task_dict[t] = task_dict.get(t, 0) + 1
        
        # sorting task_dict with values in descending order
        task_dict = dict(sorted(task_dict.items(), key= lambda x:x[1], reverse = True))
        key = list(task_dict.keys())
        
        i = 0
        while 1:
            hasInserted = 0
            task_dict = dict(sorted(task_dict.items(), key= lambda x:x[1], reverse = True))
            key = list(task_dict.keys())
            for k in key:
                # task[freq] exists
                if(self.canInsert(k, index_dict, n, i)):
                    task_dict[k] -= 1
                    if task_dict[k] == 0:
                        del task_dict[k]
                        key.remove(k)
                    index_dict[k] = i
                    hasInserted = 1
                    i += 1
                    break

            if len(key) == 0:
                break
            
            if hasInserted == 0:
                i += 1
        return i
