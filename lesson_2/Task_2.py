list_1=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_2=['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']
lists=[list_1, list_2]
for lst in lists:
    len_list = len(lst)
    i=0
    while i!=len_list+i//3: # я не знал как сделать этот цикл, поэтому методом тыка +i//3 =)
        if lst[i].isdigit()==True:
            lst[i]=list_1[i].zfill(2)
            lst.insert(i,'"')
            lst.insert(i+2,'"')
            i+=2
        elif '+'in lst[i]:
            _,v1=lst[i].split('+')
            lst[i] ="+%s" %(v1.zfill(2))
            lst.insert(i,'"')
            lst.insert(i+2,'"')
            i+=2
        elif '-' in lst[i]:
            _, v1 = lst[i].split('-')
            lst[i]="-%s" % (v1.zfill(2))
            lst.insert(i,'"')
            lst.insert(i+2,'"')
            i+=2
        else:
            i+=1
    print(lst,'\n')