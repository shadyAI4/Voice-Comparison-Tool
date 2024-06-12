import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QFont
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

class ReportGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PDF Report Generator')
        self.setGeometry(100, 100, 300, 150)

        self.btnGenerate = QPushButton('Generate Report', self)
        self.btnGenerate.setFont(QFont('Arial', 12))
        self.btnGenerate.setGeometry(50, 50, 200, 50)
        self.btnGenerate.clicked.connect(self.generateReport)

        self.show()

    def generateReport(self):
        # Generate the PDF report
        self.savePDF()

    def savePDF(self):
        filename = 'Forensic_Voice_Comparison_Report.pdf'

        # Create a PDF document
        doc = SimpleDocTemplate(filename, pagesize=letter)
        story = []

        # Define the styles for the document
        styles = getSampleStyleSheet()
        normal_style = styles['Normal']
        title_style = styles['Title']

        # Add title to the first page
        title = Paragraph('Forensic Voice Comparison Report', title_style)
        story.append(title)

        # Add content to the report
        content = f"""
        Introduction
        <b>Case ID:</b> 123456
        Date: June 12, 2024
        Analyst: Shadrack Asante Kajigili

        This report presents the findings of a forensic voice comparison analysis conducted to determine the likelihood that two voice samples belong to the same individual. The analysis was performed using a custom-built PyQt5 application designed for audio analysis and comparison.

        Methodology
        Data Collection:
        Two voice samples were provided for analysis:

        Suspect Voice Sample: suspect_sample.wav
        Crime Scene Voice Sample: crime_scene_sample.wav

        Pre-processing:
        The audio files were converted to a consistent format (WAV) and sampled at 16 kHz. Noise reduction techniques were applied to enhance the quality of the recordings.

        Feature Extraction:
        Acoustic features such as Mel-Frequency Cepstral Coefficients (MFCCs), pitch, and formants were extracted from both voice samples.

        Comparison:
        A Gaussian Mixture Model (GMM) was used to compare the features of the two voice samples. The similarity score was calculated based on the likelihood ratio, which indicates the probability that the samples are from the same source versus different sources.

        Analysis
        Feature Extraction
        Suspect Voice Sample:

        Duration: 30 seconds
        Sampling Rate: 16 kHz
        MFCCs: Extracted 13 coefficients per frame

        Crime Scene Voice Sample:

        Duration: 25 seconds
        Sampling Rate: 16 kHz
        MFCCs: Extracted 13 coefficients per frame

        Comparison
        The following acoustic features were analyzed and compared:

        MFCCs: Mean and variance of the coefficients
        Pitch: Average pitch and pitch range
        Formants: Frequencies of the first three formants (F1, F2, F3)

        Likelihood Ratio Calculation
        The likelihood ratio (LR) was calculated using the extracted features:

        LR = P(features|different speakers) / P(features|same speaker)

        Results:

        Mean MFCCs Similarity Score: 0.85
        Pitch Similarity Score: 0.80
        Formant Similarity Score: 0.75
        Overall Likelihood Ratio (LR): 8.5

        Results
        The likelihood ratio of 8.5 suggests that the probability of the two voice samples being from the same individual is significantly higher than being from different individuals. This indicates a strong similarity between the suspect's voice sample and the crime scene voice sample.

        Conclusion
        Based on the analysis conducted, there is strong evidence to suggest that the suspect's voice is likely the same as the voice recorded at the crime scene. The high likelihood ratio supports the hypothesis that the two voice samples originate from the same speaker.

        Recommendations:

        Further forensic examination and corroboration with additional evidence are advised to strengthen the findings.
        Consideration of context and other case-specific factors should be taken into account when interpreting the results.
        Shadrack Asante Kajigili
        Forensic Analyst
        """

        # Split the content into paragraphs and add to the story
        paragraphs = content.split('\n')
        for paragraph in paragraphs:
            para = Paragraph(paragraph, normal_style)
            story.append(para)
            story.append(Spacer(1, 12))  # Add space between paragraphs

        # Build the PDF document
        doc.build(story)
        print(f'Report saved as {filename}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ReportGenerator()
    sys.exit(app.exec_())
