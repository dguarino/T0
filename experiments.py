#!/usr/local/bin/ipython -i 
from mozaik.experiments import *
from mozaik.experiments.vision import *
from mozaik.sheets.population_selector import RCRandomPercentage
from parameters import ParameterSet

def create_experiments(model):
    return [
    
            # LUMINANCE SENSITIVITY
            #MeasureLuminanceSensitivity(
            #    model, 
            #    luminances=[1.0, 10.0, 20.0, 40.0, 60.0, 80.0, 100.0, 200.0, 300.0, 400.0],
            #    step_duration=147*7,
            #    num_trials=4
            #),

            # SPATIAL FREQUENCY TUNING
            #MeasureFrequencySensitivity(
            #    model, 
            #    orientation=numpy.pi/2, 
            #    contrast=100, 
            #    temporal_frequency=2,
            #    grating_duration=147*7,
            #    spatial_frequencies=[0.001, 0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.3, 1.6, 2.1, 3.2, 6.4], 
            #    num_trials=4
            #),
            
            # CONTRAST CONTROL
            #MeasureContrastSensitivity(
            #    model, 
            #    size=2.0,
            #    orientation=numpy.pi/2, 
            #    spatial_frequency=0.8, 
            #    temporal_frequency=2,
            #    grating_duration=147*7,
            #    contrasts=[0,10,20,30,40,50,60,70,80,90,100],
            #    num_trials=4
            #),
    
            # SIZE TUNING
            MeasureSizeTuning(
                model, 
                num_sizes=14, 
                max_size=8.0, 
                orientation=numpy.pi/2, 
                spatial_frequency=0.8, #0.25 
                temporal_frequency=2,
                grating_duration=147*7,
                contrasts=[100], # [40, 100] to look for contrast-dependent RF expansion
                num_trials=4,
                log_spacing=True
            ),
            
            # LIFELONG SPARSENESS
            # as Size Tuning
            
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

