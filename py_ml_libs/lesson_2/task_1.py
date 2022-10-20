import numpy as np
import pandas as pd

# ============ Numpy Task 1 ============

# Значения для инициализации столбца 1
column_1 = [1, 2, 3, 3, 1]

# Значения для инициализации столбца 2
column_2 = [6, 8, 11, 10, 7]

# Создание массива типа array + транспонирование
np_array = np.array([column_1, column_2]).transpose()

# Нахождение среднего значения по каждому признаку
mean_signs = np_array.mean(axis=0)

# ============ Numpy Task 2 ============

# Вычитание вычисленных средних значений от элементов матрицы

# Способ 1
np_array_centered_var_1: np.ndarray = np_array - mean_signs

# Способ 2
np_array_centered_var_2: np.ndarray = np.subtract(np_array, mean_signs)

# Numpy Task 3
scalar_signs = np.dot(
    np_array_centered_var_1[:, 0],
    np_array_centered_var_1[:, 1]
)

# Деление результата скалярного произведения на (число наблюдений - 1)
task_res = scalar_signs / (np_array_centered_var_1.shape[0] - 1)

# ============ Pandas Task 1 ============

authors = pd.DataFrame(
    {
        'author_id': [1, 2, 3, ],
        'author_name': ['Тургенев', 'Чехов', 'Островский', ]
    }
)

books = pd.DataFrame(
    {
        'author_id': [1, 1, 1, 2, 2, 3, 3, ],
        'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза',
                       'Таланты и поклонники', ],
        'price': [450, 300, 350, 500, 450, 370, 290, ]

    }
)

# ============ Pandas Task 2 ============

authors_price = pd.merge(authors, books, on='author_id')

# ============ Pandas Task 3 ============

top5 = authors_price.nlargest(5, 'price')

# ============ Pandas Task 4 ============

authors_stat = pd.DataFrame()

authors_price_groups = authors_price.groupby('author_name')

for group_name in authors_price_groups.groups:
    df_to_add = pd.DataFrame(
        {
            'author_name': [group_name],
            'min_price': [authors_price_groups.get_group(group_name)['price'].min(axis=0)],
            'max_price': [authors_price_groups.get_group(group_name)['price'].max(axis=0)],
            'mean_price': [round(authors_price_groups.get_group(group_name)['price'].mean(axis=0), 2)]
        }
    )
    authors_stat = pd.concat([authors_stat, df_to_add], ignore_index=True)


# ============ Pandas Task 5 ============

authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']

book_info = pd.pivot_table(
    authors_price,
    index='author_name',
    columns='cover',
    aggfunc=np.sum,
    values='price'
).fillna(0)

book_info.to_pickle(r'book_info.pkl')

book_info_from_file = pd.read_pickle(r'book_info.pkl')