Here some tips how to easily refactor code from 'without_asyncio' folder 
to asyncio code.
1) def async_foo --> async def foo
2) import asyncio
3) async_sleep(x) --> asyncio.sleep(x)