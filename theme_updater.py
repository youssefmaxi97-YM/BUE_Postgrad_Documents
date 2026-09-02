import re
import sys

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace variables
content = re.sub(
    r":root \{.*?}",
    """:root {
            --primary-bg: #f8fafc;
            --secondary-bg: #ffffff;
            --card-bg: rgba(255, 255, 255, 0.95);
            --text-main: #0f172a;
            --text-muted: #475569;
            --accent: #BA0C2F; 
            --accent-hover: #9e0a28; 
            --bue-blue: #003366; 
            --gradient-start: #f1f5f9; 
            --gradient-end: #e2e8f0; 
        }""",
    content,
    flags=re.DOTALL
)

# Replace abstract shapes
content = content.replace("background: rgba(59, 130, 246, 0.15); /* Blue */", "background: rgba(186, 12, 47, 0.15);")
content = content.replace("background: rgba(139, 92, 246, 0.15); /* Purple */", "background: rgba(0, 51, 102, 0.15);")

# Replace container border
content = content.replace("border: 1px solid rgba(255, 255, 255, 0.1);", "border: 1px solid rgba(0, 0, 0, 0.05);")

# Replace h1 gradient
content = re.sub(
    r"background: linear-gradient\(to right, #fff, #93c5fd\);\s*-webkit-background-clip: text;\s*background-clip: text;\s*-webkit-text-fill-color: transparent;",
    "color: var(--bue-blue);",
    content
)

# Replace tab header gradients
content = content.replace("var(--secondary-bg)", "var(--card-bg)")

# Replace tabs backgrounds
content = content.replace("background: rgba(255, 255, 255, 0.05);", "background: rgba(0, 0, 0, 0.03);")
content = content.replace("border: 1px solid rgba(255, 255, 255, 0.05);", "border: 1px solid rgba(0, 0, 0, 0.05);")
content = content.replace("background: rgba(255, 255, 255, 0.1);", "background: rgba(0, 0, 0, 0.08);")
content = content.replace("background: var(--accent);", "background: var(--bue-blue);")
content = content.replace("border-color: var(--accent);", "border-color: var(--bue-blue);")
content = content.replace("box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);", "box-shadow: 0 4px 12px rgba(0, 51, 102, 0.2);")

# Tab content block
content = content.replace("background: rgba(0, 0, 0, 0.2);", "background: #ffffff; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);")

# file note color
content = content.replace("color: #94a3b8;", "color: var(--text-muted);")

# btn replace
content = content.replace("background: linear-gradient(135deg, #4f46e5 0%, var(--accent-hover) 100%);", "background: linear-gradient(135deg, var(--accent) 0%, var(--accent-hover) 100%);")
content = content.replace("background: linear-gradient(to right, transparent, rgba(255, 255, 255, 0.2), transparent);", "background: linear-gradient(to right, transparent, rgba(255, 255, 255, 0.3), transparent);")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Replaced CSS variables and theme colors.")
