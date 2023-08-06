
def translation_response_to_string(translation):
    return translation['data']['translations'][0]['translatedText']

def detect_language_to_list(detection):
    return detection['data']['detections']

def translate(translator, text, language):
    try:
        detected = translator.detect_language(text)
        translator.set_source_language(detect_language_to_list(detected[0]))
        translator.set_target_language(language)
        return translation_response_to_string(translator.translate(text))
    except:
        return ConnectionError
