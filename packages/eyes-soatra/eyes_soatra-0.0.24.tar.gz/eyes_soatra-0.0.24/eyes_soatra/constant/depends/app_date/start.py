#!python3
depends = [
    '受付開始日',
    '申請開始日',
    '提出開始',
]

if __name__ == '__main__':
    length = len(depends[0])
    
    for each in depends:
        if length > len(each):
            length = len(each)
    
    print(length)