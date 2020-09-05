import matplotlib.pyplot as plt
import csv

def plot_history(history, path=None):
    list_epoch = history.epoch
    list_train_loss = history.history['loss']
    list_val_loss = history.history['val_loss']
    list_train_accuracy = history.history['accuracy']
    list_val_accuracy = history.history['val_accuracy']
    batch_sz = history.params['batch_size']

    ##plot loss
    plt.xlabel("epochs")
    plt.ylabel("Loss")
    plt.grid(True)
    plt.plot(list_train_loss, label='train_loss')
    plt.plot(list_val_loss, label='val_loss')
    plt.legend()
    plt.savefig('train_val_loss.png')
    ###clear the previous data
    plt.clf()
    ##plot accuracy
    plt.xlabel("epochs")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.gca().set_ylim(0, 1)
    plt.plot(list_train_accuracy, label='train_loss')
    plt.plot(list_val_accuracy, label='val_loss')
    plt.legend()
    plt.savefig('train_val_accuracy.png')

    ## dump params to train_params.csv
    csv_file = "train_params.csv"
    csv_columns = ['No', 'Name', 'Country']
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in train_params_dict:
                writer.writerow(data)
    except IOError:
        print("I/O error")


