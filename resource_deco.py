from auth import authenticate
from datetime import datetime
run_time=datetime.now()
get_time =run_time.strftime("%d-%m-%Y %H:%M:%S")

from contextlib import contextmanager

@contextmanager
def open_file(name,option):
    write_to=open(name,option)
    try:
        yield write_to
    finally:
        f.close()
    

def resource_deco(email='example@email.com', password='example123'):
     
    def check_role(fun):
        user = authenticate(email, password)
        def wrapper():
            if user:
                if user['role']=='admin'or user['role']=='superadmin':
                    fun()
                    result=f"{user['first_name']} {user['last_name']}\n{fun()}"
                    with open("access_granted.txt",'a') as write_to:
                        write_to.write(f'\n{user["role"]} {user["first_name"]} {user["last_name"]} tried to view this resources at {get_time}')
                    return result

                elif user['role']!='admin' or user['role']!='superadmin':
                    call_out=(f"{user['first_name']} {user['last_name']}\nYou are not allowed to view this resource")
                    with open("access_denied.txt",'a') as write_to:
                            write_to.write(f"\n{user['role']} {user['first_name']} {user['last_name']} tried to view this resources at {get_time}")  
                    return call_out        
            else:
                return "Only staff can access this resource"
        return wrapper   
    return check_role

    
    


       

            
