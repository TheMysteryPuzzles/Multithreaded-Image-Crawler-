from Models.Model import Model


class Image(Model):
    file_path = 'storage/queue/storagelinks.txt'

    def __init__(self):
        Model.__init__(self)
        self.fetch()
