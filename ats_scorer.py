#!/usr/bin/env python3
"""
ATS (Applicant Tracking System) Resume Scorer
Analyzes resume PDF and provides an ATS compatibility score
"""

import sys
import re
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("Error: pdfplumber not installed. Install with: pip install pdfplumber")
    sys.exit(1)


class ATSScorer:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = ""
        self.score = 0
        self.max_score = 100
        self.feedback = []

    def extract_text(self):
        """Extract text from PDF"""
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                self.text = "\n".join(page.extract_text() for page in pdf.pages)
            return True
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return False

    def check_contact_info(self):
        """Check for contact information"""
        points = 0
        max_points = 15

        # Email
        if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', self.text):
            points += 5
        else:
            self.feedback.append("⚠️  Missing email address")

        # Phone
        if re.search(r'\+?\d[\d\s\-\(\)]{8,}\d', self.text):
            points += 5
        else:
            self.feedback.append("⚠️  Missing phone number")

        # LinkedIn or professional link
        if re.search(r'linkedin\.com', self.text, re.IGNORECASE):
            points += 3

        # Location
        if re.search(r'\b[A-Z][a-z]+,\s*[A-Z][a-z]+\b', self.text):
            points += 2

        self.score += points
        if points == max_points:
            self.feedback.append("✓ Contact information complete")

    def check_sections(self):
        """Check for standard resume sections"""
        points = 0
        max_points = 20

        sections = {
            'Experience': [r'\bexperience\b', r'\bwork history\b', r'\bemployment\b'],
            'Education': [r'\beducation\b', r'\bacademic\b'],
            'Skills': [r'\bskills\b', r'\bcompetencies\b', r'\btechnical skills\b'],
            'Summary': [r'\bsummary\b', r'\bobjective\b', r'\bprofile\b'],
        }

        found_sections = []
        for section, patterns in sections.items():
            if any(re.search(pattern, self.text, re.IGNORECASE) for pattern in patterns):
                points += 5
                found_sections.append(section)

        self.score += points
        if found_sections:
            self.feedback.append(f"✓ Found sections: {', '.join(found_sections)}")

        missing = set(sections.keys()) - set(found_sections)
        if missing:
            self.feedback.append(f"⚠️  Missing sections: {', '.join(missing)}")

    def check_keywords(self):
        """Check for relevant technical keywords"""
        points = 0
        max_points = 25

        # Common technical/professional keywords
        keywords = [
            r'\b(python|java|javascript|c\+\+|golang?|rust)\b',
            r'\b(aws|azure|gcp|cloud|kubernetes|docker)\b',
            r'\b(machine learning|ml|ai|llm|deep learning)\b',
            r'\b(sql|database|mongodb|postgresql)\b',
            r'\b(api|rest|grpc|microservices)\b',
            r'\b(git|ci/cd|devops|agile)\b',
            r'\b(led|managed|architected|designed|implemented|developed)\b',
        ]

        keyword_count = 0
        for pattern in keywords:
            if re.search(pattern, self.text, re.IGNORECASE):
                keyword_count += 1

        points = min(keyword_count * 4, max_points)
        self.score += points

        if keyword_count >= 5:
            self.feedback.append(f"✓ Good keyword density ({keyword_count} categories found)")
        else:
            self.feedback.append(f"⚠️  Low keyword density ({keyword_count} categories found)")

    def check_formatting(self):
        """Check formatting quality"""
        points = 0
        max_points = 15

        # Bullet points
        if self.text.count('•') > 5 or self.text.count('◦') > 5:
            points += 5
            self.feedback.append("✓ Uses bullet points effectively")
        else:
            self.feedback.append("⚠️  Consider using more bullet points")

        # Action verbs
        action_verbs = r'\b(led|managed|developed|designed|implemented|architected|built|created|improved|optimized|reduced|increased)\b'
        action_count = len(re.findall(action_verbs, self.text, re.IGNORECASE))
        if action_count > 10:
            points += 5
            self.feedback.append(f"✓ Strong action verbs ({action_count} found)")
        else:
            self.feedback.append(f"⚠️  Use more action verbs (only {action_count} found)")

        # Quantifiable achievements
        numbers = len(re.findall(r'\d+[%+]|\d+\s*(?:million|billion|thousand|M\+|B\+|K\+)', self.text))
        if numbers > 5:
            points += 5
            self.feedback.append(f"✓ Good use of metrics ({numbers} found)")
        else:
            self.feedback.append(f"⚠️  Add more quantifiable achievements ({numbers} found)")

        self.score += points

    def check_length(self):
        """Check resume length"""
        points = 0
        max_points = 10

        word_count = len(self.text.split())

        # Ideal range: 400-800 words (roughly 1-2 pages)
        if 400 <= word_count <= 1000:
            points = max_points
            self.feedback.append(f"✓ Good length ({word_count} words)")
        elif word_count < 400:
            points = 5
            self.feedback.append(f"⚠️  Resume might be too short ({word_count} words)")
        else:
            points = 7
            self.feedback.append(f"⚠️  Resume might be too long ({word_count} words)")

        self.score += points

    def check_readability(self):
        """Check for readability issues"""
        points = 0
        max_points = 15

        # Check for common ATS problematic elements in text
        text_lower = self.text.lower()

        # Personal pronouns (should avoid)
        pronouns = len(re.findall(r'\b(i|me|my|we|our)\b', text_lower))
        if pronouns < 3:
            points += 5
            self.feedback.append("✓ Good: minimal personal pronouns")
        else:
            self.feedback.append(f"⚠️  Too many personal pronouns ({pronouns} found)")

        # Check for clear date formats
        dates = len(re.findall(r'\b\d{4}\b|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}\b', self.text))
        if dates > 3:
            points += 5
            self.feedback.append("✓ Clear date formatting")

        # Consistent formatting
        if len(self.text.splitlines()) > 20:
            points += 5

        self.score += points

    def analyze(self):
        """Run all checks and calculate score"""
        if not self.extract_text():
            return False

        self.check_contact_info()
        self.check_sections()
        self.check_keywords()
        self.check_formatting()
        self.check_length()
        self.check_readability()

        return True

    def print_results(self):
        """Print the ATS score and feedback"""
        print("\n" + "="*60)
        print("🤖 ATS RESUME COMPATIBILITY SCORE")
        print("="*60)

        # Calculate percentage
        percentage = (self.score / self.max_score) * 100

        # Color coding
        if percentage >= 80:
            grade = "EXCELLENT ✓"
            color = "\033[92m"  # Green
        elif percentage >= 60:
            grade = "GOOD"
            color = "\033[93m"  # Yellow
        else:
            grade = "NEEDS IMPROVEMENT"
            color = "\033[91m"  # Red

        reset = "\033[0m"

        print(f"\n{color}Score: {self.score}/{self.max_score} ({percentage:.1f}%) - {grade}{reset}\n")

        print("Feedback:")
        print("-" * 60)
        for item in self.feedback:
            print(f"  {item}")

        print("\n" + "="*60)
        print("\n💡 ATS Tips:")
        print("  • Use standard section headers (Experience, Education, Skills)")
        print("  • Include relevant keywords from job descriptions")
        print("  • Use bullet points with action verbs and metrics")
        print("  • Keep formatting simple (avoid complex tables/graphics)")
        print("  • Save as PDF to preserve formatting")
        print("="*60 + "\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python ats_scorer.py <resume.pdf>")
        sys.exit(1)

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        print(f"Error: File '{pdf_path}' not found")
        sys.exit(1)

    scorer = ATSScorer(pdf_path)
    if scorer.analyze():
        scorer.print_results()
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
