import gmsh
import sys

gmsh.initialize()

gmsh.model.add("torus")
mytorus = gmsh.model.occ.addTorus(0, 0, 0, 2, 1);
gmsh.model.occ.synchronize()
gmsh.option.setNumber("Mesh.MeshSizeMax", 0.3);
gmsh.model.mesh.generate(3)
gmsh.write("torus.msh")
gmsh.write("torus.geo_unrolled")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()

