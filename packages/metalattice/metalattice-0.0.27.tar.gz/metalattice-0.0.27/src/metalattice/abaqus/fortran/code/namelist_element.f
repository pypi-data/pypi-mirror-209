      ! namelist for *.metalattice.ele file
      integer,allocatable,target::iel2ijk(:,:),iel2didjdk(:,:)
      integer,target::ns(3)
      logical,target::periodic(3)
      namelist /nml_ele/ iel2ijk, iel2didjdk, ns, periodic