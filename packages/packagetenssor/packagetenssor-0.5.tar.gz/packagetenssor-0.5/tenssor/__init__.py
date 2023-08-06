s1 = '''
import numpy as np
import pandas as pd

column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
boston = pd.read_csv('./housing.csv', header=None, delimiter=r"\s+", names=column_names)

data = pd.DataFrame(boston.data)

"""### First look at the dataset"""

data.head()

data.columns = boston.feature_names

data['PRICE'] = boston.target

data.head()

print(data.shape)

data.isnull().sum()

"""No null values in the dataset, no missing value treatement needed"""

data.describe()

"""This is sometimes very useful, for example if you look at the CRIM the max is 88.97 and 75% of the value is below 3.677083 and mean is 3.613524 so it means the max values is actually an outlier or there are outliers present in the column"""

data.info()

"""<a id = 'visual'></a>
# Visualisation
"""

import seaborn as sns
sns.distplot(data.PRICE)

"""The distribution seems normal, has not be the data normal we would have perform log transformation or took to square root of the data to make the data normal. Normal distribution is need for the machine learning for better predictiblity of the model"""

sns.boxplot(data.PRICE)

"""<a id = 'corr'></a>
### Checking the correlation of the independent feature with the dependent feature

Correlation is a statistical technique that can show whether and how strongly pairs of variables are related.An intelligent correlation analysis can lead to a greater understanding of your data
"""

correlation = data.corr()
correlation.loc['PRICE']

import matplotlib.pyplot as plt
fig,axes = plt.subplots(figsize=(15,12))
sns.heatmap(correlation,square = True,annot = True)

"""By looking at the correlation plot LSAT is negatively correlated with -0.75 and RM is positively correlated to the price and PTRATIO is correlated negatively with -0.51"""

plt.figure(figsize = (20,5))
features = ['LSTAT','RM','PTRATIO']
for i, col in enumerate(features):
    plt.subplot(1, len(features) , i+1)
    x = data[col]
    y = data.PRICE
    plt.scatter(x, y, marker='o')
    plt.title("Variation in House prices")
    plt.xlabel(col)
    plt.ylabel('"House prices in $1000"')

"""<a id = 'split'></a>
### Splitting the dependent feature and independent feature 
"""

X = data.iloc[:,:-1]
y= data.PRICE

"""<a id = 'valid'></a>
### Splitting the data for Model Validation 
"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 4)

"""<a id  = 'NN'></a>
## Neural Networks
"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""* We are using Keras for developing the neural network.
* Models in Keras are defined as a sequence of layers
* We create a Sequential model and add layers one at a time with activation function
* Activation function decides, whether a neuron should be activated or not by calculating weighted sum and further adding bias with it. The purpose of the activation function is to introduce non-linearity into the output of a neuron.The activation we are using is relu
* As this is a regression problem, the output layer has no activation function
* Elements of neural network has input layer, hidden layer and output layer
* input layer:- This layer accepts input features. It provides information from the outside world to the network, no computation is performed at this layer, nodes here just pass on the information(features) to the hidden layer.
* Hidden layer:-  Nodes of this layer are not exposed to the outer world, they are the part of the abstraction provided by any neural network. Hidden layer performs all sort of computation on the features entered through the input layer and transfer the result to the output layer.
* Output layer:- This layer bring up the information learned by the network to the outer world.
* Model Compilation:- The compilation is the final step in creating a model. Once the compilation is done, we can move on to training phase.
* Optimizer : - The optimizer we are using is adam. Adam is an optimization algorithm that can be used instead of the classical stochastic gradient descent procedure to update network weights iterative based in training data.
* Loss - mean square error
"""

import keras
from keras.layers import Dense, Activation,Dropout
from keras.models import Sequential

model = Sequential()

model.add(Dense(128,activation  = 'relu',input_dim =13))
model.add(Dense(64,activation  = 'relu'))
model.add(Dense(32,activation  = 'relu'))
model.add(Dense(16,activation  = 'relu'))
model.add(Dense(1))
model.compile(optimizer = 'adam',loss = 'mean_squared_error')

model.fit(X_train, y_train, epochs = 100)

"""<a id = 'eval'></a>
### Evaluation of the model
"""

y_pred = model.predict(X_test)

from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
print(r2)

# Predicting RMSE the Test set results
from sklearn.metrics import mean_squared_error
rmse = (np.sqrt(mean_squared_error(y_test, y_pred)))
print(rmse)
'''

