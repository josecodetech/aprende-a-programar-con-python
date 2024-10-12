import asyncio
import websockets

# Definimos la funcion que maneja la conexion 
async def manejar_conexion(websocket, path):
    print("Cliente conectado")
    try:
        async for mensaje in websocket:
            print(f"Mensaje recibido: {mensaje}")
            respuesta = f"Eco: {mensaje}"
            await websocket.send(respuesta)
    except websockets.ConnectionClosed:
        print("Cliente desconectado")
# Iniciamos el servidor
async def iniciar_servidor():
    server = await websockets.serve(manejar_conexion, "localhost", 8765)
    await server.wait_closed()
asyncio.run(iniciar_servidor())            
