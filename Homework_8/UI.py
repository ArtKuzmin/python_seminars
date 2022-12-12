import view, backend

def run():
    while True:
        view.menu()        
        match input():
            case "1":
                backend.create_db()
            case "2":
                backend.insert_entry()                
            case "3":
                backend.delete_employee()
            case "4":
               backend. edit_employee()
            case "5":
                view.print_db()            
            case "0":
                print("Программа завершена")
                break
                

def add_employee():
   temp_entry = input("Введите id, имя, фамилию, возраст, отдел и телефон сотрудника через пробел: ").split()
   return (int(temp_entry[0]), temp_entry[1], temp_entry[2], int(temp_entry[3]), temp_entry[4], int(temp_entry[5]))


def delete_employee():   
    return int(input("Введите id сотрудника, запись о котором вы хотите удалить: "))  


def edit_employee():
    id =  int(input("Введите id сотрудника, данные которого вы хотите изменить: "))
    view.edit_menu()
    match input():
            case "1":
               value = input("Введите новое имя сотрудника: ")               
               col = "Имя"               
            case "2":
               value = input("Введите новую фамилию сотрудника: ")                              
               col = "Фамилия"
            case "3":
               value = input("Введите новый возраст сотрудника: ")                                            
               col = "Возраст"
            case "4":
               value = input("Введите новый отдел сотрудника: ")                                                          
               col = "Отдел"
            case "5":
               value = input("Введите новый телефон сотрудника: ")                                                         
               col = "Телефон"
    return (col, value, id)

