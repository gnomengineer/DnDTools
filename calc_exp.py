import sys

def main(exp=1000):
    for i in range(3,7):
        print_exp(exp,i)

def print_exp(exp,n):
    print('--------------------------------------')
    print('experience for ' + repr(n) + ' Players')
    print()
    exp_n = exp / n
    print('xp from monsters:',exp_n)
    if(n==3):
        exp_perc = 0
    else:
        exp_perc = exp_n * (2**(n - 4)) * 0.125
    print('xp from group bonus:', exp_perc)
    print('total xp:', exp_n+exp_perc)
    print()
    print()

if __name__ == "__main__":
    n=1000
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    main(n)
