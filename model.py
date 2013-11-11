import sys
import numpy
from parameters import ParameterSet
from mozaik.models import Model
from mozaik import load_component
from mozaik.space import VisualRegion

class T0_Model(Model):
    
    required_parameters = ParameterSet({
        'retina_lgn' : ParameterSet ,
        'visual_field' : ParameterSet 
    })
    
    def __init__(self, sim, num_threads, parameters):
        Model.__init__(self, sim, num_threads, parameters)        
        # Load components
        RetinaLGN = load_component( self.parameters.retina_lgn.component )
        # Build and instrument the network
        self.visual_field = VisualRegion(
            location_x = self.parameters.visual_field.centre[0],
            location_y = self.parameters.visual_field.centre[1],
            size_x = self.parameters.visual_field.size[0],
            size_y = self.parameters.visual_field.size[1]
        )
        self.input_layer = RetinaLGN( self, self.parameters.retina_lgn.params )
