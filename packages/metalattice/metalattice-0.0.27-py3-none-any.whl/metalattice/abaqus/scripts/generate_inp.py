# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def generate_inp(
    model_name: str,
    geom_inp: str,
):
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior

    model_obj = mdb.Model(name=model_name)

    part_obj = model_obj.PartFromInputFile(inputFileName=geom_inp)

    material_obj = model_obj.Material(name='Material-1')
    material_obj.Elastic(table=((200000.0, 0.3), ))
    material_obj.Density(table=((7.7e-09, ), ))

    profile_obj = model_obj.CircularProfile(name='Profile-1', r=0.1)
    section_obj = model_obj.BeamSection(
        name='Section-1',
        profile=profile_obj.name,
        material=material_obj.name,
        consistentMassMatrix=False
    )
    session.viewports['Viewport: 1'].view.fitView()
    p = mdb.models['Model-2'].parts['PART-1']
    e = p.elements
    elements = e.getSequenceFromMask(mask=('[#ffffffff:4 #ffff ]', ), )
    region = regionToolset.Region(elements=elements)
    p = mdb.models['Model-2'].parts['PART-1']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    session.viewports['Viewport: 1'].view.fitView()
    p = mdb.models['Model-2'].parts['PART-1']
    e = p.elements
    elements = e.getSequenceFromMask(mask=('[#ffffffff:4 #ffff ]', ), )
    region=regionToolset.Region(elements=elements)
    p = mdb.models['Model-2'].parts['PART-1']
    p.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(1.0, 1.0, 
        1.0))



p1 = mdb.models['Model-1'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Model-1'].parts['PART-1']
mdb.models['Model-1'].PartFromInputFile(inputFileName='D:/temp/abaqus/a.inp')