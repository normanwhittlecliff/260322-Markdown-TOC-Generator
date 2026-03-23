import re

# OPTIONS

showSubEntries = False;


def slugify(text):
    """Convert heading text into a markdown anchor link."""
    # Remove emojis and non-text symbols
    text = re.sub(r'[^\w\s-]', '', text)
    # Lowercase
    text = text.lower()
    # Replace spaces with hyphens
    text = re.sub(r'\s+', '-', text)
    return text


def extract_headings(lines):
    # Extract headings and store (level, text).
    headings = []
  
    headings = []
    separator_count = 0

    for line in lines:
        if line.strip() == "---":
            separator_count += 1
            continue

        if separator_count < 2:
            continue  # skip template section

        stripped = line.strip()
        
        # headings.append((1, stripped[2:]))

        if stripped.startswith("# "):
            headings.append((0, stripped[1:]))
        elif stripped.startswith("## "):
            headings.append((1, stripped[2:]))
        elif stripped.startswith("### "):
            headings.append((2, stripped[3:]))
        elif stripped.startswith("#### ") and showSubEntries:
            headings.append((3, stripped[4:]))

    return headings


def generate_toc(headings):
    # Generate markdown Table of Contents.
    toc_lines = []
    toc_lines.append("## 📚 Table of Contents\n\n")

    for level, text in headings:
        anchor = slugify(text)
        if (level == 0):
            toc_lines.append(f"[{text}](#{anchor})\n\n")
            continue;
        indent = "  " * (level - 1)
        toc_lines.append(f"{indent}- [{text}](#{anchor})\n\n")
        # toc_lines.append(f"[{text}](#{anchor})\n\n")

    toc_lines.append("\n\n---\n\n")
    return toc_lines


def insert_toc(filePath):
    with open(filePath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Extract headings
    headings = extract_headings(lines)

    # Generate TOC
    toc = generate_toc(headings)

    # Find first '---'
    insert_index = None
    for i, line in enumerate(lines):
        if line.strip() == "---":
            insert_index = i + 1
            break

    if insert_index is None:
        print("No '---' separator found.")
        return

    # Insert TOC
    new_lines = lines[:insert_index] + ["\n"] + toc + lines[insert_index:]

    # Write back to file
    with open(filePath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print("✅ Table of Contents inserted successfully!")
    
def remove_existing_toc(filePath):
    with open(filePath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Step 1: Find first '---'
    first_sep = None
    for i, line in enumerate(lines):
        if line.strip() == "---":
            first_sep = i
            break

    if first_sep is None:
        print("No '---' separator found.")
        return

    # Step 2: Check if TOC starts after it
    toc_start = None
    for i in range(first_sep + 1, len(lines)):
        if re.match(r'##\s+📚\s+Table of Contents', lines[i]):
            toc_start = i
            break
        # If we hit another separator first, no TOC exists
        if lines[i].strip() == "---":
            break

    if toc_start is None:
        print("No existing TOC found.")
        return

    # Step 3: Find end of TOC (next '---')
    toc_end = None
    for i in range(toc_start, len(lines)):
        if lines[i].strip() == "---":
            toc_end = i
            break

    if toc_end is None:
        print("TOC end separator not found.")
        return

    # Step 4: Remove TOC block
    new_lines = lines[:first_sep + 1] + ["\n"] + lines[toc_end + 1:]

    # Step 5: Write file back
    with open(filePath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print("🧹 Existing TOC removed successfully!")





# ==== USAGE ====

filePath = input("Enter the file path:")
# filePath = "C:\\Users\\norma\\Projects\\260322 Python MarkDown TOC Creator\\Test.md"

if filePath[0] == "\"":
    filePath = filePath[1:(len(filePath) - 1)]
if not (filePath[len(filePath)-3:] == ".md"):
    filePath = filePath + ".md"

remove_existing_toc(filePath)
insert_toc(filePath)

#input("\n\nScript finished.\nClick Enter to close it.")
