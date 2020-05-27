from main import create_model
from main import get_accuracy
from datetime import datetime

no_of_input_neuron=5

model = create_model(no_of_input_neuron)
accuracy = get_accuracy(model)

count = 0
best_accuracy = accuracy
best_no_of_neuron = no_of_input_neuron

while accuracy < 99 and count < 4:
    print("\nUpdating The Model...")
    count = count + 1
    no_of_input_neuron=no_of_input_neuron*2
    
    model = create_model(no_of_input_neuron)
    accuracy = get_accuracy(model)
    
    if best_accuracy < accuracy:
        best_accuracy = accuracy
        best_no_of_neuron = no_of_input_neuron


def save_model():    
    print('_'*40+"\nSaving the best model ...!")
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_str = "Date and Time : "+date_time
    
    no_of_input_neuron = best_no_of_neuron
    model = create_model(no_of_input_neuron)
    model.save('mnist_best.model')
    accuracy = get_accuracy(model)
    
    with open("result.txt","w") as file:
        file.write(str(dt_str+"\n"))
        log ='Accuracy : '+ str(accuracy)+'\n\n'+'*'*40
        file.write(str(log+"\n\n"))
        file.close()
    print('Best final model is saved with "mnist_best.model" filename. ')
save_model()
