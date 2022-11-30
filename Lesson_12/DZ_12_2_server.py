import socket
import asyncio


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55002))
sock.listen(5)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('Connection from: ', addr)
    data = conn.recv(1024).decode('UTF-8')
    lst = [int(x) for x in data.split(",")]
    print(f'First number: {lst[0]}', '\n' f'Second number: {lst[1]}')


    async def addition():
        print('Running addition')
        await asyncio.sleep(0)
        result = lst[0] + lst[1]
        print('Addition done')
        return result


    async def subtraction():
        print('Running subtraction')
        await asyncio.sleep(0)
        result = lst[0] - lst[1]
        print('Subtraction done')
        return result


    async def multiplication():
        print('Running multiplication')
        await asyncio.sleep(0)
        result = lst[0] * lst[1]
        print('Multiplication done')
        return result


    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(addition()),
             ioloop.create_task(subtraction()),
             ioloop.create_task(multiplication())]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)

    msg = [f'Addition:  {str(tasks[0].result())}',
           f'Subtraction:  {str(tasks[1].result())}',
           f'Multiplication: {str(tasks[2].result())}']
    msg = '\n'.join(msg)
    conn.send(bytes(msg, encoding='UTF-8'))
    conn.close()
