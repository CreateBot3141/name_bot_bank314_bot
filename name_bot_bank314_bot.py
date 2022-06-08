


def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome):
    import time
    import iz_func
    import iz_telegram



    #if message_in == 'Создать новую раздачу' != -1:
    #    iz_func.save_variable (user_id,"status","",namebot)
    #    status = ''
    #    message_out,menu,answer  = iz_telegram.send_message (user_id,namebot,'ОтменаЗапуск','S',0)
    #    label = 'no send'



    if  message_in.find ('/start') != -1:    	
        iz_func.save_variable (user_id,"status","",namebot)
        iz_telegram.language (namebot,user_id)
        status = ''

    if message_in.find ('Отмена') != -1:
        iz_func.save_variable (user_id,"status","",namebot)
        status = ''
        message_out,menu,answer  = iz_telegram.send_message (user_id,namebot,'ОтменаЗапуск','S',0)
        label = 'no send'

    if message_in == 'Создать новую раздачу':
        message_out,menu,answer  = iz_telegram.send_message (user_id,namebot,'Введите логин','S',0)
        iz_telegram.save_variable (user_id,namebot,"status",'Введите логин')
        iz_telegram.save_variable (user_id,namebot,"login",'')
        iz_telegram.save_variable (user_id,namebot,"project",'')
        iz_telegram.save_variable (user_id,namebot,"summ",'')
        iz_telegram.save_variable (user_id,namebot,"system",'')
        iz_telegram.save_variable (user_id,namebot,"wallet",'')
        iz_telegram.save_variable (user_id,namebot,"komment",'')

    if status == 'Введите логин':  
        message_out,menu = iz_telegram.get_message (user_id,'Выберите проект',namebot)
        from telebot import types
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)        
        db,cursor = iz_func.connect ()
        sql = "select id,name from bank314_bot_proekt where 1=1 "
        cursor.execute(sql)
        results = cursor.fetchall()            
        for row in results:
            id,name = row.values()  
            markup.row(name)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)
        iz_telegram.save_variable (user_id,namebot,"status",'Выберите проект')
        iz_telegram.save_variable (user_id,namebot,"login",message_in)
 

    if status == 'Выберите проект':
        label = 'No'                
        db,cursor = iz_func.connect ()
        sql = "select id,name from bank314_bot_proekt where 1=1 "
        cursor.execute(sql)
        results = cursor.fetchall()   
        ## Проверка ввода проекта         
        for row in results:
            id,name = row.values()  
            if message_in == name:
                label = 'Yes'

        if label == 'Yes':
            message_out,menu,answer  = iz_telegram.send_message (user_id,namebot,'Укажите сумму вклада','S',0)
            iz_telegram.save_variable (user_id,namebot,"status",'Сумма вклада')
            iz_telegram.save_variable (user_id,namebot,"project",message_in)
        else: 
            message_out,menu,answer  = iz_telegram.send_message (user_id,namebot,'Нужно выбрать проек','S',0)
            iz_telegram.save_variable (user_id,namebot,"status",'Выберите проект')





    if status == 'Сумма вклада':      
        if message_in.isdigit() == True:
            message_out,menu,answer  = iz_telegram.send_message (user_id,namebot,'Выберите платежную систему','S',0)
            iz_telegram.save_variable (user_id,namebot,"status",'Платежная система')
            iz_telegram.save_variable (user_id,namebot,"summ",message_in)
        else:    
            iz_telegram.save_variable (user_id,namebot,"status",'Сумма вклада')
            message_out,menu,answer  = iz_telegram.send_message (user_id,namebot,'Надо указать сумму','S',0)



    if status == 'Платежная система':
        
        if message_in == 'PerfectMoney':
            message_out,menu,answer  = iz_telegram.send_message (user_id,namebot,'Укажите кашелек','S',0)
            iz_telegram.save_variable (user_id,namebot,"status",'Укажите кашелек')
            iz_telegram.save_variable (user_id,namebot,"system",message_in)
        else:    
            message_out,menu,answer  = iz_telegram.send_message (user_id,namebot,'Выбирете платежную систему из списка','S',0)
            iz_telegram.save_variable (user_id,namebot,"status",'Платежная система')




    if status == 'Укажите кашелек':
        print ('    [+] Укажите кашелек')
        message_out,menu,answer  = iz_telegram.send_message (user_id,namebot,'Введите коментарий','S',0)
        iz_telegram.save_variable (user_id,namebot,"status",'Введите коментарий')
        iz_telegram.save_variable (user_id,namebot,"wallet",message_in)




    if status == 'Введите коментарий':
        print ('    [+] Введите коментарий')
        message_out,menu,answer  = iz_telegram.send_message (user_id,namebot,'Ваш запрос отправлен','S',0)
        iz_telegram.save_variable (user_id,namebot,"status",'')
        iz_telegram.save_variable (user_id,namebot,"komment",message_in)
        login    = iz_telegram.load_variable (user_id,namebot,"login")
        project   = iz_telegram.load_variable (user_id,namebot,"project")
        summ    = iz_telegram.load_variable (user_id,namebot,"summ")
        system   = iz_telegram.load_variable (user_id,namebot,"system")
        wallet = iz_telegram.load_variable (user_id,namebot,"wallet")
        komment  = iz_telegram.load_variable (user_id,namebot,"komment")

        db,cursor = iz_func.connect ()
        adress    = ''
        telefon   = ''

        sql = "INSERT INTO bot_active_user (language,namebot,user_id,login,project,summ,`system`,wallet,komment,adress,telefon) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format ('ru',namebot,user_id,login,project,summ,system,wallet,komment,adress,telefon)
        print ('[sql]',sql)
        cursor.execute(sql)
        db.commit()