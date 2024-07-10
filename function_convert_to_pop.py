import pandas as pd
import find_phases as find_phases
import find_common_elements as find_common_elements

def convert_to_pop(filename, pop_file):
        """读取 Excel 文件并返回 DataFrame"""
        df = pd.read_excel(filename)
        """要确定一个excel文件的命名规则，即：
        两个元素要放在最前面，用'-'连接
        而且元素排列顺序与对应元素组成顺序一致
        比如： W-Co experimental data.xlsx
        文件内顺序为x(W), x(Co)"""
        filename = filename.split()[0].split('-')
        element1 = filename[0]
        element2 = filename[1]
        elements = dict()
        x_element1 = f"x_element_{element1}"
        x_element2 = f"x_element_{element2}"
        
        with open(pop_file, 'w') as file:
            # 写入 POP 文件头部信息（根据实际需要修改）
            # 遍历 DataFrame 的每一行，写入 POP 文件
            HEADER = input('please type in popfile info: ')
            file.write(HEADER + "\n\n")
            file.write('ENTER_SYMBOL CONSTANT DX=0.02, P0=101325, DH=500, DT=10\n\n')
            i = 1
            for index, row in df.iterrows():
                if row.isnull().all():
                    print(f"Row {index + 1} is empty. Exiting the program.")                    
                else:                                 
                    elements[x_element1] = row['x(' + element1 +')']
                #    print(row['x(' + element1 +')'])
                    elements[x_element2] = row['x(' + element2 +')']    
                #    print(row['x(' + element2 +')'])
                #    print(elements.items())
                    temperature_C = row['Temperature/ºC']
                    temperature_K = row['Temperature/K']
                    lable = row['Lable']
                    transition = row['Transition']
                    find_phases_result = find_phases(transition)
                    phases = find_phases_result[0]
                    pre = find_phases_result[1]
                    post = find_phases_result[2]
                    #print(phases, pre, post)
                    phase1 = phases['phase1']
                    phase2 = phases['phase2']
                    if len(phases) == 3:
                        phase3 = phases['phase3']
                    paper = row['Paper']
                    reporter = row['Reporter']
                    methodology = row['Methodology']
                        
                    #print(phase1, 
                    #      phase2, 
                    #      phase3 if 'phase3' in locals() else "")
                       
                    file.write(f"CREATE_NEW_EQUILIBRIUM, {i}, 1\n")    
                    
                    if  find_common_elements(pre, post):
                        common_elements, unique_to_list1, unique_to_list2 = find_common_elements(pre, post)
                        print(common_elements, unique_to_list1, unique_to_list2)
                        file.write(f"CHANGE_STATUS PHASE {common_elements[0]} = FIX 1\n")
                        if unique_to_list1 == [] and unique_to_list2:
                            file.write(f"CHANGE_STATUS PHASE {unique_to_list2[0]} = FIX 0\n")
                        elif unique_to_list1 and unique_to_list2 == []:     
                            file.write(f"CHANGE_STATUS PHASE {unique_to_list1[0]} = FIX 0\n")
                        elif unique_to_list1 and unique_to_list2:
                            file.write(f"CHANGE_STATUS PHASE {unique_to_list1[0]} = FIX 0\n")
                            file.write(f"CHANGE_STATUS PHASE {unique_to_list2[0]} = FIX 1\n")
                        if len(phases) == 3:
                            file.write(f"CHANGE_STATUS PHASE {unique_to_list2[0]} = FIX 1\n") 
                    else:
                        file.write(f"CHANGE_STATUS PHASE {phase1} = FIX 1\n")
                        file.write(f"CHANGE_STATUS PHASE {phase2} = FIX 1\n")
                        file.write(f"CHANGE_STATUS PHASE {phase3} = FIX 1\n") 
                        
                    file.write(f"EXPERIMENT T={temperature_K}:DT\n")
                    file.write(f"LABEL {lable}\n")
                    file.write(f"SET_START_VALUE T={temperature_K}\n")
                    file.write("\n")  # 空行分隔每个记录
                    i = i + 1
                    
            file.write("SAVE_WORKSPACES\n")  # 添加 SAVE_WORKSPACES
                              
            return 
        
convert_to_pop("W-Co experimental data.xlsx", "output.pop")


    
