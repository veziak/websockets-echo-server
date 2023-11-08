import asyncio
import http
import websockets
import logging

logging.getLogger().setLevel(logging.INFO)
PORT = 8080


async def health_check(path, request_headers):
    if path == "/health":
        return http.HTTPStatus.OK, [], b"OK\n"


async def echo(websocket):
    async for message in websocket:
        logging.info(f"echo: {message}")
        await websocket.send(message)


async def main():
    async with websockets.serve(
        echo,
        "0.0.0.0",
        PORT,
        process_request=health_check,
    ):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    logging.info(f"Starting websockets server on {PORT}")
    asyncio.run(main())
