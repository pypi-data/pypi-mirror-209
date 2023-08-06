      module lattice
        implicit none
c
c       Math constants
c
        ! Pi
        real*8,parameter::pi=4.d0*datan(1.d0)
        ! The permutation tensor
c       The permutation tensor, also called the Levi-Civita tensor or isotropic tensor of rank 3 (Goldstein 1980, p. 172),
c       is a pseudotensor which is antisymmetric under the interchange of any two slots.
c       Recalling the definition of the permutation symbol in terms of a scalar triple product of the Cartesian unit vectors,
c         epsilon_ijk = x_i \dot (x_j \cross x_k)=[x_i,x_j.x_k]
c                     = |   1  the arguments are an even permutation
c                       |  -1  the arguments are an odd permutation
c                       |   0  two or more arguments are equal
        real*8,parameter::eps_tens(3,3,3)= reshape([
     *  0.d0,  0.d0,  0.d0,
     *  0.d0,  0.d0, -1.d0,
     *  0.d0,  1.d0,  0.d0,
     *  0.d0,  0.d0,  1.d0,
     *  0.d0,  0.d0,  0.d0,
     * -1.d0,  0.d0,  0.d0,
     *  0.d0, -1.d0,  0.d0,
     *  1.d0,  0.d0,  0.d0,
     *  0.d0,  0.d0,  0.d0  ], [3,3,3])
c
c       Enumerates
c
        enum, bind(c)           ! beam cross section
          enumerator S_ARBITRARY  ! for an arbitrary section.
          enumerator S_BOX        ! for a rectangular, hollow box section.
                                  !   Geometric input data: a, b, t1, t2, t3, t4
          enumerator S_CIRC       ! for a solid circular section.
                                  !   Geometric input data: Radius
          enumerator S_HEX        ! for a hollow hexagonal section.
          enumerator S_I          ! for an I-beam section.
          enumerator S_L          ! for an L-beam section.
          enumerator S_PIPE       ! for a thin-walled circular section.
          enumerator S_RECT       ! for a solid, rectangular section.
                                  !   Geometric input data: a, b
          enumerator S_THICK PIPE ! for a thick-walled circular section (Abaqus/Standard only).
          enumerator S_TRAPEZOID  ! for a trapezoidal section.
        end enum

        enum, bind(c)           ! beam element type
          enumerator B31
          enumerator B33
        end enum
c
c       Derived types
c
        type material
          real*8::E   = 200.d3
          real*8::nu  = 0.3d0
          real*8::G
          real*8::rho = 7.7d-9
        end type material

        type beam
          type(material)          mat
          integer(kind(S_CIRC)):: section=S_CIRC
          integer(kind(B33))::    element=B33
          real*8,allocatable::    geom(:)
          real*8                  L
          real*8                  A,I_yy,I_zz,I_yz,I_p
          real*8                  coord(3,2)              ! node physical coordinates
          real*8                  pcoord(3,2)             ! node parrent coordinates
          integer                 indices(3,2)            ! node indices
          real*8                  T(3,3)                  ! [e1, e2, e3]
          real*8                  D(18,18)
          real*8                  M(12,12)
          real*8::                SCF=0.25d0
          real*8::                xi, shear_factor
          real*8                  center(3)
          real*8::                fraction=1.d0
          logical::               lumped=.true.
        end type beam

        type stiff_pt
          real*8::pcoord(3)
          real*8::D(18,18)
          real*8::fraction=1.d0
        end type stiff_pt

        type mass_pt
          real*8::pcoord(3)
          real*8::P(6,6)
          real*8::fraction=1.d0
        end type mass_pt

        type xyz
          real*8::c(3)
        end type xyz

        type beam_list
          type(beam)::beams(64)
          integer::num=0
        end type beam_list

      contains
        ! Math subroutines
        subroutine tens_4th_transformation(tens, new_tens, tm)
          real*8,intent(in)::   tens(3,3,3,3)
          real*8,intent(out)::  new_tens(3,3,3,3)
          real*8,intent(in)::   tm(3,3)
          integer::i1,j1,k1,l1,i2,j2,k2,l2

          new_tens=0.d0
          do i1=1,3
          do j1=1,3
          do k1=1,3
          do l1=1,3
            do i2=1,3
            do j2=1,3
            do k2=1,3
            do l2=1,3
              new_tens(i1,j1,k1,l1)=new_tens(i1,j1,k1,l1)+
     *          tens(i2,j2,k2,l2)
     *        * tm(i1,i2) * tm(j1,j2) * tm(k1,k2) * tm(l1,l2)
            end do
            end do
            end do
            end do
          end do
          end do
          end do
          end do
          return
        end subroutine tens_4th_transformation
        
        
        ! type material
        subroutine calc_G(mat)
          type(material),target,intent(inout)::mat
          
          mat%G=mat%E/(2.d0*(1.d0+mat%nu))
        end subroutine calc_G
        
        
        !type beam
        pure subroutine calc_T(b)
          type(beam),target,intent(inout)::b
          real*8 mag
          real*8,parameter::diag(3,3)=reshape([
     *    1,0,0,
     *    0,1,0,
     *    0,0,1
     *    ], [3,3])
          real*8,dimension(:),pointer::e1,e2,e3
          integer idx