s2 = '''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn import model_selection
from sklearn.preprocessing import StandardScaler,LabelEncoder, OneHotEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# from sklearn import preprocessing
# from yellowbrick.classifier import ConfusionMatrix

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/MyDrive/College/DL/Assignment2/letter-recognition.data", sep = ",", header=None)

df.head(10)

names = ['letter_Class',
         'x-box',
         'y-box',
         'width',
         'high',
         'onpix',
         'x-bar',
         'y-bar',
         'x2bar',
         'y2bar',
         'xybar',
         'x2ybr',
         'xy2br',
         'x-ege',
         'xegvy',
         'y-ege',
         'yegvx']

df.columns = names

df.head(10)

# X = df.iloc[:, 1 : 17]
# Y = df.select_dtypes(include = [object])
X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

y

onehot_encoder = OneHotEncoder(categories='auto')
y = onehot_encoder.fit_transform(y.reshape(-1, 1)).toarray()

y

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Sequential()
model.add(Dense(64, input_shape=(16,), activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(26, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

score = model.evaluate(X_test, y_test)
print(f'Test loss: {score[0]}')
print(f'Test accuracy: {score[1]}')

# print(confusion_matrix(Y_test, predictions))
y_pred = model.predict(X_test)
y_pred = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)
cm = confusion_matrix(y_true, y_pred)
print(cm)

target_names = label_encoder.inverse_transform(np.arange(26))
print(classification_report(y_true, y_pred, target_names=target_names))

# create a new input with 16 feature values
new_input = [[4,2,5,4,4,8,7,6,6,7,6,6,2,8,7,10]]

# standardize the input using the scaler object
new_input = scaler.transform(new_input)

# make a prediction
prediction = model.predict(new_input)

# print the predicted letter
val=np.argmax(prediction)

print(chr(ord('A')+val))

# create a new input with 16 feature values
new_input = [[5,12,3,7,2,10,5,5,4,13,3,9,2,8,4,10]]

# standardize the input using the scaler object
new_input = scaler.transform(new_input)

# make a prediction
prediction = model.predict(new_input)

# print the predicted letter
val=np.argmax(prediction)

print(chr(ord('A')+val))
'''

s3 = '''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Dense, Flatten
#from keras.optimizers import Adam
from tensorflow.keras.optimizers import Adam
from keras.callbacks import TensorBoard
from tensorflow.keras.utils import to_categorical

fashion_train_df = pd.read_csv('fashion-mnist_train.csv', sep=',')
fashion_test_df = pd.read_csv('fashion-mnist_test.csv', sep=',')

fashion_train_df.shape   # Shape of the dataset

fashion_train_df.columns   # Name of the columns of the DataSet.

"""So we can see that the 1st column is the label or target value for each row.

Now Lets find out how many distinct lables we have.
"""

print(set(fashion_train_df['label']))

"""So we have 10 different lables. from 0 to 9. 

Now lets find out what is the min and max of values of in the other columns.
"""

print([fashion_train_df.drop(labels='label', axis=1).min(axis=1).min(), 
      fashion_train_df.drop(labels='label', axis=1).max(axis=1).max()])

"""So we have 0 to 255 which is the color values for grayscale. 0 being white and 255 being black.

Now lets check some of the rows in tabular format
"""

fashion_train_df.head()

"""So evry other things of the test dataset are going to be the same as the train dataset except the shape."""

fashion_test_df.shape

"""So here we have 10000 images instead of 60000 as in the train dataset.

Lets check first few rows.
"""

fashion_test_df.head()

training = np.asarray(fashion_train_df, dtype='float32')

height = 10
width = 10

fig, axes = plt.subplots(nrows=width, ncols=height, figsize=(17,17))
axes = axes.ravel()  # this flattens the 15x15 matrix into 225
n_train = len(training)

for i in range(0, height*width):
    index = np.random.randint(0, n_train)
    axes[i].imshow(training[index, 1:].reshape(28,28))
    axes[i].set_title(int(training[index, 0]), fontsize=8)
    axes[i].axis('off')
    
plt.subplots_adjust(hspace=0.5)

training = np.asarray(fashion_train_df, dtype='float32')
X_train = training[:, 1:].reshape([-1,28,28,1])
X_train = X_train/255   
y_train = training[:, 0]

testing = np.asarray(fashion_test_df, dtype='float32')
X_test = testing[:, 1:].reshape([-1,28,28,1])
X_test = X_test/255    
y_test = testing[:, 0]

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=12345)    # TODO : change the random state to 5

print(X_train.shape, X_val.shape, X_test.shape)
print(y_train.shape, y_val.shape, y_test.shape)

cnn_model = Sequential()
cnn_model.add(Conv2D(filters=64, kernel_size=(3,3), input_shape=(28,28,1), activation='relu'))
cnn_model.add(MaxPooling2D(pool_size = (2,2)))
cnn_model.add(Dropout(rate=0.3))
cnn_model.add(Flatten())
cnn_model.add(Dense(units=32, activation='relu'))
cnn_model.add(Dense(units=10, activation='sigmoid'))

"""**compile the model**"""

cnn_model.compile(optimizer=Adam(lr=0.001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
cnn_model.summary()

"""**Train the model**"""

cnn_model.fit(x=X_train, y=y_train, batch_size=256, epochs=4, validation_data=(X_val, y_val))

eval_result = cnn_model.evaluate(X_test, y_test)
print("Accuracy : {:.3f}".format(eval_result[1]))

y_pred = cnn_model.predict(x=X_test)

print(y_pred[0])

height = 10
width = 10

fig, axes = plt.subplots(nrows=width, ncols=height, figsize=(20,20))
axes = axes.ravel()
for i in range(0, height*width):
    index = np.random.randint(len(y_pred))
    axes[i].imshow(X_test[index].reshape((28,28)))
    #axes[i].set_title("True Class : {:0.0f}\nPrediction : {:d}".format(y_test[index],y_pred[index]))
    axes[i].axis('off')
plt.subplots_adjust(hspace=0.9, wspace=0.5)
'''

