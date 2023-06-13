#ножество - список только уникальных значений abcd -> abcd

# def strcounter(s):
#     for symbol in set(s):
#         counter = 0
#         for sub_symbol in s:
#             if symbol == sub_symbol:
#                 counter += 1
#         print(symbol, counter)
#
# strcounter("abcda")

def strcounter(s):
    syms_counter = {}
    for symbol in s:
        syms_counter[symbol] = syms_counter.get(symbol, 0) + 1

    for symbol, count in syms_counter.items():
        print(symbol, count)

strcounter("hello world")