import re

class RelBuilder:

    def __init__(self):
        pass
    
    def split_relationship_obj(self, relationship_obj: str):
        """
        Splits a relationship object string into a list of individual relationships.
        Args:
            relationship_obj (str): The relationship object string to split.
        Returns:
            list: A list of individual relationships.
        """
        # Split the relationship object by commas and strip whitespace
        relationships = [item.strip() for item in relationship_obj.split(',')]
        return relationships

    def remove_series_metadata(self, relationship_obj: str):
        """
        Removes series metadata from a relationship object string.
        Args:
            relationship_obj (str): The relationship object string to clean.
        Returns:
            str: The cleaned relationship object string without series metadata.
        """
        relationship_obj_cleaned = re.sub(r'\s*Series:.*$', '', relationship_obj)
        return relationship_obj_cleaned.strip()
    
    def identify_relationship_kind(self, tag):
        """
        Identifies the kind of relationship based on the tag.
        Args:
            tag (str): The relationship tag to analyze.
        Returns:
            str: The kind of relationship ('romantic', 'friendship', or 'unknown').
        """
        kind = None
        if "/" in tag:
            kind = "romantic"
        elif "&" in tag:
            kind = "friendship"
        else:
            kind = "unknown"
        return kind

    def identify_charachter_kind(self, character):
        character = character.lower()
        if character in ["unknown", "undisclosed", "???", "??", "?"]:
            return 0
        elif character in ["everyone", "various", "other", "others", "other(s)", "all"]:
            return 1
        elif character in ["any", "anyone", "some", "someone"]:
            return 2
        elif character in ["reader", "you"]:
            return 3
        elif character in ["me", "author"]:
            return 4
        elif character in ["oc", "ofc", "omc", "original character", "original female character", "original male character", "original character(s)", "original female character(s)", "original male character(s)"]:
            return 5
        else:
            return -1

    def identify_characters(self, tag: str, kind: str):
        if kind not in ["romantic", "friendship"]:
            raise ValueError(f"Unknown relationship kind: {kind}. Expected 'romantic' or 'friendship'.")
        
        delimiter = "/" if kind == "romantic" else "&"
        characters = re.split(rf'[{re.escape(delimiter)}]', tag)
        n_characters = len(characters)
        return characters, n_characters

    def identify_configuration(self, characters, n_characters):
        configuration = []
        if n_characters == 2:
            configuration.append("pair")
        if n_characters == 2 and len(set(characters)) == 1:
            configuration.append("self")
        if n_characters > 2:
            configuration.append("group")

        for character in characters:
            match = re.search(r'\(([^()]{2,})\)', character)
            if match:
                configuration.append("crossover")
                break
        
        return configuration        
         
    def get_fandom(self, character: str):
        match = re.search(r'\(([^()]{2,})\)', character)
        if match:
            return match.group(1).strip()
        return None
    
    def get_character_name_alternative(self, character: str):
        delimiter = "|"
        if delimiter in character:
            characters = re.split(rf'[{re.escape(delimiter)}]', character)
            return characters[0].strip(), characters[1].strip()
        return None

    def recognize_relationship(self, relationship_obj: str):
        relationship_obj = self.remove_series_metadata(relationship_obj)
        relationships = self.split_relationship_obj(relationship_obj)
        recognized_relationships = []
        for relationship in relationships:
            kind = self.identify_relationship_kind(relationship)
            try:
                characters, n_characters = self.identify_characters(relationship, kind)
                pattern_recognized = True
                configuration = self.identify_configuration(characters, n_characters)
            
                characters_features = []
                for character in characters:
                    character = character.strip()
                    character_kind = self.identify_charachter_kind(character)
                    fandom = self.get_fandom(character)
                    character_alternative = self.get_character_name_alternative(character)
                    characters_features.append({
                        "character": character,
                        "kind": character_kind,
                        "fandom": fandom,
                        "alternative": character_alternative
                    })

            except ValueError as e:
                n_characters = -1
                configuration = []
                characters_features = []

            recognized_relationships.append({
                "relationship": relationship,
                "kind": kind,
                "n_characters": n_characters,
                "configuration": configuration,
                "characters": characters_features
            })
            
        return recognized_relationships


