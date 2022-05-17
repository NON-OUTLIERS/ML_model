# ML_model
Google colab code for generating the pickle files, and then letter predicting them.

To run the model, following steps need to be followed:

1. Firstly, the Tf_idf_dod.ipynb file need to be run. (This file will interact with the dataset and produce the pickle files required for recommending the severity of the disease.)
2. 4 files namely df.pkl, df11.pkl, similarity.pkl, similarity11.pkl will be generated.
3. Place these files along with the file app.py in the same directory.
4. Run app.py and provide with the required study and interpretation data in form of a test.json file.
5. The model will predict whether the patient is critical or not.  
