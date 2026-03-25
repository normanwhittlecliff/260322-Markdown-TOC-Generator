# TOC Generator for Markdown Files

A simple Python tool that automatically generates and maintains a **Table of Contents (TOC)** for my personal markdown diary, inspired by structured journaling systems with Years, Chapters, Entries, and Subentries.

---

## Information
- **Project ID**: 260322
- **Title**: TOC Generator for Markdown Files
- **Creator**: Norman Santos (normanwhittlecliff)
- **Date of Creation**: March 22, 2026
- **Language**: Python
- **Change Log**: [CHANGELOG.md](https://github.com/normanwhittlecliff/260322-Markdown-TOC-Generator/blob/main/CHANGELOG.md)

---

## Features

* Scans markdown files for headings:

  * `#` → Year
  * `##` → Chapter
  * `###` → Entry
  * `####` → Sub Entry

* Builds a hierarchical, clickable Table of Contents

* Removes existing TOC before generating a new one

* Automatically inserts TOC after the first `---` separator

* Fully customizable parsing logic (no regex required)

---

## Example Structure

Your markdown file can look like this:

```md
# Max - Norman’s Journal

---

# 🗂️ 2025 - The Year Things Actually Happened™

## 📖 Chapter 03 - The Princesa Arc

### 🗓️ Aug 30, 2025 - Meeting Petrova

#### ⏰ 09:25 — Getting the Ride
```

And the script will generate:

```md
## 📚 Table of Contents

- [🗂️ 2025 - The Year Things Actually Happened™](#2025---the-year-things-actually-happened)
  - [📖 Chapter 03 - The Princesa Arc](#chapter-03---the-princesa-arc)
    - [🗓️ Aug 30, 2025 - Meeting Petrova](#aug-30-2025---meeting-petrova)
      - [⏰ 09:25 — Getting the Ride](#0925--getting-the-ride)
```

---

## Installation

No external dependencies required — just Python 3.

---

## Usage

Edit the script and set your file path:

```python
file_path = "your_diary.md"
```

Then run:

```bash
python main.py
```

---

## 📜 License

This project is open-source and free to use.

---

## 👤 Author

**Norman Whittlecliff (Norman Santos)**

---

> *“This isn’t just a diary. It’s a system for remembering who I was.”*
