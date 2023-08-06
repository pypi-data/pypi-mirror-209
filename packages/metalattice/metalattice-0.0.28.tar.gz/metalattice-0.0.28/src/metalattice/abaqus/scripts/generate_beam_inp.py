# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

from multiprocessing import cpu_count


def generate_inp(
    job_name,
    model_name,
    geom_inp,
    E = 200E3,
    nu = 0.3,
    rho = 7.7E-9,
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
    instance_obj = model_obj.rootAssembly.Instance(
        name=part_obj.name + "-1",
        part=part_obj,
        dependent=ON
    )

    material_obj = model_obj.Material(name='Material-1')
    material_obj.Elastic(table=((E, nu), ))
    material_obj.Density(table=((rho, ), ))

    profile_obj = model_obj.CircularProfile(name='Profile-1', r=0.1)
    section_obj = model_obj.BeamSection(
        name='Section-1',
        integration=DURING_ANALYSIS,
        profile=profile_obj.name,
        material=material_obj.name,
        consistentMassMatrix=False,
    )

    e = part_obj.elements
    region = regionToolset.Region(elements=e)
    part_obj.SectionAssignment(
        region=region,
        sectionName='Section-1',
        offset=0.0,
        offsetType=MIDDLE_SURFACE,
        offsetField='',
        thicknessAssignment=FROM_SECTION
    )
    part_obj.assignBeamSectionOrientation(
        region=region,
        method=N1_COSINES,
        n1=(0.0, 0.0, 1.0)
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
    args = parser.parse_args(sys.argv[-6:])
    print(args)
    generate_inp(
        job_name=args.job_name,
        model_name=args.model_name,
        geom_inp=args.geom_inp,
        E=args.E,
        nu=args.nu,
        rho=args.rho,
    )
