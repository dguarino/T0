#!/usr/local/bin/ipython -i 
from mozaik.experiments import *
from mozaik.experiments.vision import *
from mozaik.sheets.population_selector import RCRandomPercentage
from parameters import ParameterSet

def create_experiments(model):
    return [
            
            # CONTRAST CONTROL
            #MeasureContrastSensitivity(
            #    model, 
            #    size=14.0, 
            #    orientation=numpy.pi/2, 
            #    spatial_frequency=0.8, 
            #    temporal_frequency=2,
            #    grating_duration=147*7,
            #    contrasts=[0,10,50,80,100],#[0,10,20,30,40,50,60,70,80,90,100],
            #    num_trials=4
            #),
    
            # EXTRA-CLASSICAL SIZE TUNING (GRATING DISCS)
            MeasureSizeTuning(
                model, 
                num_sizes=14, 
                max_size=16.0, 
                orientation=numpy.pi/2, 
                spatial_frequency=0.8, 
                temporal_frequency=2,
                grating_duration=147*7,
                contrasts=[100],
                num_trials=4,
                log_spacing=True
            ),

            # MASKING
            
            # LIFELONG SPARSENESS
            
            # ORIENTATION TUNING (GRATINGS)
            #MeasureOrientationTuningFullfield(
            #    model,
            #    num_orientations=6,
            #    spatial_frequency=0.8,
            #    temporal_frequency=2,
            #    grating_duration=147*7,
            
            #    contrasts=[100],
            #    num_trials=4
            #),

            # FILLING-IN
                     
           ]

