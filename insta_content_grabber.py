#Vamsi Madhav Gajjela
from urllib.request import Request, urlopen, urlretrieve

def return_link(url, content_type):
    """
    Using a url and a content type the functionr returns the contents
    source link to be used as pleased
    """
    search_val = 'og:image'

    if content_type == 'video':
        search_val = 'og:video'
    
    for line in urlopen(url):
        line = str(line)
        if search_val in line:
            return clean_data(line)


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
            print("Seems like you didn't put in a proper type, try again!")
            
        url = input('Enter the link of the instagram post: ')
        name = input('What would you like to name the file? ')
        save_image(return_link(url, content), name + end)
        print('The image/video has been saved locally!')

        print('-'*80 + '\n')
    
            
