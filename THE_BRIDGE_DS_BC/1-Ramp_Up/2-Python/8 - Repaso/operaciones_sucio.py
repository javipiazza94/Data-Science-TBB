class traductor:
    # Diccionario de traducción con traducciones en diferentes idiomas.
    menu = {
        "fr": {"file": "Fichier", "new": "Nouveau", "open": "Ouvrir", "save": "Enregistrer", "save as": "Enregistrer sous", "print preview": "Apercu avant impressioner", "print": "Imprimer", "close": "Fermer", "exit": "Quitter"},
        "de": {"file": "Datei", "new": "Neu", "open": "Ã–ffnen", "save": "Speichern", "save as": "Speichern unter", "print preview": "Druckansicht", "print": "Drucken", "close": "SchlieÃşen", "exit": "Verlassen"},
        "it": {"file": "File", "new": "Nuovo", "open": "Apri", "save": "Salva", "save as": "Salva come", "print preview": "Anteprima di stampa", "print": "Stampa", "close": "Chiudi", "exit": "Esci"}
    }

    def __init__(self):
        pass

    def traducir_palabra(self, palabra: str, idioma_destino: str):
        if idioma_destino in self.menu:
            diccionario_idioma = self.menu[idioma_destino]
            if palabra in diccionario_idioma:
                return diccionario_idioma[palabra]
        return None  # Si la palabra no se encuentra en el diccionario de traducción o el idioma no es válido, retorna None.

# Ejemplo de uso:
x = traductor()
palabra_a_traducir = "open"
idioma_destino = "de"  # Puedes elegir el idioma al que deseas traducir.
traduccion = x.traducir_palabra(palabra_a_traducir, idioma_destino)

if traduccion is not None:
    print(f"La traducción de '{palabra_a_traducir}' al idioma '{idioma_destino}' es: {traduccion}")
else:
    print(f"La palabra '{palabra_a_traducir}' no se encuentra en el diccionario de traducción o el idioma '{idioma_destino}' no es válido.")
    
    
    
