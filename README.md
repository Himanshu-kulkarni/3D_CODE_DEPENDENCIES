# 3D Code Visualizer

Visualize a Python codebase as an interactive 3D graph in your browser.

---

## Project Structure

```
techvortex/
├── parser.py           ← Python script: reads .py files → outputs graph.json
├── graph.json          ← Pre-generated sample (auto-overwritten by parser.py)
├── index.html          ← Frontend: 3D visualization
└── sample_code/
    ├── main.py
    ├── utils.py
    └── models.py
```

---

## Step 1 — Run the Parser

Make sure Python 3 is installed, then:

```bash
cd techvortex
python parser.py
```

This reads all `.py` files in `sample_code/` and writes `graph.json`.

To point at your own folder, edit this line in `parser.py`:
```python
SAMPLE_FOLDER = "sample_code"   # ← change to your folder path
```

---

## Step 2 — Start a Local Server

You must serve the files over HTTP (not file://) so the browser can fetch `graph.json`.

**Python (easiest):**
```bash
python -m http.server 8080
```

**Node.js (npx):**
```bash
npx serve .
```

---

## Step 3 — Open in Browser

Go to:
```
http://localhost:8080
```

---

## Controls

| Action         | How                    |
|----------------|------------------------|
| Rotate         | Left-click + drag      |
| Zoom           | Scroll wheel           |
| Click node     | Shows node name + type |
| Pan            | Right-click + drag     |

---

## Node Colors

- 🔵 **Cyan** — Python files
- 🔴 **Pink/Red** — Functions
