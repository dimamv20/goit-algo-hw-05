import timeit

with open('file1.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()
    

with open('file2.txt', 'r', encoding='utf-8') as file2:
    text2 = file2.read() 
    
    
# Існуючи пошуковий обьект в першому файлы 
real_word = 'пошук'
# Не існуючий пошуковий обьект в першому файлы 
fake_word = 'Рекурсія'


# Існуючи пошуковий обьект в другому файлы 
existent_word = 'експериментів'
# Не існуючий пошуковий обьект в другому файлы 
absent_word = 'ескапізм'




#--------------------------------------------Алгоритм Кнута-Морріса-Пратта---------------------------------------------------
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1 

#--------------------------------------------Алгоритм Боєра-Мура-----------------------------------------------------
def build_shift_table(pattern):
    table = {}
    length = len(pattern)

    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1

    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):

    shift_table = build_shift_table(pattern)
    i = 0  

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  

        if j < 0:
            return i  

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1

#--------------------------------------------Алгоритм Рабіна-Карпа--------------------------------------------------

def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):

    substring_length = len(substring)
    main_string_length = len(main_string)

    base = 256 
    modulus = 101  

    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    h_multiplier = pow(base, substring_length - 1) % modulus

    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1

if __name__ == '__main__':
    alg_knuta_existent_word_text1 = timeit.timeit(stmt='kmp_search(text1,real_word)',globals=globals(),number=1)
    alg_knute_absent_word_text1 = timeit.timeit(stmt='kmp_search(text1,fake_word)',globals=globals(),number=1)
    
    alg_buera_existent_text1=timeit.timeit(stmt='boyer_moore_search(text1,real_word)',globals=globals(),number=1)
    alg_buera_absent_text1 = timeit.timeit(stmt='boyer_moore_search(text1,fake_word)',globals=globals(),number=1)
    
    alg_rabin_karp_existent_text1=timeit.timeit(stmt='rabin_karp_search(text1,real_word)',globals=globals(),number=1)
    alg_rabin_karp_absent_text1=timeit.timeit(stmt='rabin_karp_search(text1,fake_word)',globals=globals(),number=1)
    print('-'*45 + 'Text1' + '-'*45)
    print(f'Пошук наявного слова: "{real_word}" в тексті 1 через Алгоритм Кнута-Морріса-Пратта: {alg_knuta_existent_word_text1}')
    print(f'Пошук відсутнього слова: "{fake_word}" в тексті 1 через Алгоритм Кнута-Морріса-Пратта: {alg_knute_absent_word_text1}')
    
    print(f'Пошук наявного слова: "{real_word}" в тексті 1 через Алгоритм Боєра-Мура: {alg_buera_existent_text1}')
    print(f'Пошук відсутнього слова: "{fake_word}" в тексті 1 через Алгоритм Боєра-Мура: {alg_buera_absent_text1}')
    
    print(f'Пошук наявного слова: "{real_word}" в тексті 1 через Алгоритм Рабіна-Карпа: {alg_rabin_karp_existent_text1}')
    print(f'Пошук відсутнього слова: "{fake_word}" в тексті 1 через Алгоритм Рабіна-Карпа: {alg_rabin_karp_absent_text1}')
    # Алгоритм Кнута-Морріса-Пратта
    # Алгоритм Боєра-Мура
    # Алгоритм Рабіна-Карпа
    
    
    # Для другого тексту
    print('-'*45 + 'Text2' + '-'*45)
    alg_knuta_existent_word_text2 = timeit.timeit(stmt='kmp_search(text2,existent_word)',globals=globals(),number=1)
    alg_knute_absent_word_text2 = timeit.timeit(stmt='kmp_search(text2,absent_word)',globals=globals(),number=1)
    alg_buera_existent_text2=timeit.timeit(stmt='boyer_moore_search(text2,existent_word)',globals=globals(),number=1)
    alg_buera_absent_text2 = timeit.timeit(stmt='boyer_moore_search(text2,absent_word)',globals=globals(),number=1)
    alg_rabin_karp_existent_text2=timeit.timeit(stmt='rabin_karp_search(text2,existent_word)',globals=globals(),number=1)
    alg_rabin_karp_absent_text2=timeit.timeit(stmt='rabin_karp_search(text2,absent_word)',globals=globals(),number=1)
    
    print(f'Пошук наявного слова: "{existent_word}" в тексті 2 через Алгоритм Кнута-Морріса-Пратта: {alg_knuta_existent_word_text2}')
    print(f'Пошук відсутнього слова: "{absent_word}" в тексті 2 через Алгоритм Кнута-Морріса-Пратта: {alg_knute_absent_word_text2}')
    
    print(f'Пошук наявного слова: "{existent_word}" в тексті 2 через Алгоритм Боєра-Мура: {alg_buera_existent_text2}')
    print(f'Пошук відсутнього слова: "{absent_word}" в тексті 2 через Алгоритм Боєра-Мура: {alg_buera_absent_text2}')
    
    print(f'Пошук наявного слова: "{existent_word}" в тексті 2  через Алгоритм Рабіна-Карпа: {alg_rabin_karp_existent_text2}')
    print(f'Пошук відсутнього слова: "{absent_word}" в тексті 2 через Алгоритм Рабіна-Карпа: {alg_rabin_karp_absent_text2}')
    print('-'*120)
    print('Висновок:\n')
    print(f'З аналізу швидкості алгоритма пошуку можна зробити висновок,\nщо алгоритм пошуку Рабіна-Карпа виконується найвидше з усіх інших алгоритмів ')
    print('\n'+ '-'*120)