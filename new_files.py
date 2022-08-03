
import os

cur_dir = ''
for i in range(0, 10000):
    if i % 1000 == 0:
        cur_dir = f'files_{i}'
        os.makedirs(cur_dir, exist_ok=True)
    
    with open(f'{cur_dir}/file_{i}.cpp', 'w+') as f:
        f.write(f'''
class CA{i} {'{'}
    void test1() {'{'}
        int i=0;
        for (i=0; i<1000; i++) {'{'}
            if (i>30) 
                printf('abc');
            else
                print('def');
        {'}'}
    {'}'}
    void test2() {'{'}
        int i=0;
        for (i=0; i<1000; i++) {'{'}
            if (i>30) 
                printf('abc');
            else
                print('def');
        {'}'}
    {'}'}
    void test3() {'{'}
        int i=0;
        for (i=0; i<1000; i++) {'{'}
            if (i>30) 
                printf('abc');
            else
                print('def');
        {'}'}
    {'}'}
    void test4() {'{'}
        int i=0;
        for (i=0; i<1000; i++) {'{'}
            if (i>30) 
                printf('abc');
            else
                print('def');
        {'}'}
    {'}'}
{'}'}
        ''')
    