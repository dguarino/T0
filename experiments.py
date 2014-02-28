#!/usr/local/bin/ipython -i 
from mozaik.experiments import *
from mozaik.experiments.vision import *
from mozaik.sheets.population_selector import RCRandomPercentage
from parameters import ParameterSet

def create_experiments(model):
    return [
    
            # LUMINANCE SENSITIVITY
            # as in SakmannCreutzfeldt1969, although was for retina
            # as in PapaioannouWhite1972, EvtikhinPolianskiiAlymkulovSokolov2008
            # MeasureFlatLuminanceSensitivity(
            #     model, 
            #     luminances=[0.01, 0.1, 1.0, 10.0, 20.0, 100.0],
            #     step_duration=147*7,
            #     num_trials=14
            # ),

            # CONTRAST SENSITIVITY
            # as in DerringtonLennie1984, HeggelundKarlsenFlugsrudNordtug1989, SaulHumphrey1990, BoninManteCarandini2005
            # MeasureContrastSensitivity(
            #     model, 
            #     size=2.0,
            #     orientation=numpy.pi/2, 
            #     spatial_frequency=0.2, 
            #     temporal_frequency=3.0,
            #     grating_duration=147*7,
            #     contrasts=[0,10,40,100],
            #     num_trials=14
            # ),

            # SPATIAL AND TEMPORAL FREQUENCY TUNING (with different contrasts)
            # Spatial: as in SolomonWhiteMartin2002, SceniakChatterjeeCallaway2006
            # Temporal: as in SaulHumphrey1990, AlittoUsrey2004
            # MeasureFrequencySensitivity(
            #     model, 
            #     orientation=numpy.pi/2, 
            #     contrasts=[10,50,100], 
            #     spatial_frequencies=[0.01, 0.1, 0.15, 0.2, 0.25, 0.5, 0.8, 1.0, 1.6, 3.2], #[0.15], #
            #     temporal_frequencies=[8.0], #[0.5, 1.0, 2.0, 10.0, 20.0, 30.0], #[8.0], #
            #     grating_duration=147*7,
            #     frame_duration=7,
            #     num_trials=14
            # ),
    
            # SIZE TUNING
            # as in ClelandLeeVidyasagar1983, BoninManteCarandini2005
            MeasureSizeTuning(
                model, 
                num_sizes=26, 
                max_size=8.0, 
                orientation=numpy.pi/2, 
                spatial_frequency=0.1, 
                temporal_frequency=6.0,
                grating_duration=147*7,
                contrasts=[40, 100], # to look for contrast-dependent RF expansion
                num_trials=14,
                log_spacing=True
            ),
            
            # LIFELONG SPARSENESS
            # as in RathbunWarlandUsrey2010, AndolinaJonesWangSillito2007
            # stimulation as Size Tuning
            
            # ORIENTATION TUNING (GRATINGS)
            # as in DanielsNormanPettigrew1977, VidyasagarUrbas1982
            # MeasureOrientationTuningFullfield(
            #     model,
            #     num_orientations=6,
            #     spatial_frequency=0.1,
            #     temporal_frequency=2,
            #     grating_duration=147*7,
            #     contrasts=[40, 100],
            #     num_trials=14
            # ),

            # CONTOUR COMPLETION
            # as in SillitoJonesGersteinWest1994
                     
           ]

