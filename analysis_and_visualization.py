import numpy
import mozaik
import pylab
from mozaik.visualization.plotting import *
from mozaik.analysis.technical import NeuronAnnotationsToPerNeuronValues
from mozaik.analysis.analysis import *
from mozaik.analysis.vision import *
from mozaik.storage.queries import *
from mozaik.storage.datastore import PickledDataStore

def perform_analysis_and_visualization(data_store):
    analog_Xon_ids = sorted( param_filter_query(data_store,sheet_name="X_ON").get_segments()[0].get_stored_vm_ids() )
    analog_Xoff_ids = sorted( param_filter_query(data_store,sheet_name="X_OFF").get_segments()[0].get_stored_vm_ids() )
    

    if True: # ---- ANALYSIS ----
        
        # LUMINANCE SENSITIVITY
        #dsv = param_filter_query( data_store, st_name='Null', sheet_name='X_ON' )  
        #TrialAveragedFiringRate( dsv, ParameterSet({}) ).analyse()
        
        # SPATIAL AND TEMPORAL FREQUENCY TUNING, SIZE TUNING, CONTRAST SENSITIVITY, SPARSENESS
        dsv = param_filter_query( data_store, st_name='DriftingSinusoidalGratingDisk', sheet_name='X_ON' )  
        # on responses
        #TrialAveragedFiringRate( dsv, ParameterSet({}) ).analyse()
        TrialAveragedSparseness( dsv, ParameterSet({}) ).analyse()
        # on Vm
        #Analog_MeanSTDAndFanoFactor( dsv, ParameterSet({}) ).analyse()
        
        # ORIENTATION TUNING
        #dsv = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', sheet_name='X_ON' ) 
        #TrialAveragedFiringRate( dsv, ParameterSet({}) ).analyse()
        
        # Save analysis
        data_store.save()


    if True: # ---- PLOTTING ----
        activity_plot_param = {
            'frame_rate' : 5,
            'bin_width' : 5.0,
            'scatter' :  True,
            'resolution' : 0
        }
        data_store.print_content( full_ADS=True )
        

        #----------------------
        # LUMINANCE SENSITIVITY  
        # firing rate against luminance levels              
        #dsv = param_filter_query( data_store, st_name='Null', analysis_algorithm=['TrialAveragedFiringRate'] )
        #PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'parameter_name' : 'background_luminance', 
        #        'neurons': list(analog_Xon_ids), 
        #        'sheet_name' : 'X_ON'
        #    }), 
        #    fig_param={'dpi' : 100,'figsize': (60,6)}, 
        #    plot_file_name="LuminanceSensitivity_LGN_On.png"
        #).plot({
        #    '*.fontsize':17
        #})

        #-----------------
        # SPATIAL FREQUENCY TUNING
        # firing rate against spatial frequencies
        #dsv = param_filter_query( data_store, st_name='DriftingSinusoidalGratingDisk', analysis_algorithm=['TrialAveragedFiringRate'] )
        #PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'parameter_name' : 'spatial_frequency', 
        #        'neurons': list(analog_Xon_ids), 
        #        'sheet_name' : 'X_ON'
        #    }), 
        #    fig_param={'dpi' : 100,'figsize': (16,6)}, 
        #    plot_file_name="SpatialFrequencyTuning_LGN_On.png"
        #).plot({
        #    '*.y_lim':(0,80), 
        #    '*.x_scale':'log', '*.x_scale_base':2,
        #    '*.fontsize':7
        #})

        #-----------------
        # TEMPORAL FREQUENCY TUNING                
        #dsv = param_filter_query( data_store, st_name='DriftingSinusoidalGratingDisk', analysis_algorithm=['TrialAveragedFiringRate'] )
        #PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'parameter_name' : 'temporal_frequency', 
        #        'neurons': list(analog_Xon_ids), 
        #        'sheet_name' : 'X_ON'
        #   }), 
        #   fig_param={'dpi' : 100,'figsize': (16,6)}, 
        #   plot_file_name="TemporalFrequencyTuning_LGN_On.png"
        #).plot({
        #    '*.y_lim':(0,80), 
        #    '*.x_scale':'log', '*.x_scale_base':2,
        #    '*.fontsize':7
        #})
            
        #--------------------
        # CONTRAST SATURATION
        # firing rate against contrast levels
        #dsv = param_filter_query( data_store, st_name='DriftingSinusoidalGratingDisk', analysis_algorithm=['TrialAveragedFiringRate'] )
        #PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'parameter_name' : 'contrast', 
        #        'neurons': list(analog_Xon_ids), 
        #        'sheet_name' : 'X_ON'
        #    }), 
        #    fig_param={'dpi' : 100,'figsize': (16,6)}, 
        #    plot_file_name="ContrastSensitivity_LGN_On.png"
        #).plot({
        #    '*.y_lim':(0,100), 
        #    #'*.x_scale':'log', '*.x_scale_base':2,
        #    '*.fontsize':7
        #})

        #------------
        # SIZE TUNING
        # firing rate against sizes
        #dsv = param_filter_query( data_store, st_name='DriftingSinusoidalGratingDisk', analysis_algorithm=['TrialAveragedFiringRate'] )
        #PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'parameter_name' : 'radius', 
        #        'neurons': list(analog_Xon_ids), 
        #        'sheet_name' : 'X_ON'
        #    }), 
        #    fig_param={'dpi' : 100,'figsize': (16,6)}, 
        #    plot_file_name="SizeTuning_LGN_On.png"
        #).plot({
        #    '*.y_lim':(0,100), 
        #    '*.x_scale':'log', '*.x_scale_base':2,
        #    '*.fontsize':7
        #})
                
        #--------------------
        # LIFELONG SPARSENESS
        # per neuron FanoFactor level
        #dsv = param_filter_query(data_store, analysis_algorithm=['Analog_MeanSTDAndFanoFactor'], sheet_name=['X_ON'], value_name='FanoFactor(VM)')   
        #PerNeuronValuePlot(
        #    dsv,
        #    ParameterSet({}),
        #    fig_param={'dpi' : 100,'figsize': (6,6)}, 
        #    plot_file_name="FanoFactor_LGN_On.png"
        #).plot({
        #    '*.x_axis' : None, 
        #    '*.fontsize':7
        #})
        dsv = param_filter_query(data_store, analysis_algorithm=['TrialAveragedSparseness'], sheet_name=['X_ON'], value_name='Sparseness')   
        PerNeuronValuePlot(
            dsv,
            ParameterSet({}),
            fig_param={'dpi' : 100,'figsize': (6,6)}, 
            plot_file_name="Sparseness_LGN_On.png"
        ).plot({
            '*.x_axis' : None, 
            '*.fontsize':7
        })

        #-------------------
        # ORIENTATION TUNING
        # firing rate against stimulus orientations
        #dsv = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', analysis_algorithm=['TrialAveragedFiringRate'] )
        #PlotTuningCurve( 
        #   dsv, 
        #   ParameterSet({
        #       'parameter_name':'orientation', 
        #       'neurons':list(analog_Xon_ids), 
        #       'sheet_name':'X_ON'
        #   }), 
        #   fig_param={'dpi' : 100,'figsize': (16,5)}, 
        #   plot_file_name="OrTuning_LGN_On.png"
        #).plot({
        #   '*.y_lim' : (0,100),
        #    '*.fontsize':7
        #})
        
        #-----------
        # CONTOUR COMPLETION


	   # ---- OVERVIEW LGN0 ----
        #OverviewPlot(
        #    data_store,
        #    ParameterSet({
        #        'sheet_name' : 'X_ON', 
        #        'neuron' : analog_Xon_ids[0], 
        #        'sheet_activity' : {}
        #    }),
        #   fig_param={'dpi' : 100,'figsize': (14,12)},
        #    plot_file_name="LGN_On.png"
        #).plot({
        #    '*.fontsize':7
        #})
        
        #OverviewPlot(
        #    data_store,
        #    ParameterSet({
        #        'sheet_name' : 'X_OFF', 
        #        'neuron' : analog_Xoff_ids[0], 
        #        'sheet_activity' : {}
        #    }),
        #    fig_param={'dpi' : 100,'figsize': (14,12)},
        #    plot_file_name="LGN_Off.png"
        #).plot()


        # SHOW PLOTS
        import pylab
        pylab.show()





