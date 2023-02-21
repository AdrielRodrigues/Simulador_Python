class Path:
    def __init__(self, links, channel_list, modulation):
        self.links = links
        self.channel_list = channel_list
        self.modulation = modulation

    def get_num_links(self):
        return len(self.links)

    def get_modulation(self):
        return self.modulation

    def get_slot_list(self):
        return self.channel_list

    def get_links(self):
        return self.links

    def get_link(self, link):
        return self.links[link]
