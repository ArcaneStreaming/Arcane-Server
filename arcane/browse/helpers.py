# main_genres =  'Avante-Garde Blues Children\'s Classical Comedy Country Easy_Listening Electronic Folk Holiday International Jazz Latin New_Age Pop Rock R&B Rap Reggae Religious Stage&Screen Vocal'.split(' ')
from PIL import Image
from io import BytesIO
import glob
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Genre_Helpers(object):

    def __init__(self, path):
        self.images = self.import_genre_images(path)
        self.genre_tree = self.build_tree()
    # def __str__(self):
    #     str_to_print = ''
    #     for keys,values in self.genre_tree.items():
    #         str_to_print += str(keys)
    #         str_to_print += str(values)
    #     return str_to_print

    def capitalize_str(self, string):
        return string[:1].upper() + string[1:]

    def os_based_split(self, string):
        if sys.platform == 'linux':
            return(string.split('/')[-1])
        else:
            return(string.split('\\')[1])

    def import_genre_images(self, path):
        image_obj = {}

        # for filename in glob.glob('../../static/images/genres/*.jpg'):
        for filename in glob.glob(path+'/*.jpg' ):
         #assuming gif
            print('path',path)
            im=Image.open(filename)
            # print(type(im))
            # print(sys.platform)
            split_filename = self.os_based_split(filename)
            str = self.capitalize_str(split_filename)

            if '_' in str:
                str = str.replace('_', ' ')
                str2 = str.split(' ')
                str2 = self.capitalize_str(str2[0]), self.capitalize_str(str2[1])
                str = ' '.join(str2)
            path = os.path.join('static' , 'images' ,'genres', split_filename)
            image_obj[str.strip('.jpg')] = split_filename

        return image_obj

    def get_image(self, images, genre):
        # print(genre)
        if genre in images.keys():
            try:
                o = images[genre]
            except KeyError:
                o = 'hip_hop.jpg'
            return o
        else:
            return 'hip_hop.jpg'

    def get_sub_genres(self,genre):
        if genre is 'Alternative':
            return [ 'Art Punk', 'Alternative Rock', 'College Rock',
                     'Crossover Thrash', 'Crust Punk', 'Experimental Rock',
                     'Folk Punk', 'Goth', 'Gothic Rock', 'Grunge', 'Hardcore Punk',
                     'Hard Rock', 'Indie Rock', 'Lo-fi', 'New Wave',
                     'Progressive Rock', 'Punk', 'Shoegaze', 'Steampunk']
        if genre is 'Anime':
            return []
        if genre is 'Blues':
            return [ 'Acoustic Blues', 'Chicago Blues', 'Classic Blues',
                     'Contemporary Blues', 'Country Blues', 'Delta Blues',
                     'Electric Blues','Ragtime Blues']
        if genre is 'Classical':
            return []
        if genre is 'Comedy':
            return []
        if genre is 'Country':
            return []
        if genre is 'Dance':
            return [ 'Club', 'Club Dance', 'Breakcore', 'Breakbeat', 'Breakstep',
                     'Brostep', 'Chillstep', 'Deep House', 'Dubstep', 'EDM',
                     'Dance Electronic', 'Electro House', 'Electroswing',
                     'Exercise', 'Future Garage', 'Garage', 'Glitch Hop',
                     'Glitch Pop', 'Grime', 'Hardcore', 'Hard Dance', 'Hi-NRG',
                     'Eurodance', 'Horrorcore', 'House', 'Jackin House', 'Jungle',
                     'Drum n bass', 'Liquid Dub', 'Regstep', 'Speedcore', 'Techno',
                     'Trance', 'Trap' ]
        if genre is 'Easy Listening':
            return []
        if genre is 'Electronic':
            return [ '2-Step ', 'Ambient', 'Bassline', 'Chillwave', 'Chiptune',
                     'Crunk', 'Downtempo', 'Drum & Bass', 'Electro',
                     'Electro-swing', 'Electronica', 'Electronic Rock',
                     'Hardstyle', 'IDM/Experimental', 'Industrial', 'Trip Hop']
        if genre is 'Folk':
            return []
        if genre is 'Hip Hop Rap':
            return [ 'Hip Hop', 'Rap',
                      ]
        if genre is 'Inspirational':
            return []
        if genre is 'Instrumental':
            return []
        if genre is 'International':
            return []
        if genre is 'Jazz':
            return []
        if genre is 'Latin':
            return []
        if genre is 'New Age':
            return []
        if genre is 'Metal':
            return []
        if genre is 'Pop':
            return []
        if genre is 'Rock':
            return [ 'Acid Rock', 'Adult-Oriented Rock', 'Afro Punk',
                     'Adult Alternative', 'Alternative Rock', 'American Trad Rock',
                     'Anatolian Rock', 'Arena Rock', 'Art Rock', 'Blues-Rock',
                     'British Invasion', 'Cock Rock', 'Death Metal', 'Black Metal',
                     'Doom Metal', 'Glam Rock', 'Gothic Metal', 'Grind Core',
                     'Hair Metal', 'Hard Rock', 'Math Metal', 'Math Rock' ]
        if genre is 'R&B/Soul':
            return []
        if genre is 'Reggae':
            return []
        if genre is 'Soundtrack':
            return []
        if genre is 'Vocal':
            return []
        if genre is 'World':
            return []
        return ['sub1', 'sub2']

    def build_tree(self):
        roots = [ 'Alternative', 'Anime', 'Blues', 'Classical',
                  'Comedy', 'Country', 'Dance', 'Easy Listening', 'Electronic',
                  'Folk', 'Hip Hop Rap', 'Holiday', 'Inspirational',
                  'Instrumental', 'International', 'Jazz', 'Latin','Metal',
                  'New Age', 'Pop', 'Rock', 'Reggae', 'Soundtrack',
                  'Vocal', 'World' ]
        # print(roots)
        tree = {}
        for i,genre in enumerate(roots):
            sub_genres = [genre] + self.get_sub_genres(genre)
            img = self.get_image(self.images,genre)
            # print(subs)
            leaf = {'sub_genres': sub_genres, 'image': img}
            # print (leaf)
            tree[genre] = leaf
            # print(leaf, i)
            # tree[genre]['image'] = images[genre]
        return tree
# g = Genre_Helpers('../../static/images/genres')
# t = g.build_tree()
# print(g.genre_tree)
