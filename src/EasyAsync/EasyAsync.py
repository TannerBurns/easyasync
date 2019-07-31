import asyncio
import concurrent.futures
import functools

from typing import Callable


class EasyAsync:
    def __init__(self, workers=16):
        """EasyAsync Init
        
        Keyword Arguments:
            workers {int} -- Number of workers for yielded chunks (default: {16})
        """
        self._workers = workers


    async def _worker(self, fn: Callable, group: list) -> list:
        """_worker -- function for wrapping non async function call
        
        Arguments:
            fn {Callable} -- function call to map
            group {list} -- sub group that will be mapped to the function
        
        Returns:
            list -- group of returns from the mapped function
        """
        with concurrent.futures.ThreadPoolExecutor(max_workers=self._workers) as executor:
            loop = asyncio.get_event_loop()
            futures = [loop.run_in_executor(executor, functools.partial(fn, item)) 
                for item in group if item
            ]

        await asyncio.gather(*futures)

        return [f.result() for f in futures]


    def easy_work(self, fn: Callable, args: list) -> list:
        """easy_work - turn a non async work into async work
        
        Arguments:
            fn {Callable} -- function to map
            fullgroup {list} -- full list to map with function
        
        Returns:
            list -- group of returns from the mapped function
        """
        loop = asyncio.get_event_loop()
        for ind in range(0, len(args), self._workers):
            yield loop.run_until_complete(self._worker(fn, args[ind:ind+self._workers]))