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
        
        # ORIENTATION TUNING
        #dsv = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', sheet_name='X_ON' ) 
        #TrialAveragedFiringRate( dsv, ParameterSet({}) ).analyse()
        
        # SIZE TUNING
        dsv = param_filter_query( data_store, st_name='DriftingSinusoidalGratingDisk', sheet_name='X_ON' )  
        TrialAveragedFiringRate( dsv, ParameterSet({}) ).analyse()
        
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

        # ORIENTATION TUNING
        # retrieve analysed data
        #dsv = param_filter_query( data_store ,st_name='FullfieldDriftingSinusoidalGrating', analysis_algorithm=['TrialAveragedFiringRate'] )
        # plot retrieved data
        #PlotTuningCurve( dsv, ParameterSet({'parameter_name':'orientation', 'neurons':list(analog_Xon_ids), 'sheet_name':'X_ON'}), fig_param={'dpi' : 100,'figsize': (16,5)}, plot_file_name="OrTuning_LGN_On.png").plot({'*.y_lim' : (0,100)})
        
        # SIZE TUNING select data based on analysis
        dsv = param_filter_query( data_store ,st_name='DriftingSinusoidalGratingDisk', analysis_algorithm=['TrialAveragedFiringRate'], st_radius=[] )  
        PlotTuningCurve(
            dsv,
            ParameterSet({
                'parameter_name' : 'radius', 
                'neurons': list(analog_Xon_ids), 
                'sheet_name' : 'X_ON'
            }), 
            fig_param={'dpi' : 100,'figsize': (16,6)}, 
            plot_file_name="SizeTuning_LGN_On.png"
        ).plot({
            '*.y_lim':(0,100), 
            '*.x_scale':'log', '*.x_scale_base':2
        })
       
	    # ---- LGN0 ----
        OverviewPlot(
            data_store,
            ParameterSet({
                'sheet_name' : 'X_ON', 
                'neuron' : analog_Xon_ids[0], 
                'sheet_activity' : {}
            }),
            fig_param={'dpi' : 100,'figsize': (14,12)},
            plot_file_name="LGN_On.png"
        ).plot()

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





