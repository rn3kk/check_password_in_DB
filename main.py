import hashlib
import signal
import time

p=[
    'password1',
    'password1'
]


terminate = False

def handler(signum, frame):
    global terminate
    terminate = True

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler)
    pw = []
    for i in p:
        s = hashlib.sha1(i.encode()).hexdigest().upper() + '\n'
        sU = hashlib.sha1(i.upper().encode()).hexdigest().upper() + '\n'
        pw.append(s)
        pw.append(sU)
        print('s', i, s)
        print('sU', i.upper(), sU)

    f = open('d://projects//база паролей//pwned-passwords-1.0.txt', 'r')

    count = 0
    line_num_start = 0
    line_num = 0
    for i in f:
        if terminate:
            break
        if i in pw:
            count += 1
            print('Find in line', i)

        line_num += 1

    print('Count', count, 'stop line num', line_num)


