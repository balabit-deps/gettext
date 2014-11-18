from BalabitBuilder import BalabitBuilder

class GettextBuilder(BalabitBuilder):
    def configure(self):
        pass

def get_builder():
    return GettextBuilder()
