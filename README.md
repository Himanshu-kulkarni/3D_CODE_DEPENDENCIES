# CodeSphere — 3D Code Dependency Visualizer

Visualize a Python codebase as an interactive **3D dependency graph** directly in your browser.

---

## 🚀 Overview

Developers often struggle to understand large codebases due to scattered files and hidden dependencies.

**CodeSphere** solves this by:

* Parsing Python code
* Extracting structure (files, functions, imports)
* Converting it into a graph
* Rendering it in an interactive 3D environment

👉 Result: **Instant understanding of code structure**

---

## 🧠 Key Features

* 🔍 **Code Parsing Engine** — Extracts functions and dependencies from `.py` files
* 🔗 **Dependency Graph Generation** — Builds relationships between modules
* 🌐 **3D Visualization** — Interactive graph using Three.js
* 🎯 **Smart Highlighting** — Click a node to focus on related components
* 🏷 **Persistent Labels** — File names visible directly in the graph

---

## 🏗️ Project Structure

```
CodeSphere/
├── parser.py           # Backend: parses code → generates graph.json
├── graph.json          # Generated dependency graph
├── index.html          # 3D visualization (frontend)
└── sample_code/
    ├── main.py
    ├── utils.py
    └── models.py
```

---

## ⚙️ How It Works

1. **Parse Code**

   * Reads Python files
   * Extracts:

     * Functions
     * Imports (including nested imports)

2. **Build Graph**

   * Nodes → files & functions
   * Edges → dependencies

3. **Visualize**

   * Rendered in 3D using force-directed layout
   * Interactive exploration (zoom, rotate, click)

---

## ▶️ Run Locally

### 1. Run the parser

```bash
python parser.py
```

### 2. Start a local server

```bash
python -m http.server 8080
```

### 3. Open in browser

```
http://localhost:8080
```

---

## 🎮 Controls

| Action       | Input              |
| ------------ | ------------------ |
| Rotate       | Left-click + drag  |
| Zoom         | Scroll             |
| Pan          | Right-click + drag |
| Inspect node | Click              |

---

## 🎨 Node Types

* 🔵 **Files** → Python modules
* 🔴 **Functions** → Functions inside files

---

## 📈 Example Use Cases

* Understanding new codebases
* Debugging dependencies
* Learning project architecture
* Visualizing module relationships

---

## 🔮 Future Enhancements

* 📂 Upload your own codebase
* 🧠 AI-based code insights
* 🧩 Large-scale graph clustering
* 🥽 VR-based immersive exploration

---

## 🧑‍💻 Tech Stack

* **Backend:** Python
* **Visualization:** Three.js + 3d-force-graph
* **Data Format:** JSON graph

---

## 💡 Key Insight

> CodeSphere transforms code from **text → structure → visualization**

---

## 🏁 Status

✅ Working MVP
🚀 Hackathon-ready

---

## 👤 Author

Himanshu Kulkarni
Computer Science Engineering

---
