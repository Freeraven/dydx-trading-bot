from func_connections import connect_dydx
import asyncio

print("---------------------------------------------------")

async def connect():
    client = connect_dydx()
    return client

if __name__ == '__main__':
    print("Hello bot!")

    # Connect to client
    try:
        asyncio.run(connect())
    except Exception as e:
        print(e)
        print("Error connecting to client")
        exit(1)
