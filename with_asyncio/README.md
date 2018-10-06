Here some tips how to easily refactor code from 'without_asyncio' folder 
to asyncio code.
1) def async_foo --> async def foo
2) import asyncio
3) async_sleep(x) --> asyncio.sleep(x)
4) Remove original async_sleep()
5) yield from foo --> await foo


Some hints:
1) Avoid calling the "future = Future()" constructor directly - 
prevents  event-loops specialising the future implementation.
That is why have future = loop.create_future() factory function.
 
2) Never call the "task = Taks(coroutine_object)" constructor directly - 
prevents  event-loops specialising the future implementation.
That is why have task = loop.create_task(coroutine_object) factory function.
 
3) Сreating tasks: prefer 'ensure_future'.
Use task = ensure_future(awaitable, loop=loop).
In spite of its confusing name it returns a Task.
