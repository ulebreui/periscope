import matplotlib.pyplot as plt
import numpy as np
import glob
import os

# DUNE is a free software : you can redistribute it/and or modify it
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#You should have received a copy of the GNU General Public License
#along with DUNE.  If not, see <http://www.gnu.org/licenses/>.



class SharkData():
    def __init__(self,nout=1,path="",NX=1,NY=1,NDUST=1,box_x=1.,box_y=1.):
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("Periscope")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        filename=self.data_loader(nout=nout,path=path)
        info = np.loadtxt(filename+"/info.dat")

        self.x   = self.read_var(filename,'x',NX*NY)
        self.y   = self.read_var(filename,'y',NX*NY)
        self.xx  = np.linspace(-box_x/2.,box_x/2.,NX)
        self.yy  = np.linspace(-box_y/2.,box_y/2.,NY)
        self.v1   = self.read_var(filename,'v',NX*NY)
        self.vy1  = self.read_var(filename,'vy',NX*NY)
        self.P1   = self.read_var(filename,'P',NX*NY)
        self.rho1 = self.read_var(filename,'rho',NX*NY)
        
        self.rho = np.reshape(self.rho1,(NY,NX),order = "C").T
        self.vel_x  = np.reshape(self.v1,(NY,NX),order = "C").T
        self.vel_y  = np.reshape(self.vy1,(NY,NX),order = "C").T
        self.P   = np.reshape(self.P1,(NY,NX),order = "C").T
        
        if(NDUST>0):
            self.rhod0  = self.read_var(filename,'rhod',NX*NY*NDUST)
            self.vd0    = self.read_var(filename,'vd',NX*NY*NDUST)
            self.vdy0   = self.read_var(filename,'vdy',NX*NY*NDUST)
            self.rhod = np.reshape(self.rhod0,(NDUST,NY,NX),order = "C").T
            self.vxd  = np.reshape(self.vd0,(NDUST,NY,NX),order = "C").T
            self.vyd  = np.reshape(self.vdy0,(NDUST,NY,NX),order = "C").T
            for idust in range(NDUST):
                setattr("rhod_"+str(idust+1),self.rhod[:,:,idust])
                setattr("vel_d_x_"+str(idust+1) ,self.vxd[:,:,idust])
                setattr("vel_d_y_"+str(idust+1) ,self.vxd[:,:,idust])
                setattr("dust-to-gas_"+str(idust+1),self.rhod[:,:,idust]/self.rho)
            setattr("dust-to-gas",np.sum(self.rhod,axis=2)/self.rho)
            setattr("rhod",np.sum(self.rhod,axis=2))
        
        return


    def data_loader(self,nout=1,path=""):
        # Generate directory name from output number
        infile = self.generate_fname(nout,path)
        return infile

        
    def generate_fname(self,nout,path="",ftype="",cpuid=1,ext=""): #Take from OSIRIS (Vaytet)
        
        if len(path) > 0:
            if path[-1] != "/":
                path=path+"/"
        
        if nout == -1:
            filelist = sorted(glob.glob(path+"output*"))
            number = filelist[-1].split("_")[-1]
        else:
            number = str(nout).zfill(5)

        infile = path+"output_"+number
        if len(ftype) > 0:
            infile += "/"+ftype+"_"+number
            if cpuid >= 0:
                infile += ".out"+str(cpuid).zfill(5)
        
        if len(ext) > 0:
            infile += ext
            
        return infile
    
    def read_var(self,filename,varname,size):
        f=open(filename+"/"+varname, "rb")
        dat = np.fromfile(f, dtype=np.float, count=size, sep='')
        #dat = np.loadtxt(filename+"/"+varname)#
        return dat
