from llm.dspy_model import extract_entities_from_text
from processing.dedup import deduplicate_entities
from processing.graph import entities_to_mermaid

sample_text = """
Sustainable agriculture improves soil health and increases nitrogen uptake in crops.
"""

entities, relationships = extract_entities_from_text(sample_text)  # unpack tuple
entities = deduplicate_entities(entities)

mermaid = entities_to_mermaid(entities, relationships)  # pass both entities & relationships

with open("output/mermaid_1.md", "w") as f:
    f.write(mermaid)

print("Mermaid diagram generated")