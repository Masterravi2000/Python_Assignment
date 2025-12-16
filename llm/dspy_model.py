import dspy
from dotenv import load_dotenv
from llm.entity_extractor import ExtractEntities

load_dotenv()

dspy.settings.configure(
    lm=dspy.LM(model="groq/llama-3.1-8b-instant")
)

extractor = dspy.Predict(ExtractEntities)


def extract_entities_from_text(text: str):
    """
    Extract entities and relationships dynamically from any text.
    """
    result = extractor(paragraph=text)
    print("Entities:", result.entities)
    print("Raw Relationships:", result.relationships)

    # Build node_id map for Mermaid linking
    node_id_map = {e.entity: e.entity.lower().replace(" ", "_") for e in result.entities}

    # Dynamically infer edges between entities
    edges = infer_relationships(result.entities, result.relationships)

    return result.entities, edges


def infer_relationships(entities, raw_relationships):
    """
    Dynamic edge inference:
    - Create edges only between entities present in the text
    - Use LLM output relationships if possible
    """
    edges = []
    entity_names = [e.entity for e in entities]
    entity_ids = {e.entity: e.entity.lower().replace(" ", "_") for e in entities}

    # Simple heuristic: connect every pair of entities mentioned in raw_relationships
    for rel in raw_relationships:
        rel_lower = rel.lower()
        # Find entities present in this raw relationship
        matched = [name for name in entity_names if name.lower() in rel_lower]
        if len(matched) == 2:
            src, tgt = matched
            edges.append(f"{entity_ids[src]} --> {entity_ids[tgt]}")

    # Fallback: fully connect all entities if no edges inferred
    if not edges:
        for i, src in enumerate(entity_names):
            for tgt in entity_names[i + 1:]:
                edges.append(f"{entity_ids[src]} --> {entity_ids[tgt]}")

    # Remove duplicates
    edges = list(set(edges))
    return edges