import gmsh
import sys

gmsh.initialize()

gmsh.model.add("t2")

n = 10
m = 10
lc = 0.1
r1 = 3.
r2 = 2.

mytorus = gmsh.model.occ.addTorus(0, 0, 0, 2, 1);
gmsh.model.occ.synchronize()
gmsh.option.setNumber("Mesh.MeshSizeMax", 0.3);
gmsh.model.mesh.generate(3)
gmsh.write("t2.msh")
gmsh.write("t2.geo_unrolled")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()

