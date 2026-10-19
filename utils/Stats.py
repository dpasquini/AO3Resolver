

class Stats:

    def __init__(self, relationships_graph: dict):
        self.relationships_graph = relationships_graph
    
    def count_graphs(self):
        """
        Counts the number of graphs in the relationships graph.
        Returns:
            int: The number of graphs.
        """
        return len(self.relationships_graph.keys())

    def avg_relationships(self):
        """
        Calculates the average number of relationships per graph in the relationships graph.
        Returns:
            float: The average number of relationships.
        """

        sum_relationships = 0
        for graph in self.relationships_graph.values():
            rels = graph.get('recognized_relationships', [])
            sum_relationships += len(rels)
        avg_relationships = sum_relationships / self.count_graphs() if self.count_graphs() > 0 else 0
        return avg_relationships

    def avg_relationship_kind(self):
        """
        Calculates the average number of relationships per kind in the relationships graph.
        Returns:
            dict: A dictionary with the average number of relationships per kind.
        """

        kind_counts = {}
        for graph in self.relationships_graph.values():
            rels = graph.get('recognized_relationships', [])
            for rel in rels:
                kind = rel.get('kind', 'unknown')
                if kind not in kind_counts:
                    kind_counts[kind] = 0
                kind_counts[kind] += 1

        avg_kind_counts = {kind: count / self.count_graphs() if self.count_graphs() > 0 else 0 for kind, count in kind_counts.items()}
        return avg_kind_counts, kind_counts

    def avg_relationship_configuration(self):
        """
        Calculates the average number of relationships per configuration in the relationships graph.
        Returns:
            dict: A dictionary with the average number of relationships per configuration.
        """

        config_counts = {}
        for graph in self.relationships_graph.values():
            rels = graph.get('recognized_relationships', [])
            for rel in rels:
                configurations = rel.get('configuration', ['unknown'])
                for config in configurations:
                    if config not in config_counts:
                        config_counts[config] = 0
                    config_counts[config] += 1

        avg_config_counts = {config: count / self.count_graphs() if self.count_graphs() > 0 else 0 for config, count in config_counts.items()}
        return avg_config_counts, config_counts

    def avg_character_kind(self):
        """
        Calculates the average number of characters per kind in the relationships graph.
        Returns:
            dict: A dictionary with the average number of characters per kind.
        """

        char_kind_counts = {}
        for graph in self.relationships_graph.values():
            rels = graph.get('recognized_relationships', [])
            for rel in rels:
                characters = rel.get('characters', [])
                for char in characters:
                    kind = char.get('kind', 'unknown')
                    if kind not in char_kind_counts:
                        char_kind_counts[kind] = 0
                    char_kind_counts[kind] += 1

        avg_char_kind_counts = {kind: count / self.count_graphs() if self.count_graphs() > 0 else 0 for kind, count in char_kind_counts.items()}
        return avg_char_kind_counts, char_kind_counts

    def avg_character(self):
        """
        Calculates the average number of characters per graph in the relationships graph.
        Returns:
            float: The average number of characters.
        """

        sum_characters = 0
        for graph in self.relationships_graph.values():
            rels = graph.get('recognized_relationships', [])
            for rel in rels:
                characters = rel.get('characters', [])
                sum_characters += len(characters)
        avg_characters = sum_characters / self.count_graphs() if self.count_graphs() > 0 else 0
        return avg_characters