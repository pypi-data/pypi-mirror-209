import os
import sys
import h5py
import numpy as np
import datatable as dt
import czifile as zis
from pathlib import Path
import flowkit as fk
import pandas as pd




def image2table(file_name, outfile=None, input_file_type="auto", output_file_type="csv"):
    if input_file_type == "auto":
        input_file_type=os.path.splitext(file_name)[1][1:]
    if input_file_type == "czi":
        dat = czi2table(file_name=file_name, outfile=outfile)
    if input_file_type == "ims":
        dat = ims2table(file_name=file_name, outfile=outfile)
    if output_file_type == "csv":
        if outfile is None:
            file_name = os.path.basename(file_name)
            base = os.path.splitext(file_name)[0]
            
            new_file_name = base + '.csv'
            
            current_dir = os.getcwd()
        
            new_file_name = os.path.join(current_dir, new_file_name)
        else: 
            new_file_name=outfile
        dat.to_csv(new_file_name)
        print('file saved to ' + new_file_name)
    
    if output_file_type == "fcs":
        if outfile is None:
            file_name = os.path.basename(file_name)
            base = os.path.splitext(file_name)[0]
            dat = dat.to_pandas()
            dat_fcs = fk.Sample(dat, sample_id = base)
            base = os.path.splitext(new_file_name)[0]
            new_file_name = new_file_name = base + '.fcs'
            dat_fcs.export(filename=new_file_name, source = 'raw')


def ims2table(file_name, outfile=None):
    #read in image file
    
    file_name = os.path.abspath(file_name)
    f = h5py.File(file_name, 'r')
    #f.visit(print)
    #todo ensure that 'DataSet' and 'ResolutionLevel' each have only 1 key
    
    channel_names = list(f['DataSet']['ResolutionLevel 0']['TimePoint 0'].keys())
    
    
    Cn = [''.join(f['DataSetInfo'][ch].attrs['Name'].astype(str)) for ch in channel_names]
    Dn = [''.join(f['DataSetInfo'][ch].attrs['DyeName'].astype(str)) for ch in channel_names]
    Ex = [round(float(''.join(f['DataSetInfo'][ch].attrs['LSMExcitationWavelength'].astype(str)))) for ch in channel_names]
    Em = [round(float(''.join(f['DataSetInfo'][ch].attrs['LSMEmissionWavelength'].astype(str)))) for ch in channel_names]
    Ex = ['Ex' + str(x) for x in Ex]
    Em = ['Em' + str(x) for x in Em]
    for i in range(len(Dn)):
        if Dn[i] == '':
            Dn[i] = Ex[i] + '/' + Em[i]
    
    nice_names = [Cn + " [" + Dn + "]" for Cn, Dn in zip(Cn, Dn)]
    
    a = [f['DataSet']['ResolutionLevel 0']['TimePoint 0'][ch]['Data'] for ch in channel_names]
    
    a=np.stack(a)
    
    a=np.transpose(a)
    
    #flatten array
    
    Zaxis = a.shape[2]
    
    slicer = [np.any(a[:,:,i,:]) for i in range(Zaxis)]
    
    a = a[:,:,slicer,:]
    
    NI, NJ, NK, CH = a.shape
    
    dat = dt.Frame(x = np.repeat(range(NI),NJ*NK), 
    y = np.tile(np.repeat(range(NJ),NK), NI),
    z = np.tile(range(NK), NI*NJ))
    
    
    for ch in range(CH):
        dat[channel_names[ch]] = np.float32(a[:,:,:,ch].flatten())
    del dat.names
    dat.names = ['x', 'y', 'z'] + nice_names
    return dat


def czi2table(file_name, outfile=None):
    pth = Path(file_name)
    czi = zis.CziFile(pth)
    channel_names = []
    metadatadict_czi = czi.metadata(raw=False)
    sizeC = np.int64(metadatadict_czi['ImageDocument']['Metadata']['Information']['Image']['SizeC'])
    if sizeC == 1:
        [metadatadict_czi['ImageDocument']['Metadata']['DisplaySetting']['Channels']['Channel']['DyeName']]
    if sizeC > 1:
        for ch in range(sizeC):
            channel_name = metadatadict_czi['ImageDocument']['Metadata']['DisplaySetting']['Channels']['Channel'][ch]['Name']
            if 'DyeName' in metadatadict_czi['ImageDocument']['Metadata']['DisplaySetting']['Channels']['Channel'][ch].keys():
                dye_name = metadatadict_czi['ImageDocument']['Metadata']['DisplaySetting']['Channels']['Channel'][ch]['DyeName']
                channel_name = " ".join([channel_name, "".join(["(", dye_name, ")"])])
            channel_names.append(channel_name)
    print(channel_names)
    a = czi.asarray()
    axes = [i for i in czi.axes]
    slicer = [i in ['C', 'Z', 'Y', 'X'] for i in axes]
    a=np.reshape(a, np.array(a.shape)[slicer])
    CH, NK, NJ, NI = a.shape
    dat = dt.Frame(X = np.repeat(range(NI),NJ*NK), 
    Y = np.tile(np.repeat(range(NJ),NK)[::-1], NI),
    Z = np.tile(range(NK), NI*NJ))
    for ch in range(sizeC):
        print(channel_names[ch])
        dat[channel_names[ch]] = np.int64(a[ch, :,:,:].flatten(order = 'F'))
    czi.close()
    return dat





