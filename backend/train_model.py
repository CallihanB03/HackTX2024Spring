from keras.layers import Dense, Input
from keras.models import Model
from keras.optimizers import Adam
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from tensorflow import random
random.set_seed(42)


def binary_encoding(data, col, truth='W'):
  binary_col = []
  for val in data[col]:
    if val == 'W':
      binary_col.append(1)
    else:
      binary_col.append(0)
  data[col] = binary_col
  return data


def myScaler(data):
  scaled_data = {}
  for col in data.columns:
    scaled_data[col] = []
    col_mean = np.mean(data[col])
    col_std = np.std(data[col])
    for val in data[col]:
      scaled_val = (val-col_mean) / col_std
      scaled_data[col].append(scaled_val)
  scaled_data = pd.DataFrame.from_dict(scaled_data)
  return scaled_data


def build_model():
    model_input = Input(shape=(19,))

    x = Dense(19, activation='relu')(model_input)
    x = Dense(19, activation='relu')(x)
    x = Dense(15, activation='relu')(x)
    x = Dense(12, activation='relu')(x)
    x = Dense(9, activation='relu')(x)
    x = Dense(6, activation='relu')(x)
    x = Dense(3, activation='relu')(x)

    model_output = Dense(1, activation='sigmoid')(x) 

    model = Model(model_input, model_output)

    model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
    return model

def preprocess_data_split(data):
    X, y = data[data.columns[:-1]], data[data.columns[-1]]
    X = myScaler(X)
    combined_df = X.join(y)
    combined_df = combined_df.dropna()
    X, y = combined_df[combined_df.columns[:-1]], combined_df[combined_df.columns[-1]]
    return X, y
  
  
def main():
    # Get data
    data = pd.read_csv("team_data.csv")
    # preprocess data
    data = binary_encoding(data, 'WL')
    del data["Unnamed: 0"]
    X, y = preprocess_data_split(data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build and compile model
    model = build_model()
    model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

    # Train Model
    model.fit(X_train, y_train, epochs=100, batch_size=100)

    # Evaluate Model
    y_true = y_test
    model_pred = model.predict(X_test)
    y_pred = np.zeros_like(model_pred)  # Initialize all elements to zero
    y_pred[model_pred >= 0.5] = 1

    report = classification_report(y_true, y_pred)
    print("Classification Report:")
    print(report)


    # Confusion Matrix
    confu_matrix = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(confu_matrix, annot=True, fmt='d', cmap='Blues', annot_kws={"size": 14}, cbar=False)
    plt.xlabel('Predicted labels', fontsize=14)
    plt.ylabel('True labels', fontsize=14)
    plt.title('Confusion Matrix', fontsize=16)
    plt.show()

    # Save Model
    model.save("NBA_team_pred.h5")


if __name__ == "__main__":
   main()



