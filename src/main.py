from app import app
import uvicorn
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', action='store', type=int, default=8000)
    parser.add_argument('--host', action='store', type=str, default="0.0.0.0")
    args = parser.parse_args()

    uvicorn.run(app, host=args.host, port=args.port)