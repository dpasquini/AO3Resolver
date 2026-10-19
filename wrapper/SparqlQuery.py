from SPARQLWrapper import SPARQLWrapper2, JSON, CSV

class SparqlQuery:
    """
    A class to execute SPARQL queries against a specified endpoint.
    Attributes:
        sparql (SPARQLWrapper2): An instance of SPARQLWrapper2 for executing queries.
    Methods:
        __init__(self, endpoint_url: str): Initializes the SparqlQuery with the given endpoint URL.
        execute_query(self, query: str, return_format='json': str) -> dict: Executes the given SPARQL query and returns the results in the specified format.
    """

    def __init__(self, endpoint_url: str):
        self.sparql = SPARQLWrapper2(endpoint_url)

    def execute_query(self, query: str, return_format: str = 'json') -> dict:
        """
        Executes a SPARQL query against the endpoint and returns the results.
        Args:
            query (str): The SPARQL query to execute.
            return_format (str): The format of the returned results ('json' or 'csv').
        Returns:
            dict: The results of the SPARQL query in the specified format.
        """

        self.sparql.setQuery(query)
        if return_format == 'json':
            self.sparql.setReturnFormat(JSON)
        elif return_format == 'csv':
            self.sparql.setReturnFormat(CSV)
        else:
            raise ValueError("Unsupported return format. Use 'json' or 'csv'.")
        
        results = self.sparql.query().convert()
        return results