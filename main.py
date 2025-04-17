from google.cloud import translate_v2 as translate

def main():
    client = translate.Client()

    text = input("Enter the text to translate: ")
    target_lang = input("Enter the target language code (e.g., 'en' for English, 'fr' for French): ").lower()

    # Detect language
    detection = client.detect_language(text)
    source_lang = detection['language']
    print(f"Detected language: {source_lang}")

    # Translate text
    result = client.translate(text, source_language=source_lang, target_language=target_lang)
    print(f"Translated text: {result['translatedText']}")

if __name__ == "__main__":
    main()

