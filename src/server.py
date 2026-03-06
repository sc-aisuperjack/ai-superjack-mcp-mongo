import json
import sys
import logging
from mcp.server.fastmcp import FastMCP
from bson import json_util
from .database import db_manager


# Force logging to stderr so it doesn't break the JSON-RPC stream on stdout
logging.basicConfig(
    stream=sys.stderr, 
    level=logging.ERROR
)

mcp = FastMCP("AI-Superjack-Mongo-Server")

@mcp.tool()
async def query_tracks(filter_json: str, limit: int = 5) -> str:
    """Query the 'tracks' collection in the legacy_voice database."""
    try:
        collection = db_manager.get_collection("tracks")
        filter_dict = json.loads(filter_json)
        
        cursor = collection.find(filter_dict).limit(limit)
        results = await cursor.to_list(length=limit)
        
        # Serialize with json_util to handle ObjectIds safely
        return json.dumps(results, default=json_util.default, indent=2)
    except Exception as e:
        return f"Database error: {str(e)}"
    

@mcp.tool()
async def query_artists(filter_json: str, limit: int = 5) -> str:
    """Query the 'artists' collection in the legacy_voice database."""
    try:
        collection = db_manager.get_collection("artists")
        filter_dict = json.loads(filter_json)
        
        cursor = collection.find(filter_dict).limit(limit)
        results = await cursor.to_list(length=limit)
        
        # Serialize with json_util to handle ObjectIds safely
        return json.dumps(results, default=json_util.default, indent=2)
    except Exception as e:
        return f"Database error: {str(e)}"

if __name__ == "__main__":
    mcp.run()