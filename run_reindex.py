import os
from backend.config import config
from backend.chunking.chunker import DocumentChunker
from backend.embedding.embedder import GoogleEmbedder
from backend.retrieval.vector_store import QdrantVectorStore

chunker = DocumentChunker()
embedder = GoogleEmbedder()
vector_store = QdrantVectorStore()

raw_dir = config.UPLOAD_DIR
allowed = {".pdf", ".docx", ".doc", ".txt", ".md", ".xlsx", ".xls"}

existing_sources = set(vector_store.list_sources())
print(f"Existing sources: {existing_sources}")

files_to_process = []
for fname in os.listdir(raw_dir):
    if fname.startswith("."): continue
    ext = os.path.splitext(fname)[1].lower()
    if ext in allowed and fname not in existing_sources:
        files_to_process.append(fname)

print(f"Found {len(files_to_process)} missing files to index.")

for idx, fname in enumerate(files_to_process, 1):
    filepath = os.path.join(raw_dir, fname)
    print(f"\n[{idx}/{len(files_to_process)}] Processing: {fname}")
    try:
        chunks = chunker.chunk_file(filepath)
        if not chunks:
            print(f"  -> Skipped: No chunks found.")
            continue
            
        embedded = embedder.embed_chunks(chunks)
        vector_store.upsert_chunks(embedded)
        print(f"  -> OK: Indexed {len(chunks)} chunks.")
    except Exception as e:
        print(f"  -> ERROR processing {fname}: {e}")
        import traceback; traceback.print_exc()

print("\nDone! Current stats:")
print(vector_store.get_stats())
