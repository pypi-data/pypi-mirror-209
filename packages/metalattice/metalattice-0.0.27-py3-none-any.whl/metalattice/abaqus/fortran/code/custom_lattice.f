      pure function coord_of_idx(i,j,k) result(coord)
        real*8,dimension(3)::coord
        real*8,intent(in)::i,j,k
        coord(1)=i
        coord(2)=j
        coord(3)=k
        return
      end function coord_of_idx

      pure function beam_of_idx(ijk1, ijk2, npps) result(b)
        type(beam)::b
        real*8,intent(in)::ijk1(3),ijk2(3)
        integer,intent(in)::npps(3)
        real*8::i1,j1,k1,i2,j2,k2
        
        i1=ijk1(1)
        j1=ijk1(2)
        k1=ijk1(3)
        i2=ijk2(1)
        j2=ijk2(2)
        k2=ijk2(3)
        
        b%coord(:,1)=coord_of_idx(i1,j1,k1)
        b%coord(:,2)=coord_of_idx(i2,j2,k2)
        b%indices(:,1)=modulo(nint([i1,j1,k1])-1, npps)+1
        b%indices(:,2)=modulo(nint([i2,j2,k2])-1, npps)+1
        
        b%T(:,2)=(/1.d0,2.d0,3.d0/)                       ! editable: y direction of beam cross section
        call calc_T(b)
        
        b%section=S_CIRC                                  ! editable: shape of beam cross section
        allocate(b%geom(1))                               ! editable: len of geom of beam cross section
        b%geom(1)=b%L*0.1d0                               ! editable: geom of beam cross section
        
        return
      end function beam_of_idx

      pure subroutine beams_inside_cube(
     *  beams,ii,jj,kk,di,dj,dk,ns,periodic)
        type(beam),allocatable,target,intent(inout)::beams(:)
        integer,intent(in)::ii,jj,kk,di,dj,dk,ns(3)
        logical,intent(in)::periodic(3)
        integer::didjdk(3),ijk(3)
        
        integer::s(3),p(3),q(3),npps(3)
        integer::num
        integer::idx,i,j,k,l,d
        
        num=0
        do d=1,3
          s=(/di+1,dj+1,dk+1/)
          s(d)=s(d)-1
          num=num+product(s)
        end do
        allocate(beams(num))
        
        do d=1,3
          if(periodic(d)) then
            npps(d) = ns(d)
          else
            npps(d) = ns(d) + 1
          end if
        end do
        
        idx=0
        didjdk=(/di,dj,dk/)
        do d=1,3
          s=0
          s(d)=1
          do i=s(1),di
          do j=s(2),dj
          do k=s(3),dk
            idx=idx+1
            p=(/ii+i,jj+j,kk+k/)
            q=p
            p(d)=p(d)-1
            beams(idx)=beam_of_idx(dble(p), dble(q), npps)
            beams(idx)%pcoord(:,1)=dble(p)/dble(didjdk)*2.d0-1.d0
            beams(idx)%pcoord(:,2)=dble(q)/dble(didjdk)*2.d0-1.d0
            
            ! Determine fraction
            ijk=[i,j,k]
            do l=1,3
              if( (l.ne.d).and.
     *            ((ijk(l).eq.0).or.(ijk(l).eq.didjdk(l)))
     *        ) then
                if((p(l).eq.0).or.(p(l).eq.0)) then
                  if(periodic(l)) then
                    beams(idx)%fraction = beams(idx)%fraction * 0.5d0
                  end if
                else
                  beams(idx)%fraction = beams(idx)%fraction * 0.5d0
                end if
              end if
            end do
          end do
          end do
          end do
        end do
      end subroutine beams_inside_cube
      