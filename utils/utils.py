from typing import List
import multiprocessing


def sum_list(payload: List[List[int]]):
    output = [sum(item) for item in payload]
    return output


class SumModel():
    def sum_list(self, payload: List[List[int]]) -> List[int]:
        """
        Takes list of int list and return a list of sum of each sub list
        """
        pool = multiprocessing.Pool()

        # Map the sum_list function to each sublist in input_data
        results = pool.map(sum_list, payload)

        # Close the pool and wait for the worker processes to finish
        pool.close()
        pool.join()

        return results
