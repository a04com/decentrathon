
from decentrathon.services.keyboard_service import makeInlineOption


def languageChoiceKeyboard():
    keyboard = makeInlineOption({"kz": "kz",
                                 "en": "en",
                                 "ru": "ru"})
    return keyboard