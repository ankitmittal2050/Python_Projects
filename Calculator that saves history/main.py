History_File='History.txt'

# Show history

def show_history():
    file=open(History_File,'r')
    lines=file.readlines()
    if len(lines)==0:
        print('No history found!')
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()
    
def clear_history():
    file=open(History_File,'w')
    file.close()
    print("History Cleared.")

def save_to_history(equation,result):
    file=open(History_File,'a')
    file.write(equation +'='+ str(result) +'\n')
    file.close()

def calculate(user_input):
    parts=user_input.split()
    if len(parts)!=3:
        print('Invalid input. Use format: number operator number (8 + 7)')
        return
    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])
    if op=='+':
        result=num1+num2
    elif op=='-':
        result=num1-num2
    elif op=='*':
        result=num1*num2
    elif op=='/':
        if num2==0:
            print("Error! Divide by zero")
            return
        result=num1/num2
    else:
        print('Invali operator.use operator (+,-,*,/)')
        return
    if int(result)==result:
        result=int(result)
    print('Result: ',result)
    save_to_history(user_input,result)


def main():
    print("----Welcome to Calculator window type(history/clear/exit)")
    while True:
        user_input=input('Enter calculation using (+-*/) or type command (history/clear/exit): ')
        if user_input.strip().lower()=='exit':
            print('GoodBye!')
            break
        elif user_input.strip().lower()=='history':
            show_history()
        elif user_input.strip().lower()=='clear':
            clear_history()
        else:
            calculate(user_input)

main()