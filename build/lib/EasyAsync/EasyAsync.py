import asyncio
import concurrent.futures
import functools

from typing import List, Callable


class EasyAsync:
    def __init__(self):
        self._workers = 16

    async def _worker(self, fn: Callable, group: List) -> List:
        with concurrent.futures.ThreadPoolExecutor(max_workers=self._workers) as executor:
            loop = asyncio.get_event_loop()
            futures = [
                loop.run_in_executor(
                    executor,
                    functools.partial(fn, group[ind])
                )
                for ind in range(0, len(group)) if group[ind]
            ]

        await asyncio.gather(*futures)

        return [futures[ind].result() for ind in range(0, len(futures))]

    def easy_work(self, fn: Callable, fullgroup: List) -> List:
        done = []
        loop = asyncio.get_event_loop()
        for ind in range(0, len(fullgroup), self._workers):
            group = fullgroup[ind:ind+self._workers]
            done.extend(loop.run_until_complete(self._worker(fn, group)))