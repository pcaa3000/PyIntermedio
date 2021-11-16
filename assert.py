def get_divisors(num):
    divisors=[]    
    for i in range(1,num+1):
        if num %i==0:
            divisors.append(i)
    return divisors



def run():
    try:
        num=input("Enter a number: ")        
        assert num.replace("-", "").isnumeric(), "You must to enter a number..."
        num=int(num)
        assert num> 0,"You must to enter a positive number..."
        print(get_divisors(num))
        print("--------End Program--------")
    except AssertionError as e:
        print(e)


if __name__ == '__main__':
    run()