s4 = '''

### **Goals of the project -** 
* To understand the basic implemetation of the RNN and LSTM
* To build the RNN layer by layer and understanding the significance of LSTM and the arguments used
* Understanding the importance of Normalization in RNN
* To understand the concept of time steps
* Creating training and testing set from the same data by using the concept of time steps
* Comparing the forecast of the actual and predicted stock prices
* Understanding the significance of RNN in terms of forecasting and its limitations
* Evaluating the RNN by RMSE value taken as a percentage of the orignal value

## **Step 1** : Pre-processing
"""

import numpy as np
import pandas as pd
import warnings  
warnings.filterwarnings('ignore') # to ignore the warnings

training = pd.read_csv("./Google_Stock_Price_Train.csv")
training.head()

"""**Things to consider -**
* For this project sake we will be considering only the "Open" value of the stock as we are building the RNN
* This is done because in RNN, one value at a time `t` is given as an input in a module and that in return gives the next predicted value at time `t+1`
"""

real_stock_price_train = training.iloc[:, 1:2].values     # creates a 2D array having observation and feature

"""**Step - 1.1 :** Feature Scaling"""

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
training2 = sc.fit_transform(real_stock_price_train)

"""**Note -**
* We prefer `Normalization` over `Standardization` here coz the sigmoid function takes values betn 0 and 1, 
* Hence it would be better to scale our values betn 0 and 1, thus its better to do use `MinMaxScaler`

**Step - 1.2 :** Checking the shape
"""

training2.shape

"""**Step 1.3 :** Getting the input and output values

**Note -**
* The input values must be the stock prices at time `t` and the output values should be the stock prices at time `t+1`
"""

# hence in the input we take
X_train = training2[0:1257]  # all but last observation as we don't have the output value for it
y_train = training2[1:1258]  # values shifted by 1

"""**Step 1.4 :** Reshaping
* We need to convert this 2D (observation and feature)array into a 3D array because it is a time series problem
* So we need to add a *time step* of 1 because our input is stock price at time `t` and output is stock price at time `t+1` and `(t+1) - t = 1`, hence `1` is the time step
"""

X_train = np.reshape(X_train, (1257, 1, 1))
# (1257, 1, 1) the 2nd argument is no. of features and 3rd argument is the time step

"""## **Step - 2 :** Building the RNN"""

# importing libraries
from keras.models import Sequential  # initialize NN as a sequnce of layers
from keras.layers import Dense  # to add fully connected layers
from keras.layers import LSTM

"""**Step 2.1 :** Initializing the RNN"""

rnn_regressor = Sequential()

"""**Step 2.2 :** Adding input layer and LSTM layer
* In the add method, we use the class corresponding to the layer we want to add
* In this case we are adding the LSTM layer thus replacing the input layer (Dense class) by the LSTM class
"""

rnn_regressor.add(LSTM(units=4, activation='sigmoid', input_shape=(1, 1)))

"""**Arguments used -**
* `units` = no. of memory units
* `input_shape=(1, 1)` means the 1st element is the time step and the 2nd element is no. of features

**Step 2.3 :** Adding the output layer
"""

rnn_regressor.add(Dense(units=1))

"""**Arguments used -**
* `units` = no. of neurons in output layer, here it is a regressor hence 1

**Step 2.4 :** Compiling the RNN
"""

rnn_regressor.compile(optimizer='adam', loss='mean_squared_error')

"""**Step 2.5 :** Fitting the RNN to training set"""

rnn_regressor.fit(X_train, y_train, batch_size=32, epochs=200)

"""**Step 2.6 :** Predicting and Visualizing the training results"""

# predicting the training results
predicted_stock_price_train = rnn_regressor.predict(X_train)
predicted_stock_price_train = sc.inverse_transform(predicted_stock_price_train)

# visualizing the training results
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
plt.plot(real_stock_price_train, color = 'red', label='Real Google Stock Price')
plt.plot(predicted_stock_price_train, color = 'blue', label='Predicted Google Stock Price')
plt.title('Google Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.show()

"""## **Step - 3 :** Making predictions and visualizing results for testing set"""

testing = pd.read_csv("./Google_Stock_Price_Test.csv")
testing.head()

"""**Step 3.1 :** Performing similar pre-prcoessing as performed on training set"""

# taking the column of "open" value of stock price
real_stock_price_test = testing.iloc[:, 1:2].values

# feature Scaling
inputs = sc.transform(real_stock_price_test)

"""**Note -** We do only ".transform" and not "fit.transform" and we use the same scaler 'sc' we used while standardzing the training data because the scaling should be done with respect to the training data and not the testing set because the minimum and maximum of the training and testing sets may vary"""

# reshaping
inputs = np.reshape(inputs, (20, 1, 1))     # only 20 observations in testing set

# predicting the stock price (for the year 2017)
predicted_stock_price_test = rnn_regressor.predict(inputs)     # but these are the scaled values

"""**Step 3.2 :** Performing inverse scaling"""

predicted_stock_price_test = sc.inverse_transform(predicted_stock_price_test)

# visualizing the results for testing
plt.figure(figsize=(20,10))
plt.plot(real_stock_price_test, color = 'red', label='Real Google Stock Price')
plt.plot(predicted_stock_price_test, color = 'blue', label='Predicted Google Stock Price')
plt.title('Google Stock Price Prediction (Test Set)')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.show()

"""## **Conclusions**
* As there is 1 time step between the input and the output, that makes it one time step prediction
* It is seen that the predictions are actually following the real google stock prices
* If we imagine today is the 1st day of 2017 and we want to predict stock price for the next 60 days, we won't get these accurate results as our model was trained for 1 time step prediction
* As amazing as that sounds it would be hard to get such close predictions because in finance, the future variations may not always be dependent on the past, hence its nearly impossible to make long term predictions of stock price

## **Step - 4 :** Evaluating the RNN

### **Interpretation of RMSE value :**
* It is a way of figuring out how much a model disagrees with the actual data
"""

from sklearn.metrics import mean_squared_error
rmse = np.sqrt(mean_squared_error(real_stock_price_test, predicted_stock_price_test))
print('The RMSE value is', rmse)

"""* We need to express this as percentage of the orignal value coz it may tell there is a prediction error of 7, but that error won't mean the same thing whether the orignal stock price was betn 1 and 10 or betn 1000 and 10000
* Generally a good rmse expressed in terms of percentage is around or less than 1%
"""

print('RMSE in terms of % of the orignal value is', round((rmse/real_stock_price_test.mean()*100), 2) , '%')   
# we take the avg because it would be a true representative of the real stock values
'''

