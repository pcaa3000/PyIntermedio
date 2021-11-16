def get_divisors(num):
    divisors=[]    
    for i in range(1,num+1):
        if num %i==0:
            divisors.append(i)
    return divisors



def run():
    try:
        num=int(input("Enter a number: "))
        if num<=0:
            raise Exception("You must to enter a positive number")
        print(get_divisors(num))
        print("--------End Program--------")
    except ValueError:
        print("You must to enter a number...")    
    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()