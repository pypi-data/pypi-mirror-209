# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

from multiprocessing import cpu_count
import numpy as np

def generate_inp(
    job_name,
    model_name,
    geom_inp,
    E=200E3,
    nu=0.3,
    rho=7.7E-9,
    step_name="static",
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

    model_obj = mdb.ModelFromInputFile(name=model_name, inputFileName=geom_inp)
    model_obj.setValues(noPartsInputFile=ON)

    part_obj = model_obj.parts.values()[-1]

    material_obj = model_obj.Material(name='Material-1')
    material_obj.Elastic(table=((E, nu), ))
    material_obj.Density(table=((rho, ), ))

    for key, value in model_obj.rootAssembly.sets.items():
        if "BEAM" not in key: continue
        beam = value.elements[0]
        coords = [
            np.array(n.coordinates)
            for n in beam.getNodes()
        ]
        e1 = coords[1] - coords[0]
        L = np.linalg.norm(e1)
        e1 = e1 / L
        profile_obj = model_obj.CircularProfile(name='Profile'+key[4:], r=0.1*L)
        section_obj = model_obj.BeamSection(
            name='Section'+key[4:],
            integration=DURING_ANALYSIS,
            profile=profile_obj.name,
            material=material_obj.name,
            consistentMassMatrix=False,
        )

        region = regionToolset.Region(elements=part_obj.elements.sequenceFromLabels([beam.label]))
        
        part_obj.SectionAssignment(
            region=region,
            sectionName=section_obj.name,
        )

        part_obj.assignBeamSectionOrientation(
            region=region,
            method=N1_COSINES,
            n1=(0.0, 0.0, 1.0)
        )

    if step_name == "static":
        model_obj.StaticStep(
            name='Step-1',
            previous='Initial',
        )

    if int(version)>2020:
        this_job = mdb.Job(
            name=job_name,
            model=model_name,
            numCpus=cpu_count()/2,
            numDomains=cpu_count()/2,
            numGPUs=1,
            description=''
        )
    else:
        this_job = mdb.Job(
            name=job_name,
            model=model_name,
            numCpus=cpu_count(),
            numDomains=cpu_count(),
            numGPUs=1,
            description=''
        )
    this_job.submit()
    this_job.waitForCompletion()


if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "job_name",
        default=None,
        type=str,
    )
    parser.add_argument(
        "model_name",
        default=None,
        type=str,
    )
    parser.add_argument(
        "geom_inp",
        default=None,
        type=str,
    )
    parser.add_argument(
        "E",
        default=200E3,
        type=float,
    )
    parser.add_argument(
        "nu",
        default=0.3,
        type=float,
    )
    parser.add_argument(
        "rho",
        default=7.7e-9,
        type=float,
    )
    parser.add_argument(
        "step_name",
        default="static",
        type=str,
    )
    args = parser.parse_args(sys.argv[-(len(parser._actions) - 1):])
    generate_inp(
        job_name=args.job_name,
        model_name=args.model_name,
        geom_inp=args.geom_inp,
        E=args.E,
        nu=args.nu,
        rho=args.rho,
        step_name=args.step_name
    )
