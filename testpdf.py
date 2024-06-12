import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit

class VoiceComparisonReport(QMainWindow):
    def __init__(self, results):
        super().__init__()
        self.results = results
        self.setWindowTitle('Forensic Voice Comparison Report')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.title_label = QLabel("<h1>Forensic Voice Comparison Report</h1>")
        self.layout.addWidget(self.title_label)

        self.report_text_edit = QTextEdit()
        self.report_text_edit.setReadOnly(True)
        self.layout.addWidget(self.report_text_edit)

        self.generate_report_button = QPushButton("Generate Report")
        self.generate_report_button.clicked.connect(self.generate_report)
        self.layout.addWidget(self.generate_report_button)

    def generate_report(self):
        report_text = f"""
        # Forensic Voice Comparison Report

        ## Introduction

        **Case ID:** {self.results['case_id']}  
        **Date:** {self.results['date']}  
        **Analyst:** {self.results['analyst']}

        ## Methodology

        1. **Data Collection:**  
           Two voice samples were provided for analysis:
           - **Suspect Voice Sample:** {self.results['suspect_sample']}
           - **Crime Scene Voice Sample:** {self.results['crime_scene_sample']}

        2. **Pre-processing:**  
           The audio files were converted to a consistent format (WAV) and sampled at 16 kHz. Noise reduction techniques were applied to enhance the quality of the recordings.

        3. **Feature Extraction:**  
           Acoustic features such as Mel-Frequency Cepstral Coefficients (MFCCs), pitch, and formants were extracted from both voice samples.

        4. **Comparison:**  
           A Gaussian Mixture Model (GMM) was used to compare the features of the two voice samples. The similarity score was calculated based on the likelihood ratio, which indicates the probability that the samples are from the same source versus different sources.

        ## Analysis

        ### Feature Extraction

        **Suspect Voice Sample:**  
        - Duration: {self.results['suspect_duration']} seconds
        - Sampling Rate: {self.results['sampling_rate']} kHz
        - MFCCs: Extracted {self.results['mfcc_count']} coefficients per frame

        **Crime Scene Voice Sample:**  
        - Duration: {self.results['crime_scene_duration']} seconds
        - Sampling Rate: {self.results['sampling_rate']} kHz
        - MFCCs: Extracted {self.results['mfcc_count']} coefficients per frame

        ### Comparison

        The following acoustic features were analyzed and compared:
        - **MFCCs:** Mean and variance of the coefficients
        - **Pitch:** Average pitch and pitch range
        - **Formants:** Frequencies of the first three formants (F1, F2, F3)

        ### Likelihood Ratio Calculation

        The likelihood ratio (LR) was calculated using the extracted features:
        \[ \text{{LR}} = \frac{{P(\text{{features}} | \text{{same speaker}})}}{{P(\text{{features}} | \text{{different speakers}})}} \]

        **Results:**
        - **Mean MFCCs Similarity Score:** {self.results['mfcc_similarity']}
        - **Pitch Similarity Score:** {self.results['pitch_similarity']}
        - **Formant Similarity Score:** {self.results['formant_similarity']}
        - **Overall Likelihood Ratio (LR):** {self.results['likelihood_ratio']}

        ## Results

        The likelihood ratio of {self.results['likelihood_ratio']} suggests that the probability of the two voice samples being from the same individual is significantly higher than being from different individuals. This indicates a strong similarity between the suspect's voice sample and the crime scene voice sample.

        ## Conclusion

        Based on the analysis conducted, there is strong evidence to suggest that the suspect's voice is likely the same as the voice recorded at the crime scene. The high likelihood ratio supports the hypothesis that the two voice samples originate from the same speaker.

        **Recommendations:**
        - Further forensic examination and corroboration with additional evidence are advised to strengthen the findings.
        - Consideration of context and other case-specific factors should be taken into account when interpreting the results.

        ---

        **{self.results['analyst']}**  
        Forensic Analyst
        """
        self.report_text_edit.setPlainText(report_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Results from voice comparison analysis (replace with actual results)
    analysis_results = {
        'case_id': '123456',
        'date': 'June 12, 2024',
        'analyst': 'Shadrack Asante Kajigili',
        'suspect_sample': 'suspect_sample.wav',
        'crime_scene_sample': 'crime_scene_sample.wav',
        'suspect_duration': 30,
        'crime_scene_duration': 25,
        'sampling_rate': 16,
        'mfcc_count': 13,
        'mfcc_similarity': 0.85,
        'pitch_similarity': 0.80,
        'formant_similarity': 0.75,
        'likelihood_ratio': 8.5
    }

    main_window = VoiceComparisonReport(analysis_results)
    main_window.show()

    sys.exit(app.exec_())
