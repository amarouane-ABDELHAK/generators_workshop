import psutil
import resource
import os
import sys
import random
import time


names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
fields = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def memory_usage_psutil(when):
    # return the memory usage in MB
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    print(f'Memory ({when}) : {mem} Mb')


def memory_usage_resource(when):
    rusage_denom = 1024.
    if sys.platform == 'darwin':
        # ... it seems that in OSX the output is different units ...
        rusage_denom = rusage_denom * rusage_denom
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
    print(f'Memory ({when}) : {mem} Mb')




def generate_employees(how_many):
    employees = []

    while how_many > 0:
        employees.append({
            "name": random.choice(names),
            "age": random.randint(20, 60),
            "departement": random.choice(fields)
        })
        how_many -= 1
    return employees

def generate_employees_generator(how_many):
    while how_many > 0:
        employee = {
            "name": random.choice(names),
            "age": random.randint(20, 60),
            "departement": random.choice(fields)
        }
        yield employee
        how_many -= 1
    
def compute_process_time(start):
    print(f"Took {round(time.process_time() -  start, 2)} seconds")


if __name__ == "__main__":
    start = time.process_time()
    memory_usage_psutil("Before")
    employees = generate_employees(1E6)
    #employees = generate_employees_generator(1E6)
    for i, employee in enumerate(employees):
        if i % 1E5 == 0:
            print(employee, i)
    memory_usage_psutil("After")
    compute_process_time(start)

    

    
    


    