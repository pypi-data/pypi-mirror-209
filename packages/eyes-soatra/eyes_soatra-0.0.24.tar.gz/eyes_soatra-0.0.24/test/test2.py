#!python3
# import jellyfish
from eyes_soatra import eyes

# w1 = 'bcde'
# w2 = 'abcde'
# a = jellyfish.jaro_similarity(w2, w1)

# print(a)
a = eyes.view_page(
    url='https://www.town.ichikawa.lg.jp/Error/Error404',
    show_header=True,
)
print(a)