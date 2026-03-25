import os
import json
import re

SAMPLE_FOLDER = "sample_code"

def parse_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    functions = re.findall(r"^def\s+(\w+)\s*\(", content, re.MULTILINE)
    imports = []

    for line in content.splitlines():
        line = line.strip()
        # Match: import module or package.module
        m1 = re.match(r'^import\s+([\w\.]+)', line)
        if m1:
            module = m1.group(1).split('.')[-1]   # take top-level module
            imports.append(module)

        # Match: from module import ...
        m2 = re.match(r'^from\s+([\w\.]+)\s+import', line)
        if m2:
            module = m2.group(1).split('.')[-1]
            imports.append(module)

    return functions, imports


def build_graph(folder):
    nodes = []
    links = []
    node_ids = set()

    py_files = [f for f in os.listdir(folder) if f.endswith(".py")]
    file_bases = {os.path.splitext(f)[0] for f in py_files}

    def add_node(nid, ntype="file"):
        if nid not in node_ids:
            nodes.append({"id": nid, "type": ntype})
            node_ids.add(nid)

    for filename in py_files:
        filepath = os.path.join(folder, filename)
        file_id = os.path.splitext(filename)[0]
        add_node(file_id, "file")

        functions, imports = parse_file(filepath)

        for func in functions:
            func_id = f"{file_id}.{func}"
            add_node(func_id, "function")
            links.append({"source": file_id, "target": func_id})

        for imp in imports:
            if imp in file_bases and imp != file_id:
                add_node(imp, "file")
                links.append({"source": file_id, "target": imp})

    return {"nodes": nodes, "links": links}


if __name__ == "__main__":
    folder = SAMPLE_FOLDER
    if not os.path.isdir(folder):
        print(f"Folder '{folder}' not found. Create it and add .py files.")
        exit(1)

    graph = build_graph(folder)

    with open("graph.json", "w") as f:
        json.dump(graph, f, indent=2)

    print(f"Done! {len(graph['nodes'])} nodes, {len(graph['links'])} links → graph.json")
