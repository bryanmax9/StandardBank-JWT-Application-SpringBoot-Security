# >>> img = cv.imread('fly.png', cv.IMREAD_GRAYSCALE)
# # Create SURF object. You can specify params here or later.
# # Here I set Hessian Threshold to 400
# >>> surf = cv.xfeatures2d.SURF_create(400)
# # Find keypoints and descriptors directly
# >>> kp, des = surf.detectAndCompute(img,None)
# >>> len(kp)
#  699




# # Check present Hessian threshold
# >>> print( surf.getHessianThreshold() )
# 400.0
# # We set it to some 50000. Remember, it is just for representing in picture.
# # In actual cases, it is better to have a value 300-500
# >>> surf.setHessianThreshold(50000)
# # Again compute keypoints and check its number.
# >>> kp, des = surf.detectAndCompute(img,None)
# >>> print( len(kp) )
# 47




# >>> img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)
# >>> plt.imshow(img2),plt.show()



# # Check upright flag, if it False, set it to True
# >>> print( surf.getUpright() )
# False
# >>> surf.setUpright(True)
# # Recompute the feature points and draw it
# >>> kp = surf.detect(img,None)
# >>> img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)
# >>> plt.imshow(img2),plt.show()



# # Find size of descriptor
# >>> print( surf.descriptorSize() )
# 64
# # That means flag, "extended" is False.
# >>> surf.getExtended()
#  False
# # So we make it to True to get 128-dim descriptors.
# >>> surf.setExtended(True)
# >>> kp, des = surf.detectAndCompute(img,None)
# >>> print( surf.descriptorSize() )
# 128
# >>> print( des.shape )
# (47, 128)