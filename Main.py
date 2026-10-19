from wrapper.SparqlQuery import SparqlQuery
from rels.RelBuilder import RelBuilder
import yaml
from yaml import SafeLoader
from dataclasses import dataclass
from csv import writer
import json
from collections import defaultdict
from utils.Stats import Stats
from pathlib import Path

@dataclass
class Relationships:
    endpoint: str
    query: str
    return_format: str
    save_intermediate_results: str


def read_properties(file_path):
    """
    Reads the properties from a YAML file.
    Args:
        file_path (str): The path to the YAML file containing properties.
    Returns:
        dict: A dictionary containing the properties.
    """
    with open(file_path, 'r') as file:
        properties = yaml.load(file, Loader=SafeLoader)
    return properties

def main():
    properties = read_properties('properties/prop.yaml')

    output_file = properties['relationships-retrieval']['save_intermediate_results']
    output_file_path = Path(output_file)
    if not output_file_path.parent.exists():
        relationships = Relationships(
            endpoint=properties['relationships-retrieval']['endpoint'],
            query=properties['relationships-retrieval']['query'],
            return_format=properties['relationships-retrieval']['return_format'],
            save_intermediate_results=properties['relationships-retrieval']['save_intermediate_results']
        )

        s_query = SparqlQuery(relationships.endpoint)
        res = s_query.execute_query(relationships.query, relationships.return_format)
        
        rel_dict = dict()
        for r in res.bindings:
            
            character = r.get('character', None)
            if character:
                character = character.value

            story_id = r.get('story_id', None)
            if story_id:
                story_id = story_id.value

            if story_id in rel_dict:
                rel_dict[story_id].get('character', []).append(character)
                continue
            
            series_url = r.get('series_url', None)
            if series_url:
                series_url = series_url.value

            story_url = r.get('story_url', None)
            if story_url:
                story_url = story_url.value
            
            relationship = r.get('relationship', None)
            if relationship:
                relationship = relationship.value

            el = {
                'series_url': series_url,
                'story_id': story_id,
                'story_url': story_url,
                'relationship': relationship,
                'character': [character] if character else []
            }

            if story_id:
                rel_dict[story_id] = el
            else:
                rel_dict[story_url] = el

        
        rel_builder = RelBuilder()
        for story_id, el in rel_dict.items():
            relationship_obj = el['relationship']
            recognized_relationships = rel_builder.recognize_relationship(relationship_obj)
            rel_dict[story_id]['recognized_relationships'] = recognized_relationships
        
        with open(output_file, 'w') as f:
            json.dump(rel_dict, f, indent=4)
    else:
        with open(output_file, 'r') as f:
            rel_dict = json.load(f)

    if properties['relationships-retrieval']['compute_stats']:
        path = properties['relationships-retrieval']['compute_stats']
        # Compute statistics
        stats = Stats(rel_dict)
        count_graphs = stats.count_graphs()
        avg_relationships = stats.avg_relationships()
        avg_kind_counts, kind_counts = stats.avg_relationship_kind()
        avg_config_counts, config_counts = stats.avg_relationship_configuration()
        avg_char_kind_counts, char_kind_counts = stats.avg_character_kind()
        avg_characters = stats.avg_character()

        # Save statistics to a JSON file
        with open(path, 'w') as f:
            json.dump({
                'count_graphs': count_graphs,
                'avg_relationships': avg_relationships,
                'avg_kind_counts': avg_kind_counts,
                'kind_counts': kind_counts,
                'avg_config_counts': avg_config_counts,
                'config_counts': config_counts,
                'avg_char_kind_counts': avg_char_kind_counts,
                'char_kind_counts': char_kind_counts,
                'avg_characters': avg_characters
            }, f, indent=4)
    
if __name__ == "__main__":
    main()

