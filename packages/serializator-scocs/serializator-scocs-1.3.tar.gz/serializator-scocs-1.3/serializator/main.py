import pickle
import serializator

serializator.my_dump('somefile.py', 7)

def my_dump(output_filename, obj):
    with open(output_filename, 'wb') as file:
        pickle.dump(obj, file)


def my_load(input_filename):
    with open(input_filename, 'rb') as file:
        pickle.load(file)
