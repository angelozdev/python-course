import asyncio

contador = 0
lock = asyncio.Lock()


async def incrementar():
    global contador
    await lock.acquire()

    print(f"Antes de incrementar: {contador}")
    contador += 1
    await asyncio.sleep(1)
    print(f"Después de incrementar: {contador}")

    lock.release()

    print("Lock liberado")


async def main():
    await asyncio.gather(incrementar(), incrementar(), incrementar())


if __name__ == "__main__":
    asyncio.run(main())
