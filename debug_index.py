# Quick test: can we now load an Excel file?
import traceback

from backend.chunking.chunker import DocumentChunker

chunker = DocumentChunker()

for filepath in ["data/raw/ASMEP INVENTORY DETAILS.xlsx", "data/raw/fake_test_data.xlsx", "data/raw/test.xlsx"]:
    import os
    if not os.path.exists(filepath):
        print(f"SKIP: {filepath}")
        continue
    print(f"\nTesting: {filepath}")
    try:
        chunks = chunker.chunk_file(filepath)
        print(f"  OK: {len(chunks)} chunks")
        print(f"  First chunk preview: {chunks[0]['text'][:200]}...")
    except Exception as e:
        print(f"  FAILED: {e}")
        traceback.print_exc()
