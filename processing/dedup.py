def deduplicate_entities(entities):
    seen = {}
    for e in entities:
        # handle if e is a list or has 'entity' attribute
        entity_name = e.entity if hasattr(e, 'entity') else str(e)
        key = entity_name.lower().strip()
        if key not in seen:
            seen[key] = e
    return list(seen.values())