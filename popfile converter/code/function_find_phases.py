'''
只针对固液共存区的实验数据
这个函数的作用是把相转换的式子拆开并把不重复的相读入一个字典型中
例如：
print(find_phases("LIQUID->LIQUID+DIS_FCC"))
输出为
{'phase1': 'LIQUID', 'phase2': 'DIS_FCC'}
'''
def find_phases(transition) -> dict:
       
    try:
        transition = transition.strip()
        transition = transition.replace(' ', '')
        transition = transition.split('->')
        pre = transition[0]
        post = transition[1]
        pre = pre.split('+')
        post = post.split('+')
    except:
        print('transition formula goes wrong, phases can only be connected by "->" and "+"')
        import sys
        sys.exit()
    '''
    上面的代码的作用是：
    - 一定程度上规范化转换式，去掉字符串前后和之中的空格
    - 拆开表达式，只保留相的部分
    '''

    try:
        if len(pre) == 1:    
            phase_dict = dict.fromkeys(pre + post)
        elif len(pre) == 2:            
            if pre[0] == 'LIQUID':
                phase_dict = dict.fromkeys(pre + post)           
            elif pre[1] == 'LIQUID':
                pre[0], pre[1] = pre[1], pre[0]
                phase_dict = dict.fromkeys(pre + post)             
    except:
        print('transition formula goes wrong, check the number of phases')
        import sys
        sys.exit()                  
    # print(list(phase_dict))
    '''
    上面的代码的目的是不重复的，按一定顺序地把相存进一个字典
    - 这里用了dict.fromkeys，所以读入的相名会被当做key来读入字典型，去掉重复的并保持原来的顺序
    - 这里主要考虑的是固液共存区的实验数据
    - 会保持LIQUID在第一个
    '''

    try:
        phases = {}
        i = 0
        for phase in list(phase_dict):
            phases[f'phase{i+1}'] = phase
            i = i + 1
    except:
        print('transition formula goes wrong')
        import sys
        sys.exit()
    # print(phases[f"phase{i+1}"])
    return phases
    '''
    这里的作用就是循环读入phase的名字到的（key）phase1，phase2，phase3...中
    '''
#print(find_phases("LIQUID->LIQUID+DIS_FCC"))
#print(find_phases("LIQUID+MU->MU"))
#print(find_phases("LIQUID+BCC_B2->MU"))
#print(find_phases("LIQUID +BCC _B2->MU"))
#print(find_phases("LIQU ID +BCC _B 2->MU"))
#print(find_phases("LIQUID+BCC_B2MU"))    
#print(find_phases("MU+BCC_B2->MU"))    
