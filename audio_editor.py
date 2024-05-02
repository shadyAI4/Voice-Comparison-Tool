# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtCore import QUrl, QTimer
# from PyQt5.QtGui import QIcon
# from pydub import AudioSegment
# import sys
# import os
# import pyqtgraph as pg
#
# class AudioEditor(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Audio Editor")
#         self.setGeometry(100, 100, 800, 400)
#
#         self.media_player = QMediaPlayer(self)
#         self.media_player.setVolume(50)
#         self.media_player.mediaStatusChanged.connect(self.update_waveform)
#
#         self.play_button = QPushButton(QIcon("play_icon.png"), "Play", self)
#         self.play_button.clicked.connect(self.play_audio)
#
#         self.trim_button = QPushButton(QIcon("trim_icon.png"), "Trim", self)
#         self.trim_button.clicked.connect(self.trim_audio)
#
#         self.waveform_plot = pg.PlotWidget()
#         self.waveform_plot.showGrid(x=True, y=True)
#         self.waveform_plot.setLabel("left", "Amplitude")
#         self.waveform_plot.setLabel("bottom", "Time (s)")
#
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.play_button)
#         self.layout.addWidget(self.trim_button)
#         self.layout.addWidget(self.waveform_plot)
#
#         self.central_widget = QWidget()
#         self.central_widget.setLayout(self.layout)
#         self.setCentralWidget(self.central_widget)
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_waveform)
#         self.timer.start(100)
#
#     def play_audio(self):
#         file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")
#         if file_path:
#             self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
#             self.media_player.play()
#
#     def trim_audio(self):
#         start_time = self.waveform_plot.region.getRegion()[0] * 1000  # Convert to milliseconds
#         end_time = self.waveform_plot.region.getRegion()[1] * 1000    # Convert to milliseconds
#
#         file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File to Trim", "", "Audio Files (*.mp3 *.wav)")
#         if file_path:
#             audio = AudioSegment.from_file(file_path)
#
#             trimmed_audio = audio[start_time:end_time]
#
#             output_file_path, _ = QFileDialog.getSaveFileName(self, "Save Trimmed Audio", "", "Audio Files (*.mp3 *.wav)")
#             if output_file_path:
#                 trimmed_audio.export(output_file_path, format=os.path.splitext(output_file_path)[1][1:])  # Export audio
#
#     def update_waveform(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             position = self.media_player.position() / 1000  # Convert to seconds
#             duration = self.media_player.duration() / 1000  # Convert to seconds
#             self.waveform_plot.clear()
#             self.waveform_plot.plot([0, duration], [0, 0], pen=pg.mkPen("k", width=2))
#             self.waveform_plot.plot([position, position], [-1, 1], pen=pg.mkPen("r", width=2))
#             self.waveform_plot.region = pg.LinearRegionItem([0, duration])
#             self.waveform_plot.addItem(self.waveform_plot.region)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     editor = AudioEditor()
#     editor.show()
#     sys.exit(app.exec_())




#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtCore import QUrl, Qt
# from PyQt5.QtGui import QIcon
# import sys
# import os
# import pyqtgraph as pg
# from pydub import AudioSegment
#
# class AudioEditor(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Audio Editor")
#         self.setGeometry(100, 100, 800, 400)
#
#         self.media_player = QMediaPlayer(self)
#         self.media_player.setVolume(50)
#         self.media_player.mediaStatusChanged.connect(self.update_waveform)
#
#         self.play_button = QPushButton(QIcon("play_icon.png"), "Play", self)
#         self.play_button.clicked.connect(self.play_audio)
#
#         self.trim_button = QPushButton(QIcon("trim_icon.png"), "Trim", self)
#         self.trim_button.clicked.connect(self.trim_audio)
#
#         self.waveform_plot = pg.PlotWidget()
#         self.waveform_plot.showGrid(x=True, y=True)
#         self.waveform_plot.setLabel("left", "Amplitude")
#         self.waveform_plot.setLabel("bottom", "Time (s)")
#
#         self.region = pg.LinearRegionItem()
#         self.region.setZValue(-10)  # Ensure region is drawn below other items
#         self.region.setMovable(True)
#         self.region.setBrush(pg.mkBrush("#377eb8"))
#         self.region.setRegion([0, 1])  # Default region from 0 to 1 second
#         self.region.sigRegionChanged.connect(self.update_trim_region)
#
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.play_button)
#         self.layout.addWidget(self.trim_button)
#         self.layout.addWidget(self.waveform_plot)
#
#         self.central_widget = QWidget()
#         self.central_widget.setLayout(self.layout)
#         self.setCentralWidget(self.central_widget)
#
#     def play_audio(self):
#         file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")
#         if file_path:
#             self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
#             self.media_player.play()
#
#     def trim_audio(self):
#         file_path = self.media_player.media().canonicalUrl().toLocalFile()
#         audio = AudioSegment.from_file(file_path)
#
#         start_time = self.region.getRegion()[0] * 1000  # Convert to milliseconds
#         end_time = self.region.getRegion()[1] * 1000  # Convert to milliseconds
#
#         trimmed_audio = audio[start_time:end_time]
#
#         output_file_path, _ = QFileDialog.getSaveFileName(self, "Save Trimmed Audio", "", "Audio Files (*.mp3 *.wav)")
#         if output_file_path:
#             output_format = os.path.splitext(output_file_path)[1][1:]  # Get the file extension for output format
#             trimmed_audio.export(output_file_path, format=output_format)  # Export audio with specified format
#
#     def update_waveform(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             position = self.media_player.position() / 1000  # Convert to seconds
#             duration = self.media_player.duration() / 1000  # Convert to seconds
#             self.waveform_plot.clear()
#             self.waveform_plot.plot([0, duration], [0, 0], pen=pg.mkPen("k", width=2))
#             self.waveform_plot.addItem(self.region)
#             self.region.setRegion([0, duration])
#             self.region.setMovable(True)
#             self.region.setLimits([0, duration])
#             self.waveform_plot.setXRange(0, duration)
#         else:
#             self.waveform_plot.clear()
#
#     def update_trim_region(self):
#         self.media_player.pause()  # Pause playback while selecting trim region
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     editor = AudioEditor()
#     editor.show()
#     sys.exit(app.exec_())




# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtCore import QUrl, Qt
# from PyQt5.QtGui import QIcon
# import sys
# import os
# import pyqtgraph as pg
# from pydub import AudioSegment
#
# class AudioEditor(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Audio Editor")
#         self.setGeometry(100, 100, 800, 400)
#
#         self.media_player = QMediaPlayer(self)
#         self.media_player.setVolume(50)
#         self.media_player.mediaStatusChanged.connect(self.update_waveform)
#
#         self.play_button = QPushButton(QIcon("play_icon.png"), "Play", self)
#         self.play_button.clicked.connect(self.play_audio)
#
#         self.trim_button = QPushButton(QIcon("trim_icon.png"), "Trim", self)
#         self.trim_button.clicked.connect(self.trim_audio)
#
#         self.waveform_plot = pg.PlotWidget()
#         self.waveform_plot.showGrid(x=True, y=True)
#         self.waveform_plot.setLabel("left", "Amplitude")
#         self.waveform_plot.setLabel("bottom", "Time (s)")
#
#         self.region = pg.LinearRegionItem()
#         self.region.setZValue(-10)  # Ensure region is drawn below other items
#         self.region.setMovable(True)
#         self.region.setBrush(pg.mkBrush("#377eb8"))
#         self.region.setRegion([0, 1])  # Default region from 0 to 1 second
#         self.region.sigRegionChanged.connect(self.update_trim_region)
#
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.play_button)
#         self.layout.addWidget(self.trim_button)
#         self.layout.addWidget(self.waveform_plot)
#
#         self.central_widget = QWidget()
#         self.central_widget.setLayout(self.layout)
#         self.setCentralWidget(self.central_widget)
#
#     def play_audio(self):
#         file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")
#         print(file_path)
#         if file_path:
#             self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
#             self.media_player.play()
#
    # def trim_audio(self):
    #     file_path = self.media_player.media().canonicalUrl().toLocalFile()
    #     if not file_path:
    #         QMessageBox.warning(self, "No Audio File", "Please select an audio file to trim.")
    #         return
    #
    #     audio = AudioSegment.from_file(file_path)
    #
    #     start_time = self.region.getRegion()[0] * 1000  # Convert to milliseconds
    #     end_time = self.region.getRegion()[1] * 1000    # Convert to milliseconds
    #
    #     trimmed_audio = audio[start_time:end_time]
    #
    #     output_file_path, _ = QFileDialog.getSaveFileName(self, "Save Trimmed Audio", "", "Audio Files (*.mp3 *.wav)")
    #     if output_file_path:
    #         output_format = os.path.splitext(output_file_path)[1][1:].lower()  # Get the file extension for output format
    #         if output_format in ['mp3', 'wav']:
    #             trimmed_audio.export(output_file_path, format=output_format)  # Export audio with specified format
    #         else:
    #             QMessageBox.warning(self, "Unsupported Format", "Unsupported output format. Please save as MP3 or WAV.")

#     def update_waveform(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             position = self.media_player.position() / 1000  # Convert to seconds
#             duration = self.media_player.duration() / 1000  # Convert to seconds
#             self.waveform_plot.clear()
#             self.waveform_plot.plot([0, duration], [0, 0], pen=pg.mkPen("k", width=2))
#             self.waveform_plot.addItem(self.region)
#             self.region.setRegion([0, duration])
#             self.region.setMovable(True)
#             self.region.setZValue(10)  # Ensure region is drawn above other items
#             self.waveform_plot.setXRange(0, duration)
#         else:
#             self.waveform_plot.clear()
#
#     def update_trim_region(self):
#         self.media_player.pause()  # Pause playback while selecting trim region
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     editor = AudioEditor()
#     editor.show()
#     sys.exit(app.exec_())











# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtCore import QUrl, Qt
# from PyQt5.QtGui import QIcon
# import sys
# import os
# import pyqtgraph as pg
# from pydub import AudioSegment
#
# class AudioEditor(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Audio Editor")
#         self.setGeometry(100, 100, 800, 400)
#
#         self.media_player = QMediaPlayer(self)
#         self.media_player.setVolume(50)
#         self.media_player.mediaStatusChanged.connect(self.update_waveform)
#
#         self.play_button = QPushButton(QIcon("play_icon.png"), "Play", self)
#         self.play_button.clicked.connect(self.play_audio)
#
#         self.trim_button = QPushButton(QIcon("trim_icon.png"), "Trim", self)
#         self.trim_button.clicked.connect(self.trim_audio)
#
#         self.waveform_plot = pg.PlotWidget()
#         self.waveform_plot.showGrid(x=True, y=True)
#         self.waveform_plot.setLabel("left", "Amplitude")
#         self.waveform_plot.setLabel("bottom", "Time (s)")
#
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.play_button)
#         self.layout.addWidget(self.trim_button)
#         self.layout.addWidget(self.waveform_plot)
#
#         self.central_widget = QWidget()
#         self.central_widget.setLayout(self.layout)
#         self.setCentralWidget(self.central_widget)
#
#         self.trim_start = 0
#         self.trim_end = 0
#
#     def play_audio(self):
#         file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")
#         if file_path:
#             self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
#             self.media_player.play()
#
#     def trim_audio(self):
#         if self.media_player.state() != QMediaPlayer.PlayingState:
#             QMessageBox.warning(self, "Playback Error", "Please play the audio before trimming.")
#             return
#
#         self.trim_start = self.waveform_plot.region.getRegion()[0] * 1000  # Convert to milliseconds
#         self.trim_end = self.waveform_plot.region.getRegion()[1] * 1000    # Convert to milliseconds
#
#         audio = AudioSegment.from_file(self.media_player.media().canonicalUrl().toLocalFile())
#
#         trimmed_audio = audio[self.trim_start:self.trim_end]
#
#         output_file_path, _ = QFileDialog.getSaveFileName(self, "Save Trimmed Audio", "", "Audio Files (*.mp3 *.wav)")
#         if output_file_path:
#             output_format = os.path.splitext(output_file_path)[1][1:].lower()  # Get the file extension for output format
#             if output_format in ['mp3', 'wav']:
#                 trimmed_audio.export(output_file_path, format=output_format)  # Export audio with specified format
#             else:
#                 QMessageBox.warning(self, "Unsupported Format", "Unsupported output format. Please save as MP3 or WAV.")
#
#     def update_waveform(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             position = self.media_player.position() / 1000  # Convert to seconds
#             duration = self.media_player.duration() / 1000  # Convert to seconds
#             self.waveform_plot.clear()
#             self.waveform_plot.plot([0, duration], [0, 0], pen=pg.mkPen("k", width=2))
#             self.waveform_plot.region = pg.LinearRegionItem([0, duration])
#             self.waveform_plot.addItem(self.waveform_plot.region)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     editor = AudioEditor()
#     editor.show()
#     sys.exit(app.exec_())







#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtCore import QUrl, QTimer
# from PyQt5.QtGui import QIcon
# import sys
# import os
# import pyqtgraph as pg
# from pydub import AudioSegment
#
# class AudioEditor(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Audio Editor")
#         self.setGeometry(100, 100, 800, 400)
#
#         self.media_player = QMediaPlayer(self)
#         self.media_player.setVolume(50)
#         self.media_player.mediaStatusChanged.connect(self.update_waveform)
#
#         self.play_button = QPushButton(QIcon("play_icon.png"), "Play", self)
#         self.play_button.clicked.connect(self.play_audio)
#
#         self.trim_button = QPushButton(QIcon("trim_icon.png"), "Trim", self)
#         self.trim_button.clicked.connect(self.trim_audio)
#
#         self.waveform_plot = pg.PlotWidget()
#         self.waveform_plot.showGrid(x=True, y=True)
#         self.waveform_plot.setLabel("left", "Amplitude")
#         self.waveform_plot.setLabel("bottom", "Time (s)")
#
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.play_button)
#         self.layout.addWidget(self.trim_button)
#         self.layout.addWidget(self.waveform_plot)
#
#         self.central_widget = QWidget()
#         self.central_widget.setLayout(self.layout)
#         self.setCentralWidget(self.central_widget)
#
#         self.trim_start = 0
#         self.trim_end = 0
#         self.playback_line = None
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_waveform)
#         self.timer.start(100)
#
#     def play_audio(self):
#         file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")
#         if file_path:
#             self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
#             self.media_player.play()
#
#     def trim_audio(self):
#         if self.media_player.state() != QMediaPlayer.PlayingState:
#             QMessageBox.warning(self, "Playback Error", "Please play the audio before trimming.")
#             return
#
#         self.trim_start = self.waveform_plot.region.getRegion()[0] * 1000  # Convert to milliseconds
#         self.trim_end = self.waveform_plot.region.getRegion()[1] * 1000    # Convert to milliseconds
#
#         audio = AudioSegment.from_file(self.media_player.media().canonicalUrl().toLocalFile())
#
#         trimmed_audio = audio[self.trim_start:self.trim_end]
#
#         output_file_path, _ = QFileDialog.getSaveFileName(self, "Save Trimmed Audio", "", "Audio Files (*.mp3 *.wav)")
#         if output_file_path:
#             output_format = os.path.splitext(output_file_path)[1][1:].lower()  # Get the file extension for output format
#             if output_format in ['mp3', 'wav']:
#                 trimmed_audio.export(output_file_path, format=output_format)  # Export audio with specified format
#             else:
#                 QMessageBox.warning(self, "Unsupported Format", "Unsupported output format. Please save as MP3 or WAV.")
#
#     def update_waveform(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             position = self.media_player.position() / 1000  # Convert to seconds
#             duration = self.media_player.duration() / 1000  # Convert to seconds
#             self.waveform_plot.clear()
#             self.waveform_plot.plot([0, duration], [0, 0], pen=pg.mkPen("k", width=2))
#
#             # Add a line indicating the playback position
#             if self.playback_line:
#                 self.waveform_plot.removeItem(self.playback_line)
#             self.playback_line = pg.InfiniteLine(pos=position, angle=90, movable=False, pen=pg.mkPen("r", width=2))
#             self.waveform_plot.addItem(self.playback_line)
#
#             self.waveform_plot.region = pg.LinearRegionItem([0, duration])
#             self.waveform_plot.addItem(self.waveform_plot.region)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     editor = AudioEditor()
#     editor.show()
#     sys.exit(app.exec_())


