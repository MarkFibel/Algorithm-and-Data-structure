class Dictionary:
    def __init__(self):
        self.__keys = []
        self.__values = []

    def get_keys(self):
        return self.__keys

    def get_values(self):
        return self.__values

    def add_value(self, key, value):
        for i in range(len(self.__keys)):
            if self.__keys[i] == key:
                self.__values[i] = value
                break
        else:
            self.__keys.append(key)
            self.__values.append(value)

    def get_by_key(self, key):
        for i in range(len(self.__keys)):
            if self.__keys[i] == key:
                return self.__values[i]
        else:
            return 'NoValueByKey'

    def print_dictionary(self):
        print('DICT')
        for i in range(len(self.__keys)):
            print(f'{self.__keys[i]}: {self.__values[i]}')

