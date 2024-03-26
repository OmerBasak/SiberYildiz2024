import os
from colorama import init, Fore
from cryptography.fernet import Fernet
from time import sleep
from heapq import heappush, heappop

# Tahta boyutu N x N
N = 8
T = N * N

# X and Y koordinatlari
MX = [1, 2, 2, 1, -1, -2, -2, -1]
MY = [-2, -1, 1, 2, 2, 1, -1, -2] 





def temizle():
    '''
    Console verilerinin temizlenmesi
    '''
    if os.name == 'nt':
        _ = os.system('cls')
    elif os.name == 'posix':
        _ = os.system('clear')


def input_control(pozisyon):
    '''
    Girilen verilerinin dogrulugu kontrol ediliyor
    '''
    try:
        if pozisyon.find('.'):
            pozisyon = pozisyon.replace('.',',')
        elif pozisyon.find(';'):
            pozisyon = pozisyon.replace(';',',')
        else:
            return False
        
        baslagic_pozisyon = pozisyon.split(',')
        pozisyon_map = map(int, baslagic_pozisyon)
        row, col = list(pozisyon_map)

        if not 0 <= row < 8 or not 0 <= col < 8:
            raise ValueError()
    except:
        return False
    return True


def satranc_tahtasi_olusturma():
    '''
    Bos satranc tahtasi cizdiriliyor
    '''
    j = 0

    print()
    for i in range(9):
        if i != 0:
            print(
                str(j) + '   ' +
                '|   |   |   |   |   |   |   |   |')
            print('    ' + '---------------------------------')
            j += 1
        else:
            print('      ' + '0   1   2   3   4   5   6   7\n')
            print('    ' + '---------------------------------')
    print('\n')
    
    
    
def validate_result(word,encryption_key):
    f = Fernet(encryption_key)
    value = f.decrypt(word)
    return value.decode()

def is_valid_word(number):
    value = "YkM5STJWNWFXRGhSRzQ1b0RXQnVPdz09"

    f = Fernet(number)
    value = f.encrypt(value.encode())







def satranc_tahtasi(alan):
    """
    Boyutlari verilen satranc tahtasi.
    """
    print()
    for i in range(N):
        for j in range(N):
            if alan[i][j] == 1:
                print(Fore.YELLOW + '{:4d}'.format(alan[i][j]), end=' ')
            elif alan[i][j] == T:
                print(Fore.GREEN + '{:4d}'.format(alan[i][j]), end=' ')
            else:
                print('{:4d}'.format(alan[i][j]), end=' ')
        print()


def doluluk_orani(alan):
    """
    Satranc tahtasinin doluluk oranini verir
    """
    taranmis_kareler = 0
    toplam_kareler = T

    for row in range(N):
        taranmis_kareler += (N - alan[row].count(0))

    progress = (taranmis_kareler / toplam_kareler) * 100

    return progress


def is_safe(x, y, alan):
    """
    Satranc tasinin hareket edecegi karenin kontrol eder.
    """
    if 0 <= x < N and 0 <= y < N and alan[x][y] == 0:
        return True
    return False


def get_degree(x, y, alan):
    """
    Bos karelerin sayisini verir
    """
    c = 0
    for i in range(N):
        if is_safe(x + MX[i], y + MY[i], alan):
            c += 1
    return c


def algorithm(x, y, alan):
    """
    Warnsdorff's algorithm:
        1. Set P to be a random initial position on the board.
        2. Mark the board at P with the move number "1".
        3. Do following for each move number from 2 to the number of squares on the board.
        4. Return the marked board - each square will be marked with the move number on which it is visited.
    """
    # Set starting position of the knight
    p = 1
    alan[x][y] = p
    
    for _ in range(T):
        pq = []

        for i in range(8):
            nx = x + MX[i]
            ny = y - MY[i]
            
            if is_safe(nx, ny, alan):
                c = get_degree(nx, ny, alan)
                heappush(pq, (c, i))
        
        if len(pq) > 0:
            (_, m) = heappop(pq)
            x -= MX[m]
            y += MY[m]
            p += 1
            alan[x][y] = p

            # Print board and progress bar 
            print("Tamamlanan kisim: {}%".format(doluluk_orani(alan)))
            satranc_tahtasi(alan)

            if not p == T:
                sleep(0.5)
                temizle()
            else:
                if not doluluk_orani(alan)==100:
                    input("\nUpps !!! Ters giden biseyler var...")
                else:
                    input("\nTebrikler!! Gizli kelimeye ulastiniz...")
                    print(validate_result(valid_word,number))


if __name__ == "__main__":

    while True:
        temizle()
        number = Fernet.generate_key()
        valid_word=is_valid_word(number)

        satranc_tahtasi_olusturma()

        pozisyon = input("Satranc tasinin baslama pozisyonu (x,y): ")

        if input_control(pozisyon):
            break
        else:
            print('Geccersiz veri. Tekrar deneyiniz')
            sleep(1)

    temizle()
    
    if pozisyon.find('.'):
        pozisyon = pozisyon.replace('.',',')
    elif pozisyon.find(';'):
        pozisyon = pozisyon.replace(';',',')
    else:
        print('Invalid input')
    
    baslagic_pozisyon = pozisyon.split(',')
    pozisyon_map = map(int, baslagic_pozisyon)
    x, y = list(pozisyon_map)
    '''x, y = list(map(int, pozisyon.split(',')))'''
    b = [[0 for i in range(N)] for i in range(N)]
    
    init(autoreset=True) # Colorama
    algorithm(x, y, b)
    
