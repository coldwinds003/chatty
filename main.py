# main.py — App entry point
# Run: python main.py

import uvicorn
from backend.api.app import app
from backend.config import config

if __name__ == "__main__":
    print(f"""
+------------------------------------------+
|           VaultRAG -- Starting Up        |
+------------------------------------------+
|  Chat model  : {config.CHAT_MODEL:<26}|
|  Embedding   : {config.EMBEDDING_MODEL:<26}|
|  Qdrant      : {config.QDRANT_HOST}:{config.QDRANT_PORT:<22}|
|  Collection  : {config.QDRANT_COLLECTION:<26}|
|  Chunk size  : {str(config.CHUNK_SIZE):<26}|
+------------------------------------------+
    """)
    uvicorn.run(
        "main:app",
        host   = config.APP_HOST,
        port   = config.APP_PORT,
        reload = config.DEBUG,
    )
