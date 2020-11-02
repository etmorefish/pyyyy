class Man(object):
    def run(self):
        print('run Man run!')

    def stop(self):
        print('stop Man stop!')

    def pause(self):
        raise Exception('Not Implemented')


class Forrest(Man):
    def run(self):
        super(Forrest, self).run()
        print('run Forrest run!')


class Jenny(Man):
    def run(self):
        super(Jenny, self).run()
        print('run Jenny run!')

    def stop(self):
        super(Jenny, self).stop()
        print('stop Jenny stop!')


class LittleForrest(Forrest, Jenny):
    def run(self):
        super(LittleForrest, self).run()
        print('run LittleForrest run!')

    def stop(self):
        super(LittleForrest, self).stop()
        print('stop LittleForrest stop!')

    def pause(self):
        print('wait LittleForrest wait!')


class E(Forrest, Jenny):

    pass

if __name__ == '__main__':

    man = Man()
    forrest = Forrest()
    jenny = Jenny()
    littleForrest = LittleForrest()
    e = E()

    # man.run()
    # print('---')
    # forrest.run()
    # print('---')
    # jenny.run()
    # print('---')
    #
    # littleForrest.run()
    # print('---')
    #
    # e.run()
    # print('------------')
    # man.stop()
    # print('---')
    #
    # forrest.stop()
    # print('---')
    #
    # jenny.stop()
    # print('---')
    #
    # littleForrest.stop()
    # print('---')
    #
    # e.stop()
    # print('------------')
    # man.pause()
    forrest.pause()
    # jenny.pause()
    # littleForrest.pause()
    # e.pause()
