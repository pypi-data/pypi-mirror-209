#The DeepMap is a deep learning based python package for genotype to phenotype mapping in rice breeding and can be utilize for other prediction-based studies. It is based on multiple genetic-interactions approach for data augmentation and objects for the simplicity/reproducibility of the research by employing four lines of genomic prediction code.
"""
Created on Thu Sep  9 11:47:12 2021
@author: Ajay Kumar at International Rice Research Institute, South Asia Hub, Hyderabad, India
"""
#Importing Libraries
# from tabgan.sampler import OriginalGenerator, GANGenerator
from keras.layers import LeakyReLU, BatchNormalization, Dense, Dropout
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import mean_squared_error
from keras.callbacks import ReduceLROnPlateau
from keras.callbacks import ModelCheckpoint
from keras.callbacks import EarlyStopping
from tensorflow.keras import regularizers
from keras.models import Model,Sequential
from keras.layers import concatenate
from sklearn.metrics import r2_score
from keras.models import load_model
from keras.optimizers import Adam
from scipy.stats import pearsonr
import matplotlib.pyplot as plt 
import seaborn as sns
import tensorflow as tf
import pandas as pd
import numpy as np
import sklearn
import math
import os

def DeepMap(trainX,valX,trainy,valy,count,input_dimension,epochs,batch_size,learning_rate):
    # define model
    model = Sequential()
    lrelu = LeakyReLU(alpha = 0.1)
    model.add(Dense(2143,input_dim=input_dimension, activation=lrelu,kernel_regularizer=regularizers.l1(0.01), kernel_initializer='he_uniform'))
    model.add(Dense(512, activation="relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))
    model.add(Dense(512,activation="relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))
    model.add(Dense(512, activation="relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))
    model.add(Dense(512, activation="relu"))
    model.add(BatchNormalization())
    model.add(Dense(256, activation="relu"))
    model.add(BatchNormalization())
    model.add(Dense(32, activation="relu"))
    model.add(BatchNormalization())
    model.add(Dense(1, activation="linear"))
    model.compile(loss='mse', optimizer='adam',metrics='mse') # compile model
    learning_rate_reduction = ReduceLROnPlateau(monitor='val_mse',patience=2,verbose=1,factor=0.5,min_lr=0.001)
    Early_stopping = EarlyStopping(monitor='val_mse',verbose=1,restore_best_weights=True,patience=20)
    history = model.fit(trainX, trainy,validation_data=(valX,valy),epochs=epochs, verbose=1,batch_size=2143,callbacks=[learning_rate_reduction,ModelCheckpoint(filepath='./weights.hdf5',monitor='val_mse',verbose=1,save_best_only=True)]) # fit model
    predicted_train = model.predict([trainX])
    predicted_test = model.predict([valX])
    corr_training = pearsonr(trainy, predicted_train[:,0])[0]
    corr_testing = pearsonr(valy, predicted_test[:,0])[0]
    mse_train = sklearn.metrics.mean_squared_error(trainy, predicted_train)
    rmse_train = math.sqrt(mse_train)
    mse_test = sklearn.metrics.mean_squared_error(valy, predicted_test)
    rmse_test = math.sqrt(mse_test)
    r2_train = r2_score(trainy,predicted_train)
    r2_test = r2_score(valy,predicted_test)
    #len_scatter = len(valy) 
    predicted_test[:,0]
    predict_valy = pd.concat([pd.DataFrame(valy),pd.DataFrame(predicted_test[:,0])],axis=1)
    predict_valy.columns = ["Actual","Predicted"]
    predict_valy.to_csv("predict_valy_%s.csv"%count,index=None,header=True)
    #seq_x = list(range(0,len_scatter))
    scatter_plot(trainy,valy,predicted_train,predicted_test,count)
    plt.clf()
    # summarize history for loss
    hist = history.history
    plot_loss(hist,count)
    plt.clf()
    temp = [mse_train,mse_test,rmse_train,rmse_test,r2_train,r2_test,corr_training,corr_testing]
    print(temp)
    model.save("model_save.h5")
    return temp

def plot_loss(hist,count):
    plt.plot(hist['loss']) #double lines plot function
    plt.plot(hist['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper right')
    plt.savefig('loss_train_test_%s.jpg'%count)
    
    
def data_preprocessing(geno_pheno, genotypic_additive,genotypic_dominance,epochs,batch_size,n_splits,learning_rate):
    phenotypic_info = geno_pheno.iloc[:,1] #Location-1 phenotypic data
    print(phenotypic_info)
    result = pd.DataFrame(data=None,columns=('MSE_train','MSE_test','RMSE_train','RMSE_test','r2_train','r2_test','Corr_train','Corr_test'))
    A_square = genotypic_additive * genotypic_additive
    D_square = genotypic_dominance * genotypic_dominance
    additive_dominance = genotypic_additive * genotypic_dominance
    genotypic_data_merged = np.concatenate([genotypic_additive,genotypic_dominance,A_square,D_square,additive_dominance])
    phenotypic_info = pd.concat([phenotypic_info,phenotypic_info,phenotypic_info,phenotypic_info,phenotypic_info])
    phenotypic_info = phenotypic_info.to_numpy()
    input_dimension = len(genotypic_additive)
    kf = KFold(n_splits=n_splits)
    count=0
    for train_index, val_index in kf.split(phenotypic_info):
        print("Train:",train_index,"Test:",val_index)
        trainX, valX = genotypic_data_merged[train_index,],genotypic_data_merged[val_index,]
        trainy, valy = phenotypic_info[train_index],phenotypic_info[val_index]
        print("[INFO] training started model..., Please wait!")
        temp=DeepMap(trainX,valX,trainy,valy,count,input_dimension,epochs,batch_size,learning_rate)
        result.loc[count] = temp
        count = count + 1 
    result.to_csv('result.csv')
    corr_test=result['Corr_test'].to_numpy()
    plot(range(1,11),corr_test) #Manually call this function for this graph, otherwise it will merge.
    #Uncommnet to evaluate this model.
    #from keras.models import load_model
    #loaded_model = load_model("filename.h5")
    #loss, accuracy = loaded_model.evaluate(testX, testy)

def plot(x,y): #plot for correlation validations
    plt.plot(y)
    plt.title('Correlation Validations')
    plt.ylabel('Percentage')
    plt.xlabel('Cross validations')
    plt.savefig('CV.jpg')
    
def scatter_plot(seq_train,seq_test,seq_pred_train,seq_pred_test,count): #scatterplot for original and predicted value
    seq_train = (seq_train - (sum(seq_train) / len(seq_train))) / (np.std(seq_train))
    seq_pred_train = (seq_pred_train - (sum(seq_pred_train) / len(seq_pred_train))) / (np.std(seq_pred_train))
    seq_test = (seq_test - (sum(seq_test) / len(seq_test))) / (np.std(seq_test))
    seq_pred_test = (seq_pred_test - (sum(seq_pred_test) / len(seq_pred_test))) / (np.std(seq_pred_test))
    plt.scatter(seq_train,seq_pred_train,c="Black")
    plt.scatter(seq_test,seq_pred_test,c="Blue")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.savefig('plot_scatter_%s.png'%count) #Image saved


def main(geno_pheno, genotypic_additive, genotypic_dominance,epochs,batch_size,n_splits,learning_rate):
    import time
    start_time = time.time()
    data_preprocessing(geno_pheno, genotypic_additive,genotypic_dominance,epochs,batch_size,n_splits,learning_rate)
    print('%s time taken by programme is' %(time.time() - start_time))
