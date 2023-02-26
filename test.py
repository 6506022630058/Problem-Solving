class Character:

    def __init__(self,datalist):
        self.name = datalist[0]
        self.hp = datalist[1]
        self.atk = datalist[2]
        self.cr = datalist[3]
        self.cd = datalist[4]

def stat():
        n = input('Name: ')
        point = 10
        point1 = 0
        point2 = 0
        point3 = 0
        point4 = 0
        h = 10+(point1*2)
        a = 2+(point2*1)
        r = 2+(point3*2)
        d = 4+(point4*4)
        ans = ''
        while point != 0 and ans != 'q':
            print(point)
            print('1)Hp:',10+(point1*2),'\n'
                  '2)Atk:',a,'\n'
                  '3)Cri rate:',r,'\n'
                  '4)Cri dam:',d,'\n')
            ans = input('stat:')
            if ans == '1':
                point -= 1
                point1 += 1
            elif ans == '2':
                point -= 1
                point2 += 1
            elif ans == '3':
                point -= 1
                point3 += 1
            elif ans == '4':
                point -= 1
                point4 += 1
            elif ans == 'q':
                print('exit...')
        print([n,h,a,r,d])
        return [n,h,a,r,d]

Character(stat())
