import subprocess

"""Кодировка для русского языка"""
def extract_wifi_password_ru():
    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('cp866').split('\n')
    # print(profiles_data)

    # for item in profiles_data:
    #     print(item)

    profiles = [i.split(':')[1].strip() for i in profiles_data if 'Все профили пользователей' in i]
    # print(profiles)

    for profile in profiles:
        profile_info = subprocess.check_output(f'netsh wlan show profile name="{profile}" key=clear').decode('cp866').split('\n')
        # print(profile_info)

        try:
            password =[i.split(':')[1].strip() for i in profile_info if 'Содержимое ключа' in i]
        except IndexError:
            password = None

        # print(f'Profile: {profile}\nPassword: {password}\n{"#"*20}')

        with open(file='wifi_passwords_ru.txt', mode='a', encoding='utf-8') as file:
            file.write(f'Profile: {profile}\nPassword: {password}\n{"#"*20}\n')


"""Кодировка для английского языка"""
def extract_wifi_password_eng():
    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('utf-8').split('\n')
    # print(profiles_data)

    # for item in profiles_data:
    #     print(item)

    profiles = [i.split(':')[1].strip() for i in profiles_data if 'Все профили пользователей' in i]
    # print(profiles)

    for profile in profiles:
        profile_info = subprocess.check_output(f'netsh wlan show profile name="{profile}" key=clear').decode('utf-8').split('\n')
        # print(profile_info)

        try:
            password =[i.split(':')[1].strip() for i in profile_info if 'Содержимое ключа' in i]
        except IndexError:
            password = None

        # print(f'Profile: {profile}\nPassword: {password}\n{"#"*20}')

        with open(file='wifi_passwords_eng.txt', mode='a',encoding='utf-8') as file:
            file.write(f'Profile: {profile}\nPassword: {password}\n{"#"*20}\n')

def main():
    extract_wifi_password_ru()

if __name__ == '__main__':
    main()