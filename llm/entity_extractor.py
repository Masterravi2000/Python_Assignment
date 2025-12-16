import dspy
from typing import List
from schemas.entity import EntityWithAttr

class ExtractEntities(dspy.Signature):
    paragraph: str = dspy.InputField()
    entities: List[EntityWithAttr] = dspy.OutputField()
    relationships: List[str] = dspy.OutputField()

    class Config:
        prompt = """
Extract all entities and **all relationships** from the paragraph.
Return ONLY JSON in this EXACT format:

{
  "entities": [{"entity": "entity_name", "attr_type": "type"}, ...],
  "relationships": ["EntityA --> EntityB", ...]
}

- Include relationships only **between entities listed**.
- **Do not include separate verbs or isolated words.**
- Use the exact casing from the paragraph.
- Paragraph: {paragraph}
"""