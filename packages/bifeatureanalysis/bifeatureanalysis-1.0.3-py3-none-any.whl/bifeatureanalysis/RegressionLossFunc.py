'''
Date         : 2023-05-18 17:19:31
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-05-18 17:53:16
LastEditors  : BDFD
Description  : 
FilePath     : \bifeatureanalysis\RegressionLossFunc.py
Copyright (c) 2023 by BDFD, All Rights Reserved. 
'''
import numpy as np
import pandas as pd
import math as math

'''
Three are three common loss function in Regression Model included:
1) Mean Squared Error(MSE)
2) Mean Absolute Error(MAE)
3) Root Mean Squared Error(RMSE)
4) Mean Bias Error(MBE)
5) Huber Loss(HL)
'''


def MSE(y, y_predicted):
    '''
    MSE stands for Mean Square Error
    均方误差(MSE)
    均方误差是指所有预测值和真实值之间的平方差，并将其平均值。常用于回归问题。
    '''
    y = np.asarray(y)
    y_predicted = np.asarray(y_predicted)
    sq_error = (y_predicted - y) ** 2
    # print(sq_error)
    sum_sq_error = np.sum(sq_error)
    mse = sum_sq_error/y.size
    return mse

def MAE (y, y_predicted):
    '''
    MAE stands for Mean Absolute Error
    平均绝对误差(MAE)
    作为预测值和真实值之间的绝对差的平均值来计算的。当数据有异常值时，这是比均方误差更好的测量方法。
    '''
    y = np.asarray(y)
    y_predicted = np.asarray(y_predicted)
    error = y_predicted - y
    absolute_error = np.absolute(error)
    total_absolute_error = np.sum(absolute_error)
    mae = total_absolute_error/y.size
    return mae

def RMSE (y, y_predicted):
    '''
    RMSE stands for Root Mean Squared Error
    这个损失函数是均方误差的平方根。如果我们不想惩罚更大的错误，这是一个理想的方法。
    '''
    y = np.asarray(y)
    y_predicted = np.asarray(y_predicted)
    sq_error = (y_predicted - y) ** 2
    total_sq_error = np.sum(sq_error)
    mse = total_sq_error/y.size
    rmse = math.sqrt(mse)
    return rmse

def MBE (y, y_predicted):
    '''
    MBE stands for Mean Bias Error   
    类似于平均绝对误差但不求绝对值。这个损失函数的缺点是负误差和正误差可以相互抵消，
    所以当研究人员知道误差只有一个方向时，应用它会更好。
    '''
    y = np.asarray(y)
    y_predicted = np.asarray(y_predicted)
    error = y_predicted -  y
    total_error = np.sum(error)
    mbe = total_error/y.size
    return mbe

def hubber_loss (y, y_predicted):
    '''
    Hubber Loss Function
    Huber损失函数结合了平均绝对误差(MAE)和均方误差(MSE)的优点。这是因为Hubber损失是一个有两个分支的函数。一个分支应用于符合期望值的MAE，另一个分支应用于异常值。
    '''
    y = np.asarray(y)
    y_predicted = np.asarray(y_predicted)
    delta = 1.35 * MAE(y, y_predicted)
    y_size = y.size
    total_error = 0
    for i in range (y_size):
        error = np.absolute(y_predicted[i] - y[i])
        if error < delta:
            hubber_error = (error * error) / 2
        else:
            hubber_error = (delta * error) / (0.5 * (delta * delta))
        total_error += hubber_error
    total_hubber_error = total_error/y.size
    return total_hubber_error