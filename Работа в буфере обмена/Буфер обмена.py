import pyperclip

def analyze_and_process_text():
    #1
    input("Пожалуйста, скопируйте первый текст и нажмите Enter.")

    clipboard_text = pyperclip.paste()

    original_text = clipboard_text
    #2
    input("Пожалуйста, скопируйте второй текст начинающийся на '!!!' и нажмите Enter.")

    clipboard_text_2 = pyperclip.paste()

    if clipboard_text_2.startswith("!!!"):

        modified_text = f"{original_text.strip()} {clipboard_text_2[3:].strip()}"
        
        pyperclip.copy(modified_text)

        print("Текст успешно обработан и скопирован в буфер обмена.")
    else:

        pyperclip.copy(original_text.strip())
        print("Текст не начинается с '!!!', копирован только первоначальный текст.")

if __name__ == "__main__":

    analyze_and_process_text()
