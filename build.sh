#!/bin/bash

# Build the resume PDF
xelatex resume.tex

# Run twice to resolve cross-references
xelatex resume.tex

# Clean up auxiliary files
rm -f *.aux *.log *.out

# Run ATS scorer if Python 3 is available
if command -v python3 &> /dev/null; then
    # Check if pdfplumber is installed
    if python3 -c "import pdfplumber" 2> /dev/null; then
        python3 ats_scorer.py resume.pdf
    else
        echo ""
        echo "⚠️  ATS Scorer requires pdfplumber. Install with:"
        echo "   pip install pdfplumber"
        echo ""
    fi
else
    echo "⚠️  Python 3 not found. Skipping ATS score."
fi