def entities_to_mermaid(entities, relationships):
    """
    Convert any set of entities and edges into a Mermaid graph dynamically.
    """
    lines = ["graph TD"]
    nodes = set()

    for e in entities:
        node = e.entity.lower().replace(" ", "_")
        if node not in nodes:
            lines.append(f"    {node}[{e.entity}]")  # display original name
            nodes.add(node)

    for rel in relationships:
        if "-->" in rel:
            src, tgt = rel.split("-->")
            lines.append(f"    {src.strip()} --> {tgt.strip()}")

    return "\n".join(lines)