c
          e1=>b%T(:,1)
          e2=>b%T(:,2)
          e3=>b%T(:,3)
c
c         e1 = n2 - n1, and nomalizing
c
          e1=b%coord(:,2)-b%coord(:,1)
          b%center=0.5d0*(b%coord(:,2)+b%coord(:,1))
          b%L=norm2(e1)
          e1=e1/b%L
c
c         e2 = e2 - e1 * e2, and nomalizing(if e1 // e2, let e2 be x,y,z direction)
c
          e2=e2-dot_product(e1,e2)
          idx=0
          do while(dabs(norm2(e2))<epsilon(e2))
            idx=idx+1
            e2=diag(idx,:)
            e2=e2-dot_product(e1,e2)
          end do
          e2=e2/norm2(e2)
c
c         e3 = e1 x e2
c
          e3(1)=e1(2)*e2(3)-e1(3)*e2(2)
          e3(2)=e1(3)*e2(1)-e1(1)*e2(3)
          e3(3)=e1(1)*e2(2)-e1(2)*e2(1)
        end subroutine calc_T
        
        
        pure function py_coord_of_idx(i,j,k) result(coord)
          type(xyz) coord
          real*8,intent(in)::i,j,k

          coord%c=coord_of_idx(i,j,k)
          return
        end function py_coord_of_idx
        
        
        pure function py_beams_inside_cube(
     *  ii, jj, kk, di, dj, dk, ns, periodic) result(beam_list_out)
          type(beam_list)::beam_list_out
          integer,intent(in)::ii,jj,kk,di,dj,dk,ns(3)
          logical,intent(in)::periodic(3)
          type(beam),allocatable,target::beams(:)
          integer::i,shp(1)
        
          call beams_inside_cube(beams,ii,jj,kk,di,dj,dk,ns,periodic)
        
          shp = shape(beams)
          beam_list_out%num = shp(1)
          do i=1,beam_list_out%num
            beam_list_out%beams(i)%mat%E   = beams(i)%mat%E
            beam_list_out%beams(i)%mat%nu  = beams(i)%mat%nu
            beam_list_out%beams(i)%mat%G   = beams(i)%mat%G
            beam_list_out%beams(i)%mat%rho = beams(i)%mat%rho
            beam_list_out%beams(i)%section = beams(i)%section
            beam_list_out%beams(i)%element = beams(i)%element
            allocate(beam_list_out%beams(i)%geom, source=beams(i)%geom)
            beam_list_out%beams(i)%L       = beams(i)%L
            beam_list_out%beams(i)%A       = beams(i)%A
            beam_list_out%beams(i)%I_yy    = beams(i)%I_yy
            beam_list_out%beams(i)%I_zz    = beams(i)%I_zz
            beam_list_out%beams(i)%I_yz    = beams(i)%I_yz
            beam_list_out%beams(i)%I_p     = beams(i)%I_p
            beam_list_out%beams(i)%coord   = beams(i)%coord
            beam_list_out%beams(i)%pcoord  = beams(i)%pcoord
            beam_list_out%beams(i)%indices = beams(i)%indices
            beam_list_out%beams(i)%T       = beams(i)%T
            beam_list_out%beams(i)%D       = beams(i)%D
            beam_list_out%beams(i)%M       = beams(i)%M
            beam_list_out%beams(i)%SCF     = beams(i)%SCF
            beam_list_out%beams(i)%xi      = beams(i)%xi
            beam_list_out%beams(i)%shear_factor = beams(i)%shear_factor
            beam_list_out%beams(i)%center  = beams(i)%center
            beam_list_out%beams(i)%fraction= beams(i)%fraction
            beam_list_out%beams(i)%lumped  = beams(i)%lumped
          end do

        end function py_beams_inside_cube
        
        
        include 'custom_lattice.f'
        
      end module lattice