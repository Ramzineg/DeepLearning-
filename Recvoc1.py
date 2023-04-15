import nltk
import streamlit as st
import speech_recognition as sr

# Importer le fichier texte et prétraiter les données avec l'algorithme du chatbot

# Définir une fonction pour transcrire la parole en texte à l'aide de l'algorithme de reconnaissance vocale
def transcribe_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dites quelque chose...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='fr-FR')
        return text
    except:
        return ""

# Modifier la fonction du chatbot pour prendre en compte la saisie textuelle et vocale
def chatbot(input_text):
    # Code de l'algorithme de chatbot
    output_text = "Réponse du chatbot"
    return output_text


# Créer l'application Streamlit
def main():
    st.title("Chatbot")

    # Demander à l'utilisateur de choisir entre la saisie textuelle et vocale
    input_mode = st.radio("Sélectionnez le mode d'entrée", ["Texte", "Voix"])

    # Si l'utilisateur choisit la saisie textuelle, afficher une zone de texte
    if input_mode == "Texte":
        input_text = st.text_input("Entrez votre message")

        # Si l'utilisateur fournit un texte, exécuter l'algorithme du chatbot
        if input_text:
            output_text = chatbot(input_text)
            st.write(output_text)

    # Si l'utilisateur choisit la saisie vocale, transcrire la parole en texte
    elif input_mode == "Voix":
        input_text = transcribe_audio()

        # Si l'utilisateur fournit une entrée vocale, exécuter l'algorithme du chatbot
        if input_text:
            output_text = chatbot(input_text)
            st.write(output_text)

if __name__ == "__main__":
    main()
