
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

class NeuralSearcher:

    def __init__(self, collection_name):
        self.collection_name = collection_name
        # Initialize encoder model
        self.model = SentenceTransformer('T-Systems-onsite/cross-en-de-roberta-sentence-transformer', device='cpu')
        # initialize Qdrant client
        self.qdrant_client = QdrantClient(
            url="https://02442ebd-ee10-476b-8a02-72c6bfa78340.us-east-1-0.aws.cloud.qdrant.io:6333",
            api_key="zwzv5ncQj6rfjbQauYU8u1rzG8pLtqKb8rGiZ7zmhgPhVbK5oG8WUg"
        )

    def search(self, text: str):
        # Convert text query into vector
        vector = self.model.encode(text).tolist()

        # Use `vector` for search for closest vectors in the collection
        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            query_filter=None,  # We don't want any filters for now
            limit=3  
        )
        # `search_result` contains found vector ids with similarity scores along with the stored payload
        # In this function we are interested in payload only

        payloads = [hit.payload for hit in search_result]
        
        return payloads