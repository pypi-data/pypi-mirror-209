      include 'lattice.f'
      include 'kshape8h.f'
      include 'kshape20h.f'

c********************************************************************
c
c     Un = first/second-order, micropolar 3d brick, delta/full/reduced integration
c
c     State variables: each integration point has nsvint SDVs
c
c       isvinc=(npt-1)*nsvint                       integration point counter
c       statev(isvinc +                           1 : isvinc +                           nstretch)      stretch
c       statev(isvinc + 1*nstretch +            + 1 : isvinc + 1*nstretch +              nwryness)      wryness
c       statev(isvinc + 1*nstretch + 1*nwryness + 1 : isvinc + 1*nstretch + 1*nwryness + nstretch)      stress
c       statev(isvinc + 2*nstretch + 1*nwryness + 1 : isvinc + 2*nstretch + 1*nwryness + nstretch)      couple stress
c
c
c     jtype           1: delta integration
c                     2: full gauss integration
c                     3: reduced gauss integration
c     lflags for Static, direct incrementation
c     2  0 1 1 0 1 0
c     lflags for matrix generate
c     99 0 4 1 0 1 -604188160
c     99 0 2 1 0 1 0
c     99 0 3 1 0 1 1
c     99 0 3 1 0 1 2
c     99 0 4 1 0 1 2
c     lflags for Eigenvalue frequency extraction
c     41 0 4 1 0 1 8
c     41 0 2 1 0 1 0
c********************************************************************
      subroutine uel(rhs,amatrx,svars,energy,ndofel,nrhs,nsvars,
     1 props,nprops,coords,mcrd,nnode,u,du,v,a,jtype,time,dtime,
     2 kstep,kinc,jelem,params,ndload,jdltyp,adlmag,predef,npredf,
     3 lflags,mlvarx,ddlmag,mdload,pnewdt,jprops,njprop,period)
c
      use lattice
      include 'aba_param.inc'
      include 'SMAUsubs\PublicInterfaces\SMAAspUserArrays.hdr'
c
      dimension rhs(mlvarx,*),amatrx(ndofel,ndofel),props(*),
     1 svars(*),energy(8),coords(mcrd,nnode),u(ndofel),
     2 du(mlvarx,*),v(ndofel),a(ndofel),time(2),params(*),
     3 jdltyp(mdload,*),adlmag(mdload,*),ddlmag(mdload,*),
     4 predef(2,npredf,nnode),lflags(*),jprops(*)

c
c     user coding to define rhs, amatrx, svars, energy, and pnewdt
c
      integer nelems
      integer::iel2ijk(3,*),iel2didjdk(3,*)
      integer::ns(3),periodic(3)
      type(material)::mat
      pointer(ptr_nelems, nelems)
      pointer(ptr_iel2ijk, iel2ijk)
      pointer(ptr_iel2didjdk, iel2didjdk)
      pointer(ptr_ns, ns)
      pointer(ptr_periodic, periodic)
      pointer(ptr_mat, mat)
      
      ptr_nelems=SMAIntArrayAccess(1)
      ptr_iel2ijk=SMAIntArrayAccess(2)
      ptr_iel2didjdk=SMAIntArrayAccess(3)
      ptr_ns=SMAIntArrayAccess(4)
      ptr_periodic=SMAIntArrayAccess(5)
      ptr_mat=SMAStructArrayAccess(1)
      
      write(7,*) nelems
      do i=1,nelems
        do j=1,3
          write(7,*) i,j,iel2ijk(j,i)
        end do
      end do
      
      write(7,*) mat

      return
      end
      
      subroutine uexternaldb(lop,lrestart,time,dtime,kstep,kinc)
c
      use lattice
      include 'aba_param.inc'
      include 'SMAUsubs\PublicInterfaces\SMAAspUserArrays.hdr'
c
      dimension time(2)
c
c     user coding to set up the fortran environment, open files, close files, 
c     calculate user-defined model-independent history information,
c     write history information to external files,
c     recover history information during restart analyses, etc.
c     do not include calls to utility routine xit
c
      character*256::jobname=' ',outdir=' ',filename=' '
      integer::lenjobname=0,lenoutdir=0
      include 'namelist_element.f'
      include 'namelist_info.f'
      
      integer twin_nelems
      integer::twin_iel2ijk(3,*),twin_iel2didjdk(3,*)
      integer::twin_ns(3),twin_periodic(3)
      type(material)::twin_mat
      pointer(ptr_nelems, twin_nelems)
      pointer(ptr_iel2ijk, twin_iel2ijk)
      pointer(ptr_iel2didjdk, twin_iel2didjdk)
      pointer(ptr_ns, twin_ns)
      pointer(ptr_periodic, twin_periodic)
      pointer(ptr_mat, twin_mat)
      
      analysis_status: select case (lop)
      case (0)  ! the user subroutine is being called at the start of the analysis.
        call getjobname( jobname, lenjobname )
        call getoutdir( outdir, lenoutdir )
        
        filename=jobname
        filename(lenjobname+1:)='.metalattice.info'
        write(7,*) 'Reading file: ',
     *             filename(:lenjobname+len('.metalattice.info'))
        open(101,
     *    file=filename, mode='read', defaultfile=outdir(1:lenoutdir))
        read(101, nml=nml_info)
        close(101)
        write(7,*) 'finished!!!'
        
        call calc_G(mat)
        ptr_mat = SMAStructArrayCreate(1, 1, sizeof(mat), mat)
        
        allocate(iel2ijk(3,nelems))
        allocate(iel2didjdk(3,nelems))
        
        filename=jobname
        filename(lenjobname+1:)='.metalattice.ele'
        write(7,*) 'Reading file: ',
     *             filename(:lenjobname+len('.metalattice.info'))
        open(101,
     *    file=filename, mode='read', defaultfile=outdir(1:lenoutdir))
        read(101, nml=nml_ele)
        close(101)
        write(7,*) 'finished!!!'
      
        ptr_nelems=SMAIntArrayCreate(1,1,nelems)
        
        ptr_iel2ijk=SMAIntArrayCreate(2,3*nelems,0)
        twin_iel2ijk(1:3,1:nelems)=iel2ijk
        
        ptr_iel2didjdk=SMAIntArrayCreate(3,3*nelems,0)
        twin_iel2didjdk(1:3,1:nelems)=iel2didjdk
        
        ptr_ns=SMAIntArrayCreate(4,3,0)
        twin_ns=ns
        
        ptr_periodic=SMAIntArrayCreate(5,3,0)
        twin_periodic=periodic
      end select analysis_status
      return
      end
