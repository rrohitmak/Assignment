from typing import List


class SumModel():
    def sum_list(self, payload: List[List[int]]) -> List[int]:
        """
        Takes list of int list and return a list of sum of each sub list
        """
        return [sum(item) for item in payload]