s5 = '''
#include<bits/stdc++.h>
#include<omp.h>
#include<chrono>
using namespace std;
using namespace std::chrono;

int N = 10, M = 10;
vector<int> graph [10];
void bfs_p(int start) {
	vector<bool> vis(N);
	queue<int> q;
	q.push(start);

	while(!q.empty()) {
		int cur = q.front();
		q.pop();
		if(!vis[cur]) {
			vis[cur] = 1; cout << cur <<" ";
			
			#pragma omp parallel for
			for (int next: graph[cur]) {
				if(!vis[next]) q.push(next);			
			}		
		}	
	}
}

void bfs(int start) {
	vector<bool> vis(N);
	queue<int> q;
	q.push(start);

	while(!q.empty()) {
		int cur = q.front();
		q.pop();
		if(!vis[cur]) {
			vis[cur] = 1; cout << cur <<" ";
			
			for (int next: graph[cur]) {
				if(!vis[next]) q.push(next);			
			}		
		}	
	}
}

void dfs_p(int start) {
	vector<bool> vis(N);
	stack<int> q;
	q.push(start);

	while(!q.empty()) {
		int cur = q.top();
		q.pop();
		if(!vis[cur]) {
			vis[cur] = 1; cout << cur <<" ";
			
			#pragma omp parallel for
			for (int next: graph[cur]) {
				if(!vis[next]) q.push(next);			
			}		
		}	
	}
}
void dfs(int start) {
	vector<bool> vis(N);
	stack<int> q;
	q.push(start);

	while(!q.empty()) {
		int cur = q.top();
		q.pop();
		if(!vis[cur]) {
			vis[cur] = 1; cout << cur <<" ";
			
			for (int next: graph[cur]) {
				if(!vis[next]) q.push(next);			
			}		
		}	
	}
}

int main() {
	cout << "Enter 4 edges :" << endl;
	for(int i = 0; i < 4; i++) {
		int x, y; cin >> x >> y;
		graph[x].push_back(y);
		graph[y].push_back(x);	
	}
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	cout << "Paralel BFS traversal : ";

	auto start = high_resolution_clock::now();
	bfs_p(0);
	cout << endl;
	auto end = high_resolution_clock::now();
	auto dur = duration_cast<microseconds>(end - start);
	cout << "Time taken : " <<dur.count() << " ms" <<endl; 

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	cout << "Normal BFS traversal : ";

	start = high_resolution_clock::now();
	bfs(0);
	cout << endl;
	end = high_resolution_clock::now();
	dur = duration_cast<microseconds>(end - start);
	cout << "Time taken : " <<dur.count() << " ms" <<endl; 

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
	cout << "Paralel DFS traversal : ";
	start = high_resolution_clock::now();
	dfs_p(0);
	cout << endl;
	end = high_resolution_clock::now();
	dur = duration_cast<microseconds>(end - start);
	cout << "Time taken : " <<dur.count() << " ms" <<endl; 
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
	cout << "Common DFS traversal : ";
	start = high_resolution_clock::now();
	dfs(0);
	cout << endl;
	end = high_resolution_clock::now();
	dur = duration_cast<microseconds>(end - start);
	cout << "Time taken : " <<dur.count() << " ms" <<endl; 
	
}
'''

