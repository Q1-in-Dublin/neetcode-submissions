class TimeMap:

    def __init__(self):
        #Key-value
        self.time_dict = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dict :
            self.time_dict[key] = []
        self.time_dict[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:

            if key not in self.time_dict :
                return ""
            
            entries = self.time_dict[key]
            left, right = 0, len(entries)-1
            result = ""

            while left <= right:
                mid = (left+right)//2
                entry_time, entry_value = entries[mid]

                if entry_time <= timestamp :
                    result= entry_value
                    left = mid + 1
                else:
                    right = mid-1

            return result