#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtCore import QUrl, QTimer
# from PyQt5.QtGui import QIcon
# import sys
# import os
# import pyqtgraph as pg
# from pydub import AudioSegment
#
# class AudioEditor(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Audio Editor")
#         self.setGeometry(100, 100, 800, 400)
#
#         self.media_player = QMediaPlayer(self)
#         self.media_player.setVolume(50)
#         self.media_player.mediaStatusChanged.connect(self.update_waveform)
#
#         self.play_button = QPushButton(QIcon("play_icon.png"), "Play", self)
#         self.play_button.clicked.connect(self.play_audio)
#
#         self.trim_button = QPushButton(QIcon("trim_icon.png"), "Trim", self)
#         self.trim_button.clicked.connect(self.trim_audio)
#
#         self.waveform_plot = pg.PlotWidget()
#         self.waveform_plot.showGrid(x=True, y=True)
#         self.waveform_plot.setLabel("left", "Amplitude")
#         self.waveform_plot.setLabel("bottom", "Time (s)")
#
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.play_button)
#         self.layout.addWidget(self.trim_button)
#         self.layout.addWidget(self.waveform_plot)
#
#         self.central_widget = QWidget()
#         self.central_widget.setLayout(self.layout)
#         self.setCentralWidget(self.central_widget)
#
#         self.trim_start = 0
#         self.trim_end = 0
#         self.playback_line = None
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_waveform)
#         self.timer.start(100)
#
#     def play_audio(self):
#         file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")
#         if file_path:
#             self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
#             self.media_player.play()
#
    # def trim_audio(self):
    #     file_path = self.media_player.media().canonicalUrl().toLocalFile()
    #     if not file_path:
    #         QMessageBox.warning(self, "No Audio File", "Please select an audio file to trim.")
    #         return
    #
    #     audio = AudioSegment.from_file(file_path)
    #
    #     start_time = self.region.getRegion()[0] * 1000  # Convert to milliseconds
    #     end_time = self.region.getRegion()[1] * 1000  # Convert to milliseconds
    #
    #     trimmed_audio = audio[start_time:end_time]
    #
    #     output_file_path, _ = QFileDialog.getSaveFileName(self, "Save Trimmed Audio", "", "Audio Files (*.mp3 *.wav)")
    #     if output_file_path:
    #         output_format = os.path.splitext(output_file_path)[1][
    #                         1:].lower()  # Get the file extension for output format
    #         if output_format in ['mp3', 'wav']:
    #             trimmed_audio.export(output_file_path, format=output_format)  # Export audio with specified format
    #         else:
    #             QMessageBox.warning(self, "Unsupported Format", "Unsupported output format. Please save as MP3 or WAV.")

#     def update_waveform(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             position = self.media_player.position() / 1000  # Convert to seconds
#             duration = self.media_player.duration() / 1000  # Convert to seconds
#             self.waveform_plot.clear()
#             self.waveform_plot.plot([0, duration], [0, 0], pen=pg.mkPen("k", width=2))
#
#             # Draw a line indicating the playback position
#             if self.playback_line:
#                 self.waveform_plot.removeItem(self.playback_line)
#             self.playback_line = self.waveform_plot.plot([position, position], [-1, 1], pen=pg.mkPen("r", width=2))
#
#             self.waveform_plot.region = pg.LinearRegionItem([0, duration])
#             self.waveform_plot.addItem(self.waveform_plot.region)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     editor = AudioEditor()
#     editor.show()
#     sys.exit(app.exec_())




# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtCore import QUrl, QTimer
# from PyQt5.QtGui import QIcon
# import sys
# import os
# import pyqtgraph as pg
# from pydub import AudioSegment
#
# class AudioEditor(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Audio Editor")
#         self.setGeometry(100, 100, 800, 400)
#
#         self.media_player = QMediaPlayer(self)
#         self.media_player.setVolume(50)
#         self.media_player.mediaStatusChanged.connect(self.update_waveform)
#
#         self.play_button = QPushButton(QIcon("play_icon.png"), "Play", self)
#         self.play_button.clicked.connect(self.play_audio)
#
#         self.pause_button = QPushButton(QIcon("pause_icon.png"), "Pause", self)
#         self.pause_button.clicked.connect(self.pause_audio)
#
#         self.trim_button = QPushButton(QIcon("trim_icon.png"), "Trim", self)
#         self.trim_button.clicked.connect(self.trim_audio)
#
#         self.waveform_plot = pg.PlotWidget()
#         self.waveform_plot.showGrid(x=True, y=True)
#         self.waveform_plot.setLabel("left", "Amplitude")
#         self.waveform_plot.setLabel("bottom", "Time (s)")
#
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.play_button)
#         self.layout.addWidget(self.pause_button)
#         self.layout.addWidget(self.trim_button)
#         self.layout.addWidget(self.waveform_plot)
#
#         self.central_widget = QWidget()
#         self.central_widget.setLayout(self.layout)
#         self.setCentralWidget(self.central_widget)
#
#         self.trim_start = 0
#         self.trim_end = 0
#         self.playback_line = None
#         self.region = pg.LinearRegionItem([0, 0])  # Initialize the region for trimming
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_waveform)
#         self.timer.start(100)
#
#     def play_audio(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             self.media_player.pause()
#         else:
#             file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")
#             if file_path:
#                 self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
#                 self.media_player.play()
#
#     def pause_audio(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             self.media_player.pause()
#
#     def trim_audio(self):
#         file_path = self.media_player.media().canonicalUrl().toLocalFile()
#         if not file_path:
#             QMessageBox.warning(self, "No Audio File", "Please select an audio file to trim.")
#             return
#
#         audio = AudioSegment.from_file(file_path)
#
#         start_time = self.region.getRegion()[0] * 1000  # Convert to milliseconds
#         end_time = self.region.getRegion()[1] * 1000  # Convert to milliseconds
#
#         trimmed_audio = audio[start_time:end_time]
#
#         output_file_path, _ = QFileDialog.getSaveFileName(self, "Save Trimmed Audio", "", "Audio Files (*.mp3 *.wav)")
#         if output_file_path:
#             output_format = os.path.splitext(output_file_path)[1][
#                             1:].lower()  # Get the file extension for output format
#             if output_format in ['mp3', 'wav']:
#                 trimmed_audio.export(output_file_path, format=output_format)  # Export audio with specified format
#             else:
#                 QMessageBox.warning(self, "Unsupported Format", "Unsupported output format. Please save as MP3 or WAV.")
#
#     def update_waveform(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             position = self.media_player.position() / 1000  # Convert to seconds
#             duration = self.media_player.duration() / 1000  # Convert to seconds
#             self.waveform_plot.clear()
#             self.waveform_plot.plot([0, duration], [0, 0], pen=pg.mkPen("k", width=2))
#
#             # Draw a line indicating the playback position
#             if self.playback_line:
#                 self.waveform_plot.removeItem(self.playback_line)
#             self.playback_line = self.waveform_plot.plot([position, position], [-1, 1], pen=pg.mkPen("r", width=2))
#
#             self.waveform_plot.addItem(self.region)  # Add the region item for trimming
#             self.region.setRegion([self.trim_start, self.trim_end])  # Set the region based on trim start and end
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     editor = AudioEditor()
#     editor.show()
#     sys.exit(app.exec_())





# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtCore import QUrl, QTimer
# from PyQt5.QtGui import QIcon
# import sys
# import os
# import pyqtgraph as pg
# from pydub import AudioSegment
#
# class AudioEditor(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Audio Editor")
#         self.setGeometry(100, 100, 800, 400)
#
#         self.media_player = QMediaPlayer(self)
#         self.media_player.setVolume(50)
#         self.media_player.mediaStatusChanged.connect(self.update_waveform)
#
#         self.play_button = QPushButton(QIcon("play_icon.png"), "Play", self)
#         self.play_button.clicked.connect(self.play_audio)
#
#         self.pause_button = QPushButton(QIcon("pause_icon.png"), "Pause", self)
#         self.pause_button.clicked.connect(self.pause_audio)
#
#         self.trim_button = QPushButton(QIcon("trim_icon.png"), "Trim", self)
#         self.trim_button.clicked.connect(self.trim_audio)
#
#         self.waveform_plot = pg.PlotWidget()
#         self.waveform_plot.showGrid(x=True, y=True)
#         self.waveform_plot.setLabel("left", "Amplitude")
#         self.waveform_plot.setLabel("bottom", "Time (s)")
#
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.play_button)
#         self.layout.addWidget(self.pause_button)
#         self.layout.addWidget(self.trim_button)
#         self.layout.addWidget(self.waveform_plot)
#
#         self.central_widget = QWidget()
#         self.central_widget.setLayout(self.layout)
#         self.setCentralWidget(self.central_widget)
#
#         self.trim_start = 0
#         self.trim_end = 0
#         self.playback_line = None
#         self.region = pg.LinearRegionItem([0, 0])  # Initialize the region for trimming
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_waveform)
#         self.timer.start(100)
#
#     def play_audio(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             self.media_player.pause()
#         else:
#             file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")
#             if file_path:
#                 self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
#                 self.media_player.setPosition(self.region.getRegion()[0] * 1000)  # Set position to region start
#                 self.media_player.play()
#
#     def pause_audio(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             self.media_player.pause()
#
#     def trim_audio(self):
#         file_path = self.media_player.media().canonicalUrl().toLocalFile()
#         if not file_path:
#             QMessageBox.warning(self, "No Audio File", "Please select an audio file to trim.")
#             return
#
#         audio = AudioSegment.from_file(file_path)
#
#         start_time = self.region.getRegion()[0] * 1000  # Convert to milliseconds
#         end_time = self.region.getRegion()[1] * 1000  # Convert to milliseconds
#
#         trimmed_audio = audio[start_time:end_time]
#
#         output_file_path, _ = QFileDialog.getSaveFileName(self, "Save Trimmed Audio", "", "Audio Files (*.mp3 *.wav)")
#         if output_file_path:
#             output_format = os.path.splitext(output_file_path)[1][
#                             1:].lower()  # Get the file extension for output format
#             if output_format in ['mp3', 'wav']:
#                 trimmed_audio.export(output_file_path, format=output_format)  # Export audio with specified format
#             else:
#                 QMessageBox.warning(self, "Unsupported Format", "Unsupported output format. Please save as MP3 or WAV.")
#
#     def update_waveform(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             position = self.media_player.position() / 1000  # Convert to seconds
#             duration = self.media_player.duration() / 1000  # Convert to seconds
#             self.waveform_plot.clear()
#             self.waveform_plot.plot([0, duration], [0, 0], pen=pg.mkPen("k", width=2))
#
#             # Draw a line indicating the playback position
#             if self.playback_line:
#                 self.waveform_plot.removeItem(self.playback_line)
#             self.playback_line = self.waveform_plot.plot([position, position], [-1, 1], pen=pg.mkPen("r", width=2))
#
#             self.waveform_plot.addItem(self.region)  # Add the region item for trimming
#             self.region.setRegion([self.trim_start, self.trim_end])  # Set the region based on trim start and end
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     editor = AudioEditor()
#     editor.show()
#     sys.exit(app.exec_())



