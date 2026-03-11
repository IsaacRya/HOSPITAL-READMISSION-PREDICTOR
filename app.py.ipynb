{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d94a9ae1-12a6-4e3a-b95f-d0b2fec8c2ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "model = joblib.load(\"models/readmission_model.pkl\")\n",
    "\n",
    "st.title(\"Hospital Readmission Risk Predictor\")\n",
    "\n",
    "age = st.number_input(\"Age\")\n",
    "bmi = st.number_input(\"BMI\")\n",
    "length_of_stay = st.number_input(\"Length of Stay\")\n",
    "medication_count = st.number_input(\"Medication Count\")\n",
    "diabetes = st.selectbox(\"Diabetes\", [\"No\", \"Yes\"])\n",
    "hypertension = st.selectbox(\"Hypertension\", [\"No\", \"Yes\"])\n",
    "\n",
    "if st.button(\"Predict\"):\n",
    "\n",
    "    diabetes = 1 if diabetes==\"Yes\" else 0\n",
    "    hypertension = 1 if hypertension==\"Yes\" else 0\n",
    "\n",
    "    input_data = np.array([[age, bmi, length_of_stay,\n",
    "                            medication_count,\n",
    "                            diabetes, hypertension]])\n",
    "\n",
    "    probability = model.predict_proba(input_data)[0][1]\n",
    "    \n",
    "    st.write(f\"Readmission Probability: {probability*100:.2f}%\")\n",
    "    \n",
    "    if probability < 0.3:\n",
    "        st.success(\"Low Risk\")\n",
    "    elif probability < 0.7:\n",
    "        st.warning(\"Medium Risk\")\n",
    "    else:\n",
    "        st.error(\"High Risk\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
