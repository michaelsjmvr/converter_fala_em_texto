# Importação das bibliotecas necessárias
import sys
import speech_recognition as sr
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget

# Definição da classe principal da aplicação
class VoiceRecognitionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Inicialização da interface gráfica
        self.initUI()

    def initUI(self):
        # Configurações iniciais da janela
        self.setWindowTitle("Aplicação de Reconhecimento de Voz")
        self.setGeometry(100, 100, 600, 400)

        # Criação do widget central
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Criação do layout vertical para organizar os elementos
        self.layout = QVBoxLayout()

        # Criação da caixa de texto para exibir os resultados
        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        # Criação do botão "Iniciar Reconhecimento de Voz" e conexão com a função start_recognition
        self.start_button = QPushButton("Iniciar Reconhecimento de Voz")
        self.start_button.clicked.connect(self.start_recognition)
        self.layout.addWidget(self.start_button)

        # Aplicação do layout ao widget central
        self.central_widget.setLayout(self.layout)

        # Inicialização do objeto reconhecedor de voz da biblioteca SpeechRecognition
        self.recognizer = sr.Recognizer()

    def start_recognition(self):
        # Início do processo de reconhecimento de voz
        with sr.Microphone() as source:
            self.text_edit.clear()  # Limpa a caixa de texto
            self.text_edit.append("Aguardando comando de voz...")
            self.recognizer.adjust_for_ambient_noise(source)  # Ajusta para o ruído ambiente
            audio = self.recognizer.listen(source)  # Grava o áudio do microfone

        try:
            # Tenta reconhecer o áudio usando o Google Web Speech API com idioma em português (pt-BR)
            text = self.recognizer.recognize_google(audio, language="pt-BR")
            self.text_edit.append(f"Texto reconhecido: {text}")  # Exibe o texto reconhecido na caixa de texto
        except sr.UnknownValueError:
            self.text_edit.append("Não foi possível entender o comando de voz.")
        except sr.RequestError as e:
            self.text_edit.append(f"Erro na solicitação ao serviço de reconhecimento de voz: {str(e)}")

# Função principal para iniciar a aplicação
def main():
    app = QApplication(sys.argv)
    window = VoiceRecognitionApp()  # Cria uma instância da classe principal
    window.show()  # Exibe a janela
    sys.exit(app.exec())  # Inicia o loop principal da aplicação

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar a aplicação