s6 = '''
#include <bits/stdc++.h>
#include <omp.h>
#include<chrono>
using namespace std;
using namespace std::chrono;

int N = 6;

void bubble_sort_p(int a[], int n) {
	#pragma omp parallel shared (a, n)
	{
		int i,j;
		#pragma omp for
		for(int i = 0; i < n-1; i++) {
			for(j = 0; j < n-i-1; j++) {
				if(a[j] > a[j+1]) swap(a[j], a[j+1]);			
			} 		
		}
	}
}


void bubble_sort(int a[], int n) {

	{
		int i,j;

		for(int i = 0; i < n-1; i++) {
			for(j = 0; j < n-i-1; j++) {
				if(a[j] > a[j+1]) swap(a[j], a[j+1]);			
			} 		
		}
	}
}
void merge(int a[], int l, int md, int r) {
	vector<int> temp(r - l + 1);
	int i = l, j = md + 1, k = 0;
	
	while(i <= md && j <= r) {
		if(a[i] <= a[j]) temp[k++] = a[i++];
		else temp[k++] = a[j++];
	} 

	while(i <= md) temp[k++] = a[i++];
	while(j <= r) temp[k++] = a[j++];
	
	for(int i = 0; i < k; i++) a[l+i] = temp[i];

}

void merge_sort_p(int a[], int l, int r) {
	if( l < r){
		int md = (l + r) / 2;
		#pragma omp parallel sections 
		{
			#pragma omp section
				merge_sort_p(a, l, md);
			#pragma omp section
				merge_sort_p(a, md + 1, r);
 			
			merge(a, l, md, r);		
		}
	}
}

void merge_sort(int a[], int l, int r) {
	if( l < r){
		int md = (l + r) / 2;

		{

				merge_sort(a, l, md);

				merge_sort(a, md + 1, r);
 			
			merge(a, l, md, r);		
		}
	}
}

int main() {
	cout << "Enter " << N << " elements: ";
	int a[N], a1[N], a2[N], a3[N];	
	for(int i = 0; i < N; i++) {cin >> a[i]; a1[i] = a[i]; a2[i] = a[i]; a3[i] = a[i];  }
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	cout << "Array after normal Bubble sort: ";
	auto start = high_resolution_clock::now();
	bubble_sort(a, N);
	auto end = high_resolution_clock::now();
	auto dur = duration_cast<microseconds>(end - start);
	for(int i = 0; i < N; i++) {cout << a[i] <<" ";} cout << endl;

	cout << "Time taken : " <<dur.count() << " ms" <<endl; 	

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	cout << "Array after parallel Bubble sort: ";
	start = high_resolution_clock::now();
	bubble_sort_p(a1, N);
	end = high_resolution_clock::now();
	dur = duration_cast<microseconds>(end - start);
	for(int i = 0; i < N; i++) {cout << a1[i] <<" ";} cout << endl;

	cout << "Time taken : " <<dur.count() << " ms" <<endl; 	


//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	cout << "Array after normal Merge sort: ";
	start = high_resolution_clock::now();
	merge_sort(a2, 0, N-1);
	end = high_resolution_clock::now();
	dur = duration_cast<microseconds>(end - start);
	for(int i = 0; i < N; i++) {cout << a2[i] << " ";} cout << endl;
	cout << "Time taken : " <<dur.count() << " ms" <<endl; 	
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
	cout << "Array after parallel Merge sort: ";
	start = high_resolution_clock::now();
	merge_sort_p(a3, 0, N-1);
	end = high_resolution_clock::now();
	dur = duration_cast<microseconds>(end - start);
	for(int i = 0; i < N; i++) {cout << a3[i] << " ";} cout << endl;
	cout << "Time taken : " <<dur.count() << " ms" <<endl; 	
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
  
}
'''

