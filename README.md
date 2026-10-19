# KG relationships - Archive of Our Own (AO3) README

AO3 guidelines define how relationships between fictional characters are identified and classified throughout the archive.

## Relationship category #1: Romantic and/or sexual relationships

AO3 uses a **slash (`/`)** to indicate romantic or sexual relationships between characters. A relationship can involve multiple characters, not just two.

Examples:

`Harry Potter / Ginny Weasley`

`Harry Potter / Ginny Weasley / Hermione Granger`

AO3 does not distinguish between sexual and romantic relationships, nor does it specify whether a relationship has been consummated, when it takes place, whether it is established, or whether it is mutual.

## Relationship category #2: Friendship and family

AO3 uses an **ampersand (`&`)** to indicate non-romantic, non-sexual relationships between characters, such as friendships, family relationships, and other platonic relationships. These relationships can involve multiple characters, not just two.

Examples:

`Harry Potter & Ginny Weasley`

`Harry Potter & Ginny Weasley & Hermione Granger`

The relationship may indicate friendship, family ties, or other platonic connections. The tag does not specify whether the relationship is established, ongoing, or mutual.

### Relationship configuration #1: Group relationships

If more than two characters are involved, AO3 treats the group relationship as separate from the individual pairings.

Example of a three-character relationship:

`Harry Potter / Ginny Weasley / Hermione Granger`

Possible individual pairings:

`Harry Potter / Ginny Weasley`

`Ginny Weasley / Hermione Granger`

`Harry Potter / Hermione Granger`

However, we do not actually know how the individual characters in the group interact with each other. Therefore, we cannot assume that every possible pair represents a separate tagged relationship, as this would introduce information that the source does not explicitly provide.

### Relationship configuration #2: Self-relationships

AO3 allows relationships between a character and themselves.

### Relationship configuration #3: Crossover relationships

AO3 allows relationships between characters belonging to different universes or fandoms. To specify the crossover, the fandom name may also be included in parentheses next to the character's name.

> **Q#1:** Should we preserve the fandom information, also considering that characters with the same name may belong to different universes? **A: Preserved**

### Participant identification #1: Collective entities

AO3 also allows collective entities in relationship tags.

Example: `Class 77 & Hinata Hajime`

**Warning:** It is not possible to establish which characters belong to the collective entity. The `golem:characters` predicate cannot be used to resolve the members of the collective entity because it does not specify whether all the characters are involved in the collective relationship.

> **Q#2:** Does the GOLEM ontology provide a way to represent groups?

### Participant identification #2: Duplicated characters and clones

Sometimes, a relationship involving multiple participants may include the same character more than once. This is not necessarily a **mistake**: the duplicated character may represent multiple versions of the same character.

AO3 specifies that it is possible to normalize this kind of relationship into an ordinary two-character relationship or treat it as a separate canonical group relationship.

> **Q#3:** Since the decision depends on the fictional context, which approach should we adopt?

### Participant identification #3: Relationships involving original characters

AO3 allows relationships involving characters created by fanfiction authors, generically referred to as "original characters."

Commonly used tags include: `OC`, `OFC`, `OMC`, `Original Character`, `Original Female Character`, and `Original Male Character`.

These tags should be interpreted as placeholders rather than as references to individual characters.

### Participant identification #4: Relationships involving named original characters

As in Participant identification #3, relationships may involve original characters, but in some cases, these characters have specific names.

Example:

`Harry Potter / Alexandra Smith`

### Participant identification #5: Unknown characters

Some relationships involve participants whose identities are hidden or unknown.

The tags used include: `undisclosed`, `???`, and `?`.

> **Q#4:** Should we create an anonymous participant or ignore the relationship?

### Participant identification #6: Generic participants

Some relationships involve generic groups of characters. In this scenario, a character is involved in a relationship with many or all characters, without specifying the identities of the individual participants.

The tags used include: `Everyone`, `Various`, and `Other(s)`.

### Participant identification #7: Relationships involving someone

In this scenario, a character is involved in a relationship with another character whose identity is not important to the story.

The tag used is: `Any`.

### Participant identification #8: Creator/Reader inserts

These relationships involve readers, authors, or other self-insert participants.

The tags used include: `Reader`, `You/Me`, and `Author`.

## Critical issues

### The "Series" tag

Some `golem:socialRelationship` entries include a `golem:series` tag in the unstructured text following the list of relationships, in the form `Series: [text]`.

Example:

`"Remus Lupin/Severus Snape Series: 100 Quills BY Snegurochka [12]"`

> **S:** Remove the text introduced by `Series:` after the list of relationships, if present.

## Stats

|     |  |
| -------- | ------- |
| # graphs  | 6823    |
| # avg relationships | 2.00     |
| # romantic relationships | 10243     |
| # friendship relationships | 2452     |
| # unknown relationships | 1015    |
| # two-relationships    | 11980    |
| # group-relationships    | 715    |
| # self-relationships    | 23    |
| # crossover    | 303    |
| # normal characters    | 24862    |
| # unknown characters    | 6    |
| # "everyone" character    | 44    |
| # reader/you character    | 473    |
| # author character    | 1    |
| # "original" character    | 983    |

