import streamlit as st
import cv2

# Ajouter des instructions à l'interface
st.write("Téléchargez une image et cliquez sur le bouton 'Détecter les visages' pour détecter les visages.")
st.write("Utilisez les curseurs pour ajuster les paramètres de détection de visages et choisissez la couleur des rectangles dessinés autour des visages détectés.")

# Ajouter une fonctionnalité pour télécharger l'image
uploaded_file = st.file_uploader("Télécharger une image", type=["jpg", "jpeg", "png"])

# Ajouter une fonctionnalité pour enregistrer les images avec les visages détectés
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, minNeighbors=minNeighbors, scaleFactor=scaleFactor)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.imwrite("face_detection.jpg", img)
    st.image(img, caption='Image avec les visages détectés', use_column_width=True)

# Ajouter une fonctionnalité pour choisir la couleur des rectangles
color = st.color_picker('Choisissez une couleur pour les rectangles', '#ff0000')

# Ajouter une fonctionnalité pour ajuster le paramètre minNeighbors
minNeighbors = st.slider('Ajustez le paramètre minNeighbors', 1, 10, 3)

# Ajouter une fonctionnalité pour ajuster le paramètre scaleFactor
scaleFactor = st.slider('Ajustez le paramètre scaleFactor', 1.05, 1.5, 1.2, 0.01)
