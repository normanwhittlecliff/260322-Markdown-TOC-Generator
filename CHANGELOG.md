# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog
and this project follows Semantic Versioning.

---

# # [1.0.1] - 2026-03-24


### Fixed

Fixed bug where the script always skip the sections under the first `---` by changing to the following code:

```
def extract_headings(lines):
    # Extract headings and store (level, text).
    headings = []
  
    headings = []
    separator_count = 0

    for line in lines:
        if line.strip() == "---":
            separator_count += 1
            continue

        if separator_count < 1:
            continue  # skip template section

        stripped = line.strip()
        
        # headings.append((1, stripped[2:]))
        
        if stripped.startswith("#"):
            debugPrint(stripped)

        if stripped.startswith("# "):
            headings.append((0, stripped[1:]))
        elif stripped.startswith("## "):
            headings.append((1, stripped[2:]))
        elif stripped.startswith("### "):
            headings.append((2, stripped[3:]))
        elif stripped.startswith("#### ") and showSubEntries:
            headings.append((3, stripped[4:]))

    return headings
```

---

# [1.0.0] - 2026-03-22 

Finished and released.
