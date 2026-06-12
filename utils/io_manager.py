import os
import shutil

class IOManager:
    @staticmethod
    def setup_environment(base_dir: str):
        """Ensures the compilation environment is clean and ready."""
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

    @staticmethod
    def purge_cache(cache_dir: str):
        """Deletes temporary vector files created during generation."""
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
            os.makedirs(cache_dir)

    @staticmethod
    def validate_binary(filepath: str) -> bool:
        """Checks if the generated TTF/OTF is valid and greater than 0 bytes."""
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0
