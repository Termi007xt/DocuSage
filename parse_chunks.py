from extract_chunk_support import extract_text, chunk_text
import json
from typing import Union

def parse_chunk(document: Union[str, bytes], file_name: str = "Insurance") -> str:
    """
    Accepts:
      - bytes: raw PDF bytes (from file upload)
      - str:   http(s) URL to a PDF OR plain text
    Returns:
      - JSON string of chunk objects (same shape as before)
    """
    text = extract_text(document)
    chunks = chunk_text(text)

    json_chunks = [] #new chunking method
    for i, item in enumerate(chunks):
        json_chunks.append(
            {
                "file_name": file_name,
                "chunk_id": i,
                "text": item,
            }
        )

    return json.dumps(json_chunks)
