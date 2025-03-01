#This class is created using a BaseRetriever class.
#The use of this is to avoid fetching repeated or duplicated documents from the vector database.

"""If we load the vector database with same data multiple times, that data will get appended
to the database. Later when we search for top k similar results, the same data will be fetched. """

#This can be avoided using a custom retriever class

from langchain_chroma.vectorstores import Chroma
from langchain.embeddings.base import Embeddings
from langchain.schema import BaseRetriever

class RedundantFilterRetriever(BaseRetriever):
    embeddings : Embeddings
    chroma : Chroma
    def _get_relevant_documents(self, query):
        #calculate embeddings for the query string
        emb = self.embeddings.embed_query(query)
        #take embeddings and feed them into the max_marginal_relevance_search_by_vector function
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb,
            lambda_mult=0.8)
    async def _aget_relevant_documents(self):
        return []