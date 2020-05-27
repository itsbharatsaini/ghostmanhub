from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist
from keras.utils import np_utils
from datetime import datetime

(X_train, y_train), (X_test, y_test) = mnist.load_data()
no_of_pixel = X_train.shape[1] * X_train.shape[2]

X_train = X_train.reshape((X_train.shape[0], no_of_pixel)).astype('float32')
X_train = X_train / 255
y_train = np_utils.to_categorical(y_train)

X_test = X_test.reshape((X_test.shape[0], no_of_pixel)).astype('float32')
X_test = X_test / 255
y_test = np_utils.to_categorical(y_test)

no_of_output_neuron = y_test.shape[1]
def create_model(no_of_input_neuron,no_of_pixel=no_of_pixel,no_of_output_neuron=no_of_output_neuron):
    model = Sequential()
    model.add(Dense(no_of_input_neuron, input_dim=no_of_pixel, kernel_initializer='normal', activation='relu'))
    model.add(Dense(no_of_output_neuron, kernel_initializer='normal', activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=5, batch_size=200, verbose=0)
    return model


def get_accuracy(model): 
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_str = "Date and Time : "+date_time
    print(dt_str)
    scores = model.evaluate(X_test, y_test, verbose=0)
    accuracy = scores[1]*100
    
    with open("accuracy_logs.txt","a+") as file:
        file.write(str(dt_str+'\n'))
        log ='Accuracy : '+ str(accuracy)+'\n\n'+'*'*40
        print(log)
        file.write(str(log+"\n\n"))
        file.close()
    return accuracy
def save_model(model):    
    print('_'*40+"\nSaving the best model ...!")
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_str = "Date and Time : "+date_time
    
    model.save('mnist.model')
    
    with open("result.txt","w") as file:
        file.write(str(dt_str+"\n"))
        log ='Accuracy : '+ str(accuracy)+'\n\n'+'*'*40+"\n"
        file.write(str(log))
        file.close()
    print('final model is saved with "mnist.model" filename. ')

if __name__ == "__main__":
    no_of_input_neuron=no_of_pixel
    model = create_model(no_of_input_neuron)
    accuracy = get_accuracy(model)
    save_model(model)