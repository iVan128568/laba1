# TODO Напишите функцию для поиска индекса товара

def find(arr, elem):
    findd = [i for i in range(len(arr)) if arr[i] == elem]
    return findd[0] if len(findd) else None



items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")





