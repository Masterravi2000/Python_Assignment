import dspy
from dotenv import load_dotenv
from llm.entity_extractor import ExtractEntities

load_dotenv()

dspy.settings.configure(
    lm=dspy.LM(model="groq/llama-3.1-8b-instant")
)

extractor = dspy.Predict(ExtractEntities)


def infer_relationships(entities, raw_relationships):
    """
    Convert LLM output into proper edges if needed.
    Creates 'EntityA --> EntityB' for every pair of entities
    that appear in the raw relationships list.
    """
    edges = []
    names = [e.entity.lower() for e in entities]
    for i, src in enumerate(names):
        for tgt in names[i+1:]:
            # simple heuristic: if either entity appears in raw list, create edge
            raw_lower = [r.lower() for r in raw_relationships]
            if src in raw_lower or tgt in raw_lower:
                edges.append(f"{src} --> {tgt}")
    return list(set(edges))


def extract_entities_from_text(text: str):
    """
    Extract entities and relationships from text using LLM.
    Uses infer_relationships to ensure valid Mermaid edges.
    """
    result = extractor(paragraph=text)
    
    # debug output to check what LLM returned
    print("Entities:", result.entities)
    print("Relationships:", result.relationships)
    
    # ensure relationships are in 'EntityA --> EntityB' format
    relationships = infer_relationships(result.entities, result.relationships)
    
    return result.entities, relationships