class Nuke:
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power

    def detonate(self):
        print('BOOOOM!')

nuclear_arsenal = []
nuclear_arsenal.append(Nuke('LitleBoy', 'atomic', '100 KiloTons'))
nuclear_arsenal.append(Nuke('Tsar', 'termonuclear', '100 MegaTons'))
nuclear_arsenal[0].detonate()
nuclear_arsenal[1].detonate()
