class Vehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print('Gas tank is now full.')

    def drive(self):
        print(f'The {self.model} is now driving.')

    def update_fuel_level(self, new_level):
        if new_level <= self.gas_tank_size:
            self.fuel_level = new_level
        else:
            print('Exceeded capacity')

    def lorem_ipsum(self):
        text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tempus arcu quis est sodales, fermentum ' \
               'ultrices lectus finibus. Ut eget semper ligula. Ut faucibus metus in lectus tristique finibus. Cras ' \
               'venenatis lectus eu neque porttitor aliquet. Maecenas finibus mollis fermentum. Fusce lobortis massa ' \
               'nisl, id iaculis turpis tempor in. Donec arcu leo, scelerisque et vulputate id, aliquam gravida eros. ' \
               'Maecenas pretium nisi sed nisi scelerisque cursus. Pellentesque porta lectus non venenatis rutrum. ' \
               'Vestibulum pulvinar mi non dictum suscipit. In consectetur sagittis nunc et finibus. Pellentesque ' \
               'vitae ultricies massa, sit amet tristique leo. Interdum et malesuada fames ac ante ipsum primis in ' \
               'faucibus. Integer mollis odio a porttitor auctor. Phasellus nibh elit, commodo a ornare sed, ' \
               'cursus ac enim. Donec ullamcorper, massa et mattis vulputate, turpis dui eleifend dolor, ac maximus ' \
               'sem nulla eget ex. Cras dictum rutrum dapibus. Aliquam pharetra nisl eu facilisis vulputate. Donec ' \
               'feugiat velit magna. Duis et enim a neque sodales malesuada nec id elit. Curabitur a augue et felis ' \
               'auctor semper. Nunc ut purus vitae nisi eleifend interdum et ac ligula. Etiam vitae lectus ut massa ' \
               'commodo aliquam in ut ante. Phasellus quam arcu, cursus ac ullamcorper quis, lacinia sed tortor. Duis ' \
               'et risus commodo, congue tortor vel, rutrum metus. Duis et augue vitae urna finibus semper. ' \
               'Pellentesque a dui magna. Vivamus eleifend urna dui, non dictum arcu accumsan vel. Fusce vitae augue ' \
               'turpis. Aenean volutpat vestibulum arcu, vel scelerisque diam malesuada in. Pellentesque varius elit ' \
               'quis dapibus mattis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos ' \
               'himenaeos. Vestibulum dapibus mi nec lacinia rutrum. Mauris pellentesque enim non viverra feugiat. In ' \
               'a urna posuere, aliquam ipsum vitae, finibus dolor. Suspendisse fermentum vitae turpis ut semper. ' \
               'Vivamus erat dui, convallis sed lorem eget, rhoncus lacinia leo. In congue lectus risus, non vehicula ' \
               'odio posuere eget. Fusce eleifend, urna quis aliquet tincidunt, ex dui pellentesque ante, ' \
               'dictum gravida tortor quam at felis. Ut aliquam nisl vel nisl tempor, quis efficitur neque imperdiet. ' \
               'Nam a molestie turpis, in lobortis elit. Mauris consequat, mauris mollis finibus sagittis, ' \
               'nunc arcu fermentum dui, ac molestie arcu sem a lacus. Ut felis felis, posuere in dui in, ' \
               'pharetra ultricies lorem. Sed laoreet egestas commodo. Nulla vitae dolor dictum, accumsan dolor sit ' \
               'amet, scelerisque metus. Cras nec augue in odio dignissim ultrices eu sit amet elit. Integer at nisi ' \
               'bibendum, maximus nunc eu, cursus odio. Quisque est libero, imperdiet finibus suscipit quis, ' \
               'imperdiet in erat. Pellentesque maximus mi vel rhoncus ultrices. Nunc tellus augue, bibendum vitae ' \
               'egestas nec, ultricies ut est. ' \
               'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tempus arcu quis est sodales, fermentum ' \
               'ultrices lectus finibus. Ut eget semper ligula. Ut faucibus metus in lectus tristique finibus. Cras ' \
               'venenatis lectus eu neque porttitor aliquet. Maecenas finibus mollis fermentum. Fusce lobortis massa ' \
               'nisl, id iaculis turpis tempor in. Donec arcu leo, scelerisque et vulputate id, aliquam gravida eros. ' \
               'Maecenas pretium nisi sed nisi scelerisque cursus. Pellentesque porta lectus non venenatis rutrum. ' \
               'Vestibulum pulvinar mi non dictum suscipit. In consectetur sagittis nunc et finibus. Pellentesque ' \
               'vitae ultricies massa, sit amet tristique leo. Interdum et malesuada fames ac ante ipsum primis in ' \
               'faucibus. Integer mollis odio a porttitor auctor. Phasellus nibh elit, commodo a ornare sed, ' \
               'cursus ac enim. Donec ullamcorper, massa et mattis vulputate, turpis dui eleifend dolor, ac maximus ' \
               'sem nulla eget ex. Cras dictum rutrum dapibus. Aliquam pharetra nisl eu facilisis vulputate. Donec ' \
               'feugiat velit magna. Duis et enim a neque sodales malesuada nec id elit. Curabitur a augue et felis ' \
               'auctor semper. Nunc ut purus vitae nisi eleifend interdum et ac ligula. Etiam vitae lectus ut massa ' \
               'commodo aliquam in ut ante. Phasellus quam arcu, cursus ac ullamcorper quis, lacinia sed tortor. Duis ' \
               'et risus commodo, congue tortor vel, rutrum metus. Duis et augue vitae urna finibus semper. ' \
               'Pellentesque a dui magna. Vivamus eleifend urna dui, non dictum arcu accumsan vel. Fusce vitae augue ' \
               'turpis. Aenean volutpat vestibulum arcu, vel scelerisque diam malesuada in. Pellentesque varius elit ' \
               'quis dapibus mattis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos ' \
               'himenaeos. Vestibulum dapibus mi nec lacinia rutrum. Mauris pellentesque enim non viverra feugiat. In ' \
               'a urna posuere, aliquam ipsum vitae, finibus dolor. Suspendisse fermentum vitae turpis ut semper. ' \
               'Vivamus erat dui, convallis sed lorem eget, rhoncus lacinia leo. In congue lectus risus, non vehicula ' \
               'odio posuere eget. Fusce eleifend, urna quis aliquet tincidunt, ex dui pellentesque ante, ' \
               'dictum gravida tortor quam at felis. Ut aliquam nisl vel nisl tempor, quis efficitur neque imperdiet. ' \
               'Nam a molestie turpis, in lobortis elit. Mauris consequat, mauris mollis finibus sagittis, ' \
               'nunc arcu fermentum dui, ac molestie arcu sem a lacus. Ut felis felis, posuere in dui in, ' \
               'pharetra ultricies lorem. Sed laoreet egestas commodo. Nulla vitae dolor dictum, accumsan dolor sit ' \
               'amet, scelerisque metus. Cras nec augue in odio dignissim ultrices eu sit amet elit. Integer at nisi ' \
               'bibendum, maximus nunc eu, cursus odio. Quisque est libero, imperdiet finibus suscipit quis, ' \
               'imperdiet in erat. Pellentesque maximus mi vel rhoncus ultrices. Nunc tellus augue, bibendum vitae ' \
               'egestas nec, ultricies ut est. ' \
               'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tempus arcu quis est sodales, fermentum ' \
               'ultrices lectus finibus. Ut eget semper ligula. Ut faucibus metus in lectus tristique finibus. Cras ' \
               'venenatis lectus eu neque porttitor aliquet. Maecenas finibus mollis fermentum. Fusce lobortis massa ' \
               'nisl, id iaculis turpis tempor in. Donec arcu leo, scelerisque et vulputate id, aliquam gravida eros. ' \
               'Maecenas pretium nisi sed nisi scelerisque cursus. Pellentesque porta lectus non venenatis rutrum. ' \
               'Vestibulum pulvinar mi non dictum suscipit. In consectetur sagittis nunc et finibus. Pellentesque ' \
               'vitae ultricies massa, sit amet tristique leo. Interdum et malesuada fames ac ante ipsum primis in ' \
               'faucibus. Integer mollis odio a porttitor auctor. Phasellus nibh elit, commodo a ornare sed, ' \
               'cursus ac enim. Donec ullamcorper, massa et mattis vulputate, turpis dui eleifend dolor, ac maximus ' \
               'sem nulla eget ex. Cras dictum rutrum dapibus. Aliquam pharetra nisl eu facilisis vulputate. Donec ' \
               'feugiat velit magna. Duis et enim a neque sodales malesuada nec id elit. Curabitur a augue et felis ' \
               'auctor semper. Nunc ut purus vitae nisi eleifend interdum et ac ligula. Etiam vitae lectus ut massa ' \
               'commodo aliquam in ut ante. Phasellus quam arcu, cursus ac ullamcorper quis, lacinia sed tortor. Duis ' \
               'et risus commodo, congue tortor vel, rutrum metus. Duis et augue vitae urna finibus semper. ' \
               'Pellentesque a dui magna. Vivamus eleifend urna dui, non dictum arcu accumsan vel. Fusce vitae augue ' \
               'turpis. Aenean volutpat vestibulum arcu, vel scelerisque diam malesuada in. Pellentesque varius elit ' \
               'quis dapibus mattis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos ' \
               'himenaeos. Vestibulum dapibus mi nec lacinia rutrum. Mauris pellentesque enim non viverra feugiat. In ' \
               'a urna posuere, aliquam ipsum vitae, finibus dolor. Suspendisse fermentum vitae turpis ut semper. ' \
               'Vivamus erat dui, convallis sed lorem eget, rhoncus lacinia leo. In congue lectus risus, non vehicula ' \
               'odio posuere eget. Fusce eleifend, urna quis aliquet tincidunt, ex dui pellentesque ante, ' \
               'dictum gravida tortor quam at felis. Ut aliquam nisl vel nisl tempor, quis efficitur neque imperdiet. ' \
               'Nam a molestie turpis, in lobortis elit. Mauris consequat, mauris mollis finibus sagittis, ' \
               'nunc arcu fermentum dui, ac molestie arcu sem a lacus. Ut felis felis, posuere in dui in, ' \
               'pharetra ultricies lorem. Sed laoreet egestas commodo. Nulla vitae dolor dictum, accumsan dolor sit ' \
               'amet, scelerisque metus. Cras nec augue in odio dignissim ultrices eu sit amet elit. Integer at nisi ' \
               'bibendum, maximus nunc eu, cursus odio. Quisque est libero, imperdiet finibus suscipit quis, ' \
               'imperdiet in erat. Pellentesque maximus mi vel rhoncus ultrices. Nunc tellus augue, bibendum vitae ' \
               'egestas nec, ultricies ut est. '
        print(text)
