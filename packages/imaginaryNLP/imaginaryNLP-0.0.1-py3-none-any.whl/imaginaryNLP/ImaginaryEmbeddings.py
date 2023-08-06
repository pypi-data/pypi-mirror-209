from typing import Optional
from sentence_transformers import SentenceTransformer


class ImaginaryEmbeddings:
    """
    will be puplished soon
    """
    def __init__(self, model_name_or_path: Optional[str] = None):
        """
        :param model_name_or_path: Path to the model or the model name from huggingface.co/models
        """
        self.model = SentenceTransformer(model_name_or_path)

        print('Sorry, but the code for Imaginary Embeddings is not yet published. '
              'You will be able to test this package during the ACL 2023 conference.')
