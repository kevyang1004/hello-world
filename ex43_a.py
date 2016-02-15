from sys import exit


class Scene(object):
    def enter(self):
        print "Not yet classified. Add enter()."
        exit(0)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        present_scene = self.scene_map.opening_scene()s
        final_scene = self.scene_map.next_scene('finish')

        while present_scene != final_scene:
            next_scene_name = present_scene.enter()
            present_scene = self.scene_map.next_scene(next_scene_name)

        present_scene.enter()


class Death(Scene):

    def enter(self):
        print "You have decided a foolish choice."
        exit(0)
