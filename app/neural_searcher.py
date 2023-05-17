
from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer

class NeuralSearcher:

    def __init__(self, collection_name):
        self.collection_name = collection_name
        # Initialize encoder model
        self.model = SentenceTransformer('T-Systems-onsite/cross-en-de-roberta-sentence-transformer', device='cpu')
        # self.model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens', device='cpu')
        
        
        # initialize Qdrant client
        self.qdrant_client = QdrantClient(
            url="https://b0eed5cb-c627-4d70-a71a-6095a28f371e.eu-central-1-0.aws.cloud.qdrant.io:6333", 
            api_key="Pk7U0-GA-uUZlBRQPtvYIdf6aqtNZFVGMUrG_K9jx7Ydu0hbd8pyEg",
        )

    def search(self, text: str, genre):
        # Convert text query into vector
        vector = self.model.encode(text).tolist()
        # Use 'vector' for search for closest vectors in the collection
        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            # Adding a filter for the checked genre
            query_filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key="tag",
                        match=models.MatchAny(any=genre)
                    )
                ]
            ),
            limit=3  
        )
        
        print(search_result)
        payloads = [hit.payload for hit in search_result]
        return payloads
