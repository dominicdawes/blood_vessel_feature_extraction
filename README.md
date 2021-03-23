# dawes_skeletonize_v1.0 README


## About
`dawes_skeletonize_v1.0`, skeletonizes vascular structures and identifies key bifurcations and crossing points


## API (key functions)
`skel_to_branchpoints(in_skel)`
* returns boolean np array of bifurcations/intersections x,y coordinates when given a skeletonized input (np array)


## Use
1. install Dependencies from requirements.txt
2. run: `dawes_skeletonize_v1.0.py`  
3. outputs:
  + skel: pixel thin skeleton
  + intersections: bifurcation point np array
  + plot of input, skel, and branch points


## Dependencies
- skimage
- cv2
- matplotlib
- skan
