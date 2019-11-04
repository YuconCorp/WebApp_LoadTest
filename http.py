import asyncio

# remainder of functions omitted

# Entrypoint to making requests
def assault(url, requests, concurrency):
    results = []
    asyncio.run(distribute_work(url, requests, concurrency, results))
    print(results)
