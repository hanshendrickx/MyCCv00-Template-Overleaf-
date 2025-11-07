# Overleaf Book Template

A comprehensive LaTeX template for writing academic and professional books on Overleaf.

## Features

- **Book document class** with proper formatting for two-sided printing
- **Front matter** including title page, dedication, abstract, table of contents, and preface
- **Main chapters** with structured content and cross-referencing
- **Back matter** with bibliography and appendix
- **Mathematical support** with theorem environments, equations, and proofs
- **Bibliography management** using BibLaTeX with author-year citation style
- **Figure and table support** with automatic numbering and referencing
- **Hyperlinks** for easy navigation in PDF output

## Structure

```
.
├── main.tex                 # Main LaTeX file
├── references.bib          # Bibliography database
├── chapters/
│   ├── chapter1.tex        # Introduction chapter
│   ├── chapter2.tex        # Main concepts chapter
│   ├── chapter3.tex        # Applications chapter
│   └── appendix.tex        # Appendix with additional resources
└── README.md               # This file
```

## Getting Started

### On Overleaf

1. Upload all files to a new Overleaf project
2. Set `main.tex` as the main document
3. Compile using PDFLaTeX (recommended) or XeLaTeX
4. For bibliography, the compiler will automatically run BibTeX/Biber

### Locally

To compile this document locally, you need a LaTeX distribution (e.g., TeX Live, MikTeX):

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

Or use latexmk for automatic compilation:

```bash
latexmk -pdf main.tex
```

## Customization

### Document Information

Edit the following lines in `main.tex`:

```latex
\title{Your Book Title Here}
\author{Your Name}
\date{\today}
```

### Adding Chapters

1. Create a new `.tex` file in the `chapters/` directory
2. Add `\include{chapters/yourchapter}` in the main matter section of `main.tex`

### Bibliography

Add your references to `references.bib` following BibTeX format. Citation styles and formats can be customized in the preamble of `main.tex`.

### Page Layout

Adjust margins and spacing in the preamble:

```latex
\usepackage[margin=2.5cm]{geometry}  % Adjust margins
\usepackage{setspace}                 % Line spacing
```

## Included Packages

- **inputenc/fontenc**: Character encoding and font handling
- **babel**: Language support
- **amsmath/amssymb/amsthm**: Mathematical typesetting
- **graphicx**: Image inclusion
- **geometry**: Page layout
- **fancyhdr**: Custom headers and footers
- **hyperref**: Hyperlinks and PDF metadata
- **biblatex**: Bibliography management
- **xcolor**: Color support
- **csquotes**: Quotation marks

## Tips

- Use `\label{}` and `\ref{}` for cross-referencing
- Use `\cite{}` for citations
- Use `\eqref{}` for equation references
- Comment out `\listoffigures` and `\listoftables` if not needed
- Customize theorem styles in the preamble

## License

This template is provided under the MIT License. See LICENSE file for details.

## Contributing

Feel free to suggest improvements or report issues!