#!python3
depends = [
    '受付期間',
    '申請期間',
    '申請受付期間'
]

if __name__ == '__main__':
    length = len(depends[0])
    
    for each in depends:
        if length > len(each):
            length = len(each)
    
    print(length)