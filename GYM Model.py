{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9ce20041",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RandomForestClassifier(n_estimators=20)\n",
      "[1]\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn import datasets\n",
    "from sklearn import metrics\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "data = pd.read_excel(r'C:\\Users\\USER\\Downloads\\dataGYM.xlsx')\n",
    "\n",
    "df = data.copy()\n",
    "del df['BMI']\n",
    "del df['Class']\n",
    "label_encoder = LabelEncoder()\n",
    "df['Prediction'] = label_encoder.fit_transform(df['Prediction'])\n",
    "\n",
    "\n",
    "X = df.iloc[:,:-1]\n",
    "y = df.iloc[:,-1]\n",
    "\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)\n",
    "\n",
    "model_GYM = RandomForestClassifier(n_estimators=20)\n",
    "\n",
    "model_GYM.fit(X_train, y_train)\n",
    "\n",
    "print(model_GYM)\n",
    "\n",
    "\n",
    "# make predictions\n",
    "expected = y_test\n",
    "predicted = model_GYM.predict(X_test)\n",
    "# summarize the fit of the model\n",
    "#Correction\n",
    "metrics.classification_report(expected, predicted)\n",
    "metrics.confusion_matrix(expected, predicted)\n",
    "\n",
    "import pickle\n",
    "\n",
    "pickle.dump(model_GYM, open(\"Model_GYM.pkl\", \"wb\"))\n",
    "\n",
    "model = pickle.load(open(\"Model_GYM.pkl\", \"rb\"))\n",
    "\n",
    "print(model.predict([[40,5.6,70]]))\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38250e80",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
