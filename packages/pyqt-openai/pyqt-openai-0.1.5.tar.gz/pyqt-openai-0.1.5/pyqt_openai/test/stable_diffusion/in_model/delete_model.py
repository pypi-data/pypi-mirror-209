import huggingface_hub
from huggingface_hub import scan_cache_dir

# required tool
# cuda or image with not as good quality
# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# pip install transformers, accelerate

# want to delete the model cache (which takes a lot of space)
# pip install huggingface_hub["cli"]

commit_hashes = []
cache_dir_result = scan_cache_dir()
for i in cache_dir_result.repos:
    for j in i.revisions:
        print(j.snapshot_path)
        commit_hashes.append(j.commit_hash)
delete_strategy = cache_dir_result.delete_revisions(*commit_hashes)
print("Will free " + delete_strategy.expected_freed_size_str)
delete_strategy.execute()