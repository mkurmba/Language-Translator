# Language-Translator

This Python code provides a graphical user interface (GUI) for a language translator application. It uses the Tkinter library to create a window with specific dimensions. The window includes two textboxes that allow the user to choose the source and destination languages for translation. The available language options are populated from the googletrans library, which provides a list of supported languages.

The GUI features two text boxes, one for input and one for output. The input text box is placed within a frame, and the user can enter the text to be translated here. The output text box, placed in a separate frame, displays the translated text.

When the user clicks the "Translate" button, the translation process is initiated. The program retrieves the selected source and destination languages and the text from the input text box. It uses the googletrans library to create an instance of the Translator class and performs the translation using the translate() method. The translated text is then displayed in the output text box.

In case the user fails to enter any text for translation, an error message box is shown. The "Clear" button can be used to reset both the input and output text boxes.

Overall, this code provides a user-friendly interface for translating text between different languages, making it convenient for users to communicate and understand content in various languages.
