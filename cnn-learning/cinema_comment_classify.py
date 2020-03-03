from keras.datasets import imdb

# 高频率 10000 个单词
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words = 10000)

# 映射为以整数为索引的字典
word_index = imdb.get_word_index()

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])