#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtCore import QUrl, QTimer
# from PyQt5.QtGui import QIcon
# import sys
# import os
# import pyqtgraph as pg
# from pydub import AudioSegment
#
# class AudioEditor(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Audio Editor")
#         self.setGeometry(100, 100, 800, 400)
#
#         self.media_player = QMediaPlayer(self)
#         self.media_player.setVolume(50)
#         self.media_player.mediaStatusChanged.connect(self.update_waveform)
#
#         self.upload_button = QPushButton("Upload Audio File", self)
#         self.upload_button.clicked.connect(self.upload_audio)
#
#         self.play_button = QPushButton(QIcon("play_icon.png"), "Play", self)
#         self.play_button.clicked.connect(self.play_audio)
#
#         self.pause_button = QPushButton(QIcon("pause_icon.png"), "Pause", self)
#         self.pause_button.clicked.connect(self.pause_audio)
#
#         self.trim_button = QPushButton(QIcon("trim_icon.png"), "Trim", self)
#         self.trim_button.clicked.connect(self.trim_audio)
#
#         self.waveform_plot = pg.PlotWidget()
#         self.waveform_plot.showGrid(x=True, y=True)
#         self.waveform_plot.setLabel("left", "Amplitude")
#         self.waveform_plot.setLabel("bottom", "Time (s)")
#
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.upload_button)
#         self.layout.addWidget(self.play_button)
#         self.layout.addWidget(self.pause_button)
#         self.layout.addWidget(self.trim_button)
#         self.layout.addWidget(self.waveform_plot)
#
#         self.central_widget = QWidget()
#         self.central_widget.setLayout(self.layout)
#         self.setCentralWidget(self.central_widget)
#
#         self.trim_start = 0
#         self.trim_end = 0
#         self.playback_line = None
#         self.region = pg.LinearRegionItem([0, 0])  # Initialize the region for trimming
#
#         self.selected_audio = None  # Store the selected audio
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_waveform)
#         self.timer.start(100)
#
#     def upload_audio(self):
#         file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")
#         if file_path:
#             self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
#
#     def play_audio(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             self.media_player.pause()
#         else:
#             self.media_player.play()
#
#     def pause_audio(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             self.media_player.pause()
#
#     def trim_audio(self):
#         if self.selected_audio is None:
#             QMessageBox.warning(self, "No Selection", "Please select a region to trim.")
#             return
#
#         output_file_path, _ = QFileDialog.getSaveFileName(self, "Save Trimmed Audio", "", "Audio Files (*.mp3 *.wav)")
#         if output_file_path:
#             output_format = os.path.splitext(output_file_path)[1][
#                             1:].lower()  # Get the file extension for output format
#             if output_format in ['mp3', 'wav']:
#                 self.selected_audio.export(output_file_path, format=output_format)  # Export selected audio with specified format
#             else:
#                 QMessageBox.warning(self, "Unsupported Format", "Unsupported output format. Please save as MP3 or WAV.")
#
#     def update_waveform(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             position = self.media_player.position() / 1000  # Convert to seconds
#             duration = self.media_player.duration() / 1000  # Convert to seconds
#             self.waveform_plot.clear()
#             self.waveform_plot.plot([0, duration], [0, 0], pen=pg.mkPen("k", width=2))
#
#             # Draw a line indicating the playback position
#             if self.playback_line:
#                 self.waveform_plot.removeItem(self.playback_line)
#             self.playback_line = self.waveform_plot.plot([position, position], [-1, 1], pen=pg.mkPen("r", width=2))
#
#             self.waveform_plot.addItem(self.region)  # Add the region item for trimming
#             self.region.setRegion([self.trim_start, self.trim_end])  # Set the region based on trim start and end
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     editor = AudioEditor()
#     editor.show()
#     sys.exit(app.exec_())


# #
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtGui import QIcon
import sys
import os
import pyqtgraph as pg
from pydub import AudioSegment

class AudioEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Audio Editor")
        self.setGeometry(100, 100, 800, 400)

        self.media_player = QMediaPlayer(self)
        self.media_player.setVolume(50)
        self.media_player.mediaStatusChanged.connect(self.update_waveform)

        self.upload_button = QPushButton("Upload Audio File", self)
        self.upload_button.clicked.connect(self.upload_audio)

        self.play_button = QPushButton(QIcon("play_icon.png"), "Play", self)
        self.play_button.clicked.connect(self.play_audio)

        self.pause_button = QPushButton(QIcon("pause_icon.png"), "Pause", self)
        self.pause_button.clicked.connect(self.pause_audio)

        self.trim_button = QPushButton(QIcon("trim_icon.png"), "Trim", self)
        self.trim_button.clicked.connect(self.trim_audio)

        self.waveform_plot = pg.PlotWidget()
        self.waveform_plot.showGrid(x=True, y=True)
        self.waveform_plot.setLabel("left", "Amplitude")
        self.waveform_plot.setLabel("bottom", "Time (s)")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.upload_button)
        self.layout.addWidget(self.play_button)
        self.layout.addWidget(self.pause_button)
        self.layout.addWidget(self.trim_button)
        self.layout.addWidget(self.waveform_plot)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.trim_start = 0
        self.trim_end = 0
        self.playback_line = None
        self.region = pg.LinearRegionItem([0, 0])  # Initialize the region for trimming
        self.region.sigRegionChangeFinished.connect(self.update_trim_region)

        self.selected_audio = None  # Store the selected audio

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_waveform)
        self.timer.start(100)

    def upload_audio(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")
        if file_path:
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))

    def play_audio(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def pause_audio(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()

    def trim_audio(self):
        file_path = self.media_player.media().canonicalUrl().toLocalFile()
        if not file_path:
            QMessageBox.warning(self, "No Audio File", "Please select an audio file to trim.")
            return

        audio = AudioSegment.from_file(file_path)

        start_time = self.region.getRegion()[0] * 1000  # Convert to milliseconds
        end_time = self.region.getRegion()[1] * 1000  # Convert to milliseconds

        trimmed_audio = audio[start_time:end_time]

        output_file_path, _ = QFileDialog.getSaveFileName(self, "Save Trimmed Audio", "", "Audio Files (*.mp3 *.wav)")
        if output_file_path:
            output_format = os.path.splitext(output_file_path)[1][
                            1:].lower()  # Get the file extension for output format
            if output_format in ['mp3', 'wav']:
                trimmed_audio.export(output_file_path, format=output_format)  # Export audio with specified format
            else:
                QMessageBox.warning(self, "Unsupported Format", "Unsupported output format. Please save as MP3 or WAV.")

    def update_waveform(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            position = self.media_player.position() / 1000  # Convert to seconds
            duration = self.media_player.duration() / 1000  # Convert to seconds
            self.waveform_plot.clear()
            self.waveform_plot.plot([0, duration], [0, 0], pen=pg.mkPen("k", width=2))

            # Draw a line indicating the playback position
            if self.playback_line:
                self.waveform_plot.removeItem(self.playback_line)
            self.playback_line = self.waveform_plot.plot([position, position], [-1, 1], pen=pg.mkPen("r", width=2))

            self.waveform_plot.addItem(self.region)  # Add the region item for trimming
            self.region.setRegion([self.trim_start, self.trim_end])  # Set the region based on trim start and end

    def update_trim_region(self):
        region = self.region.getRegion()
        self.trim_start = region[0]
        self.trim_end = region[1]

        if self.selected_audio is not None:
            self.selected_audio.close()

        file_path = self.media_player.media().canonicalUrl().toLocalFile()
        audio = AudioSegment.from_file(file_path)
        start_time = int(region[0] * 1000)  # Convert to milliseconds
        end_time = int(region[1] * 1000)  # Convert to milliseconds
        self.selected_audio = audio[start_time:end_time]

        self.media_player.setPosition(start_time)
        self.media_player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = AudioEditor()
    editor.show()
    sys.exit(app.exec_())




# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtCore import QUrl, QTimer
# from PyQt5.QtGui import QIcon
# import sys
# import os
# import pyqtgraph as pg
# from pydub import AudioSegment
#
# class AudioEditor(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Audio Editor")
#         self.setGeometry(100, 100, 800, 400)
#
#         self.media_player = QMediaPlayer(self)
#         self.media_player.setVolume(50)
#         self.media_player.mediaStatusChanged.connect(self.update_waveform)
#
#         self.upload_button = QPushButton("Upload Audio File", self)
#         self.upload_button.clicked.connect(self.upload_audio)
#
#         self.play_button = QPushButton(QIcon("play_icon.png"), "Play", self)
#         self.play_button.clicked.connect(self.play_audio)
#
#         self.pause_button = QPushButton(QIcon("pause_icon.png"), "Pause", self)
#         self.pause_button.clicked.connect(self.pause_audio)
#
#         self.listen_button = QPushButton(QIcon("listen_icon.png"), "Listen Selected Region", self)
#         self.listen_button.clicked.connect(self.listen_selected_region)
#
#         self.trim_button = QPushButton(QIcon("trim_icon.png"), "Trim", self)
#         self.trim_button.clicked.connect(self.trim_audio)
#
#         self.waveform_plot = pg.PlotWidget()
#         self.waveform_plot.showGrid(x=True, y=True)
#         self.waveform_plot.setLabel("left", "Amplitude")
#         self.waveform_plot.setLabel("bottom", "Time (s)")
#
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.upload_button)
#         self.layout.addWidget(self.play_button)
#         self.layout.addWidget(self.pause_button)
#         self.layout.addWidget(self.listen_button)
#         self.layout.addWidget(self.trim_button)
#         self.layout.addWidget(self.waveform_plot)
#
#         self.central_widget = QWidget()
#         self.central_widget.setLayout(self.layout)
#         self.setCentralWidget(self.central_widget)
#
#         self.trim_start = 0
#         self.trim_end = 0
#         self.playback_line = None
#         self.region = pg.LinearRegionItem([0, 0])  # Initialize the region for trimming
#         self.region.sigRegionChangeFinished.connect(self.update_trim_region)
#
#         self.selected_audio = None  # Store the selected audio
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_waveform)
#         self.timer.start(100)
#
#     def upload_audio(self):
#         file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")
#         if file_path:
#             self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
#
#     def play_audio(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             self.media_player.pause()
#         else:
#             self.media_player.play()
#
#     def pause_audio(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             self.media_player.pause()
#
#     def listen_selected_region(self):
#         if self.selected_audio is not None:
#             temp_file_path = "temp_selected_audio.wav"  # Temporary file path
#             self.selected_audio.export(temp_file_path, format="wav")  # Export selected audio to a temporary file
#
#             self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(temp_file_path)))
#             self.media_player.setPosition(0)  # Start from the beginning of the selected region
#             self.media_player.play()
#
#     def trim_audio(self):
#         if self.selected_audio is None:
#             QMessageBox.warning(self, "No Selection", "Please select a region to trim.")
#             return
#
#         output_file_path, _ = QFileDialog.getSaveFileName(self, "Save Trimmed Audio", "", "Audio Files (*.mp3 *.wav)")
#         if output_file_path:
#             output_format = os.path.splitext(output_file_path)[1][
#                             1:].lower()  # Get the file extension for output format
#             if output_format in ['mp3', 'wav']:
#                 self.selected_audio.export(output_file_path, format=output_format)  # Export selected audio with specified format
#             else:
#                 QMessageBox.warning(self, "Unsupported Format", "Unsupported output format. Please save as MP3 or WAV.")
#
#     def update_waveform(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             position = self.media_player.position() / 1000  # Convert to seconds
#             duration = self.media_player.duration() / 1000  # Convert to seconds
#             self.waveform_plot.clear()
#             self.waveform_plot.plot([0, duration], [0, 0], pen=pg.mkPen("k", width=2))
#
#             # Draw a line indicating the playback position
#             if self.playback_line:
#                 self.waveform_plot.removeItem(self.playback_line)
#             self.playback_line = self.waveform_plot.plot([position, position], [-1, 1], pen=pg.mkPen("r", width=2))
#
#             self.waveform_plot.addItem(self.region)  # Add the region item for trimming
#             self.region.setRegion([self.trim_start, self.trim_end])  # Set the region based on trim start and end
#
#     def update_trim_region(self):
#         region = self.region.getRegion()
#         self.trim_start = region[0]
#         self.trim_end = region[1]
#
#         if self.selected_audio is not None:
#             self.selected_audio.close()
#
#         file_path = self.media_player.media().canonicalUrl().toLocalFile()
#         audio = AudioSegment.from_file(file_path)
#         start_time = int(region[0] * 1000)  # Convert to milliseconds
#         end_time = int(region[1] * 1000)  # Convert to milliseconds
#         self.selected_audio = audio[start_time:end_time]
#
#         self.media_player.setPosition(start_time)
#         self.media_player.play()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     editor = AudioEditor()
#     editor.show()
#     sys.exit(app.exec_())


# ****************************** PLAYBACK , WAVEFORM AND TRIM FUNCTIONALITY

#
#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtCore import QUrl, QTimer
# from PyQt5.QtGui import QIcon
# import sys
# import os
# import pyqtgraph as pg
# from pydub import AudioSegment
#
# class AudioEditor(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Audio Editor")
#         self.setGeometry(100, 100, 800, 400)
#
#         self.media_player = QMediaPlayer(self)
#         self.media_player.setVolume(50)
#         self.media_player.mediaStatusChanged.connect(self.update_waveform)
#
#         self.upload_button = QPushButton("Upload Audio File", self)
#         self.upload_button.clicked.connect(self.upload_audio)
#
#         self.play_button = QPushButton(QIcon("play_icon.png"), "Play", self)
#         self.play_button.clicked.connect(self.play_audio)
#
#         self.pause_button = QPushButton(QIcon("pause_icon.png"), "Pause", self)
#         self.pause_button.clicked.connect(self.pause_audio)
#
#         self.trim_button = QPushButton(QIcon("trim_icon.png"), "Trim", self)
#         self.trim_button.clicked.connect(self.trim_audio)
#
#         self.waveform_plot = pg.PlotWidget()
#         self.waveform_plot.showGrid(x=True, y=True)
#         self.waveform_plot.setLabel("left", "Amplitude")
#         self.waveform_plot.setLabel("bottom", "Time (s)")
#
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.upload_button)
#         self.layout.addWidget(self.play_button)
#         self.layout.addWidget(self.pause_button)
#         self.layout.addWidget(self.trim_button)
#         self.layout.addWidget(self.waveform_plot)
#
#         self.central_widget = QWidget()
#         self.central_widget.setLayout(self.layout)
#         self.setCentralWidget(self.central_widget)
#
#         self.trim_start = 0
#         self.trim_end = 0
#         self.playback_line = None
#         self.region = pg.LinearRegionItem([0, 0])  # Initialize the region for trimming
#         self.region.sigRegionChangeFinished.connect(self.update_trim_region)
#         self.region.setBrush((0, 0, 255, 100))  # Set the region color (blue with transparency)
#
#         self.selected_audio = None  # Store the selected audio
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_waveform)
#         self.timer.start(100)
#
#     def upload_audio(self):
#         file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")
#         if file_path:
#             self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
#
#     def play_audio(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             self.media_player.pause()
#         else:
#             self.media_player.play()
#
#     def pause_audio(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             self.media_player.pause()
#
#     def trim_audio(self):
#         if self.selected_audio is None:
#             QMessageBox.warning(self, "No Selection", "Please select a region to trim.")
#             return
#
#         output_file_path, _ = QFileDialog.getSaveFileName(self, "Save Trimmed Audio", "", "Audio Files (*.mp3 *.wav)")
#         if output_file_path:
#             output_format = os.path.splitext(output_file_path)[1][1:].lower()  # Get the file extension for output format
#             if output_format in ['mp3', 'wav']:
#                 self.selected_audio.export(output_file_path, format=output_format)  # Export selected audio with specified format
#             else:
#                 QMessageBox.warning(self, "Unsupported Format", "Unsupported output format. Please save as MP3 or WAV.")
#
#     def update_waveform(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             position = self.media_player.position() / 1000  # Convert to seconds
#             duration = self.media_player.duration() / 1000  # Convert to seconds
#
#             file_path = self.media_player.media().canonicalUrl().toLocalFile()
#             audio = AudioSegment.from_file(file_path)
#
#             # Calculate the waveform data for the entire audio
#             samples_per_second = 44100  # Adjust as per your audio sample rate
#             total_samples = len(audio.get_array_of_samples())
#             total_duration = total_samples / samples_per_second
#
#             waveform_data = audio.get_array_of_samples()
#
#             # Plot the waveform data
#             self.waveform_plot.clear()
#             self.waveform_plot.plot(waveform_data, pen=pg.mkPen("b", width=1))
#
#             # Draw a line indicating the playback position
#             playback_position = (position / total_duration) * len(waveform_data)
#             if self.playback_line:
#                 self.waveform_plot.removeItem(self.playback_line)
#             self.playback_line = self.waveform_plot.plot([playback_position, playback_position], [-1, 1], pen=pg.mkPen("r", width=2))
#
#             self.waveform_plot.addItem(self.region)  # Add the region item for trimming
#
#     def update_trim_region(self):
#         region = self.region.getRegion()
#         self.trim_start = region[0]
#         self.trim_end = region[1]
#
#         if self.selected_audio is not None:
#             self.selected_audio.close()
#
#         file_path = self.media_player.media().canonicalUrl().toLocalFile()
#         audio = AudioSegment.from_file(file_path)
#         start_time = int(region[0] * 1000)  # Convert to milliseconds
#         end_time = int(region[1] * 1000)  # Convert to milliseconds
#         self.selected_audio = audio[start_time:end_time]
#
#         self.media_player.setPosition(start_time)
#         self.media_player.play()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     editor = AudioEditor()
#     editor.show()
#     sys.exit(app.exec_())
#
