from BalabitBuilder import BalabitBuilder

class GettextBuilder(BalabitBuilder):
    def configure(self, configure_opts = None):
        return True

    def make(self, subcommand = None):
        return True

def get_builder():
    return GettextBuilder()
