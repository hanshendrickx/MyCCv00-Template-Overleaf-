# Contributing to the Book Template

Thank you for using this Overleaf book template! This guide will help you customize it for your needs.

## Quick Start Customization

### 1. Update Book Information

In `main.tex`, modify these lines:

```latex
\title{Your Book Title Here}
\author{Your Name}
\date{\today}
```

Also update the PDF metadata in the hyperref setup:

```latex
\hypersetup{
    pdftitle={Book Title},
    pdfauthor={Author Name},
}
```

### 2. Customize Front Matter

Edit or remove these sections in `main.tex`:
- **Dedication**: Remove or modify the dedication page
- **Abstract**: Write your book's abstract
- **Preface**: Add your preface content
- **Table of Contents**: Automatically generated
- **List of Figures/Tables**: Uncomment if needed

### 3. Add Your Chapters

#### Method 1: Edit Existing Chapters
Simply replace the content in `chapters/chapter1.tex`, `chapters/chapter2.tex`, etc.

#### Method 2: Add New Chapters
1. Create a new file: `chapters/chapter4.tex`
2. Add this line in `main.tex` in the main matter section:
   ```latex
   \include{chapters/chapter4}
   ```

### 4. Add References

Add your bibliography entries to `references.bib` in BibTeX format. Example:

```bibtex
@book{yourkey2023,
  author    = {Author Name},
  title     = {Book Title},
  publisher = {Publisher},
  year      = {2023}
}
```

Then cite in your text using `\cite{yourkey2023}`.

### 5. Add Figures

1. Create a `figures/` directory
2. Add your image files (PNG, JPG, PDF recommended)
3. Include in your chapter:
   ```latex
   \begin{figure}[htbp]
       \centering
       \includegraphics[width=0.8\textwidth]{figures/myimage.png}
       \caption{Description of the figure}
       \label{fig:myimage}
   \end{figure}
   ```

### 6. Customize Styling

#### Change Margins
```latex
\usepackage[margin=2.5cm]{geometry}  % Adjust values
```

#### Change Line Spacing
```latex
\onehalfspacing  % or \doublespacing
```

#### Change Font Size
```latex
\documentclass[11pt,a4paper,twoside,openright]{book}  % Change 12pt to 11pt or 10pt
```

## Advanced Customization

### Add More Theorem Environments

In the preamble of `main.tex`, add:

```latex
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{axiom}[theorem]{Axiom}
```

### Change Citation Style

Modify the biblatex package options:

```latex
\usepackage[style=numeric,backend=biber]{biblatex}  % For numeric citations
\usepackage[style=alphabetic,backend=biber]{biblatex}  % For alphabetic citations
```

### Add Index

1. Uncomment `\printindex` in `main.tex`
2. Add `\usepackage{makeidx}` to the preamble
3. Add `\makeindex` before `\begin{document}`
4. Mark index entries in text: `\index{keyword}`

## Compiling on Overleaf

1. Upload all files to Overleaf
2. Set `main.tex` as the main document
3. Click "Recompile" (Ctrl+Enter / Cmd+Enter)

## Compiling Locally

### Using latexmk (recommended)
```bash
latexmk -pdf main.tex
```

### Manual compilation
```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

## Tips

- Save frequently while editing
- Use comments (`%`) to temporarily disable sections
- Keep chapter files modular for easier management
- Use descriptive labels for cross-references
- Preview often to catch errors early

## Getting Help

- LaTeX Documentation: https://www.latex-project.org/help/documentation/
- Overleaf Documentation: https://www.overleaf.com/learn
- TeX Stack Exchange: https://tex.stackexchange.com/

## Reporting Issues

If you find problems with this template, please report them on the repository's issue tracker.
