#Vamsi Madhav Gajjela
def return_link(url, content_type):
    """
    Using a url and a content type the function returns the contents
    source link to be used as pleased
    """
    search_val = 'og:image'
    final = None

    if content_type == 'video':
        search_val = 'og:video'
    try:
        for line in urlopen(url):
            line = str(line)
            if search_val in line:
                final = clean_data(line)

            elif 'is_private' in line:
                clean1 = line.find('"is_private"') + len('"is_private"') - 1
                clean2 = line[clean1:]
                priv_check = clean2[2:clean2.find(',')]
                return (True if priv_check == 'true' else False, final)
    except:
        return True, ''


def clean_data(line):
    """
    Cleans given line from it's byte form to a usuable link
    """
    return line[line.find('content') + 8:].split('"')[1]
    
    
def save_image(url, name):
    """
    Saves the image locally onto the computer of the user
    """
    urlretrieve(url, name)
    
if __name__ == '__main__':

    print('Type 1 for Images/2 for Videos/3 to quit\n')
    while True:
        content_type = input('What type of content would you like to get: ')
        if content_type == '1':
            content = '1'
            end = ' .jpg'

        elif content_type == '2':
            content = 'video'
            end = '.mp4'
            
        elif content_type == '3':
            print('Thank you for using the program, bye!')
            quit()

        else:
            print("Seems like you didn't put in a proper type, try again!\n")
            continue 
            
        url = input('Enter the link of the instagram post: ')
        contents = return_link(url, content)

        if contents[0]:
            print('Sorry, This seems to be a private account or an invalid link try another one!\n' + '-'*80 + '\n')
            continue
        
        name = input('What would you like to name the file? ')
        
        save_image(contents[1], name + end)
        print('The image/video has been saved locally!')

        print('-'*80 + '\n')
    
    
            
