import os.path
import urllib.parse
import errno


class Model:

    file_path = ''

    def __init__(self):
        # Decleared a variable _links with an empty set.
        self.links = set()

    def fetch(self):

        '''Load all the extracted links from a file and add to Set()'''
        self.init_dir()
        with open(self.file_path, 'r') as f:
            for line in f:
                self.links.add(line.replace('\n', ''))
        return self.links

    def save(self):
        '''
        :type links: object'''

        with open(self.file_path, 'w') as f:
            for line in sorted(self.links):
                f.write(line + "\n")
        return True


    def has(self, link):
        '''Check a links is stored in a set of links'''
        if not link in self.links:
            return False
        else:
            return True

    def add(self, link):
        self.links.add(link)
        return self

    def remove(self, link):
        self.links.discard(link)
        return self


    def init_dir(self):
        dir_name = os.path.dirname(self.file_path)
        print(dir_name)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        if not os.path.isfile(self.file_path):
            with open(self.file_path, 'w') as f:
                f.write('')
