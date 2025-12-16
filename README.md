Entity-Relationship Extraction System
Overview

This project is a dynamic system to extract entities and their relationships from any input paragraph and visualize them as Mermaid diagrams. It uses a large language model (LLM) to identify entities and infer relationships, then converts the output into a graph format suitable for visualization.

The system is fully dynamic — it works for any text input, not limited to a predefined set of entities or relationships.













Features

Dynamic Entity Extraction: Automatically detects all entities in a given paragraph.

Relationship Inference: Infers relationships between entities using LLM output and simple heuristics.

Deduplication: Removes duplicate entities to ensure a clean graph.

Mermaid Graph Generation: Produces diagrams in Mermaid syntax, ready for visualization.

Flexible Input: Works with any text input without hardcoding entities or relationships.













Technologies Used

Python 3.13

dspy – LLM integration for entity and relationship extraction.

Mermaid.js – Graph visualization format.

Pydantic – For structured entity schema (EntityWithAttr).

dotenv – Environment variable management.














Project Struture -
.
├── llm/
│   ├── entity_extractor.py     # LLM signature for entity extraction
│   └── dspy_model.py           # LLM prediction & dynamic edge inference
├── processing/
│   ├── dedup.py                # Deduplicate entities
│   └── graph.py                # Convert entities & relationships to Mermaid
├── output/
│   └── mermaid_1.md            # Generated Mermaid diagram
├── main.py                     # Main script to run extraction and graph generation
├── README.md                   # Project documentation
└── .env                        # Environment variables (LLM API key, etc.)














1. Install dependencies -
pip install dspy pydantic python-dotenv

2. Provide your input paragraph in main.py:-
sample_text = """
Photosynthesis converts sunlight into chemical energy. Plants need water and nutrients to grow.
"""

3. Run the main script:
python main.py


Example Output
input paragraph :- Photosynthesis converts sunlight into chemical energy. Plants need water and nutrients to grow.

Generated Mermaid diagram :-
graph TD
    photosynthesis[Photosynthesis]
    plants[Plants]
    water[water]
    nutrients[nutrients]
    sunlight[sunlight]
    plants --> water
    photosynthesis --> plants
    plants --> nutrients















How It Works

The LLM extracts entities and raw relationships from the input paragraph.

dedup.py removes duplicates from the entity list.

dspy_model.py dynamically infers relationships between entities using heuristics.

graph.py converts the entities and relationships into Mermaid graph syntax.















Notes

This system is fully dynamic and can handle any text input.

Edge inference can be further improved to detect verb-based directionality automatically.

Ensure the .env file contains the required LLM API keys.