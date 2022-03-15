def upsertAcureAircraftData(this):
    """
    Function to Open files in the SimulationOutputFile table with acure-aircraft container and then populate SimulationModelOutput and SimulationModelOutputSeries data.
    
    - Arguments:
        -this: an instance of SimulationOutputFile

    - Returns:
        -bool: True if file was processed, false if file has already been processed or if container type does not match.
    """
    from datetime import datetime, timedelta
    import pandas as pd

    # verify file container
    if(this.container == 'acure-aircraft'):
        #open file
        sample = c3.NetCDFUtil.openFile(this.file.url)
    
        # cast it to dataframe
        df = pd.DataFrame()
        df['time'] = sample.variables['time'][:]
        df['longitude'] = sample.variables['longitude'][:]
        df['latitude'] = sample.variables['latitude'][:]
        df['altitude'] = sample.variables['altitude'][:]
        df['model_level_number'] = sample.variables['model_level_number'][:]
        df['air_potential_temperature']= sample.variables['air_potential_temperature'][:]
        df['air_pressure'] = sample.variables['air_pressure'][:]
        df['cloud_flag'] = sample.variables['m01s38i478'][:]
        df['cdnc_x_cloud_flag'] = sample.variables['m01s38i479'][:]
        df['ambient_extinction_550'] = sample.variables['m01s02i530_550nm'][:]
        df['ambient_scattering_550'] = sample.variables['m01s02i532_550nm'][:]
        df['num_nuc'] = sample.variables['number_of_particles_per_air_molecule_of_soluble_nucleation_mode_aerosol_in_air'][:]
        df['num_Ait'] = sample.variables['number_of_particles_per_air_molecule_of_soluble_aitken_mode_aerosol_in_air'][:]
        df['num_acc'] = sample.variables['number_of_particles_per_air_molecule_of_soluble_accumulation_mode_aerosol_in_air'][:]
        df['num_cor'] = sample.variables['number_of_particles_per_air_molecule_of_soluble_coarse_mode_aerosol_in_air'][:]
        df['num_Aitins'] = sample.variables['number_of_particles_per_air_molecule_of_insoluble_aitken_mode_aerosol_in_air'][:]
        df['mass_SU_Ait'] = sample.variables['mass_fraction_of_sulfuric_acid_in_soluble_aitken_mode_dry_aerosol_in_air'][:] 
        df['mass_SU_acc'] = sample.variables['mass_fraction_of_sulfuric_acid_in_soluble_accumulation_mode_dry_aerosol_in_air'][:] 
        df['mass_SU_cor'] = sample.variables['mass_fraction_of_sulfuric_acid_in_soluble_coarse_mode_dry_aerosol_in_air'][:] 
        df['mass_BC_Ait'] = sample.variables['mass_fraction_of_black_carbon_in_soluble_aitken_mode_dry_aerosol_in_air'][:] 
        df['mass_BC_acc'] = sample.variables['mass_fraction_of_black_carbon_in_soluble_accumulation_mode_dry_aerosol_in_air'][:]
        df['mass_BC_cor'] = sample.variables['mass_fraction_of_black_carbon_in_soluble_coarse_mode_dry_aerosol_in_air'][:] 
        df['mass_BC_Aitins'] = sample.variables['mass_fraction_of_black_carbon_in_insoluble_aitken_mode_dry_aerosol_in_air'][:]
        df['mass_OC_Ait'] = sample.variables['mass_fraction_of_particulate_organic_matter_in_soluble_aitken_mode_dry_aerosol_in_air'][:]  
        df['mass_OC_acc'] = sample.variables['mass_fraction_of_particulate_organic_matter_in_soluble_accumulation_mode_dry_aerosol_in_air'][:]
        df['mass_OC_cor'] = sample.variables['mass_fraction_of_particulate_organic_matter_in_soluble_coarse_mode_dry_aerosol_in_air'][:]
        df['mass_OC_Aitins'] = sample.variables['mass_fraction_of_particulate_organic_matter_in_insoluble_aitken_mode_dry_aerosol_in_air'][:] 
        df['mass_SS_acc'] = sample.variables['mass_fraction_of_seasalt_in_soluble_accumulation_mode_dry_aerosol_in_air'][:]
        df['mass_SS_cor'] = sample.variables['mass_fraction_of_seasalt_in_soluble_coarse_mode_dry_aerosol_in_air'][:] 
        # a little gymnastic to get Datetime objs
        zero_time = datetime(1970,1,1,0,0)
        transformed_times = []
        for time in df['time']:
            target_time = zero_time + timedelta(hours=time)
            transformed_times.append(target_time)
        df['start'] = transformed_times
        df.drop(columns=['time'], inplace=True)

        parent_id = "SMOS_" + this.simulationSample.id
        df['parent'] = parent_id

        now_time = datetime.now()
        diff_time = (now_time - zero_time)
        versionTag= -1 * diff_time.total_seconds()
        df['dataVersion'] = versionTag

        output_records = df.to_dict(orient="records")

        # upsert this batch
        c3.SimulationModelOutput.upsertBatch(objs=output_records)

        this.processed = True
        c3.SimulationOutputFile.merge(this)
        return True
    else:
        return False
    


def upsertAcureAircraftData(this):
    """
    Function to Open files in the SimulationOutputFile table with monthly-mean container and then populate SimulationMonthlyMeanOutput data.
    
    - Arguments:
        -this: an instance of SimulationOutputFile

    - Returns:
        -bool: True if file was processed, false if file has already been processed or if container type does not match.
    """
    from datetime import datetime, timedelta
    import pandas as pd

    # verify file container
    if(this.container == 'monthly-mean'):
        variable_names = {
            "dust" : "atmosphere_optical_thickness_due_to_dust_ambient_aerosol",
            "solubleAitkenMode" : "atmosphere_optical_thickness_due_to_soluble_aitken_mode_ambient_aerosol",
            "solubleAccumulationMode" : "atmosphere_optical_thickness_due_to_soluble_accumulation_mode_ambient_aerosol",
            "solubleCoarseMode" : "atmosphere_optical_thickness_due_to_soluble_coarse_mode_ambient_aerosol",
            "insolubleAitkenMode" : "atmosphere_optical_thickness_due_to_insoluble_aitken_mode_ambient_aerosol",
            "insolubleAccumulationMode" : "atmosphereOpticalThickness_due_to_insoluble_accumulation_mode_ambient_aerosol",
            "insolubleCoarseMode" : "atmosphere_optical_thickness_due_to_insoluble_coarse_mode_ambient_aerosol"
        }
        #open file
        sample = c3.NetCDFUtil.openFile(this.file.url)
        df = pd.DataFrame()
        

        return True
    
    else:
        return False


def upsertData(this):
    """
    Function to Open files in the SimulationOutputFile table then populates Simulation***Output data.
    
    - Arguments:
        -this: an instance of SimulationOutputFile

    - Returns:
        -bool: True if file was processed, false if file has already been processed 
    """
    if(this.container == 'monthly-mean'):
        return this.upsertMonthlyMeanData()
    elif(this.container == 'acure-aircraft'):
        return this.upsertAcureAircraftData()
    else:
        return False