s7 = '''
#include <bits/stdc++.h>
#include <omp.h>

using namespace std;

int N = 6, a[100];

void max_red(int a[], int n) {
	int mx = INT_MIN;
	
	#pragma omp parallel for reduction(max: mx)
	for(int i = 0; i < n; i++) if(a[i] > mx) mx = a[i];
	
	cout << "Maximum value: " << mx << endl; 
}
void min_red(int a[], int n) {
	int mn = INT_MAX;
	
	#pragma omp parallel for reduction(min: mn)
	for(int i = 0; i < n; i++) if(a[i] < mn) mn = a[i];
	
	cout << "Minimum value: " << mn << endl; 
}


void sum_red(int a[], int n) {
	int sum = 0;
	
	#pragma omp parallel for reduction(+: sum)
	for(int i = 0; i < n; i++) sum += a[i];
	
	cout << "Sum: " << sum << endl; 
}


void avg_red(int a[], int n) {
	double sum = 0, cnt = n;
	
	#pragma omp parallel for reduction(+: sum)
	for(int i = 0; i < n; i++) sum += a[i];
	double avg = sum / cnt;
	cout << "Average: " << avg << endl; 
}

int main() {
	cout << "Enter " << N << " elements: ";
	int a[N] ;	
	for(int i = 0; i < N; i++) cin >> a[i];
	
	max_red(a, N);
	min_red(a, N);
	sum_red(a, N);
	avg_red(a, N);
	max_red(a, N);
}

/* 
Sample Input :
3 1 8 0 5

*/
'''

