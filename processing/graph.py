def entities_to_mermaid(entities, relationships):
    lines = ["graph TD"]
    nodes = set()

    # Add nodes from entities
    for e in entities:
        name = e.entity if hasattr(e, "entity") else str(e)
        node = name.lower().replace(" ", "_")
        if node not in nodes:
            lines.append(f"    {node}[{name}]")
            nodes.add(node)

    # Add edges from relationships
    for rel in relationships:
        # Support multiple arrow formats
        if "-->" in rel:
            parts = rel.split("-->")
        elif "->" in rel:
            parts = rel.split("->")
        elif " to " in rel.lower():
            parts = rel.lower().split(" to ")
        else:
            continue

        if len(parts) != 2:
            continue

        src, tgt = parts[0].strip(), parts[1].strip()
        src_node, tgt_node = src.lower().replace(" ", "_"), tgt.lower().replace(" ", "_")

        # Add missing nodes
        if src_node not in nodes:
            lines.append(f"    {src_node}[{src}]")
            nodes.add(src_node)
        if tgt_node not in nodes:
            lines.append(f"    {tgt_node}[{tgt}]")
            nodes.add(tgt_node)

        # Add arrow
        lines.append(f"    {src_node} --> {tgt_node}")

    return "\n".join(lines)