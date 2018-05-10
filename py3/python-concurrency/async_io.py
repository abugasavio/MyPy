import asyncio


async def amap(fut, fn, seq):
    res = []
    for item in seq:
        res.append(fn(item))
        await asyncio.sleep(0)
    fut.set_result(res)