s8 = '''
#include <iostream>
#include <vector>

// CUDA kernel function for vector addition
__global__ void vectorAddition(const float* a, const float* b, float* result, int size) {
    int index = blockIdx.x * blockDim.x + threadIdx.x;

    if (index < size) {
        result[index] = a[index] + b[index];
    }
}

int main() {
    int size = 1000000;  // Size of the vectors
    std::vector<float> a(size, 1.0f);  // Vector a initialized with 1.0
    std::vector<float> b(size, 2.0f);  // Vector b initialized with 2.0
    std::vector<float> result(size);   // Result vector

    // Declare device pointers
    float* d_a;
    float* d_b;
    float* d_result;

    // Allocate memory on the device
    cudaMalloc(&d_a, size * sizeof(float));
    cudaMalloc(&d_b, size * sizeof(float));
    cudaMalloc(&d_result, size * sizeof(float));

    // Copy input vectors from host to device
    cudaMemcpy(d_a, a.data(), size * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, b.data(), size * sizeof(float), cudaMemcpyHostToDevice);

    // Define the grid and block sizes
    int blockSize = 256;
    int gridSize = (size + blockSize - 1) / blockSize;

    // Launch the kernel on the GPU
    vectorAddition<<<gridSize, blockSize>>>(d_a, d_b, d_result, size);

    // Copy the result vector from device to host
    cudaMemcpy(result.data(), d_result, size * sizeof(float), cudaMemcpyDeviceToHost);

    // Print the result
    for (int i = 0; i < size; ++i) {
        std::cout << result[i] << " ";
    }
    std::cout << std::endl;

    // Free device memory
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_result);

    return 0;
}
'''

s9 = '''

#include <iostream>
#include <vector>

// CUDA kernel function for matrix multiplication
__global__ void matrixMultiplication(const float* a, const float* b, float* result, int size) {
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;

    if (row < size && col < size) {
        float sum = 0.0f;
        for (int k = 0; k < size; ++k) {
            sum += a[row * size + k] * b[k * size + col];
        }
        result[row * size + col] = sum;
    }
}

int main() {
    int size = 1000;  // Size of the matrices
    std::vector<float> a(size * size, 1.0f);  // Matrix a initialized with 1.0
    std::vector<float> b(size * size, 2.0f);  // Matrix b initialized with 2.0
    std::vector<float> result(size * size);   // Result matrix

    // Declare device pointers
    float* d_a;
    float* d_b;
    float* d_result;

    // Allocate memory on the device
    cudaMalloc(&d_a, size * size * sizeof(float));
    cudaMalloc(&d_b, size * size * sizeof(float));
    cudaMalloc(&d_result, size * size * sizeof(float));

    // Copy input matrices from host to device
    cudaMemcpy(d_a, a.data(), size * size * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, b.data(), size * size * sizeof(float), cudaMemcpyHostToDevice);

    // Define the block and grid sizes
    dim3 blockSize(16, 16);
    dim3 gridSize((size + blockSize.x - 1) / blockSize.x, (size + blockSize.y - 1) / blockSize.y);

    // Launch the kernel on the GPU
    matrixMultiplication<<<gridSize, blockSize>>>(d_a, d_b, d_result, size);

    // Copy the result matrix from device to host
    cudaMemcpy(result.data(), d_result, size * size * sizeof(float), cudaMemcpyDeviceToHost);

    // Print the result (Optional)
    // for (int i = 0; i < size; ++i) {
    //     for (int j = 0; j < size; ++j) {
    //         std::cout << result[i * size + j] << " ";
    //     }
    //     std::cout << std::endl;
    // }

    // Free device memory
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_result);

    return 0;
}
'''

s10 = '''
#include<bits/stdc++.h>
#include<omp.h>
using namespace std;

int N = 5;

double linear_reg(const double x[], const double y[]) {
	double x_mean = 0, y_mean= 0;

	#pragma omp parallel for reduction(+: x_mean, y_mean)
	for(int i = 0; i < N; i++) {
		x_mean += x[i];
		y_mean += y[i];	
	}
	
	double n = N;
	x_mean /= n;
	y_mean /= n;

	double num = 0, den = 0;
	

	#pragma omp parallel for reduction(+: num, den)
	for( int i = 0; i < N; i++) {
		num += (x[i] - x_mean) * (y[i] - y_mean);
		den += (x[i] - x_mean) * (x[i] - x_mean);
	}

	return num / den;
}

int main() {
	double x[N], y[N];
	cout << "Enter co-ordinates(x, y) of " << N <<" points" <<endl;
	for(int i = 0 ; i < N; i ++) {
		cin >> x[i] >> y[i];	
	}

	cout << "Linear Regression line has slope : " << linear_reg(x, y) <<endl;

	return 0;
}
'''


a = [s1, s2, s3, s4, s5, s6, s6, s7, s8, s9, s10]

def pray(number):
    if number < 1 or number > 10:
        return "Laude 1 se 10 tak ke hi codes hai isme"
    return a[number - 1]